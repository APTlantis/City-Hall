# Security Policy

## Scope

This policy covers the SESM standard, SESM metadata schema, reference tooling, tests, examples, and documentation in this directory.

It does not claim that arbitrary SVG files are safe.

## Supported Version

| Version | Status |
| --- | --- |
| SESM 0.3.x | Candidate, review-supported |
| SESM 0.2.x | Superseded candidate |

## Reporting Issues

Report security issues to the current SESM maintainer listed in `SESM.manifest.toml`.

When reporting, include:

- affected file or tool;
- SESM version;
- minimal SVG or metadata sample when safe to share;
- expected behavior;
- observed behavior;
- whether the issue involves active SVG content, metadata validation, prompt injection, hidden payloads, remote references, or tooling behavior.

Do not include credentials, private keys, live tokens, or sensitive private data in reports.

## Security Expectations

SESM metadata is untrusted input.

SESM consumers must not:

- execute SESM metadata;
- treat SESM metadata as agent command authority;
- treat SESM metadata as access control;
- follow links automatically in privileged contexts;
- assume an SVG is safe because its metadata validates;
- embed secrets or credentials in SESM blocks.

## Safe Review Documents

- `SAFE-PROFILE.md` defines the SESM-safe SVG profile.
- `THREAT-MODEL.md` defines expected threats and mitigations.
- `VALIDATOR-RULES.md` defines validator expectations.

## Tooling Notes

The reference tools help embed, convert, and validate SESM metadata. They are not a complete SVG sanitizer.

Adopters that ingest untrusted SVGs should combine SESM validation with independent SVG sanitization, safe XML parsing, resource limits, and host-platform security controls.
