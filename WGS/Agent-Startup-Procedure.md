# Agent Startup Procedure

## Purpose

This procedure defines how an agent should orient itself before working in the Aptlantis workspace.
The goal is to preserve context, reduce accidental drift, and make work recoverable.

Agent compatibility is a WGS requirement.
Agents should be able to understand workspace identity, project intent, lifecycle state, class, governing standard, and next safe action without project-specific training.

## Required Read Order

When entering the workspace or a project, read in this order:

1. `D:\AGENTS.md`
2. `D:\INDEX.md`
3. `D:\Development.manifest.toml`
4. each nearer `AGENTS.md` from the drive root toward the target
5. nearest entity-named manifest matching its containing directory
6. `Project-README.md`, when entering a project or group
7. governing standards linked by the manifests
8. roadmap, release note, or current task notes

If a required document is missing, record the gap before proceeding.

The manifest establishes machine-readable identity.
The project identity document establishes intent and boundaries.
The governing standard establishes the rules of engagement.

## Workspace Entry

For workspace-level work:

1. Read `D:\AGENTS.md` and `D:\INDEX.md`.
2. Read `D:\Development.manifest.toml`.
3. If `D:\Development.manifest.toml` is absent in a future pass, record the root-governance drift and continue from the active library records unless the task requires reconstructing the root manifest.
4. Read `D:\.city_hall\README.md`, `D:\.city_hall\WORKSHOP-MAP.md`, and the relevant active suite.
5. Use `D:\.city_hall` only when the task concerns standards incubation, promotion history, lineage, or workshop material.
6. Identify affected root directory.
7. Read that root's entity-named manifest if it exists.
8. Read the governing standard for the affected class.
9. Record any missing context in the task notes or implementation report.

## Project Entry

For project-level work:

1. Locate the project root.
2. Read parent instructions and the nearest entity-named project manifest.
3. Identify lifecycle state, project class, and governing standard from the manifest or parent root.
4. Read the proposal, roadmap, release note, or standard-specific planning docs.
5. Inspect current code or content only after the governing context is known.

## Missing Document Behavior

| Missing item | Agent behavior |
| --- | --- |
| Root `AGENTS.md` | Stop workspace-wide changes and report the blocker. |
| `D:\Development.manifest.toml` | Record root-governance drift and use `D:\INDEX.md` plus `D:\.city_hall` as the recovery path; restore the manifest only through an explicit root-governance pass. |
| Directory manifest | Continue only for read-only discovery; record missing directory manifest. |
| Project manifest | Continue only if the task is small or explicitly requested; recommend `[ProjectName].manifest.toml` creation. |
| `Project-README.md` | Avoid scope-expanding changes; use existing README/docs as fallback. |
| Governing standard | Use WGS defaults and record the missing standard link. |
| Roadmap / current notes | Ask for or infer the narrow task only; avoid unrelated cleanup. |

## Agent Work Rules

- Prefer existing standards and templates over improvising new structure.
- Treat manifests as machine records and docs as human recovery records.
- Treat lifecycle state and project class as operating context before broad changes.
- Keep current state and proposed state separate.
- Do not move, rename, or delete project roots without explicit approval.
- Record mismatches instead of silently correcting them.
- When creating new docs, include purpose, scope, required artifacts, and next action.

## Agent Closeout Procedure

An agent task is not complete merely because files, code, standards, or artifacts were changed.
Before ending a substantial session, the agent must update the documents that let the next human or agent recover the new state.

Closeout requires:

1. Update the direct records for the changed entity: manifest, `AGENTS.md`, `Project-README.md`, README, changelog, validation checklist, release note, adoption note, or standard-specific record as applicable.
2. Update the parent or controlling records when identity, lifecycle, location, authority, child lists, governing standard, or promotion state changed.
3. Update extended navigation records when the change affects workspace discovery, including `D:\Development.manifest.toml`, `D:\INDEX.md`, library README/maps, City Hall README/workshop maps, WGS responsibility matrices, inventories, target maps, or standards registries.
4. Record known gaps if an expected direct or extended document could not be updated.
5. Verify that updated links, manifests, and machine-readable records parse or resolve where practical.
6. Summarize what changed, what was intentionally left unchanged, and the next safe action.

For small code-only changes inside an already governed project, the extended records may be unchanged.
For root, standard, promotion, relocation, lifecycle, or governance changes, direct and extended documentation updates are part of the work, not a follow-up nicety.

## Handoff Notes

Every substantial agent task should leave enough context for another agent to continue:

- What was inspected.
- What changed.
- What was intentionally left unchanged.
- Which standard governs the work.
- Which documents or manifests are missing.
- Which direct and extended documentation records were updated or intentionally left unchanged.
- What the next safe action is.
