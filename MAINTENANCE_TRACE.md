# Maintenance Trace

This file records visible maintenance work applied to DatasetPassport.

## Maintenance cycle 1

- Expanded the repository entry point.
- Added field guidance, quality gates, workflow notes, and explicit limitations.
- Preserved the existing command-line interface.

## Maintenance cycle 2

- Added the audit model, default rules, report format, sample report, remediation guide, and performance baseline.
- Added release-decision and report schemas.

## Maintenance cycle 3

- Added a stable CLI contract, release decision template, and performance regression policy.

## Maintenance cycle 4 — English-only documentation

### Iteration 64

- Replaced the Chinese README with a complete English project guide.
- Converted examples, tables, workflows, and limitations to English.

### Iteration 65

- Added an English command-line reference with CSV, JSON, and JSONL examples.
- Documented the current error behavior and reproducibility record.

### Iteration 66

- Updated this maintenance trace.
- Confirmed that documented field names, CLI arguments, and report semantics remain backward compatible.

## Validation record

| Check | Result |
|---|---|
| Existing CLI retained | pass |
| CSV, JSON, and JSONL scope retained | pass |
| English README completed | pass |
| English CLI reference completed | pass |
| Unimplemented source-page checks not claimed | pass |
| Technical findings remain distinct from final review decisions | pass |

## Maintenance policy

1. Every rule change requires positive and negative fixtures.
2. Report-schema changes require migration notes.
3. False positives and false negatives must be documented separately.
4. Declared license values must remain separate from verified conclusions.
5. Example records must be synthetic and non-sensitive.
6. Releases must distinguish blocking errors from review findings.
7. User-facing documentation and examples are maintained in English.

## Open items

- No automatic source-page retrieval.
- No semantic duplicate detection in the current baseline.
- No automatic compatibility decision across multiple licenses.
- No model-based quality score is claimed.
