# Support

## Start here

Review these documents before opening an issue:

- [README](README.md) for commands and supported formats
- [About](ABOUT.md) for project scope and maturity
- [CLI Reference](docs/CLI_REFERENCE.md) for command usage
- [Audit Model](docs/AUDIT_MODEL.md) for finding semantics
- [Remediation Guide](docs/REMEDIATION_GUIDE.md) for follow-up actions
- [Report Format](docs/REPORT_FORMAT.md) for output structure

## Bug reports

Use the structured **Bug report** form for parser, audit, comparison, checksum, coverage, or report defects.

Include:

- exact commit or release;
- operating system and Python version;
- file format and approximate record count;
- minimal synthetic fixture;
- required-field and declared-license arguments;
- comparison file details when relevant;
- expected and actual report behavior.

## Feature requests

Use the **Feature request** form. Define the data-quality problem, proposed report fields, false-positive and false-negative risks, privacy impact, performance expectations, and acceptance criteria.

## Data-sharing rules

Do not upload private datasets, credentials, personal information, access-controlled content, or matched sensitive values. Reduce every example to a synthetic fixture that preserves only the structure needed to reproduce the issue.

## Scope boundaries

DatasetPassport does not provide:

- legal conclusions about reuse rights;
- automatic source authorization;
- semantic correctness review;
- near-duplicate or model-quality guarantees;
- privacy clearance based only on pattern counts.

## Report interpretation

`pass`, `review`, and `blocking` are technical workflow statuses. They are not legal, privacy, safety, or publication approvals.

## Response expectations

Support is best effort. Reports with exact commands, small fixtures, and clearly stated expected behavior receive the most reliable review.
