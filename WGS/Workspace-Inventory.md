# D:\ Workspace Inventory

Last reviewed: 2026-08-22

## Authority

`D:\Development.manifest.toml` is the machine-readable root registry. `D:\AGENTS.md` is the operational constitution. `D:\INDEX.md` is the human-readable map. `D:\.city_hall` is the active standards and adopted overview library.

Canonical local manifests are entity-named: the exact containing directory name plus `.manifest.toml`. `Development.manifest.toml` remains the drive-root exception.

## Current Inventory Run

The read-only WGS inventory command was rerun on 2026-08-22 after `.zoning` was restored as the current intake root and `.dpw` was reconciled to the cleaned-up filesystem.
The root manifest parses and the hidden foundation roots now pass inventory. Several visible portfolio manifests still have child-list drift against the current filesystem.

| Root | Canonical manifest | Registered children | Physical children | Inventory state |
| --- | --- | ---: | ---: | --- |
| `D:\.city_hall` | `CITY-HALL.manifest.toml` | 18 | 18 | pass |
| `D:\.library` | `.library.manifest.toml` | 4 | 4 | pass |
| `D:\.dpw` | `.dpw.manifest.toml` | 3 | 3 | pass |
| `D:\.pnpm-store` | `.pnpm-store.manifest.toml` | 3 | 3 | pass |
| `D:\.data` | `.data.manifest.toml` | 3 | 3 | pass |
| `D:\.zoning` | `.zoning.manifest.toml` | 7 | 7 | pass |
| `D:\CTS` | `CTS.manifest.toml` | 12 | 8 | drift: missing `.cts_holding`, `FH-RefToolkit`, `HolyC-Llama`, `LangThemeGenerator`, `ScriptWriters`; unregistered `Single-Project Evaluator` |
| `D:\DRS` | `DRS.manifest.toml` | 8 | 9 | drift: missing `Filing Cabinet`; unregistered `CodeNote`, `File Cabinet` |
| `D:\LDS` | `LDS.manifest.toml` | 1 | 0 | drift: missing `ReactComponentLibrary` |
| `D:\WDS` | `WDS.manifest.toml` | 3 | 1 | drift: missing `LinuxGenealogy`, `WebsiteTemplate` |

## Reconciliation Notes

- `D:\BASIC`, `D:\DATA`, and `D:\.sonar` are not registered in the restored root manifest because they were not physically present during the 2026-08-20 restoration pass.
- `D:\.zoning` is present again and is registered as the current intake/incubation root with seven direct children.
- `D:\LDS` is registered as the governed portfolio for library-first projects, but its child registration currently points to missing `ReactComponentLibrary`.
- `D:\.pnpm-store` is registered as a tool-managed shared PNPM package cache.
- WDS still needs child-list reconciliation against its current physical directory.
- CTS still needs child-list reconciliation; the current audit reports `Single-Project Evaluator` as physical but unregistered and several registered children as missing.
- DRS still needs child-list reconciliation; the current audit reports a `Filing Cabinet` / `File Cabinet` naming mismatch and unregistered `CodeNote`.
- DPW now registers only physically present children: `HF`, `JetBrains`, and `Ollama`. Removed runtime/cache registrations remain noted as historical gaps rather than active children.
- `.library` registers only physically present collections.
- Strict City Hall audit repairs normalized Blue Slate artifacts, WDS `LinuxGenealogy` and `WebsiteTemplate`, CTS `ArchiveHasher`, `HolyC-Llama`, `ScriptWriters`, HolyC-Llama child layers, DRS `CodeNote`, `QB-Winget`, `WingettingQB64`, and moved DPW runtime parents.

## Repeatable Command

```powershell
python D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\
python D:\.city_hall\WGS\tools\city_hall_audit.py --root D:\.city_hall --workspace-root D:\
```

The inventory command is read-only and returns nonzero when registered roots drift from physical child directories. The City Hall audit additionally checks promoted standards, portfolio children, and foundation records.

## Remaining Work

- Perform project-specific build, test, artifact, deployment, release, and lifecycle verification before making release-readiness claims.
- Review cache/resource retention policies for `.dpw` and `.pnpm-store`.
- Reconcile child lists for CTS, DRS, LDS, and WDS against current physical directories.
- Reconcile `.zoning` child records one project at a time, especially stale DRS paths, promotion decisions, and artifact/source separation.
- Refresh root-governance recovery snapshots after root/index/agent instruction edits.
