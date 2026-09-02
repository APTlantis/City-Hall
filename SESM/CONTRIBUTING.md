# Contributing to SESM

## Contribution Goals

SESM welcomes review focused on:

- metadata vocabulary clarity;
- safe-profile rules;
- validator behavior;
- privacy considerations;
- examples and fixtures;
- interoperability with SVG, JSON-LD, archives, crawlers, and design systems.

## Before Proposing Changes

Read:

1. `EXPLAINER.md`
2. `SAFE-PROFILE.md`
3. `THREAT-MODEL.md`
4. `PRIVACY.md`
5. `CONFORMANCE.md`
6. `VALIDATOR-RULES.md`

## Change Expectations

Proposed changes should:

- preserve the non-executable metadata boundary;
- avoid granting authority to agents, crawlers, or renderers;
- avoid embedding sensitive or private data;
- include tests or fixtures when behavior changes;
- update schema, examples, and validator rules together when vocabulary changes;
- update `CHANGELOG.md` for public-facing changes.

## Running Tests

Run:

```powershell
python SESM\tests\run_tests.py
python SESM\Validate-SESM-Safe.py SESM\fixtures\valid\basic-safe.svg --safe-profile
```

## Security and Privacy

Security issues should follow `SECURITY.md`.

Privacy-impacting changes should update `PRIVACY.md` and should explain how the change avoids covert tracking, accidental personal data exposure, and unauthorized agent behavior.

## Standards Venue Notes

If SESM moves into a formal community venue, contributor license or patent policy requirements from that venue may apply. Until then, this local suite uses the license file in this directory.
