# Report Format

DatasetPassport emits a JSON report intended for both automation and human review.

## Core fields

| Field | Type | Meaning |
|---|---|---|
| `records` | integer | total records read successfully |
| `unique_records` | integer | unique normalized records |
| `duplicate_records` | integer | exact duplicate count |
| `duplicate_rate` | number | duplicates divided by total records |
| `missing_required` | object | missing counts by required field |
| `pii_findings` | object | configured pattern match counts |
| `pii_risk` | string | low, medium, or high technical risk label |
| `declared_license` | string or null | license supplied to the CLI |
| `source_traceability` | number | observed provenance-field coverage indicator |
| `commercial_use` | string | review status, not a legal conclusion |

## Example

```json
{
  "records": 1000,
  "unique_records": 980,
  "duplicate_records": 20,
  "duplicate_rate": 0.02,
  "missing_required": {
    "source": 15
  },
  "pii_findings": {
    "email": 2,
    "phone_cn": 0,
    "id_cn": 0
  },
  "pii_risk": "medium",
  "declared_license": "Apache-2.0",
  "source_traceability": 0.985,
  "commercial_use": "verify_license_terms"
}
```

## Automation guidance

Consumers should treat absent fields as an incompatible report rather than silently assuming zero. Future reports should add a `report_version` field before changing existing semantics.

## Redaction guidance

Externally shared reports should avoid local file paths, matching record contents, credentials, internal source identifiers, and unreviewed personal information.

## Exit-code proposal

Future versions may use:

- `0`: completed with no blocking findings;
- `1`: input or parsing failure;
- `2`: completed with review findings;
- `3`: completed with blocking findings.
