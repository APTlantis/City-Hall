# Project Proposal Standard

## Status

Candidate v0.2.3.

PPS governs project birth.
It defines the proposal artifacts that freeze mission, boundaries, success, failure, constraints, risks, and early roadmap before broad implementation begins.

## Scope

PPS governs project creation, project revival, proposal records, design boundaries, success criteria, failure criteria, constraints, risks, operational personas, project responsibility posture, technical direction, and early roadmaps.

PPS applies before a project enters broad implementation and whenever an existing project has drifted far enough that its intent is unclear.

## Does Not Govern

PPS does not govern release packaging, CLI output contracts, service lifecycle behavior, website deployment, dataset validation, artifact integrity, or workspace root placement.
Those responsibilities belong to DRS, CTS, SIS, WDS, DDS, AAMHS/ARHS, and WGS.

## Core Philosophy

A project proposal is a design boundary before a code boundary.

The purpose is not approval.
The purpose is clarity.

A project can be approved and still be a bad project.
A project with a good proposal knows what success looks like, what failure looks like, and what tempting ideas are deliberately outside the fence.

## Relationship to WGS

WGS decides where a project lives, how it is registered, and which lifecycle state it occupies.
PPS decides whether the project intent is clear enough to create, revive, expand, or resume.

PPS normally governs the transition from WGS `concept` into `planning`, and from `planning` into `active`.
If a project in `active`, `paused`, `archived`, or `superseded` no longer has recoverable intent, PPS is used to reconstruct or refresh the proposal boundary before broad work continues.

`WGS-Lifecycle-Mapping.md` records the current operational mapping between PPS readiness levels and WGS lifecycle states.

## Relationship to Delivery Standards

PPS is the north star.
Delivery standards are the rules of execution.

Every proposal must identify the likely governing delivery standard:

- DRS for desktop applications.
- CTS for command tools and automation utilities.
- SIS for services, local APIs, daemons, schedulers, shared caches, and infrastructure.
- WDS for websites and web applications.
- DDS for datasets and corpora.
- SFDS for standards and frameworks.
- AAS, ATS, AADR, SESM, NeonInk, AAMHS, or ARHS when specialized governance applies.

If the delivery standard is unknown, the proposal may remain `sketch` or `draft`, but it is not ready for broad implementation.

## Required Proposal Sections

Every PPS proposal must include:

- Project name.
- Project class or type.
- Project responsibility posture.
- WGS lifecycle state.
- Project theme.
- Problem statement.
- Mission statement.
- Design boundaries.
- Success criteria.
- Failure criteria.
- Operational personas.
- Technical direction.
- Constraints.
- Risk assessment.
- Roadmap.
- Version milestone sketch.
- Entity-named project manifest.
- Project read map.
- Governing standard.

## Problem Statement

The problem statement is mandatory.
It must answer:

- What specific problem exists?
- Who experiences it?
- How is it solved today?
- Why is that insufficient?

A weak problem statement names a category.
A strong problem statement names the friction that makes the project worth preserving.

Example:

```text
Useful files become difficult to relocate, categorize, and understand over time.
Windows Explorer stores files.
FileCabinet stores context.
```

## Mission Statement

The mission statement is one clear paragraph.
It says what the project is for and what kind of value it preserves.

The mission should be narrow enough to prevent drift and durable enough that a future maintainer can still use it after the original implementation details have changed.

## Design Boundaries

Design boundaries state what the project intentionally does and does not do.

Every proposal must include:

- In-scope work.
- Out-of-scope work.
- Explicit non-goals.
- Behaviors the project must not grow into without a proposal revision.

Design boundaries should be written early enough that they shape implementation, not late enough that they merely explain it.

## Success Criteria

Success criteria describe observable outcomes, not a feature wishlist.

Good success criteria answer:

- What can a user or operator do after this project succeeds?
- What context can be recovered later?
- What evidence proves the project works?
- What must remain true over time?

Success criteria should be testable, inspectable, or otherwise observable.

## Failure Criteria

Failure criteria name conditions that would stop, shrink, redirect, or invalidate the project.

They are required because they help agents and maintainers reject attractive but drifting work.

Examples:

- The project fails if it requires cloud services.
- The project fails if it requires AI to perform its core function.
- The project fails if it becomes slower than the manual workflow it replaces.
- The project fails if it cannot recover the context it claims to preserve.

## Operational Personas

Personas in PPS are operational, not marketing personas.
They identify the role of the person or system using the project.

Common Aptlantis personas include:

- Archivist.
- Researcher.
- Developer.
- Power user.
- Operator.
- Agent.

## Project Responsibility Posture

Project responsibility posture defines who the project is responsible to once it exists.
It is not the same as project type, delivery standard, or WGS lifecycle state.

Every proposal should identify one posture:

| Posture | Responsibility level | Proposal expectation |
| --- | --- | --- |
| `personal` | Built primarily for the owner/operator's use. | Record enough mission, recovery, and completion evidence that the owner or a future agent can resume or retire it without guessing. |
| `shared` | Built for a known collaborator, team, portfolio, or recurring local workflow. | Add clearer onboarding, compatibility, support, data-safety, and change-boundary expectations. |
| `adoptable` | Built so an independent operator could use, maintain, package, or extend it. | Require the strongest handoff posture: install or run path, release evidence, recovery notes, governance links, and explicit maintenance boundaries. |

If the posture is not known, the proposal should remain `sketch` or `draft`.
A personal project can be serious and release-worthy; it simply does not imply the same public support or independent-adopter obligations as an adoptable project.

## Technical Direction

