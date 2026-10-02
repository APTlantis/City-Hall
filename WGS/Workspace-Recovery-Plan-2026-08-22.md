# Workspace Recovery Plan - 2026-08-22

## Purpose

This plan records the remaining workspace recovery shape after the 2026-08-22 PPS and parent-record reconciliation pass.

The immediate goal is not moving projects, finishing every project, or forcing release cleanup across the portfolios. The immediate goal is to keep the workspace understandable enough that each project can be resumed, verified, promoted, completed, or archived without another heroic rediscovery pass.

## Current Boundary

The onboarding layer answers: what is this?

The verification layer answers: does it currently work?

Those are separate phases. A project may be properly onboarded with `AGENTS.md`, an entity-named manifest, `Project-README.md`, and PPS proposal coverage while still carrying open build, test, packaging, data, deployment, or release-evidence gaps.

Filing Cabinet is the only current completed release lane noted during this recovery pass. It is recorded as a Store MSIX candidate under approval, not as proof that all DRS projects are release-ready.

## Chunk 7 - Verification Passes

Run verification only after structure and identity records are sane enough to interpret the result.

Verification should be portfolio-specific:

| Portfolio | Verification focus |
| --- | --- |
| CTS | Command contracts, help output, version output, tests, structured output, stdout/stderr behavior, exit codes, and destructive-operation safeguards. |
| DRS | Build, packaging, installer, launch, release notes, artifact hashes, signatures, install/uninstall behavior, recovery behavior, and release evidence. |
| LDS | Package/API tests, examples, public surface checks, dependency boundaries, and known consumer compatibility. |
| WDS | Build, route coverage, accessibility, deployment records, asset handling, and current published/private deployment status. |
| `.data` | Provenance, hashes, schemas, source/derived separation, regeneration notes, licensing or origin notes, and dataset consumers. |

Verification records should distinguish local checks from certification, publication, distribution signing, external availability, or long-term operational stability. A passing command is evidence for the command that was run; it is not a substitute for a release claim.

## Chunk 8 - Maintenance Loop

The workspace should settle into a repeatable maintenance loop:

1. Run a root inventory command.
2. Compare physical roots, parent manifests, child registrations, and `D:\INDEX.md`.
3. Record drift as active, intake, holding, archive, cache, reference, generated, absent, or historical.
4. Route new material through `.zoning` before promotion.
5. Promote only after parent manifests, local manifests, `AGENTS.md`, `Project-README.md`, PPS proposal coverage, and `D:\INDEX.md` are updated together.
6. Preserve a lightweight periodic audit note when a review creates useful evidence.

The repeatable root inventory command is:

```powershell
C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\ --format jsonl
```

Use the default text output for human review when JSONL is not needed:

```powershell
C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\
```

## Portfolio Reconciliation Checklist

For each portfolio root:

- Confirm the nearest `AGENTS.md` and portfolio manifest are present.
- Confirm active child registrations match physical active child directories.
- Move missing children into an absent or historical registration field instead of leaving stale active records.
- Keep holding directories named and documented as holding, not active project roots.
- Check that project manifests, `Project-README.md`, PPS proposals, and README files agree on identity, class, lifecycle, version posture, and responsibility level.
- Record verification gaps without turning them into release claims.
- Update `D:\INDEX.md` only for discovery, status, authority, or navigation changes that matter beyond the local project.

## Promotion Rule

New project material enters through `.zoning` unless the user explicitly directs a different governed root.

Promotion requires:

- A target portfolio and governing standard.
- A PPS proposal or a documented reason PPS does not apply.
- An entity-named manifest at the promoted root.
- `AGENTS.md` and `Project-README.md` at the promoted root.
- Parent manifest child registration.
- `D:\INDEX.md` discovery update when the project should be findable from the workspace index.
- A note preserving source location and promotion rationale.

Moving a directory alone is not promotion.

## Periodic Audit Note Shape

A lightweight periodic audit note should include:

- Date and operator.
- Command(s) run.
- Portfolio roots reviewed.
- Counts for parsed manifests, active project manifests, missing proposals, and malformed proposals when applicable.
- Drift found.
- Records updated.
- Verification intentionally deferred.
- Next bounded action.

Store named recovery notes under WGS migration notes or another WGS-designated audit-history location when the note is evidence worth preserving.

## Stop Condition

This recovery phase is complete when:

- Workspace and portfolio navigation records are coherent.
- Project identity/onboarding records exist for active and intake projects.
- Absent, holding, archive, cache, reference, and generated material are not mislabeled as active projects.
- Verification is queued by portfolio and project, not tangled into onboarding.
- Future agents can run the inventory command and follow the reconciliation checklist without rebuilding the map from scratch.
