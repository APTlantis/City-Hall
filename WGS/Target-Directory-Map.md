# Target Directory Map

## Purpose

This document defines the proposed target state for the Aptlantis workspace.
It is not a migration log and does not authorize moves by itself.

Current state is recorded in `Workspace-Inventory.md`.

## Target Roots

| Path | Role | Governing standard | Required manifest |
| --- | --- | --- | --- |
| `D:\.agents` | Drive-level agent directory and agent-facing workspace services | WGS / ATS | `.agents.manifest.toml` |
| `D:\010-CITY-HALL` | Canonical standards, rules, frameworks, references | WGS / SFDS | `010-CITY-HALL.manifest.toml` |
| `D:\015-DPW` | Public works and shared services | WGS | `015-DPW.manifest.toml` |
| `D:\020-LIBRARY` | Document nexus | WGS | `020-LIBRARY.manifest.toml` |
| `D:\030-ZONING` | Initial project scaffolding area for required docs | WGS / PPS | `030-ZONING.manifest.toml` |
| `D:\100-DRS` | Desktop application projects | DRS | `100-DRS.manifest.toml` |
| `D:\200-CTS` | Command-line tools and automation utilities | CTS | `200-CTS.manifest.toml` |
| `D:\300-WDS` | Websites and web applications | WDS | `300-WDS.manifest.toml` |
| `D:\400-DDS` | Datasets, corpora, and training data projects | DDS | `400-DDS.manifest.toml` |
| `D:\500-SFDS` | Standards and framework projects | SFDS | `500-SFDS.manifest.toml` |
| `D:\960-QB` | QuickBASIC / QB64 ecosystem | WGS | `960-QB.manifest.toml` |
| `D:\970-EVALS` | Evaluation records, local benchmark results, analysis outputs | AAS / WGS | `970-EVALS.manifest.toml` |
| `D:\980-DATA` | General data storage and governed data assets | DDS / WGS | `980-DATA.manifest.toml` |
| `D:\990-TESTS` | Workspace-level tests and validation fixtures | WGS | `990-TESTS.manifest.toml` |

## Directory Numbering Intent

| Range | Meaning |
| --- | --- |
| `000-099` | Governance, references, setup, and staging |
| `100-199` | Desktop release projects |
| `200-299` | Command tools and automation |
| `300-399` | Websites and web applications |
| `400-499` | Datasets and corpora |
| `500-599` | Standards and framework projects |
| `900-999` | Legacy, evaluation, data, tests, and special-purpose roots |

## Implemented Category Numbering

| Root | Category | Purpose |
| --- | --- | --- |
| `D:\100-DRS` | `110-CRYPTO` | Cryptography, trust, and security-sensitive desktop apps. |
| `D:\100-DRS` | `120-STORAGE` | Storage, vault, and local data desktop apps. |
| `D:\100-DRS` | `130-ARCHIVAL` | Archival desktop apps and plugins. |
| `D:\100-DRS` | `140-TAURI` | Tauri/webview desktop applications. |
| `D:\100-DRS` | `150-QB` | QB-related desktop utility packages. |
| `D:\100-DRS` | `160-UTILITIES` | General desktop utilities. |
| `D:\200-CTS` | `210-CONVERSION` | Conversion and transformation command tools. |
| `D:\200-CTS` | `220-API` | API acquisition and reference tooling. |
| `D:\200-CTS` | `230-HASHING` | Hashing and integrity command tools. |
| `D:\200-CTS` | `240-DATA-PIPELINES` | Dataset and training pipeline tools. |
| `D:\200-CTS` | `250-DOCS-SCRIPTING` | Documentation, project analysis, and script-writing tools. |
| `D:\200-CTS` | `260-LLM` | LLM-related command tooling. |
| `D:\200-CTS` | `270-MEDIA` | Media and asset generation tools. |
| `D:\300-WDS` | `310-aptlantis.net` | Canonical aptlantis.net website project. |
| `D:\300-WDS` | `320-aptlantis.studio` | Canonical aptlantis.studio website project. |
| `D:\300-WDS` | `330-TEMPLATE` | Web templates and starters. |
| `D:\300-WDS` | `340-SITES` | Additional website projects. |
| `D:\300-WDS` | `390-SERVER` | Website server infrastructure. |
| `D:\980-DATA` | `981-CRATESIO` | Crates.io data assets. |
| `D:\980-DATA` | `982-NODEJS` | Node.js data assets. |
| `D:\980-DATA` | `983-WINGET` | Winget data assets. |

## Standard Project Layout

Every governed project should eventually have:

```text
ProjectRoot\
├─ ProjectName.manifest.toml
├─ PROJECT.md or proposal document
├─ README.md
├─ docs\
├─ templates\          # if the project defines reusable docs or structures
├─ examples\           # if the project defines a standard or reusable pattern
└─ tests\              # if validation is executable
```

Project-specific standards can add required folders, but WGS requires an entity-named manifest and enough human-readable context for future recovery. The reusable `project.manifest.toml` file remains the generic v2.4 template/schema default.

## Standard / Framework Layout

Standards governed by SFDS should move toward:

```text
StandardRoot\
├─ StandardName.manifest.toml
├─ README.md
├─ [Standard Name].md
├─ schema\
├─ templates\
├─ examples\
├─ validators\
├─ adoption-guide.md
└─ CHANGELOG.md
```

## Migration Rule

No current root should be renamed, moved, or merged only because this target map exists.
Every structural change requires:

- Current-state inventory entry.
- Target path.
- Reason for the change.
- Safety classification.
- Manual approval if data could be orphaned, duplicated, or made harder to recover.

## Implementation Status

As of 2026-06-11, the primary target roots use entity-named manifest records.
The live workspace manifest uses Aptlantis Entity Manifest v2.4 so directories and projects are both first-class manifest entities.

Completed structural migrations:

- `D:\LIBRARY` -> `D:\020-LIBRARY`
- `D:\970-DATA` -> `D:\980-DATA`
- `D:\980-EVALS` -> `D:\970-EVALS`
- created `D:\030-ZONING`
- restored legacy root manifests to canonical entity-named manifest files
- added directory manifests to top-level service/cache roots
- categorized DRS, CTS, WDS, and DATA child roots into numbered groups
