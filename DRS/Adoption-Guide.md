# DRS Adoption Guide

Use DRS for desktop applications that produce installable or distributable releases.

## Steps

1. Read `README.md` and `Desktop Application Release Standard.md`.
2. Copy required templates from `templates/`.
3. Create or update the project manifest.
4. Write the release note before release finalization.
5. Build the final artifact.
6. Record the artifact hash in the release note, manifest, and checklist.
7. Run or manually complete the release validation checklist.

## SFDS Note

DRS predates SFDS and remains authoritative.
SFDS adds governance metadata around the DRS suite; it does not replace the existing DRS release process.

DRS follows the SFDS two-layer model:

- `DRS.manifest.toml` describes DRS as a standard suite.
- `DesktopApplicationRelease.manifest.schema.toml` and `templates/ProjectName.manifest.toml` describe project release manifests for DRS adopters.

When applying DRS, use the DRS specification, templates, schema, examples, and CLI as the release authority. Use SFDS to understand how DRS is organized as a standard suite.
