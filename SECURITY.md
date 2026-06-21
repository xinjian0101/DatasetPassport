# Security Policy

## Supported versions

Security fixes target the current `main` branch. Historical commits and unsupported forks may not receive updates.

## Reporting a vulnerability

Do not place private datasets, personal information, credentials, access-controlled source content, or matched sensitive values in public issues.

Use GitHub private vulnerability reporting when available. If it is unavailable, open a minimal public issue without sensitive details and identify the affected commit and component.

A useful report includes:

- affected commit;
- input format and parser path;
- impact summary;
- minimal synthetic fixture;
- operating system and Python version;
- expected and actual report behavior.

## Security and data-handling boundaries

DatasetPassport processes local files and writes local reports. Users remain responsible for file permissions, secure storage, source authorization, output access controls, and review of generated reports before sharing.

Standard reports should contain counts and metadata rather than matched private values.

## Out of scope

- legal conclusions about dataset reuse;
- authorization for third-party sources;
- exposure caused by users attaching private datasets publicly;
- unsupported local modifications;
- semantic correctness or model-safety claims.

## Disclosure

Allow maintainers time to reproduce, correct, test, and document confirmed issues before public disclosure.
