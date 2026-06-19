# About DatasetPassport

## Mission

DatasetPassport provides a repeatable local audit layer for datasets before training, internal delivery, publication, or commercial packaging.

## Intended users

- Data engineers preparing training corpora
- Teams reviewing dataset versions
- Developers building data-quality gates
- Researchers documenting provenance and overlap
- Maintainers who need machine-readable audit records

## Core capabilities

- CSV, JSON, and JSONL ingestion
- Required-field checks
- Exact duplicate detection
- Exact cross-file overlap analysis
- Selected identifier-pattern findings
- Field coverage reporting
- Input checksums and versioned reports

## Boundaries

The project does not verify changing source websites, determine legal compatibility, perform semantic deduplication, or replace human review.

## Architecture

```text
Input reader -> record normalization -> fingerprinting
             -> field checks -> pattern checks -> report generation
             -> optional split comparison
```

## Design priorities

1. Local processing
2. Reproducible reports
3. Clear separation between observations and decisions
4. Non-sensitive examples
5. Stable report contracts
6. Low dependency footprint

## Maturity

The project is an executable MVP with structured reports, checksums, overlap analysis, schemas, examples, tests, and documented remediation workflows.

## Data handling principle

Reports should contain counts and metadata rather than copying matched sensitive values. Public fixtures must remain synthetic.

## Governance

Rule changes require positive and negative fixtures. Report-schema changes require migration notes. Performance changes should be tested on representative record counts.
