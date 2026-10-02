# WGS Validation Checklist

This checklist validates workspace governance readiness under WGS. SFDS suite conformance for WGS is tracked by `WGS.manifest.toml` and the WGS suite map.

- [ ] `D:\AGENTS.md` and `D:\INDEX.md` exist.
- [ ] `D:\Development.manifest.toml` exists and parses, or its absence is recorded as root-governance drift with a dedicated restoration path.
- [ ] Root inventory is current.
- [ ] Target directory map is separate from current state.
- [ ] Governed portfolios and containers have `AGENTS.md` and `[DirectoryName].manifest.toml`.
- [ ] Projects and project groups have `AGENTS.md`, `[ProjectName].manifest.toml`, `PROJECT-READMAP.toml`, and `Project-README.md`.
- [ ] Each governed directory has exactly one canonical entity manifest.
- [ ] Standards have entity-named standard manifests.
- [ ] Governed projects have exactly one lifecycle state or a recorded lifecycle gap.
- [ ] Project classes are recorded closely enough to identify the governing domain standard.
- [ ] Shared services are registered, intentionally excluded, or queued for directory manifests.
- [ ] Metadata records support discovery by purpose, class, lifecycle state, governing standard, or relationship.
- [ ] Agent startup procedure is available.
- [ ] Agent closeout procedure requires direct and extended documentation updates before substantial tasks are complete.
- [ ] Canonical active standard links resolve under `D:\.city_hall`; City Hall-only draft and lineage material is not treated as active authority.
- [ ] Manifest physical paths and parent/child relationships match the current filesystem.
- [ ] Manifest schema expectations are checked against `EntityManifest-v2.4.schema.json` when machine-schema compatibility is in scope.
- [ ] Manifest changes are reviewed with `tools/manifest_diff.py` when field-level drift matters.
- [ ] Local Markdown links are checked with `tools/link_integrity.py` for touched documentation scopes.
- [ ] Agent read-first order is available from manifests or identity docs.
- [ ] Project read maps identify mandatory, priority, evidence, secondary, and excluded paths closely enough for bounded evaluators to avoid broad generated-directory searches.
- [ ] Direct records were updated for changed entities, or intentionally left unchanged with a reason.
- [ ] Extended navigation records such as `D:\Development.manifest.toml`, `D:\INDEX.md`, library README/maps, City Hall README/maps, parent manifests, responsibility matrices, inventories, and standards registries were updated when discovery or authority changed.
- [ ] Workspace health state is recorded for reviewed roots.
- [ ] Drift between current state and target state is recorded before moves or renames.
- [ ] Next safe action is documented for blocked or drifted roots.
- [ ] Superseded projects link to their successor.
- [ ] Paused or archived projects have enough context to be reactivated or audited later.
