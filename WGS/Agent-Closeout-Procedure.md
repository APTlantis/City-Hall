# Agent Closeout Procedure

## Purpose

This procedure defines the required closeout steps for agent work in a WGS-governed workspace.
Closeout makes work recoverable: a future human or agent should be able to identify what changed, why it changed, what was verified, and what still needs attention.

This procedure applies when an agent changes governed documentation, manifests, tooling, templates, examples, or project artifacts under a WGS-governed root.

## Closeout Principles

- Preserve operator work. Do not revert unrelated edits, untracked files, or in-progress changes unless the operator explicitly asks for that.
- Record decisions near the artifact they affect.
- Prefer durable repository documentation over chat-only context for changes that future agents must understand.
- Keep closeout proportional. Small edits need a concise record; standards, schemas, tools, and migrations need fuller evidence.
- Make validation limits explicit. If a check cannot run, record the blocker rather than implying the work was verified.

## Required Closeout Steps

1. Review the changed surface.
   - Identify files changed by the agent.
   - Identify unrelated pre-existing changes and leave them untouched.
   - Confirm that the completed work matches the requested scope.

2. Update direct documentation.
   - If a new artifact was added, register it in the nearest README or suite index.
   - If behavior, policy, schema, or workflow changed, update the primary document that defines that behavior.
   - If a template or example becomes the canonical pattern, update adjacent adoption or validation guidance.

3. Update extended documentation when the change affects governance.
   - For WGS-wide behavior, update the WGS README, roadmap, backlog, or validation checklist as appropriate.
   - For cross-standard behavior, update the standards backlog or documentation-suite roadmap.
   - For maturity, status, compatibility, or validation claims, update the relevant manifest or changelog only when the change actually changes that claim.

4. Record validation evidence.
   - Run the smallest meaningful checks for the touched surface.
   - Prefer read-only scans for documentation-only work.
   - For tools, run targeted tests or dry-run commands.
   - Record any checks that could not run and why.

5. Leave a concise handoff.
   - Summarize what changed.
   - Name the files that matter.
   - List validation performed.
   - List remaining follow-up items or blockers.

## Documentation Update Matrix

| Change type | Direct update | Extended update |
| --- | --- | --- |
| New WGS procedure or policy | WGS README document suite table | Validation checklist if it affects conformance |
| New WGS tool or tool behavior | Tool docstring or usage notes | WGS manifest, README, validation checklist |
| New standard-suite artifact | Standard README | Documentation-suite roadmap if maturity or suite status changes |
| New template or example | Adjacent adoption guide or README | Standards backlog if it changes planned work |
| Schema or manifest convention change | Primary specification and schema file | Changelog, manifest, migration notes if compatibility changes |
| Audit or inventory output change | Tool usage notes and output documentation | Dashboard spec, validation checklist, roadmap if status changes |

## Closeout Record Shape

Use this shape in final handoffs, changelog entries, task records, or issue comments when a durable closeout record is needed:

```text
Summary:
- <what changed>

Files:
- <path>: <reason it changed>

Validation:
- <check run>
- <check not run, with reason>

Follow-up:
- <remaining item or none>
```

## Agent-Specific Requirements

- Agents must not claim broad repository health from narrow checks.
- Agents must not mark a standard complete solely because a backlog item was organized.
- Agents must distinguish between implemented work, planned work, and optional improvements.
- Agents must include exact file paths for new governance artifacts in handoffs.
- Agents must keep unresolved validation blockers visible until a later task resolves them.

## Completion Criteria

Agent work is ready for closeout when:

- The requested scope is implemented or the blocker is documented.
- New or changed artifacts are discoverable from their suite entrypoint.
- Relevant direct and extended documentation has been updated.
- Targeted validation has been attempted and accurately reported.
- Remaining work is captured in an appropriate backlog, roadmap, or handoff note.
