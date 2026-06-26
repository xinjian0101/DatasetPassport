<div align="center">

# DatasetPassport

**Local-first dataset quality, overlap, provenance, and release-readiness reports.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)
[![Formats](https://img.shields.io/badge/Input-CSV%20%7C%20JSON%20%7C%20JSONL-0969da)](docs/CLI_REFERENCE.md)
[![Status](https://img.shields.io/badge/Status-Active%20MVP-f59e0b)](MAINTENANCE_TRACE.md)

[Quick start](#quick-start) · [Quality gates](#quality-gates) · [Report model](docs/REPORT_FORMAT.md) · [About](ABOUT.md) · [CLI reference](docs/CLI_REFERENCE.md)

</div>

---

DatasetPassport scans structured datasets before training, delivery, publication, or commercial packaging. It produces versioned JSON or Markdown reports containing checksums, completeness metrics, duplicate counts, selected pattern findings, provenance coverage, and exact split-overlap results.

> [!NOTE]
> DatasetPassport reports technical observations. It does not replace source authorization, semantic review, privacy assessment, or professional legal advice.

## At a glance

| Area | Current support |
|---|---|
| Inputs | CSV, JSON, JSONL, NDJSON |
| Integrity | SHA-256 input checksum |
| Quality | Required fields, exact duplicates, field coverage |
| Review | Selected identifier-pattern findings |
| Splits | Exact cross-file overlap comparison |
| Reports | Versioned JSON and Markdown |
| Runtime | Python standard library, local processing |

## Quick start

```bash
python main.py examples/data.jsonl \
  --required instruction,output,source \
  --license apache-2.0 \
  --format markdown \
  -o dataset-passport.md
```

Compare two dataset splits:

```bash
python main.py train.jsonl \
  --compare test.jsonl \
  --required instruction,output,source \
  -o overlap-report.json
```

Run tests:

```bash
python -m unittest -v
```

## Capability matrix

| Capability | Status | Notes |
|---|---:|---|
| Required-field validation | ✅ | Per-field missing counts |
| Exact normalized duplicates | ✅ | SHA-256 record fingerprints |
| Exact split overlap | ✅ | Reports overlap of smaller set |
| Field coverage | ✅ | Coverage per observed field |
| Versioned reproducibility data | ✅ | Timestamp, checksum, format, config |
| Semantic duplicate detection | ⏳ | Not implemented |
| Automatic license compatibility | ❌ | Requires source review |

## Report status

Every report receives one technical workflow status:

| Status | Meaning |
|---|---|
| `pass` | No configured blocking or review finding |
| `review` | Duplicates, pattern findings, or missing declared license require review |
| `blocking` | One or more required fields are missing |

These statuses are workflow signals, not final legal or publication decisions.

## Recommended record fields

| Field | Purpose |
|---|---|
| `id` | Stable record identifier |
| `instruction` or `text` | Input content |
| `output` or `label` | Expected result |
| `source` | Source or batch identifier |
| `license` | Declared license label |
| `source_url` | Optional source locator |
| `created_at` | Optional processing date |
| `processing_version` | Optional transformation version |

## Quality gates

| Finding | Suggested workflow action |
|---|---|
| Parsing failure | Stop the pipeline |
| Missing required field | Correct and rerun |
| Exact duplicate | Confirm whether repetition is intentional |
| Pattern match | Review the matching record in context |
| Missing provenance | Complete the source record |
| Split overlap | Correct the split before evaluation |
| Unclear source terms | Pause release and collect evidence |

## Report package

A complete delivery package should preserve:

```text
source checksum
processed dataset
scan command
scanner commit
JSON report
Markdown review report
schema and field definitions
source inventory
remediation notes
release decision record
```

## Repository map

| Path | Purpose |
|---|---|
| `main.py` | Readers, audit rules, comparison, and report writers |
| `rules/` | Versioned audit profiles |
| `schema/` | Report contract |
| `templates/` | Release-decision records |
| `examples/` | Synthetic fixtures and sample reports |
| `docs/` | Audit, remediation, performance, and CLI guidance |
| `test_*.py` | Audit, overlap, and report tests |
| `ABOUT.md` | Mission, maturity, boundaries, and governance |

## Support & Security

- 📖 See [About](ABOUT.md) for scope
- 🐛 Use Issue templates for reproducible bugs
- 💡 Use Feature requests for improvements
- 🔐 Security policy in SECURITY.md

## Project boundaries

- No source-site crawling
- No semantic correctness score
- No near-duplicate model
- No automatic authorization conclusion
- No sensitive value disclosure in standard reports

## Documentation

- [About the project](ABOUT.md)
- [Audit model](docs/AUDIT_MODEL.md)
- [Report format](docs/REPORT_FORMAT.md)
- [Remediation guide](docs/REMEDIATION_GUIDE.md)
- [Performance baseline](docs/PERFORMANCE_BASELINE.md)
- [Quality gates](docs/QUALITY_GATES.md)
- [CLI reference](docs/CLI_REFERENCE.md)
- [Maintenance trace](MAINTENANCE_TRACE.md)
- [Changelog](CHANGELOG.md)

## License

MIT