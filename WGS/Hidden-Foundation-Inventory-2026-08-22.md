# Hidden Foundation Inventory - 2026-08-22

## Scope

This pass inventories the live leading-dot foundation directories under `D:\` after the recent cleanup. It records current filesystem shape, governing records, and obvious drift. It does not move, delete, promote, build, or certify any project.

Read-only evidence command:

```powershell
C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\
```

## Summary

| Directory | Role | Current children | Inventory result |
| --- | --- | --- | --- |
| `D:\.city_hall` | Standards workshop, sandbox, lineage, review, and promotion path. | 18 standard/design/reference folders. | Pass; remains non-governing unless material is promoted into `aptlantis_core` or adopted by an active standard. |
| `D:\.library` | Active standards library plus reference collections. | `aptlantis_core`, `docusaurus`, `ghclones`, `youtube`. | Pass; `aptlantis_core` is the active authority boundary. |
| `D:\.dpw` | Shared infrastructure, caches, service state, and tool-managed storage. | `HF`, `JetBrains`, `Ollama`. | Reconciled in this pass from stale registration that still named removed runtime/cache folders. |
| `D:\.pnpm-store` | Shared PNPM content-addressed package store. | `v3`, `v10`, `v11`. | Pass; tool-managed cache, not project source. |
| `D:\.data` | Shared datasets, snapshots, dataset-producing groups, and root artifacts. | `crates.io`, `node.js`, `winget`. | Pass; dataset provenance gaps remain child-specific. |
| `D:\.zoning` | Intake and incubation for not-yet-promoted project material. | `Aegis`, `AptDiskwright`, `CloneCratesGUI`, `Ops-Control-Surface`, `WingettingQB64`, `WinTrim`, `WSL`. | Added root AGENTS, README, manifest, root registration, and intake ledger in this pass. Child onboarding remains uneven but every direct child is now named and classified. |

## Zoning Child Snapshot

| Child | Present records | Notes |
| --- | --- | --- |
| `Aegis` | Direct intake AGENTS, manifest, and Project-README added during the ledger pass. | Legacy Aegis material is now recorded as input to Pridwen, the intended renamed Rust-first/Tauri-possible successor. The nested C++ project has source, docs, artifacts, and an older manifest, but should not be directly promoted without explicit review. |
| `AptDiskwright` | AGENTS, manifest, README, Project-README, proposal, architecture docs. | Manifest is structurally useful but still records `D:\DRS` paths. |
| `CloneCratesGUI` | AGENTS, manifest, README, Project-README, release docs, build artifacts. | Manifest is structurally useful but still records `D:\DRS` paths. |
| `Ops-Control-Surface` | Direct intake AGENTS, manifest, and Project-README added during the ledger pass. | Merge-review candidate because `D:\DRS\Ops Control Surface` is physically present. |
| `WingettingQB64` | AGENTS, manifest, Project-README. | Minimal reconciliation record; manifest still records `D:\DRS` paths. |
| `WinTrim` | AGENTS, manifest, Project-README, proposal. | Manifest still records `D:\DRS` paths. |
| `WSL` | AGENTS, manifest, Project-README. | Project group with large ISO/archive artifacts; manifest still records `D:\DRS` paths. |

## Next Work

- Reconcile `.zoning` child records one at a time, starting with stale path drift and promotion decisions.
- Decide target homes before moving anything: likely DRS for desktop apps, CTS for command tooling, LDS for reusable libraries, WDS for websites, `.data` for durable datasets, and `.dpw` only for shared service/cache state.
- Refresh CTS, DRS, LDS, and WDS parent child lists in separate portfolio passes.
- Keep City Hall as reference/playground unless a standard is explicitly promoted into `D:\.city_hall`.
