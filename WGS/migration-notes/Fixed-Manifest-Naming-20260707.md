# Fixed Manifest Naming Migration — 2026-07-07

> Historical trial, superseded on 2026-07-08 by the permanent entity-named convention documented in `Entity-Named-Live-Migration-20260708.md`. This file is retained as decision history and is not current policy.

## Decision

The current `D:\` development layout uses fixed lowercase manifest names:

- `directory.manifest.toml` for governed portfolios and containers.
- `project.manifest.toml` for individual projects and project groups.

Identity belongs in `[entity]`, not in the filename. `D:\Development.manifest.toml` remains the drive-level identity record.

## Reason

The workspace accumulated entity-named, uppercase, generic, and historical filenames during earlier numbered-directory rollouts. Fixed names make inheritance and validation predictable while allowing directories to move without renaming their canonical record.

## Preservation rule

Legacy manifests must not be deleted merely because a new canonical record exists. Their useful fields must be reconciled into the new record, contradictions recorded under migration gaps, and disposition reviewed manually. Until that review, they are historical evidence and not parallel authority.

## Documentation roles

- `AGENTS.md`: executable modification rules and boundaries.
- `directory.manifest.toml`: machine-readable portfolio or container truth.
- `project.manifest.toml`: machine-readable project or project-group truth.
- `Project-README.md`: internal project orientation, architecture, state, workflows, evidence, roadmap, and handoff context.
- `README.md`: optional ecosystem-facing or user-facing entry point.
