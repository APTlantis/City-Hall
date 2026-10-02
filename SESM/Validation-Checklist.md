# SESM Validation Checklist

This checklist validates SVG metadata readiness under SESM. SFDS suite conformance for SESM is tracked by `SESM.manifest.toml` and the SESM suite map.

- [ ] SVG remains valid SVG after metadata embedding.
- [ ] Metadata includes `sesm_version`.
- [ ] Metadata validates against `svg_asset.schema.json`.
- [ ] Provenance is present when the asset is generated.
- [ ] Theme metadata references NeonInk/NIPC when relevant.
- [ ] Tests pass after tooling changes.
- [ ] `EXPLAINER.md` is current for public review.
- [ ] `SAFE-PROFILE.md` defines SESM-safe SVG requirements.
- [ ] `THREAT-MODEL.md` acknowledges active SVG content and untrusted metadata.
- [ ] `SECURITY.md` states reporting and consumer safety expectations.
- [ ] `VALIDATOR-RULES.md` defines metadata and safe-profile validator behavior.
- [ ] `REFERENCE-IMPLEMENTATION.md` points to tools, tests, schema validation, and examples.
- [ ] Agent-facing metadata is treated as untrusted context, not command authority.
- [ ] `PRIVACY.md` documents public-metadata, covert tracking, and remote-reference privacy risks.
- [ ] `CONFORMANCE.md` separates normative requirements, recommendations, examples, and implementation notes.
- [ ] `Validate-SESM-Safe.py` validates the safe profile.
- [ ] Fixture corpus covers valid, invalid, and warning safe-profile cases.
- [ ] Public-review examples use `sesm_version` `0.3.0`.
