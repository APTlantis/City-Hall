# Standards Framework Development Standard

## Status

Stable v1.0.0.

SFDS is the governing standard for how Aptlantis standards are formulated, structured, validated, versioned, adopted, and preserved inside City Hall.

## Scope

SFDS governs standards, frameworks, specifications, contracts, and reusable governance patterns in the Aptlantis workspace.

It applies to WGS, PPS, DRS, CTS, SIS, WDS, DDS, ATS, AAS, AAMHS, AADR, ARHS, SESM, NeonInk, LDS, and future standards.

## Does Not Govern

SFDS does not govern ordinary application code, website implementation details, dataset contents, release artifacts, CLI behavior, analysis outputs, or design assets directly.
Those are governed by their domain standards.

SFDS governs the formulation and maintenance of those standards.

## Core Principles

- A standard is not complete because it is written.
- A standard is complete when another project can understand it, implement it, validate against it, and preserve its versioned boundaries.
- Every standard directory needs both an index and an authority: the README explains the standard's role in City Hall, and the primary specification states the actual rules.
- Examples are required because they make abstract rules concrete.
- Validators are first-class artifacts whenever compliance can be tested.
- Standards must define what they govern and what they do not govern.
- A mature standard suite separates suite governance from adopter artifacts.
- Proven standards may normalize into SFDS without being rewritten.

## Operating Tone

SFDS standards should feel like useful engineering agreements.
They should reduce decisions, preserve context, and help agents act safely.
They should not become decorative policy documents that sound complete but fail to guide work.

## Standard Directory Contract

Every SFDS-governed standard directory must provide:

- `README.md`: the standard's City Hall index, role statement, document map, quick-start path, and relationship to adjacent standards.
- Primary specification: the authoritative standard document that states the rules, scope, non-goals, required behavior, validation expectations, and compatibility policy.
- `[StandardName].manifest.toml`: the machine-readable manifest for the standard suite itself.
- Adoption guide: how a project, artifact, or another standard adopts the rules.
- Validation checklist: how suite conformance and adopter/domain readiness are checked.
- Changelog: version history for the standard suite.

Every standard directory should provide, when applicable:

- Adopter-facing schemas or manifest descriptions.
- Templates for adopter records or governed documents.
- Examples or reference suites.
- Validator scripts, CLIs, or manual validation procedures.
- Governance boundary notes for standards with overlapping scope.
- Lineage or adoption notes when the standard predates SFDS.

## README Role

The README is not the standard itself.
It is the front door for humans and agents.

A standard README must answer:

- What role does this standard play in City Hall?
- What work or artifact does it govern?
- Which document is the authoritative specification?
- Which files are suite governance artifacts?
- Which files are adopter-facing artifacts?
- What should a new adopter read first?
- Which adjacent standards should be consulted for overlapping responsibilities?

The README may summarize rules, but it must point to the primary specification for authority.

## Primary Specification Role

The primary specification is the actual standard.
It must define:

- Scope.
- Non-goals.
- Required artifacts or behaviors.
- Conformance levels or maturity expectations, when relevant.
- Validation procedure.
- Compatibility and versioning policy.
- Release blockers or adoption blockers.
- Relationship to WGS, SFDS, and adjacent domain standards.

The specification should be specific enough that another human or agent can apply the standard without reconstructing intent from planning notes.

## Two-Layer Manifest Model

SFDS distinguishes the standard suite from the projects or artifacts that adopt it.

### Standard Suite Manifest

`[StandardName].manifest.toml` describes the standard itself:

- Standard identity, title, abbreviation, status, maturity, and version.
- Governance relationship to SFDS and WGS.
- Scope and non-goals.
- Required suite artifacts.
- Lifecycle metadata and maintainer.
- Agent read-first guidance.

This manifest is the machine-readable index for the standard suite.
It is not the manifest template for adopter projects.

### Adopter Schemas and Templates

Domain schemas and templates describe what adopters must create.

Examples:

- DRS uses `DRS.manifest.toml` to describe the DRS suite.
- DRS uses `DesktopApplicationRelease.manifest.schema.toml` and `templates/ProjectName.manifest.toml` to describe desktop application release manifests.

