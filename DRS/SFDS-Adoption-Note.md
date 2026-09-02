# DRS SFDS Adoption Note

DRS predates the formal WGS/SFDS structure and is treated as the reference implementation for practical standard suites.

## Authoritative Existing Artifacts

- `Desktop Application Release Standard.md`
- `DesktopApplicationRelease.manifest.schema.toml`
- `templates/`
- `examples/MiniVault/`
- `drs.ps1`

## Normalization Rule

Do not rewrite DRS from scratch.
Use SFDS to add manifest metadata, adoption context, validation tracking, and changelog continuity around the existing mature suite.

## Two-Layer Manifest Rule

- `DRS.manifest.toml` describes DRS as a standard suite.
- `DesktopApplicationRelease.manifest.schema.toml` describes DRS adopter project manifests.
- `templates/ProjectName.manifest.toml` is the starter manifest for desktop applications adopting DRS.

The adopter manifest schema and template are part of the DRS domain standard. They do not replace the suite manifest.
