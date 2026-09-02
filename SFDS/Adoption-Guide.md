# SFDS Adoption Guide

Adopt SFDS when a document is intended to govern repeated work across multiple projects or agents.

## Steps

1. Create a standard folder under `D:\010-CITY-HALL`.
2. Add `README.md` that explains the standard's role in City Hall, names the primary specification, and maps suite artifacts versus adopter artifacts.
3. Write the primary specification with scope, non-goals, rules, validation expectations, compatibility policy, and adoption blockers.
4. Add `[StandardName].manifest.toml` for the standard suite.
5. Add adopter-facing schemas or manifest templates when the standard governs project or artifact records.
6. Add templates, examples, validation checklist, adoption guide, and changelog.
7. Assign a maturity level.
8. Record known adopters when real projects begin using it.

## Two-Layer Manifest Rule

Use `[StandardName].manifest.toml` for the standard suite itself.
Use domain-specific schemas and templates for adopter projects or artifacts.

Example: DRS uses `DRS.manifest.toml` for the DRS suite and `DesktopApplicationRelease.manifest.schema.toml` plus `templates/ProjectName.manifest.toml` for desktop release adopters.

## README and Specification Rule

The README is the entry point. It explains what the standard is for, how it fits City Hall, and what to read first.

The primary specification is the authority. It contains the actual rules, validation expectations, and compatibility policy.

Do not make the README the only standard document unless the standard is explicitly still at concept maturity.

## Existing Mature Standards

If a standard predates SFDS and already works in practice, preserve its authoritative specification, examples, templates, and tools.
Normalize it by adding SFDS metadata, clarifying governance boundaries, and separating suite validation from domain validation.

## Known Adopters

These standard suites currently use the SFDS suite model:

| Standard | Adoption role | Evidence |
| --- | --- | --- |
| DRS | Reference implementation for mature release-standard suites | `DRS/DRS.manifest.toml`, `SFDS/examples/DRS-Reference-Suite.md` |
| WGS | Candidate governance-standard suite using SFDS structure | `WGS/WGS.manifest.toml`, `SFDS/examples/WGS-Candidate-Suite.md` |
| PPS | Candidate proposal-standard suite using SFDS structure | `PPS/PPS.manifest.toml` |
| CTS | Candidate command-tool standard suite using SFDS structure | `CTS/CTS.manifest.toml` |
| WDS | Candidate website standard suite using SFDS structure | `WDS/WDS.manifest.toml` |
| AAMHS | Candidate archive-integrity standard suite using SFDS structure | `AAMHS/AAMHS.manifest.toml` |
| ARHS | Candidate active release-hash standard suite using SFDS structure | `ARHS/ARHS.manifest.toml` |
| SESM | Candidate metadata standard suite using SFDS structure | `SESM/SESM.manifest.toml` |
| LDS | Candidate-active library standard suite using SFDS structure | `LDS/LDS.manifest.toml` |

## Adoption Complete

Adoption is complete when a future agent can read the suite and know what the standard governs, how to apply it, how to validate it, and where its version history lives.
