# Workspace Governance Standard

## Status

Candidate v0.2.7.

WGS is the architectural constitution of the Aptlantis workspace.
It governs the environment itself: where things live, how they are registered, how context survives, how agents orient, and how workspace health is judged.

## Scope

WGS governs the Aptlantis workspace as a first-class system: root directories, project registration, manifests, workspace services, standard relationships, agent startup, lifecycle visibility, and workspace health.

## Does Not Govern

WGS does not define how desktop apps release, how command tools print output, how services run, how websites deploy, how datasets are licensed, or how libraries manage public APIs.
Those responsibilities belong to DRS, CTS, SIS, WDS, DDS, LDS, and related standards.

## Core Rule

Projects create artifacts.
Standards govern projects.
WGS governs the workspace where they live.

## Paradigm

The workspace should not depend on memory.
It should describe itself clearly enough that a paused project, standard, or service can be understood years later.

WGS is successful when it makes work easier to resume, not harder to start.

WGS shifts the workspace from a collection of repositories into a governed ecosystem.
The goal is to prevent architectural entropy: orphaned repositories, forgotten prototypes, ambiguous roots, and project histories that only survive in one person's memory.

## Core Principles

| Principle | Meaning |
| --- | --- |
| The workspace is a system | The workspace is a durable asset. One dormant project must not make the broader environment harder to understand. |
| Projects must be discoverable | A project can be found and understood through manifests, registries, and read-first documents without source-code archaeology. |
| Context must survive time | Documentation and manifests preserve intent, boundaries, and state so work can be resumed after long dormancy. |
| Standards reduce decisions | Common structure keeps humans and agents from reinventing placement, naming, lifecycle, and validation rules. |
| Agent compatibility is required | Non-human collaborators must be able to orient through standard entry points without project-specific training. |

## Required Artifacts

- `D:\AGENTS.md` and `D:\INDEX.md`.
- `D:\Development.manifest.toml`; if absent in a future pass, record root-governance drift and restore it only through a dedicated root-governance pass.
- `[DirectoryName].manifest.toml` and `AGENTS.md` for governed portfolios and containers.
- `[ProjectName].manifest.toml`, `PROJECT-READMAP.toml`, `Project-README.md`, and `AGENTS.md` for project and project-group roots.
- `[StandardName].manifest.toml` for standards.
- Workspace inventory.
- Target directory map.
- Agent startup procedure.
- Standards backlog.

## Four-Layer Workspace Architecture

WGS separates rules, working artifacts, services, and metadata so the workspace can evolve without hiding governance inside project-specific implementation details.

| Layer | Primary function | Examples |
| --- | --- | --- |
| Standards layer | Defines behavior and meta-governance for projects, standards, and artifacts. | WGS, SFDS, PPS, DRS, CTS, SIS, WDS, DDS, LDS, AAMHS, AADR, ARHS, SESM, NeonInk, blue.slate, AAS, ATS |
| Projects layer | Produces functional artifacts, tools, websites, datasets, and technical systems. | FileCabinet, Aegis, Structra, ArchiveHasher, CloneCratesio |
| Shared services layer | Provides workspace-level infrastructure used across projects. | `.agents`, `.evals`, `.sonar`, `.docs`, `.data`, `.start`, local caches, Docker storage |
| Metadata layer | Describes the workspace as a self-aware system. | Workspace manifests, directory manifests, project manifests, registries, relationship maps, health records |

The metadata layer is the connective tissue of the workspace.
It enables intent search: finding projects by purpose, lifecycle state, governing standard, artifact class, or technical suite rather than by filename guesses.

## Project Lifecycle

Every governed project must have exactly one lifecycle state in its manifest.
The state is not a vibe check; it is the current operational posture of the project.

