# AAMHS Validation Checklist

This checklist validates archive integrity readiness under AAMHS. SFDS suite conformance for AAMHS is tracked by `AAMHS.manifest.toml` and the AAMHS suite map.

- [ ] Hash suite is declared.
- [ ] Hash manifest exists.
- [ ] Integrity record exists.
- [ ] Archive files are referenced unambiguously.
- [ ] Validation procedure is documented.
- [ ] Signature policy is recorded when signatures are used.
- [ ] File sizes are recorded when known.
- [ ] Hash generation date and tool/command are recorded when practical.
- [ ] Hash manifest passes `tools/aamhs_validate.py` or equivalent verification.
- [ ] Detached signatures are checked with `tools/aamhs_signature_check.py` when signatures are used.
- [ ] Integrity record states what archive or collection is covered.
- [ ] Missing files, known gaps, or validation limits are documented.
- [ ] ARHS is used separately for release hash manifests when applicable.
- [ ] AAMHS detached signatures are not described as replacing Store, Authenticode, or package-ecosystem signing/provenance.
