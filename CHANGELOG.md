# Changelog

## Unreleased

### Added

- Technical audit model and severity guidance.
- Versioned rule profile under `rules/default-rules.json`.
- CSV, JSON, and JSONL input support.
- Exact normalized-record duplicate detection.
- Required-field completeness reporting.
- Privacy-pattern findings for selected identifiers.
- Provenance coverage indicator.
- GitHub Actions test workflow and a public roadmap issue.

### Security and privacy notes

- Reports do not include matching sensitive values by default.
- Input paths should be removed from externally shared reports when they contain internal directory names.
- Pattern matches must be manually reviewed.
- Dataset contents are processed locally by the CLI.

### Known limitations

- Near-duplicate and semantic overlap detection are not implemented.
- Parquet support is not included in the standard-library MVP.
- License strings are not validated against source terms.
- The risk level is based on configured match counts rather than contextual sensitivity.

## 0.1.0 — 2026-06-19

Initial executable dataset audit MVP.

## Maintenance policy

- Rule changes require a rule-profile version update.
- New privacy patterns require positive, negative, and boundary fixtures.
- Reports must distinguish observations from legal conclusions.
- Performance changes must be tested on representative record counts.
