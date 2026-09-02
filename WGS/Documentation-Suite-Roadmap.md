# Documentation Suite Roadmap

## Purpose

This roadmap tracks documentation-suite normalization across Aptlantis standards.
Detailed action items from the 2026-07-30 standards evaluation are tracked in `Standards-Evaluation-Backlog.md`; this roadmap remains the maturity and suite-status summary.

| Standard | Current maturity | Suite status | Next action |
| --- | --- | --- | --- |
| WGS | Candidate v0.2.7 | Workspace constitution, lifecycle, metadata spine, manifest naming, agent startup and closeout, audit tooling, SIS integration, dashboard data contract, manifest-to-metric mapping, and suite roadmap aligned | Use structured audit outputs for named health snapshots when a review or migration checkpoint requires preserved evidence. |
| SFDS | Stable v1.0.0 | Governs suite structure and standard maturity | Add validators for suite completeness and link integrity. |
| PPS | Candidate v0.2.2 | Project intent, proposal readiness, WGS lifecycle alignment, delivery-standard mapping, and cross-project examples deepened | Use examples to seed future project proposals. |
| DRS | Reference v1.0.2 | Mature reference implementation | Keep DRS authoritative and use it as the reference pattern for validators. |
| CTS | Candidate v0.2.1 | Command contracts, output rules, stability levels, destructive command safety, and JSON output envelope schema defined | Add command-specific schema examples as tools mature. |
| SIS | Candidate v0.1.0 | Service and infrastructure lifecycle, health, ports, storage, logs, resource bounds, runbooks, and recovery rules defined | Apply SIS to shared services and infrastructure roots. |
| WDS | Candidate v0.2.1 | Deployment evidence, route checks, accessibility, metadata, rollback rules, site schema, and accessibility/metadata example defined | Add production deployment examples as real sites mature. |
| DDS | Candidate v0.2.1 | Dataset classes, provenance, validation, splits, integrity, release blockers, schema, and license/split examples defined | Add production dataset snapshots as real datasets mature. |
| ATS | Candidate v0.2.1 | Task lifecycle, context capture, validation records, handoffs, replayability, examples, and lightweight schema defined | Use ATS records for long-running standards work. |
| AAS | Candidate v0.2.1 | Analysis manifests, metric rules, comparisons, interpretation boundaries, blockers, example run records, and schema defined | Use AAS for standards-health trend analysis. |
| ARHS | Candidate v0.3.0 | Active library copy promoted; release hash manifests aligned with ReleaseHasher, SHA256, BLAKE3-256, KT128, distribution channel, and signing/provenance authority | Add validator support for `.hashmanifest.toml` when release tooling is finalized. |
| AAMHS | Candidate v1.0.3 | Archive preservation integrity boundary clarified against ARHS with example records and hash manifest schema | Add archive validator support when preservation workflow stabilizes. |
| AADR | Candidate v1.0.3 | Representation record, levels, compatibility, validation boundaries, example, and schema defined | Add richer component-map examples as representations mature. |
| SESM | Candidate v0.3.0 | Public-review candidate with metadata spec, schema, safe profile, privacy/conformance materials, threat model, validator, fixtures, tests, and non-authoritative `llm.interpretation_hints` vocabulary registered | Seek external review on safety, privacy, validator behavior, and interoperability. |
| NeonInk | Candidate v0.1.6 | Design-language suite registered with app-surface guidance, SESM v0.3.x-aligned examples/compatibility notes, and legacy manifest preserved | Deepen contract classification without flattening existing docs/assets. |

## 2026-06-10 Normalization Pass

The DRS reference pattern is now applied across the City Hall standards at the suite-governance layer.
Each standard has or now references:

- Entity-named standard manifests as suite manifests.
- Adopter-facing schemas, manifest templates, or document templates where available.
- A suite map or reference example under `examples/`.
- README, adoption, and validation wording that separates SFDS suite conformance from domain readiness.

## 2026-06-10 Deepening Pass

The first post-normalization deepening pass added practical adopter guidance to the next queued standards:

- WGS: workspace health states, drift rules, health record template, and City Hall health example.
- PPS: proposal readiness levels, proposal quality rules, expanded proposal template, and filled CLI proposal example.
- CTS: command contract requirements, stdout/stderr rules, exit code bands, stability policy, and filled command contract example.
- WDS: deployment evidence requirements, readiness levels, expanded site/deployment templates, and filled deployment example.
- DDS: provenance requirements, dataset readiness levels, validation rules, expanded dataset/provenance templates, and filled provenance example.

## 2026-06-11 Standards Development Pass

The standards suite now uses entity-named manifests and updated maturity states:

- SFDS is stable and defines the standard-suite contract.
- DRS is the reference implementation.
- WGS, PPS, CTS, SIS, WDS, DDS, ATS, AAS, ARHS, AAMHS, AADR, SESM, and NeonInk are active candidate standards or mature candidate suites.
- ARHS owns release hash manifests and distribution/signing provenance records; AAMHS owns archive preservation integrity.
- ATS records agent task history; AAS records analytical credibility.
- PPS owns project intent before implementation; WGS owns placement, lifecycle visibility, and workspace metadata.
- SIS fills the service and infrastructure delivery-standard gap for WGS shared services.

## 2026-06-10 Structure Rollout

The workspace structure rollout created the target root layout, renamed legacy root manifests to canonical names, and adapted the default TOML model from project-only v2.3 to entity-aware v2.4.

- Every governed top-level target root should use an entity-named manifest.
- Every bounded project root under the governed class roots now has an entity-named project manifest.
- `D:\WORKSPACE.manifest.toml` is the v2.4 workspace registry.
- Migration notes are preserved under `WGS/migration-notes/`.
