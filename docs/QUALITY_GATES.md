# Dataset Quality Gates

This document defines a practical review model for deciding whether a dataset can proceed to training, internal delivery, or public distribution.

## Severity levels

| Level | Meaning | Default action |
|---|---|---|
| Blocker | The dataset cannot be safely or reliably used | Stop the pipeline |
| Warning | Human review is required before release | Hold for review |
| Advisory | Improvement is recommended but not automatically blocking | Record and continue |

## Structural gates

### Blocker

- File cannot be parsed.
- Required fields are absent from the schema.
- Record identifiers are missing when stable IDs are required.
- Train and test partitions share the same IDs.
- Output report cannot be written.

### Warning

- Required fields exist but contain unexpected null rates.
- Field types vary across records.
- Character encoding is inconsistent.

## Privacy gates

### Blocker

- Confirmed personal information is present without a valid purpose and authorization.
- Secrets, access tokens, passwords, or private keys are detected.

### Warning

- Email, phone, identification-number, address, or account patterns are detected.
- Free-text fields contain unexplained identifiers.

A regular-expression hit is a review signal, not final proof. Review the source record and surrounding context.

## Provenance gates

### Blocker

- Source is unknown for a commercial release.
- License or authorization evidence is unavailable.
- Terms explicitly prohibit the intended use.

### Warning

- License string is present but not linked to evidence.
- Source metadata is incomplete.
- Multiple sources are merged without per-record provenance.

## Quality gates

### Blocker

- Labels are systematically shifted or mapped to the wrong class.
- Required output fields are empty at a material rate.
- Evaluation leakage invalidates the stated benchmark.

### Warning

- Exact duplicate rate exceeds the project threshold.
- Class distribution is severely imbalanced without documentation.
- Generated records use repeated templates.
- Translations contain unresolved placeholders or mixed-language artifacts.

### Advisory

- Add semantic deduplication.
- Add stratified sampling and manual review.
- Publish label definitions and annotator guidance.

## Suggested release evidence

- Dataset version and creation date
- File checksums
- Schema
- Source and license inventory
- DatasetPassport scan report
- Manual sampling report
- Train/validation/test split policy
- Known limitations
- Change log from the previous version

## Example decision

```json
{
  "dataset_version": "1.2.0",
  "decision": "hold",
  "blockers": 0,
  "warnings": 3,
  "required_actions": [
    "review 12 phone-pattern hits",
    "add source evidence for batch-04",
    "remove train-test ID overlap"
  ]
}
```

The final release decision should be signed off by a responsible human reviewer.