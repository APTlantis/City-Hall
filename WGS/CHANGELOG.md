# WGS Changelog

## Unreleased - 2026-07-08

- Promoted the adopted Aptlantis overview path to `D:\.city_hall` by adding the library README/map, copying the City Hall Operational Case Study PDF there, and reframing City Hall as workshop/sandbox/lineage rather than the active standards front door.
- Restored `D:\Development.manifest.toml` from current physical roots and live entity manifests, then updated WGS startup, validation, manifest convention, and inventory guidance to treat it as the active root registry while preserving drift behavior if it goes missing again.
- Updated live WGS tooling/templates to use `D:\.city_hall` active-standard paths, added a local TOML writer fallback for runtimes without `tomli_w`, and moved the root-governance snapshot default into the active WGS suite.
- Recorded the 2026-08-20 root inventory drift results after the restored root manifest parsed successfully.
- Added the 2026-08-22 hidden-foundation inventory, restored `.zoning` as the current intake root, and reconciled `.dpw` to the cleaned-up live children.
- Added the `.zoning` intake ledger and lightweight direct-child front-door records for `Aegis` and `Ops-Control-Surface`.
- Recorded the first incoming project queue for DRS/CTS recovery, including Pridwen as the renamed Rust-first successor direction for Aegis.
- Added Entity Manifest v2.4 JSON Schema export, WGS CI usage guidance, manifest diff tooling, Markdown link integrity tooling, query-store reference notes, and a minimal static workspace-health dashboard example.
- Reconciled `D:\Development.manifest.toml`, root/portfolio manifests, and `Workspace-Inventory.md` with the current physical `D:\` root layout; the read-only workspace inventory now passes for every registered root.
- Added `Workspace-Recovery-Plan-2026-08-22.md` to separate project onboarding from portfolio-specific verification passes and define the repeatable maintenance loop.
- Added agent closeout requirements for direct and extended documentation updates, including `D:\Development.manifest.toml`, `D:\INDEX.md`, parent manifests, responsibility matrices, inventories, and standards registries when discovery or authority changes.
- Added `PROJECT-READMAP.toml` as a WGS-governed project discovery form and updated scaffolding so new project roots receive a starter read map.
- Updated `city_hall_audit.py` to audit portfolio paths registered in `Development.manifest.toml` instead of assuming every portfolio directory is the uppercase portfolio ID; this supports the canonical `D:\.data` root.
- Finalized entity-named manifests for the current `D:\` layout after a one-day fixed-name trial.
- Archived conflicting live legacy records under `migration-notes/Legacy-Live-Manifests-20260708` before promotion.
- Added metadata reconciliation, normalization, scaffold, inventory, duplicate-authority, holding, and shortcut validation tooling.
- Added root, directory, and project `AGENTS.md` templates plus a `Project-README.md` template.
- Updated agent startup order to inherit instructions from the drive root toward the target and resolve governance through canonical `.city_hall` links.
- Preserved the superseded fixed-name decision as historical migration evidence.

## 0.2.7 - 2026-06-12

- Added SIS to the City Hall standards suite as the delivery standard for services and infrastructure.
- Updated project-class delivery-standard guidance, responsibility matrix, roadmap, and reference index for SIS.

## 0.2.6 - 2026-06-11

- Updated the documentation suite roadmap for NeonInk SESM v0.3.x compatibility-note cleanup.

## 0.2.5 - 2026-06-11

- Updated the documentation suite roadmap for SESM v0.3.0 public-review readiness, privacy/conformance materials, safe-profile validator, and fixture corpus.
- Expanded the City Hall audit to verify manifest-declared governance notes.

## 0.2.4 - 2026-06-11

- Updated the documentation suite roadmap for the SESM `llm.interpretation_hints` vocabulary change and NeonInk mirrored SESM example alignment.
- Updated the ecosystem overview reference to describe SESM LLM metadata as non-authoritative interpretation context.

## 0.2.3 - 2026-06-11

- Updated the documentation suite roadmap for SESM public-review readiness, safe-profile framing, threat-model documentation, and external validator notes.

## 0.2.2 - 2026-06-11

- Added a lightweight City Hall standard-suite audit script.
- Added a generated standards audit health record as a WGS reference example.
- Linked WGS validation metadata to the repeatable audit utility.

## 0.2.1 - 2026-06-11

- Updated coordination docs to match current standard maturity states, entity-named manifest convention, and the expanded 14-standard suite.
- Added ARHS to the responsibility matrix and clarified the boundary between release-artifact hashing and archive preservation integrity.
- Refreshed the documentation roadmap, standards backlog, and workspace inventory after the PPS/CTS/WDS/DDS/ATS/AAS/ARHS/AAMHS/AADR development passes.

## 0.2.0 - 2026-06-11

- Expanded WGS into the architectural constitution for the Aptlantis workspace.
- Added the four-layer workspace architecture: standards, projects, shared services, and metadata.
- Defined project lifecycle states, project classes, metadata spine expectations, standards hierarchy, and agent-first governance rules.
- Clarified that Entity Manifest v2.4 is current while older Project Manifest v2.3 records remain historical evidence until migrated.
- Expanded validation and agent startup guidance for lifecycle visibility, discoverability, shared services, and long-term recoverability.
- Restored the entity-named manifest convention for directory and standard manifests.

## 0.1.5 - 2026-06-11

- Aligned the reusable standard manifest template with SFDS v1.0.
- Clarified that README files are role/index documents and primary specifications are authoritative standard documents.

## 0.1.4 - 2026-06-10

- Completed numbered category rollout for DRS, CTS, WDS, and DATA roots.
- Added manifests for top-level service/cache roots.
- Updated workspace inventory and target map with implemented category layout.
- Corrected the initial migration note and added a category migration note.

## 0.1.3 - 2026-06-10

- Adapted the default TOML manifest model from project-only v2.3 to entity-aware v2.4.
- Updated workspace, directory, and project manifest templates with `[manifest]` and `[entity]` headers.
- Recorded workspace structure rollout state in inventory and target map.

## 0.1.2 - 2026-06-10

- Added the workspace health model to the WGS specification.
- Added a workspace health record template and a filled City Hall health example.
- Expanded validation checks for health state, drift, and next safe action.

## 0.1.1 - 2026-06-10

- Added SFDS two-layer suite metadata to the WGS standard manifest.
- Added a WGS suite map example.
- Clarified README, adoption, and validation language for SFDS suite conformance versus workspace governance readiness.
- Updated the documentation suite roadmap for the City Hall normalization pass.

## 0.1.0 - 2026-06-10

- Added formal WGS standard suite wrapper.
- Linked existing workspace inventory, target map, manifest conventions, and agent startup procedure.
