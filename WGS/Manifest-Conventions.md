# Manifest Conventions

## Purpose

Manifests make the workspace machine-readable without replacing human documentation. The current Aptlantis model is Entity Manifest v2.4.

Every v2.4 manifest starts with:

- `[manifest]` for schema identity, type, canonical filename, maintainer, and review date.
- `[entity]` for id, title, kind, class, status, description, and tags.
- A domain table such as `[workspace]`, `[directory]`, `[project]`, or `[standard]`.

## Canonical naming

| Entity | Canonical filename | Example |
| --- | --- | --- |
| Development drive | `Development.manifest.toml` | `D:\Development.manifest.toml` |
| Governed directory or container | `[DirectoryName].manifest.toml` | `D:\CTS\CTS.manifest.toml` |
| Project or project group | `[ProjectName].manifest.toml` | `D:\CTS\CloneCratesio\CloneCratesio.manifest.toml` |
| Standard suite | `[StandardName].manifest.toml` | `D:\.city_hall\WGS\WGS.manifest.toml` |

`D:\Development.manifest.toml` was restored on 2026-08-20 as the drive-root manifest.
If it is missing in a future pass, record that as root-governance drift and restore it only through an explicit root-governance pass.

The entity name is the exact containing directory name, preserving casing and punctuation. A hidden directory therefore uses names such as `.dpw.manifest.toml` or `.cts_holding.manifest.toml`.

Each governed directory has exactly one canonical entity manifest. Other TOML files may describe datasets, schemas, components, or artifacts, but they must use distinct names and must not claim to be the directory's canonical entity record.

## Required companion documents

| Entity | Required documents |
| --- | --- |
| Portfolio, container, service, reference, or archive | `AGENTS.md` and the entity-named manifest |
| Project or project group | `AGENTS.md`, the entity-named manifest, and `Project-README.md` |

`README.md` remains optional ecosystem-facing documentation. `Project-README.md` owns internal recovery, governance, architecture, operating state, evidence, roadmap, and handoff context.

## Minimum fields

Directory manifests record identity, absolute path, role/class, governance links, lifecycle, allowed contents, physical children, parent, policy, and agent orientation.

Project manifests record identity, project class, lifecycle/status, version or `not-versioned`, absolute path, governing standards, documentation, parent/children, stability, known gaps, verification evidence, and agent orientation.

## Authority and links

- Canonical active standard suites live under `D:\.city_hall`.
- City Hall-only suites and references are workshop, lineage, or candidate material until promoted or explicitly adopted.
- Manifests use resolvable absolute paths for canonical standards.
- `AGENTS.md` and README documents use Markdown links.
- Windows `.lnk` files and copied standard documents are not governance dependencies.
- Templates are non-authoritative until every placeholder is replaced.

## Migration and preservation

Do not leave a superseded generic or duplicate manifest beside the canonical entity record.

Before promotion:

1. Identify each record's role and useful evidence.
2. Reconcile current physical paths, classifications, lifecycle, and documentation.
3. Move superseded records into a dated City Hall migration archive that preserves the original relative path.
4. Record the archive paths in the canonical manifest or migration report.
5. Validate that exactly one local entity manifest remains.

Historical migration notes remain historical evidence even when they document an older convention.

## Agent requirements

The `[agent]` table identifies read-first files, authoritative local records, modification safety, known gaps, and any explicit restrictions. Agents must traverse instructions and manifests from the drive root toward the target before broad work.
