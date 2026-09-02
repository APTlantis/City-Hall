# LDS Adoption Guide

Use LDS when a project's core deliverable is a library, crate, package, or SDK that other code consumes, and no CLI command or long-running service is the primary interface.

## Steps

1. Confirm PPS/WGS are already in place or being created during zoning intake.
2. Create `Library-Interface-Note.md` from `templates/Library-Interface-Note.md`.
3. Record the public API surface summary.
4. Assign a stability level (`experimental`, `interface-stable`, `versioned`, `reference`).
5. Document the versioning/breaking-change policy appropriate to that level.
6. Document any extension contracts (traits, interfaces, plugin points).
7. Track known consumers; update when a new consumer starts depending on the library.
8. Record known gaps instead of silently resolving them.

## SFDS Relationship

Use SFDS to maintain LDS as a standard suite.
Use LDS to govern a library's public surface, stability, versioning policy, extension contracts, and consumer tracking.

## Combining With Other Standards

If the project also ships a CLI crate or a service crate built on the library, govern those crates under CTS or SIS respectively. The `Library-Interface-Note.md` should name which companion crates exist and which standard governs each.

For mixed crate families, assign standards by consumption surface:

| Surface | Use |
| --- | --- |
| Code consumed by other code | LDS |
| Human or automation command | CTS |
| Long-running local service or API | SIS |
| Website or web app | WDS |
| Desktop application release | DRS |
| Dataset product | DDS |

## Candidate-Active Use

Candidate-active LDS may be used by real projects, but the adoption record should be honest about evidence.

- A planned or unimplemented library can adopt LDS only at `experimental`.
- `interface-stable` requires a described public surface and at least one independent consumer expectation.
- `versioned` requires a documented versioning and breaking-change policy.
- `reference` requires multiple tracked consumers and evidence of maintained change history.

Use `examples/render-manifest.crate-Library-Interface-Note.md` as the first candidate-adopter pattern, especially when a project is still in `.zoning`.
