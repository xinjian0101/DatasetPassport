from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPORT_VERSION = 1
PII_PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone_cn": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "id_cn": re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)"),
}


def file_checksum(path: str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_record(record: dict) -> str:
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def record_fingerprint(record: dict) -> str:
    return hashlib.sha256(normalize_record(record).encode("utf-8")).hexdigest()


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
                try:
                    value = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSON at line {line_number}: {exc}") from exc
                if not isinstance(value, dict):
                    raise ValueError(f"Line {line_number} is not a JSON object")
                yield value
        return
    if suffix == ".json":
        value = json.loads(source.read_text(encoding="utf-8"))
        records = value if isinstance(value, list) else value.get("records") if isinstance(value, dict) else None
        if not isinstance(records, list):
            raise ValueError("JSON must be a list or contain a records list")
        for index, record in enumerate(records, 1):
            if not isinstance(record, dict):
                raise ValueError(f"JSON record {index} is not an object")
            yield record
        return
    raise ValueError("Supported formats: CSV, JSON, JSONL")


def compare_datasets(first_path: str, second_path: str) -> dict:
    first = {record_fingerprint(record) for record in iter_records(first_path)}
    second = {record_fingerprint(record) for record in iter_records(second_path)}
    overlap = first & second
    denominator = min(len(first), len(second))
    return {
        "other_file": Path(second_path).name,
        "first_unique_records": len(first),
        "second_unique_records": len(second),
        "exact_overlap_records": len(overlap),
        "overlap_rate_of_smaller_set": round(len(overlap) / denominator, 6) if denominator else 0.0,
    }


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
        fingerprints.add(record_fingerprint(record))
        normalized = normalize_record(record)
        for name, pattern in PII_PATTERNS.items():
            pii[name] += len(pattern.findall(normalized))

    duplicates = max(0, total - len(fingerprints))
    trace_fields = ("source", "source_url", "license", "provenance")
    traceability = max((fields.get(field, 0) / total for field in trace_fields), default=0.0) if total else 0.0
    findings = sum(pii.values())
    risk = "high" if findings > 20 else "medium" if findings else "low"
    coverage = {field: round(count / total, 4) if total else 0.0 for field, count in sorted(fields.items())}

    report = {
        "report_version": REPORT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "input": {
            "file": Path(path).name,
            "format": Path(path).suffix.lower().lstrip("."),
            "checksum_algorithm": "sha256",
            "checksum": file_checksum(path),
        },
        "configuration": {
            "required_fields": required_fields,
            "declared_license": declared_license,
        },
        "records": total,
        "unique_records": len(fingerprints),
        "duplicate_records": duplicates,
        "duplicate_rate": round(duplicates / total, 6) if total else 0.0,
        "missing_required": dict(missing),
        "field_coverage": coverage,
        "pii_findings": dict(pii),
        "pii_risk": risk,
        "declared_license": declared_license,
        "source_traceability": round(traceability, 4),
        "commercial_use": "review_required" if not declared_license else "verify_license_terms",
    }
    report["review_status"] = report_status(report)
    return report


def report_status(report: dict) -> str:
    if any(int(value) > 0 for value in report.get("missing_required", {}).values()):
        return "blocking"
    if report.get("duplicate_records", 0) or sum(report.get("pii_findings", {}).values()):
        return "review"
    if not report.get("declared_license"):
        return "review"
    return "pass"


def infer_report_format(path: str, requested: str | None = None) -> str:
    if requested:
        return requested
    return "markdown" if Path(path).suffix.lower() in {".md", ".markdown"} else "json"


def render_markdown(report: dict) -> str:
    lines = [
        "# Dataset Passport",
        "",
        f"- Review status: **{report.get('review_status', report_status(report))}**",
        f"- Records: {report.get('records', 0)}",
        f"- Unique records: {report.get('unique_records', 0)}",
        f"- Exact duplicates: {report.get('duplicate_records', 0)}",
        f"- Duplicate rate: {report.get('duplicate_rate', 0)}",
        f"- Source traceability: {report.get('source_traceability', 0)}",
        f"- Declared license: {report.get('declared_license') or 'not provided'}",
        f"- Pattern risk: {report.get('pii_risk', 'unknown')}",
        "",
        "## Missing required fields",
        "",
    ]
    missing = report.get("missing_required", {})
    if missing:
        lines.extend(["| Field | Missing records |", "|---|---:|"])
        lines.extend(f"| {field} | {count} |" for field, count in sorted(missing.items()))
    else:
        lines.append("No missing required fields were reported.")

    lines.extend(["", "## Pattern findings", ""])
    findings = report.get("pii_findings", {})
    if findings:
        lines.extend(["| Pattern | Matches |", "|---|---:|"])
        lines.extend(f"| {name} | {count} |" for name, count in sorted(findings.items()))
    else:
        lines.append("No configured pattern findings were reported.")

    comparison = report.get("comparison")
    if comparison:
        lines.extend([
            "",
            "## Dataset comparison",
            "",
            f"- Other file: {comparison.get('other_file')}",
            f"- Exact overlap records: {comparison.get('exact_overlap_records', 0)}",
            f"- Overlap rate of smaller set: {comparison.get('overlap_rate_of_smaller_set', 0)}",
        ])

    lines.extend([
        "",
        "## Reproducibility",
        "",
        f"- Report version: {report.get('report_version')}",
        f"- Generated at: {report.get('generated_at')}",
        f"- Input checksum: `{report.get('input', {}).get('checksum', '')}`",
    ])
    return "\n".join(lines) + "\n"


def write_report(report: dict, path: str, output_format: str | None = None) -> None:
    output_format = infer_report_format(path, output_format)
    target = Path(path)
    if output_format == "json":
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return
    if output_format == "markdown":
        target.write_text(render_markdown(report), encoding="utf-8")
        return
    raise ValueError(f"Unsupported report format: {output_format}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit an AI dataset.")
    parser.add_argument("dataset")
    parser.add_argument("-o", "--output", default="dataset-passport.json")
    parser.add_argument("--format", choices=("json", "markdown"))
    parser.add_argument("--required", default="")
    parser.add_argument("--license", dest="declared_license")
    parser.add_argument("--compare", help="Optional second dataset for exact cross-file overlap analysis")
    args = parser.parse_args()
    required = [item.strip() for item in args.required.split(",") if item.strip()]
    report = audit(args.dataset, required, args.declared_license)
    if args.compare:
        report["comparison"] = compare_datasets(args.dataset, args.compare)
    write_report(report, args.output, args.format)
    print(f"Wrote audit report to {args.output}")


if __name__ == "__main__":
    main()