When a standard governs a domain-specific manifest, that schema belongs beside the standard as an adopter-facing artifact.
It does not replace `[StandardName].manifest.toml`.

## Required Suite Artifacts

The required suite artifacts are the minimum for an adoptable standard:

- README.
- Primary specification.
- `[StandardName].manifest.toml`.
- Adoption guide.
- Validation checklist.
- Changelog.

If templates, schemas, examples, or validators are not applicable, the standard must say so in its README, manifest, or validation checklist.

## Mature Suite Artifacts

Mature suites may also include:

- Reference examples with filled-in adopter artifacts.
- Validators, scripts, or CLIs that make validation executable.
- Governance boundary notes.
- Adoption notes for standards that existed before SFDS.
- Reference implementation or lineage records.
- Evidence of real projects using the standard.

DRS is the reference pattern for this mature form: it preserves a practical release standard, templates, a project manifest schema, a MiniVault example, and an executable PowerShell helper while adding SFDS/WGS governance metadata around the suite.

## Maturity Levels

| Level | Name | Meaning |
| --- | --- | --- |
| 0 | Concept | Idea exists, but structure is incomplete. |
| 1 | Draft | Specification exists and scope is understandable. |
| 2 | Candidate | Templates and examples exist; real projects can test adoption. |
| 3 | Stable | Safe for other projects to adopt. |
| 4 | Reference | Has examples, validation, and at least one real implementation. |

`reference-candidate` may be used as a transitional maturity label for an existing mature standard that has the practical artifacts of a reference suite but is still being normalized into SFDS metadata and validation language.

## Conformance Levels

| Level | Requirement |
| --- | --- |
| Minimal | README, primary specification, suite manifest, and scope boundary exist. |
| Standard | Minimal plus adoption guide, validation checklist, changelog, and clear two-layer artifact separation. |
| Reference Candidate | Standard plus examples and executable or manual validator notes; normalization may still be in progress. |
| Reference | Reference Candidate plus known adopters or a completed reference implementation. |

## Validation Expectations

SFDS validation has two parts:

- Suite validation checks whether the standard directory is complete, navigable, versioned, and aligned with WGS/SFDS.
- Domain validation checks whether an adopter project or artifact satisfies the standard's domain rules.

A standard may use one checklist with separate sections or separate checklists, but it must not blur these layers.
For example, DRS suite validation checks whether the DRS standard directory is complete; DRS release validation checks whether a desktop application release is ready.

## Compatibility Policy

Minor versions may add fields, examples, optional guidance, templates, governance notes, and validator coverage without changing required meaning.
Patch versions may clarify wording, register additional examples, fix broken links, or document validation procedures when those changes do not alter conformance requirements.
Major versions may change required artifacts, required fields, conformance meanings, maturity semantics, or validation gates.
Deprecated documents must remain discoverable or have migration notes.

Machine-readable compatibility should be preserved for:

- Suite manifest identity fields.
- Required artifact keys under `[artifacts]`.
- Adopter artifact group names under `[adopter_artifacts]`.
- Maturity labels used by existing standard suites.

When a compatibility-impacting change is unavoidable, the standard must record the change in `CHANGELOG.md`, preserve or migrate existing examples, and state whether older suites remain valid, require migration, or require revalidation.

## Stability Blockers

A standard is not stable if:

- Scope is unclear.
- The README does not identify the standard's City Hall role.
- The primary specification is missing or not authoritative.
- Required suite artifacts are missing without an explicit deferral.
- No adoption path exists.
- No validation procedure exists.
- Suite governance artifacts are confused with adopter/domain artifacts.
- It conflicts with WGS manifest conventions.

## Normalizing Existing Standards

Some standards predate SFDS and may already contain useful domain rules, examples, and release history.
Do not rewrite those standards from scratch only to make them look newer.

Normalize existing mature standards by:

1. Preserving the authoritative specification and adopter-facing artifacts.
2. Adding or updating `[StandardName].manifest.toml`.
3. Clarifying the relationship to SFDS and WGS.
4. Separating suite validation from adopter/project validation.
5. Recording any remaining gaps in the validation checklist or changelog.

When SFDS and a mature working standard disagree, prefer the proven practice unless it conflicts with WGS manifest conventions or creates ambiguity for future adopters.
