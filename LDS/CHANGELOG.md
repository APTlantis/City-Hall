# LDS Changelog

## Unreleased

- Added `LibraryInterfaceNote.schema.json`.
- Added `tools/lds_validate.py` for lightweight interface-note validation.
- Added two completed-interface validation examples.
- Added a simulated breaking-change cycle example.
- Clarified that `render-manifest.crate` remains staged until real crate artifacts exist.
- Added JSON-LD context mapping, semver/MSRV policy template, CI usage guidance, and lifecycle transition example.

## 0.2.0 - 2026-07-25

- Promoted LDS to candidate-active status.
- Added first candidate adopter example for `render-manifest.crate`.
- Clarified mixed project families where library crates use LDS and companion CLI/service surfaces use CTS/SIS.
- Expanded adoption and validation guidance for speculative APIs, stability claims, and candidate-active use.

## 0.1.0 - 2026-07-22

- Created initial LDS documentation suite (README, specification, manifest, adoption guide, validation checklist).
- Defined library stability levels (`experimental`, `interface-stable`, `versioned`, `reference`).
- Defined scope boundary against CTS, SIS, WDS, DRS, and DDS.
- Identified `render-manifest.crate` as the first candidate adopter.
