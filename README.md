# DatasetPassport

DatasetPassport is a local-first quality scanner for CSV, JSON, and JSONL datasets. It creates a structured review report before a dataset is used, delivered, or published.

> The report contains technical observations. It does not replace source review, manual sampling, or professional assessment.

## Use cases

- Check instruction, classification, support, sentiment, and reading-comprehension datasets
- Add a basic quality gate before internal delivery
- Compare dataset versions
- Prepare machine-readable review records
- Track source and license fields during data processing

## Current capabilities

- Read CSV, JSON, and JSONL
- Count exact normalized duplicates
- Check required fields
- Detect selected identifier-like text patterns
- Measure source-field coverage
- Record the declared license value
- Write a JSON report for automation and human review

## Requirements

- Python 3.10 or newer
- No paid API

## Run

```bash
python main.py data.jsonl --required instruction,output,source --license apache-2.0 -o report.json
```

## Test

```bash
python -m unittest -v
```

## Recommended fields

| Field | Purpose |
|---|---|
| `id` | stable record identifier |
| `instruction` or `text` | input content |
| `output` or `label` | expected result |
| `source` | source or batch name |
| `license` | declared license value |
| `source_url` | optional source locator |
| `created_at` | optional processing date |
| `processing_version` | optional pipeline version |

Use one documented missing-value strategy. Avoid mixing empty strings, placeholder words, and `null` without a clear rule.

## Command reference

```bash
python main.py <input> \
  --required instruction,output,source \
  --license apache-2.0 \
  -o report.json
```

- `<input>`: dataset file
- `--required`: comma-separated field names
- `--license`: declared license for the reviewed batch
- `-o`: output report path

## Report interpretation

The report helps answer:

1. Can the file be parsed?
2. Are required fields complete?
3. Are exact duplicates present?
4. Did configured text patterns match?
5. Are source and license fields available for review?

Pattern checks are indicators. Review matching records in context.

## Suggested gates

| Finding | Suggested action |
|---|---|
| Parsing failure | stop the workflow |
| Missing required field | correct the dataset and rerun |
| Pattern match | inspect the matching record |
| Exact duplicate | decide whether repetition is intentional |
| Missing source | complete the source record |
| Unclear license value | review the original terms |
| Split overlap | correct the split before evaluation |

## Recommended workflow

1. Record the input checksum.
2. Run DatasetPassport.
3. Review and correct findings.
4. Run the scan again.
5. Keep the before-and-after reports.
6. Deliver the report, schema, source inventory, and version notes together.

## Documentation

- [Audit Model](docs/AUDIT_MODEL.md)
- [Report Format](docs/REPORT_FORMAT.md)
- [Remediation Guide](docs/REMEDIATION_GUIDE.md)
- [Performance Baseline](docs/PERFORMANCE_BASELINE.md)
- [Quality Gates](docs/QUALITY_GATES.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## Known limitations

- The current release focuses on structure and configured rules.
- It does not visit source websites.
- It does not decide whether two licenses are compatible.
- It does not replace semantic review or near-duplicate analysis.

## License

MIT
