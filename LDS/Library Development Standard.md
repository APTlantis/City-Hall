# Library Development Standard

## Status

Candidate active v0.2.0.

## Scope

LDS governs library crates, packages, and SDKs whose primary deliverable is code that other code consumes - not a command a human runs directly and not a long-running service. It covers public API surface definition, stability levels, versioning/semver policy, breaking-change handling, minimum supported runtime/toolchain constraints, extension points (traits, interfaces, plugin contracts), and known-consumer tracking.

LDS exists to fill a gap: a project can be well-governed under PPS (why it exists) and WGS (where it lives) while still having no delivery standard, because CTS assumes a command contract and SIS assumes a running service. LDS is for the crates in between - the parts of a project other code links against.

## Does Not Govern

LDS does not govern CLI command contracts, output streams, or exit codes (CTS); service lifecycle, health checks, or runtime infrastructure (SIS); desktop application packaging or release (DRS); website deployment (WDS); dataset provenance, licensing, or splits (DDS); workspace root placement or manifest conventions (WGS); or project mission, boundaries, and success/failure criteria (PPS).

A single project may combine standards: a crate family can have its core library governed by LDS while a companion CLI is governed by CTS and a companion service is governed by SIS. LDS governs only the library-shaped parts.

## City Hall Role

LDS sits alongside CTS, SIS, WDS, DRS, and DDS as a delivery/domain standard. Where those standards assume a specific consumption shape (a command, a service, a page, an installer, a dataset), LDS assumes the consumption shape is *other code* — another crate, another service's internals, a plugin host, or a rendering pipeline. Projects that are pure libraries at their core (no direct CLI or service entry point of their own) should adopt LDS for that core, and layer CTS/SIS/WDS/DRS on top for any companion delivery surface built on it.

## Required Behaviors or Artifacts

- `README.md` as the role statement and document map.
- This primary specification as the authoritative ruleset.
- `LDS.manifest.toml` for the standard suite.
- `templates/Library-Interface-Note.md` as the adopter-facing record of public API surface, stability, and versioning policy.
- Adoption guide.
- Validation checklist.
- Changelog.
- Examples, including at least one candidate adopter for candidate-active maturity.

## Manifest Model

`LDS.manifest.toml` describes the LDS standard suite itself (identity, scope, artifacts, lifecycle). It does not describe any individual library. An adopting project keeps its normal WGS entity-named project manifest (`[ProjectName].manifest.toml`, `project.type = "library"`) and adds a `Library-Interface-Note.md` (from `templates/`) recording the library-specific facts that a project manifest does not have fields for: public surface summary, stability level, versioning policy, MSRV/runtime constraints, extension contract, and known consumers.

## Mixed Project Families

A repository or project group may contain multiple delivery shapes.
Apply LDS to the library-shaped crates or packages and apply the adjacent delivery standard to companion surfaces.

For example:

| Surface | Governing standard |
| --- | --- |
| Core library crate | LDS |
| Schema/helper library crate | LDS |
| CLI crate | CTS |
| Service crate | SIS |
| Website or documentation site | WDS |
| Desktop shell | DRS |

Do not assign LDS to a CLI, service, website, desktop release, or dataset merely because it is implemented in the same repository as a library.

## Library Stability Levels

| Level | Meaning |
| --- | --- |
| `experimental` | Public API is not fixed; breaking changes expected without notice. |
| `interface-stable` | The public surface is fixed enough that a second, independent consumer can build against it without expecting churn. |
| `versioned` | A semver (or equivalent) policy is documented and enforced; breaking changes are recorded in the changelog and gated behind a version bump. |
| `reference` | Has two or more real, tracked consumers and a maintained changelog across at least one breaking change. |

Stability claims must match evidence.
An idea, proposal, or unimplemented crate can be governed by LDS, but it must remain `experimental` until a public surface exists.

## Versioning and Breaking-Change Policy

Every `versioned` or higher library must state:

- Its versioning scheme (semver or an explicit alternative) and what counts as breaking.
- Where breaking changes are recorded (changelog, migration notes).
- Whether pre-1.0 breaking changes are allowed without a major bump (common in early Rust crates) and, if so, that this is stated explicitly rather than assumed.

## Extension Contracts

When a library exposes an extension point (a trait to implement, a plugin registry, a renderer interface), the interface note must name the trait/interface, describe its contract in enough detail that a new implementer doesn't need to read the core source, and state what adding a new implementation does and does not require changing in the core crate.

## Validation

Suite validation checks whether the LDS standard directory is complete, navigable, and aligned with WGS/SFDS (see `Validation-Checklist.md`, Suite Validation section).

Domain validation checks whether an adopting library has a stability level, a versioning policy appropriate to that level, its extension contracts documented, and its known consumers tracked (see `Validation-Checklist.md`, Adopter/Domain Validation section).

## Compatibility Policy

Minor versions of LDS may add optional guidance, stability sub-levels, or additional adopter template fields without changing required meaning. Major versions may change required artifacts, stability-level definitions, or validation gates.

## Adoption Blockers

An LDS-governed library is blocked from being called `interface-stable` or higher when:

- No `Library-Interface-Note.md` (or equivalent) exists.
- The public surface is not described.
- A stability level is claimed without a matching versioning policy.
- Extension contracts exist but are undocumented.
- Known consumers are untracked once a second consumer exists.

## Candidate Evidence

LDS includes:

- a machine-readable interface-note schema;
- a lightweight interface-note validator;
- two completed-interface validation examples;
- a simulated breaking-change cycle example.

These examples validate the standard shape.
They do not promote `render-manifest.crate` out of staging until real crate artifacts exist.

## Relationship to PPS and WGS

PPS defines why the library exists, who needs it, and what success/failure look like. WGS registers the project, its lifecycle state, and workspace placement. LDS governs the library-specific delivery concerns — API stability, versioning, extension contracts, and consumer tracking — once PPS/WGS have established that the project is real and where it lives.
