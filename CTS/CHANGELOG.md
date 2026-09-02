# CTS Changelog

## Unreleased

- Added a condensed Quick Reference for implementers and reviewers, linked to the authoritative specification and supporting adoption materials.
- Added CLI distribution guidance for GitHub releases, package ecosystems, Windows portable/package-manager distribution, and internal utilities.
- Linked publishable CLI artifacts to ARHS `.hashmanifest.toml` release hash manifests.
- Clarified that ArchiveHasher and `manifest-signer.exe` are AAMHS archive-preservation signing tools, not normal CLI release signing.
- Added machine-checkable JSON fixtures, progress-output compatibility notes, a contract stability linter, and a minimal Python reference implementation.
- Added `tools/cts_validate.py` as lightweight validation support for command contracts and JSON envelope examples.
- Added JSON `data` payload guidance for command-specific result shapes.
- Added command versioning and migration notes.
- Added CI usage guidance for CTS checks.
- Added successful and error JSON output examples for the manifest-audit example command.

## 0.2.1 - 2026-06-11

- Added a reusable JSON output envelope schema for CTS-governed command tools.
- Registered the schema in the CTS suite manifest as an adopter artifact.

## 0.2.0 - 2026-06-11

- Promoted CTS to candidate maturity.
- Added command stability levels, breaking-change rules, destructive command safety rules, and release blockers.
- Clarified the PPS/WGS relationship for command-tool projects.

## 0.1.2 - 2026-06-10

- Added command contract requirements, output rules, exit code bands, and stability rules.
- Expanded command contract and CLI release checklist templates.
- Added a filled manifest-audit command contract example.

## 0.1.1 - 2026-06-10

- Added SFDS two-layer suite metadata to the CTS standard manifest.
- Added a CTS suite map example.
- Clarified README, adoption, and validation language for suite conformance versus command-tool readiness.

## 0.1.0 - 2026-06-10

- Created initial CTS documentation suite.