| State | Meaning | Exit criteria |
| --- | --- | --- |
| `concept` | A coherent idea exists with initial scope and boundaries. | Mission and problem statement are recorded. |
| `planning` | Formal architecture, proposal, and governance work are underway. | PPS documentation and project manifest are ready. |
| `active` | The project is under active implementation. | Core logic or data spine is operational enough for feature completion review. |
| `feature-complete` | Core architectural requirements are operational. | Ready for release-side verification and audit. |
| `release-prep` | Final checking, hardening, and packaging are underway. | Domain standard compliance and build verification are complete. |
| `released` | A stable artifact or service has been released. | Published or distributed artifacts have release notes and verified hashes where applicable. |
| `maintenance` | The project is sustained through fixes, updates, or compatibility work. | Update history and stability monitoring continue. |
| `paused` | The project is intentionally inactive but expected to remain recoverable. | Context freeze, known state, and reactivation notes are recorded. |
| `archived` | The project is historically preserved but inactive. | Metadata and archival integrity records are complete enough for long-term recovery. |
| `superseded` | The project has been replaced by a successor. | Manifest links explicitly name the replacement project or standard. |

Lifecycle states must be machine-readable.
If a project does not fit a state cleanly, record the ambiguity as a governance gap instead of inventing a private state.

## Project Classes

The lifecycle state says when the project is in its life.
The project class says what kind of thing it is.

Project manifests should classify the project using the closest governed class, such as:

- `desktop-app`
- `command-tool`
- `website`
- `dataset`
- `standard`
- `service`
- `document`
- `infrastructure`
- `research`

The class determines which domain standard is consulted after WGS:

- Desktop applications use DRS for release behavior.
- Command tools use CTS for automation and CLI contracts.
- Services and infrastructure use SIS for lifecycle, health, ports, storage, logs, resources, and recovery.
- Websites use WDS for deployment and site documentation.
- Datasets use DDS for provenance and dataset validation.
- Standards use SFDS for suite structure.

## Metadata Spine

Manifests are the machine-readable source of truth for identity, state, relationships, and agent orientation.
Human documents provide narrative depth, but manifests are the canonical records for automated discovery.
Project read maps provide the discovery contract between those records and bounded evaluators.

The current manifest family is Entity Manifest v2.4.
Older Project Manifest v2.3 records remain valid historical evidence until migrated.

Every governed entity manifest must answer:

- What is this entity?
- Where does it live?
- What class of thing is it?
- What is its lifecycle state?
- Which standard governs it?
- Which documents are authoritative?
- What relationships or successors matter?
- What should an agent read first?

## Project Read Map

`PROJECT-READMAP.toml` is a WGS-governed project discovery form.
It is not a separate standard.
It tells humans, agents, and evaluators which project records are mandatory, which records are priority context, which evidence roots matter, which documentation roots are secondary, and which generated directories should normally be excluded from exploratory reading.

The read map should be generated during PPS onboarding and updated as the project grows.
Missing read maps, stale paths, or mandatory entries that no longer exist are governance deficiencies because they force evaluators back into broad source-code archaeology.

A project read map may include evaluator budget guidance such as reserved mandatory files and remaining exploratory budget.
Budget guidance is advisory, but evaluators should consume mandatory entries before spending exploratory file budget.

The release note is the human promise.
The manifest is the machine record.
WGS owns the existence, placement, identity, and discoverability of that record.

## Agent-First Governance

Agent compatibility is mandatory.
An agent entering the workspace must be able to recover context through standard read order rather than project-specific memory.

### Required Agent Orientation

For workspace or project work, agents read:

1. `D:\AGENTS.md`, `D:\INDEX.md`, and each nearer `AGENTS.md` toward the target.
2. `D:\Development.manifest.toml` for drive-wide identity and registration.
3. `D:\.city_hall\README.md` and the relevant active standard suite when the task concerns active governance, or when the root manifest is absent and must be recovered.
4. Nearest entity-named manifest matching its containing directory.
5. `PROJECT-READMAP.toml`, when working in a project or group.
6. `Project-README.md`, when working in a project or group.
7. Canonical governing standards linked by the manifests.
8. Roadmap, current task note, release note, or handoff record.

Agents must record missing entry-point documents before making broad changes.

### Required Agent Closeout

An agent leaving a substantial workspace, project, standard, promotion, relocation, or lifecycle task must update both direct and extended recovery records before treating the task as complete.

Direct records are the documents beside the changed entity: manifest, `AGENTS.md`, `Project-README.md`, README, changelog, validation checklist, release note, adoption note, or standard-specific record.

Extended records are the navigation and authority documents that make the changed entity discoverable from outside itself: `D:\Development.manifest.toml`, `D:\INDEX.md`, library README/maps, City Hall README/workshop maps, WGS responsibility matrices, workspace inventories, target maps, parent manifests, standards registries, or promotion notes.

