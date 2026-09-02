# DRS Validation Checklist

This checklist separates DRS suite conformance from desktop application release validation.
The suite checks confirm that the DRS folder satisfies SFDS v1.0.
The release checks confirm that an adopter desktop application release satisfies DRS.

## Suite Conformance

- [ ] `README.md` explains DRS's City Hall role and names the primary specification.
- [ ] `Desktop Application Release Standard.md` is present as the authoritative DRS specification.
- [ ] `DRS.manifest.toml` describes the DRS standard suite, not an adopter project.
- [ ] `DesktopApplicationRelease.manifest.schema.toml` is separate from the DRS suite manifest.
- [ ] Adopter templates live under `templates/`.
- [ ] `Adoption-Guide.md`, `Validation-Checklist.md`, and `CHANGELOG.md` are present.
- [ ] `examples/MiniVault/` demonstrates a completed adopter suite.
- [ ] `drs.ps1` provides executable validation support.
- [ ] `Governance-Boundary.md` and `SFDS-Adoption-Note.md` explain the SFDS/WGS relationship.

## Desktop Release Validation

- [ ] Project manifest exists.
- [ ] Release note exists for the release.
- [ ] Release checklist exists.
- [ ] Artifact hash is recorded in release docs and manifest.
- [ ] Version values match across manifest, release note, and built artifact.
- [ ] Security-sensitive releases include threat/trust documentation.
- [ ] Evidence folder exists when the release makes a public or security claim.
