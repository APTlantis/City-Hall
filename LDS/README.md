# Library Development Standard (LDS)

![Standard](https://img.shields.io/badge/library%20standard-LDS%20v0.2.0-blue)
![Manifest](https://img.shields.io/badge/manifest-TOML-orange)
![Scope](https://img.shields.io/badge/scope-library%20crates-green)
![Status](https://img.shields.io/badge/status-candidate--active-lightgrey)

LDS governs library crates, packages, and SDKs whose primary deliverable is code that other code consumes - filling the delivery-standard gap between CTS (commands), SIS (services), WDS (websites), DRS (desktop apps), and DDS (datasets).

LDS is candidate active as of 2026-07-25. Projects may adopt it for library-shaped deliverables, while remaining validation gaps and first-adopter evidence stay visible.

## Document Suite

| File | Purpose |
| --- | --- |
| `Library Development Standard.md` | Primary LDS specification. |
| `LDS.manifest.toml` | Standard manifest. |
| `LibraryInterfaceNote.schema.json` | Machine-readable schema for interface note summaries. |
| `LibraryInterfaceNote.context.jsonld` | JSON-LD context mapping for interface note fields. |
| `templates/Library-Interface-Note.md` | Adopter template: public API surface, stability level, versioning policy, extension contracts, known consumers. |
| `Semver-Breaking-Change-Policy.md` | Semver, breaking-change, and Rust MSRV policy template. |
| `CI-Usage.md` | Local and CI snippets for LDS validator runs. |
| `examples/render-manifest.crate-Library-Interface-Note.md` | First candidate adopter example. |
| `examples/ManifestQuery.Core-Library-Interface-Note.md` | Completed public API validation example. |
| `examples/HashSuite.Core-Library-Interface-Note.md` | Second independent library validation example. |
| `examples/Breaking-Change-Cycle.md` | Simulated breaking-change cycle evidence. |
| `examples/Library-Lifecycle-Transition.md` | Example lifecycle transition from experimental to reference. |
| `tools/lds_validate.py` | Lightweight interface-note shape validator. |
| `Adoption-Guide.md` | LDS adoption procedure. |
| `Validation-Checklist.md` | Library readiness checklist. |
| `CHANGELOG.md` | LDS version history. |

## SFDS Suite Model

`LDS.manifest.toml` describes LDS as a standard suite. `templates/Library-Interface-Note.md` describes the adopter-facing record a library project fills in; it does not replace the project's normal WGS entity-named manifest.

## Role in City Hall

CTS assumes a command a human runs. SIS assumes a service that runs continuously. WDS assumes a deployed website. DRS assumes a packaged desktop release. DDS assumes a dataset. None of them assume a bare library with no entry point of its own — LDS is that standard.

A single project can combine standards by crate: a core library crate under LDS, a companion CLI crate under CTS, a companion service crate under SIS.

## Read First

1. `README.md` (this file)
2. `Library Development Standard.md`
3. `LDS.manifest.toml`
4. `templates/Library-Interface-Note.md` when adopting

## Maturity

Candidate active (Level 2 per SFDS maturity levels): templates and a first candidate adopter example exist, and real projects can test adoption.

`render-manifest.crate` (staged under `D:\.zoning`) remains the first candidate adopter. It proves the routing need for LDS, but does not yet prove stable library API maturity because no source code or public API exists.

LDS now also includes two completed-interface validation examples and a simulated breaking-change cycle so the standard can be tested without pretending that `render-manifest.crate` has been promoted.

## Related Standards

- PPS — project intent, mission, and boundaries (applies before LDS).
- WGS — workspace placement, project manifest, lifecycle state.
- CTS / SIS / WDS / DRS / DDS — adjacent delivery standards for non-library consumption shapes.
