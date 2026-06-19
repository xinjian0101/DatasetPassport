# Changelog

## Unreleased

### Added

- Versioned audit reports with generation timestamps.
- SHA-256 input checksums and input-format metadata.
- Per-field coverage reporting.
- Exact cross-file overlap analysis through `--compare`.
- Reusable record fingerprint helpers.
- Validation for non-object JSON array entries.
- Tests for checksums, coverage, overlap rates, and invalid records.
- Technical audit model and severity guidance.
- Versioned rule profile under `rules/default-rules.json`.
- CSV, JSON, and JSONL input support.
- Required-field completeness reporting.
- Privacy-pattern findings for selected identifiers.
- Provenance coverage indicator.

### Changed

- JSONL parsing now reports malformed line numbers consistently.
- Reports use the input filename rather than an absolute local path.
- Exact duplicate detection and cross-file comparison share one canonical normalization function.

### Security and privacy notes

- Reports do not include matching sensitive values by default.
- Input paths should be removed from externally shared reports when they contain internal directory names.
- Pattern matches must be manually reviewed.
- Dataset contents are processed locally by the CLI.

### Known limitations

- Cross-file comparison detects exact normalized overlap only.
- Near-duplicate and semantic overlap detection are not implemented.
- Parquet support is not included in the standard-library MVP.
- License strings are not validated against source terms.
- The risk level is based on configured match counts rather than contextual sensitivity.

## 0.1.0 — 2026-06-19

Initial executable dataset audit MVP.

## Maintenance policy

- Rule changes require a rule-profile version update.
- New privacy patterns require positive, negative, and boundary fixtures.
- Reports must distinguish observations from final review conclusions.
- Performance changes must be tested on representative record counts.
- Report-schema changes require migration notes and tests.