Technical direction is high-level guidance, not implementation lock-in.

It may include:

- Language.
- Framework.
- Storage model.
- Distribution model.
- Runtime or platform.
- Expected governing standard.

Technical direction should reduce uncertainty without pretending that architecture is complete before discovery.

## Constraints

Constraints are design guardrails.

Common Aptlantis constraints include:

- Must work offline.
- Must not require accounts.
- Must remain local-first.
- Must support a named operating system or runtime.
- Must remain understandable by a single maintainer.
- Must preserve user data unless explicitly authorized.

Constraints are stronger than preferences.
If a constraint changes, the proposal should be revised.

## Risk Assessment

Risks must be honest and actionable.
A vague risk is a note, not a control.

Every proposal should consider:

- Technical risks.
- Data risks.
- Security or trust risks.
- Project risks.
- Maintenance risks.
- Dependency risks.

Each meaningful risk should have a mitigation, an owner, or an explicit acceptance note.

## Roadmap

The roadmap describes phases, not a random feature list.

Recommended phase model:

| Phase | Meaning |
| --- | --- |
| Phase 1: Data spine | Establish the core data model, manifest, storage, or identity record. |
| Phase 2: Core workflows | Build the minimum workflows that prove the mission. |
| Phase 3: Verification | Add tests, validation, integrity checks, examples, or review evidence. |
| Phase 4: Release readiness | Apply DRS, CTS, SIS, WDS, DDS, or another delivery standard. |

The roadmap should help agents choose the next logical step instead of generating unrelated features.

## Version Milestone Sketch

The version milestone sketch gives the project an initial stopping frame for early releases.
It is a lightweight planning aid, not a rigid release contract.

Every ready proposal should identify at least the first intended version and, when practical, the next one or two likely milestones.
Each milestone should describe:

- The version label or milestone name.
- The purpose of that version.
- The rough completion shape for that version.
- The responsibility posture that version must satisfy.
- Work that is plausible but intentionally deferred.

The milestone sketch may change as the project takes shape.
Its purpose is to make clear that the project will mature through versions, and that each version has a final state that can be evaluated without treating every useful future refinement as current-version incompletion.

A milestone may also be marked as a complete project endpoint.
If the stated version satisfies the mission, success criteria, failure criteria, delivery-standard checks, and responsibility posture, the project may be considered complete at that release version rather than automatically becoming an open-ended maintenance commitment.
Any later idea should then be recorded as a new version, revival, fork, or separate proposal, not as proof that the completed version was unfinished.

## Project Manifest

Every PPS-governed project must have or queue an entity-named project manifest, such as `FileCabinet.manifest.toml`.

The manifest is the machine-readable project record.
The proposal is the human intent record.

At minimum, the manifest should record:

- Project id and title.
- Project class.
- Project responsibility posture.
- WGS lifecycle state.
- Governing standard.
- Current proposal or identity documents.
- Relationships.
- Known gaps.
- Agent read-first notes.

## Project Read Map

Every PPS onboarding pass should create or refresh `PROJECT-READMAP.toml`.
The read map is a WGS-governed form, not a separate PPS standard.
PPS uses it to record the first project records that evaluators should read before exploratory source inspection.

At minimum, the read map should identify the entity-named project manifest, PPS proposal, `Project-README.md`, project-local `AGENTS.md`, priority architecture or release records when they exist, evidence roots, secondary documentation roots, and generated directories that should normally be excluded.

## Proposal Readiness Levels

| Level | Meaning | May implementation begin? |
| --- | --- | --- |
| `sketch` | The idea exists, but mission, boundaries, or success criteria are incomplete. | No broad implementation. |
| `draft` | The proposal has the required sections, but risks or governing standards may still be incomplete. | Prototype only. |
| `ready` | Mission, boundaries, success/failure criteria, constraints, risks, roadmap, and governing standards are clear. | Yes, within the proposal boundary. |
| `rework` | The project has drifted or the proposal no longer matches reality. | Pause broad work until updated. |

## Exit Criteria

A proposal is complete when:

- Problem statement exists.
- Mission statement exists.
- Design boundaries exist.
- Success criteria exist.
- Failure criteria exist.
- Constraints exist.
- Risks exist.
- Roadmap exists.
- Project responsibility posture is identified.
- Version milestone sketch exists.
- Governing standard is identified.
- Entity-named project manifest exists or is queued.
- `PROJECT-READMAP.toml` exists or is queued.

Broad implementation should not begin until the proposal is `ready`.

## Proposal Blockers

A project is blocked from broad implementation when:

- The problem statement is vague.
- The mission cannot be summarized in one paragraph.
- Success criteria are not observable.
- Failure criteria are missing.
- Constraints are missing or contradicted by the technical direction.
- Out-of-scope work is not explicit.
- No project responsibility posture is identified.
- No initial version milestone or completion shape is described.
- The governing delivery standard is unknown.
- No entity-named project manifest exists or is queued.
- No project read map exists or is queued.
- The project has drifted beyond the proposal boundary.

## Agent Use

Agents should use PPS as the north star document.
When a proposed feature or cleanup appears, the agent should ask:

Does this move the project closer to its success criteria without violating its failure criteria or design boundaries?

When evaluating completion, agents should also ask whether the work is required for the current milestone's stated completion shape.
Useful but undeclared refinements should be recorded as later-version candidates unless they reveal a defect, missing requirement, governance failure, or invalid evidence.

If the answer is unclear, the next safe action is to update the proposal rather than broaden the implementation.

## Example

`examples/Example-CLI-Project-Proposal.md` shows a filled proposal for a small CTS-governed command-line tool.
