from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


PII_PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone_cn": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "id_cn": re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)"),
}


def iter_records(path: str) -> Iterable[dict]:
    source = Path(path)
    suffix = source.suffix.lower()
    if suffix == ".csv":
        with source.open("r", encoding="utf-8-sig", newline="") as handle:
            yield from csv.DictReader(handle)
        return
    if suffix in {".jsonl", ".ndjson"}:
        with source.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError(f"Line {line_number} is not a JSON object")
                yield value
        return
    if suffix == ".json":
        value = json.loads(source.read_text(encoding="utf-8"))
        records = value if isinstance(value, list) else value.get("records") if isinstance(value, dict) else None
        if not isinstance(records, list):
            raise ValueError("JSON must be a list or contain a records list")
        yield from records
        return
    raise ValueError("Supported formats: CSV, JSON, JSONL")


def audit(path: str, required_fields: list[str] | None = None, declared_license: str | None = None) -> dict:
    required_fields = required_fields or []
    total = 0
    fingerprints: set[str] = set()
    missing = Counter()
    pii = Counter()
    fields = Counter()

    for record in iter_records(path):
        total += 1
        fields.update(record.keys())
        for field in required_fields:
            if record.get(field) in (None, "", []):
                missing[field] += 1
        normalized = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        fingerprints.add(hashlib.sha256(normalized.encode("utf-8")).hexdigest())
        for name, pattern in PII_PATTERNS.items():
            pii[name] += len(pattern.findall(normalized))

    duplicates = max(0, total - len(fingerprints))
    trace_fields = ("source", "source_url", "license", "provenance")
    traceability = max((fields.get(field, 0) / total for field in trace_fields), default=0.0) if total else 0.0
    findings = sum(pii.values())
    risk = "high" if findings > 20 else "medium" if findings else "low"

    return {
        "records": total,
        "unique_records": len(fingerprints),
        "duplicate_records": duplicates,
        "duplicate_rate": round(duplicates / total, 6) if total else 0.0,
        "missing_required": dict(missing),
        "pii_findings": dict(pii),
        "pii_risk": risk,
        "declared_license": declared_license,
        "source_traceability": round(traceability, 4),
        "commercial_use": "review_required" if not declared_license else "verify_license_terms",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit an AI dataset.")
    parser.add_argument("dataset")
    parser.add_argument("-o", "--output", default="dataset-passport.json")
    parser.add_argument("--required", default="")
    parser.add_argument("--license", dest="declared_license")
    args = parser.parse_args()
    required = [item.strip() for item in args.required.split(",") if item.strip()]
    report = audit(args.dataset, required, args.declared_license)
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote audit report to {args.output}")


if __name__ == "__main__":
    main()
