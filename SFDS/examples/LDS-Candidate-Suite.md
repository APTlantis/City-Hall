# LDS Candidate Suite Example

## Purpose

This example shows SFDS applied to a library-development standard.
It gives SFDS a non-DRS, non-WGS adopter pattern where the standard governs package and SDK readiness rather than releases or workspace governance.

## Suite Identity

- Standard: LDS
- Suite manifest: `LDS/LDS.manifest.toml`
- Primary specification: `LDS/Library Development Standard.md`
- Maturity pattern: candidate standard with schema, examples, and lightweight validator support

## SFDS Suite Artifacts

| Artifact | LDS example |
| --- | --- |
| README | `LDS/README.md` |
| Primary specification | `LDS/Library Development Standard.md` |
| Suite manifest | `LDS/LDS.manifest.toml` |
| Adoption guide | `LDS/Adoption-Guide.md` |
| Validation checklist | `LDS/Validation-Checklist.md` |
| Changelog | `LDS/CHANGELOG.md` |
| Adopter schema | `LDS/LibraryInterfaceNote.schema.json` |
| Adopter template | `LDS/templates/Library-Interface-Note.md` |
| Examples | `LDS/examples/ManifestQuery.Core-Library-Interface-Note.md`, `LDS/examples/HashSuite.Core-Library-Interface-Note.md` |
| Validator | `LDS/tools/lds_validate.py` |

## Validation Notes

Validate LDS as an SFDS suite by checking:

- Required suite artifacts are present and registered.
- The library-interface note schema and template are listed as adopter artifacts.
- Examples demonstrate at least two independent library shapes before reference maturity is claimed.
- Any real-adopter promotion, such as `render-manifest.crate`, remains deferred until concrete crate artifacts exist.

LDS is a useful SFDS example because it proves candidate maturity without pretending that staged or simulated adopters are production evidence.
