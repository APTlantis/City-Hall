# LDS Validation Checklist

This checklist validates library readiness under LDS and separates suite conformance from adopter/domain readiness.

## Suite Validation

- [ ] `README.md` exists and explains the standard's City Hall role.
- [ ] Primary specification exists and is named by the README.
- [ ] `LDS.manifest.toml` exists and describes the standard suite.
- [ ] Scope and non-goals are clear.
- [ ] Adopter template (`templates/Library-Interface-Note.md`) is separate from the standard-suite manifest.
- [ ] At least one candidate adopter example exists.
- [ ] Validation procedure is documented.
- [ ] Interface notes pass `tools/lds_validate.py` or equivalent review.
- [ ] Known gaps are recorded.

## Adopter / Domain Validation

- [ ] `Library-Interface-Note.md` (or equivalent) exists.
- [ ] Public API surface is described.
- [ ] Stability level is assigned.
- [ ] Versioning/breaking-change policy matches the claimed stability level.
- [ ] Extension contracts (traits, interfaces, plugin points), if any, are documented well enough for a new implementer to use without reading core source.
- [ ] Known consumers are tracked once a second consumer exists.
- [ ] Companion CLI or service crates, if any, name which standard (CTS/SIS) governs them.
- [ ] Unimplemented or speculative APIs are not labeled `interface-stable`, `versioned`, or `reference`.

## Candidate-Active Gaps

- [x] LDS has been validated against completed public API examples.
- [x] LDS has been validated against two independent library examples.
- [x] LDS has been tested against a simulated breaking-change cycle.
- [ ] `render-manifest.crate` has not been promoted from staging because concrete crate artifacts do not yet exist.