If the direct or extended records do not need changes, the handoff should say so.
If they should change but cannot be updated in the current task, the gap must be recorded plainly.

### Agent Drift Rules

- Do not infer project purpose from code alone when manifests or identity docs are available.
- Do not move, rename, or delete roots as a cleanup reflex.
- Do not silently correct manifest drift.
- Prefer narrow changes until the governing standard and lifecycle state are known.
- Preserve context even when a project is paused, archived, or superseded.

## Standards Hierarchy

WGS is the workspace meta-layer.
It governs the environment.
Other standards govern objects inside that environment.

| Layer | Standards | Role |
| --- | --- | --- |
| Workspace constitution | WGS | Placement, registration, manifests, services, lifecycle visibility, agent orientation, workspace health. |
| Meta-standards | SFDS, PPS | Standards formulation, project birth, intent boundaries, proposal readiness. |
| Domain standards | DRS, CTS, SIS, WDS, DDS, LDS | Release, automation, service, deployment, dataset, and library/API rules for project classes. |
| Technical and specialized standards | AAMHS, ARHS, AAS, ATS, AADR, SESM, NeonInk | Integrity, analysis, task handoff, representation, metadata, and design language. |

When standards overlap, use `Governance-Responsibility-Matrix.md`.
WGS decides where an entity lives and how it is discoverable; it does not replace the entity's domain standard.

## Validation

A WGS workspace is valid enough for planning when:

- The workspace root is identifiable.
- Root directories are inventoried.
- Current state and target state are separate.
- Standards have declared scopes.
- Agents have a startup procedure.

A WGS workspace is governed when:

- `D:\Development.manifest.toml` exists, parses, and names governed roots.
- Governed portfolios and containers have entity-named directory manifests and inherited instructions.
- Projects and project groups have entity-named manifests, instructions, project read maps, and project orientation documents.
- Standards have entity-named standard manifests and SFDS conformance.
- Lifecycle state is explicit for governed projects.
- Shared services are registered or intentionally excluded.
- Drift is recorded before moves, renames, or deletions.
- Direct and extended documentation records are updated before substantial tasks close.
- Workspace health records identify next safe actions.

## Workspace Health Model

Workspace health is a planning signal, not a moral score.
It tells a future human or agent how safely the workspace can be changed.

| State | Meaning | Required response |
| --- | --- | --- |
| `unknown` | The root exists, but current state has not been inspected. | Inventory before making broad changes. |
| `observed` | Current state is recorded, but target state or ownership may be incomplete. | Make local changes only; update inventory as facts are discovered. |
| `planned` | Current and target state are both documented. | Changes may proceed when they match the target map. |
| `governed` | Required manifests and agent read-first docs exist. | Normal project and standard work may proceed. |
| `drifted` | Current state conflicts with the target map or manifests. | Record the mismatch before moving, renaming, or deleting anything. |
| `blocked` | A conflict, missing owner, or unsafe ambiguity prevents responsible changes. | Stop broad changes and create a review note or backlog item. |

### Minimum Health Record

A workspace health note should record:

- Date reviewed.
- Root or directory reviewed.
- Observed state.
- Target state, if known.
- Health state.
- Blocking gaps.
- Next safe action.

### Drift Rules

- Do not silently correct drift by moving or deleting roots.
- Preserve legacy manifest-like files until their role is understood.
- If a current root and target root disagree, record both names and require manual review.
- If a standard owns the domain behavior, WGS owns only placement, registration, and discoverability.

## Preservation and Health Metrics

The terminal goal of WGS is recoverability.
A workspace is healthy when its projects, standards, services, and metadata can be audited or resumed without depending on memory.

Workspace health reviews should track:

- Manifest coverage.
- Documentation coverage.
- Standards compliance.
- Lifecycle state coverage.
- Drift between current state and target state.
- Missing owner or maintainer records.
- Blocked roots and next safe actions.

Metrics are evidence for stewardship.
They should guide cleanup and planning, not become vanity scores.

## Tone Requirement

WGS documents should be plain, concrete, and useful.
They may carry the civic metaphor of City Hall, zoning, public works, and library roots, but the metaphor should clarify responsibility rather than decorate the system.
