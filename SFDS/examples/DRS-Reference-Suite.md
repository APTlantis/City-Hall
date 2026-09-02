# DRS Reference Suite Example

DRS is the first reference implementation for the SFDS standard-suite pattern.

## Suite Layer

The DRS suite is described by:

- `DRS/DRS.manifest.toml`
- `DRS/README.md`
- `DRS/Desktop Application Release Standard.md`
- `DRS/Adoption-Guide.md`
- `DRS/Validation-Checklist.md`
- `DRS/CHANGELOG.md`

These files explain what DRS governs, how it is adopted, how the suite is indexed, and how its history is preserved.

## Adopter Layer

Desktop application projects adopting DRS use:

- `DRS/DesktopApplicationRelease.manifest.schema.toml`
- `DRS/templates/ProjectName.manifest.toml`
- `DRS/templates/Release-Note.md`
- `DRS/templates/Release-Checklist.md`
- Other release, trust, provenance, migration, and withdrawal templates in `DRS/templates/`

These files govern adopter release artifacts. They do not replace the DRS suite manifest.

## Validation Layer

DRS also includes executable and example evidence:

- `DRS/drs.ps1`
- `DRS/examples/MiniVault/`

This is the SFDS reference pattern for a mature suite: human specification, machine-readable suite metadata, adopter-facing templates and schemas, examples, and validation support.
