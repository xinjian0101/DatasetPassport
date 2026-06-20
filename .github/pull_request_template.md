## Summary

Describe the reader, audit rule, comparison, report, test, or documentation change.

## Data-quality problem

Explain the failure mode this change addresses and the expected user impact.

## Behavior change

- Previous behavior:
- New behavior:
- Report-schema impact:
- Compatibility impact:

## Verification

- [ ] Added positive, negative, and boundary fixtures
- [ ] Ran `python -m unittest -v`
- [ ] Used synthetic data only
- [ ] Checked CSV, JSON, and JSONL behavior when relevant
- [ ] Checked JSON and Markdown report output when relevant
- [ ] Documented false-positive and false-negative risks

## Privacy and provenance

- [ ] Reports do not expose matched private values
- [ ] Declared license metadata remains separate from review conclusions
- [ ] New source or provenance fields are documented

## Documentation

- [ ] Updated README or CLI reference
- [ ] Updated CHANGELOG.md for user-visible behavior
- [ ] Added migration notes for report-schema changes

## Reviewer notes

Include performance measurements, representative record counts, limitations, and follow-up work.
