# DDS Validation Checklist

This checklist validates dataset readiness under DDS. SFDS suite conformance for DDS is tracked by `DDS.manifest.toml` and the DDS suite map.

- [ ] Dataset manifest exists.
- [ ] Sources are recorded.
- [ ] License status is recorded.
- [ ] Validation procedure is documented.
- [ ] Splits are documented when applicable.
- [ ] Hashes are recorded for preserved artifacts.
- [ ] Known limitations are documented.
- [ ] Collection method and transformation steps are documented.
- [ ] Removed or filtered records are explained.
- [ ] Split method, seed, and counts are recorded when applicable.
- [ ] License uncertainty is resolved before public release.
- [ ] Dataset class is identified.
- [ ] Derived datasets link to source datasets or provenance records.
- [ ] Data dictionary or schema notes exist when consumers depend on fields.
- [ ] Generated data is labeled and generation method is recorded.
- [ ] Sensitive, restricted, or licensed data handling constraints are documented.
- [ ] Evaluation sets are protected from accidental training use when applicable.
