# Audit Model

DatasetPassport produces a technical risk snapshot for tabular and record-oriented datasets. It does not make a legal determination.

## Audit dimensions

### Record integrity

- Total records.
- Unique normalized records.
- Exact duplicate count and duplicate rate.
- Required-field completeness.

### Privacy indicators

The MVP scans normalized records for selected patterns such as email addresses, mainland China mobile numbers, and mainland China identity-number shapes.

Pattern matches are indicators, not proof. False positives and false negatives are expected. Reports must be reviewed before publication or commercial distribution.

### Provenance coverage

The scanner checks whether common provenance fields are present across records:

- `source`
- `source_url`
- `license`
- `provenance`

The current `source_traceability` value is the highest observed coverage among these fields. Future versions may support weighted provenance scoring.

### License handling

A declared license changes the report from `review_required` to `verify_license_terms`. This deliberately avoids claiming that a dataset is commercially safe merely because a license string exists.

## Severity guidance

| Level | Meaning | Suggested action |
|---|---|---|
| Low | No configured PII pattern was detected | Continue manual sampling |
| Medium | One or more configured patterns were detected | Quarantine and review matching records |
| High | More than 20 configured pattern matches were detected | Stop release until remediation |

## Non-goals

- Legal advice.
- Copyright ownership verification.
- Terms-of-service interpretation.
- Semantic near-duplicate detection in the MVP.
- Re-identification risk measurement.

## Reproducibility

For repeatable reports, preserve the input checksum, scanner version, required-field list, declared license argument, and rule-set version.
