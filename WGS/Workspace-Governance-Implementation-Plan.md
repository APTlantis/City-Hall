# Workspace Governance Implementation Plan

## Purpose

This package establishes the first WGS planning layer for the Aptlantis workspace on `D:\`.
It documents the current drive, the intended target layout, the standards backlog, manifest conventions, and the agent startup procedure before any broad restructuring occurs.

The objective is not bureaucracy.
The objective is reducing ambiguity so the workspace remains understandable, maintainable, recoverable, and agent-friendly over time.

## Governing Model

WGS is the workspace constitution.
It governs the environment where projects, standards, services, datasets, websites, and archives live.

The working hierarchy is:

```text
WGS
├─ PPS
├─ SFDS
│  ├─ DRS
│  ├─ CTS
│  ├─ WDS
│  ├─ DDS
│  ├─ AAS
│  ├─ ATS
│  ├─ AAMHS
│  ├─ AADR
│  ├─ SESM
│  └─ NeonInk
└─ Projects and workspace services
```

## Deliverables

This package creates the following WGS planning documents:

| Document | Role |
| --- | --- |
| `Workspace-Inventory.md` | Current-state record of top-level drive roots, manifests, mismatches, and project classes. |
| `Target-Directory-Map.md` | Target-state directory map and intended role of each root. |
| `Standards-Backlog.md` | Ordered worklists for standards normalization, drafting, and later automation. |
| `Manifest-Conventions.md` | Naming, placement, and minimum content rules for workspace, directory, project, and standard manifests. |
| `Agent-Startup-Procedure.md` | Required read order for agents entering the workspace or a project. |
| `templates/` | Starter TOML templates for future manifest instantiation. |

## Implementation Passes

### Pass 1 - Inventory

Status: complete for this package.

Actions:

- Scan the top-level roots of `D:\`.
- Record present and missing root manifests.
- Record known naming mismatches between current and target state.
- Record existing standards folders in `D:\010-CITY-HALL`.

### Pass 2 - Planning Docs

Status: complete for this package.

Actions:

- Write WGS planning docs in `D:\010-CITY-HALL\WGS`.
- Keep current state and target state explicitly separate.
- Avoid moving, renaming, deleting, or restructuring existing projects.

### Pass 3 - Manifest Templates

Status: complete for this package.

Actions:

- Create TOML templates for workspace, directory, project, and standard manifests.
- Include fields for project class, governing standard, lifecycle state, paths, relationships, and agent notes.
- Keep templates conservative until real project audits fill in exact values.

### Pass 4 - Scaffold Checklist

Status: planned.

Actions to perform later:

| Action | Target | Safety |
| --- | --- | --- |
| Create missing target roots | `D:\020-LIBRARY`, `D:\030-ZONING` | review |
| Review current library root | `D:\LIBRARY` -> target `D:\020-LIBRARY` | manual |
| Review current data/evals ordering | `D:\970-DATA`, `D:\980-EVALS` vs target `D:\970-EVALS`, `D:\980-DATA` | manual |
| Add entity-named manifests to every governed root | root directories listed in target map | safe after review |
| Add an entity-named manifest to every audited project | DRS, CTS, SIS, WDS, DDS, SFDS project directories | review |
| Replace schema-like placeholder manifests with real records | existing placeholder manifests | manual |
| Register projects in the workspace manifest | `D:\WORKSPACE.manifest.toml` | review |

### Pass 5 - Standards Roadmap

Status: planned.

Priority order:

1. WGS - workspace governance.
2. PPS - project proposals and design boundaries.
3. SFDS - standard authoring and maturity.
4. CTS - command tools and automation utilities.
5. WDS - websites and web applications.
6. DDS - datasets and corpora.

Each standard should move toward an SFDS-style document suite:

- Specification.
- Manifest schema.
- Templates.
- Examples.
- Validator notes.
- Adoption guide.
- Changelog.

## Completion Criteria

This package is complete when:

- Every document listed in the deliverables table exists under `D:\010-CITY-HALL\WGS`.
- The inventory reflects actual observed top-level roots on `D:\`.
- The target directory map is clearly marked as proposed state.
- Existing mismatches are recorded without being resolved prematurely.
- Manifest templates parse as TOML.
- No existing project directories have been moved, renamed, or deleted.
