# DRS Changelog

## Unreleased

- Added a condensed Quick Reference for implementers and release reviewers, linked to the authoritative specification and supporting adoption materials.
- Restored the `examples/MiniVault/` adopter example from the City Hall reference copy so the active DRS suite's declared reference examples resolve again.
- Added Microsoft Store MSIX as the default public Windows GUI application distribution path.
- Clarified that Store-submitted MSIX packages are signed by Microsoft, while sideloaded self-signed MSIX packages are development/test builds only.
- Added `winapp` and `msstore` workflow guidance for Windows GUI packaging and Store submission.
- Clarified that Microsoft Store product identity should be reserved before building the submission package and that first submissions may use Partner Center website upload for certification feedback.
- Clarified that ARHS hash evidence for Store packages is generated after the final Store candidate passes package acceptance, not before identity/display/asset corrections.
- Clarified cross-platform GUI packaging: use MSIX/Microsoft Store for the Windows build while keeping native or ecosystem package flows for other platforms.
- Added direct MSI/EXE distribution guidance requiring documented rationale and appropriate signing/provenance.
- Linked publishable desktop artifacts to ARHS `.hashmanifest.toml` release hash manifests.
- Added release-note metadata schema, JSON-LD template, companion integrity checker, release-gating workflow guidance, and a minimal release-folder verifier example.
- Added CI usage guidance for running `drs.ps1` from local automation and Windows CI.
- Added troubleshooting, PowerShell 7 compatibility, and script trust guidance.
- Added optional BLAKE3 support to `drs.ps1 hash` and `check-release` when `b3sum` or `blake3` is available.
- Added a second filled adopter manifest example, `examples/FieldDesk/FieldDesk.manifest.toml`.

## 1.0.2 - 2026-06-11

- Promoted DRS to SFDS reference maturity after SFDS v1.0 stabilization.
- Updated suite validation language to distinguish DRS folder conformance from adopter desktop release validation.
- Clarified README language so DRS is explicitly the reference implementation for the mature City Hall standard-suite pattern.

## 1.0.1 - 2026-06-10

- Clarified that DRS conforms to SFDS at the standard-suite governance layer while remaining authoritative for desktop release behavior.
- Documented the two-layer manifest model for the DRS suite and DRS adopter project manifests.
- Added SFDS-facing manifest metadata for validators, governance notes, reference examples, and adopter artifacts.
- Clarified that the DRS validation checklist is for release readiness, not SFDS suite conformance.

## 1.0.0 - 2026-06-10

- Registered DRS under WGS/SFDS with a standard manifest.
- Preserved existing DRS specification, schema, templates, examples, and CLI as authoritative.
