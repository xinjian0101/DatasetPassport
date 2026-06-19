# Remediation Guide

This guide converts scanner findings into a repeatable review process. It is not legal advice.

## Exact duplicates

1. Confirm whether repetition is intentional.
2. Group duplicate records by source and label.
3. Keep one canonical record when repetition has no training purpose.
4. Regenerate train and evaluation splits after removal.
5. Re-run the audit and compare counts.

## Missing fields

1. Check whether the field exists under another name.
2. Define a field mapping instead of editing values manually.
3. Keep unknown values empty rather than inventing provenance.
4. Stop publication when required source or license fields are missing.

## Privacy findings

1. Isolate matching records.
2. Review the original source and collection purpose.
3. Remove, mask, aggregate, or retain with documented approval.
4. Run the scanner again after changes.
5. Keep public reports free of matching values.

## License uncertainty

- Locate the publisher-controlled terms.
- Confirm that the terms apply to the exact data version.
- Review attribution, redistribution, modification, and commercial-use conditions.
- Separate records with incompatible terms.
- Record the source page and verification date.

## Split overlap

Until automated overlap checking is added:

- audit each split separately;
- compare exact normalized fingerprints between splits;
- review close paraphrases manually or with an approved local tool;
- regenerate splits after deduplication.

## Release record

Record the dataset version, input checksum, scanner commit, rule-profile version, reviewer, unresolved findings, remediation summary, and approval date.
