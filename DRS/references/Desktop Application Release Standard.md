# Desktop Application Release Standard

This document defines the release model used across local-first Windows desktop applications in this organization. It was derived from practices established in Filing Cabinet and refined through the Aegis project.

The goal is a release process that is honest, inspectable, and reproducible — one that leaves a clear record of what shipped, how it was verified, and what it deliberately does not do.

---

## 1. Core Principles

These principles are non-negotiable. Every release decision should trace back to at least one of them.

**Ship understanding, not just binaries.**
A release is not complete until someone who did not build it can understand what changed, why it changed, and how to verify the artifact they received.

**Every release has a theme.**
Before writing a line of code, name the release. The name is a commitment. If the work does not match the name, either the name was wrong or the scope drifted. Both problems should be caught before the release note is written, not after.

**Design boundaries are part of the release.**
Stating what a release intentionally does not include is as important as stating what it includes. Boundaries prevent scope creep, manage user expectations, and make future releases easier to plan.

**Detect before mutating.**
Any system that changes state — installer, upgrade, repair workflow — should make the change visible before it happens. Irreversible actions require explicit operator approval.

**The artifact hash is the release.**
Publishing an installer without a hash is not a release. It is a file drop. SHA-256 is the minimum. Record it in the release document, not just a manifest.

**Documentation ships with the build.**
Release notes, trust documents, and core docs should be part of the publish output. An operator who has only the installed application should be able to find the documentation that describes it.

**The release note is the human promise. The manifest is the machine record. The hash binds them.**
A release note explains what shipped, written for the operator deciding whether to install. The project manifest records the same information as machine-readable truth. The SHA-256 hash binds the written description to the specific artifact that was built. All three must be consistent — if any conflict with the others, the release is broken.

---

## 2. Versioning

Use semantic versioning: **MAJOR.MINOR.PATCH**

For Windows installers and package metadata, use the four-part Windows version: **MAJOR.MINOR.PATCH.0**

The fourth component is always `0` unless a hotfix requires an emergency re-release of the same patch version without a version bump.

| Increment | Trigger |
|---|---|
| MAJOR | Breaking vault format, storage structure, or protocol change. A user upgrading needs to be warned explicitly. |
| MINOR | New features, new workflows, new capabilities. Backward-compatible with existing data. |
| PATCH | Bug fixes, UI corrections, dependency refreshes, documentation corrections. No new capability added. |

**Patch policy:** A patch is appropriate when a fix is isolated, the change surface is small, and no new feature is introduced. A patch should be releasable in a single session: identify the problem, fix it, verify it, document it, ship it. If the fix requires a design decision or touches multiple systems, it is a minor release.

**Version source of truth:** The project manifest (`*.manifest.json` or `*.manifest.toml`) is the canonical version record. The installer build script reads the version from the manifest or receives it as a parameter. The application assembly version must match.

---

## 3. Release Document

Every release — including patches — requires a release document.

The release document is the written promise of what the release contains. It is the artifact the operator reads to decide whether to install. It should be written before or simultaneously with the final build, not after.

### Required Structure

```
# [AppName] v[X.Y.Z] — [Release Theme Name]

[One paragraph: what this release is about and why it exists.
The tone is honest about scope. Do not oversell a patch as a feature release.]

---

## Highlights

### [Feature or Change Area Name]
[Plain description. What changed, why it matters, what the operator can now do.]

[Repeat for each meaningful change. A patch may have only one section.]

---

## What This Release Improves

[Optional for patches. For minor releases: a short paragraph connecting the
highlights to the broader direction of the project.]

---

## Design Boundaries

[AppName] v[X.Y.Z] intentionally does not:

* [Thing that was considered but scoped out]
* [Behavior that operators might expect but is deliberately absent]
* [Complexity that will be addressed in a future release]

---

## Built With

* [Framework]
* [Language]
* [Runtime]
* [Installer toolchain]
* [Other notable dependencies]

---

## Release Artifact

Expected installer:

* `[AppName]-[X.Y.Z.0]-win-x64.[ext]`

SHA-256:

* `[UPPERCASE HEX HASH]`

[Optional BLAKE3 hash if applicable.]

[One sentence about signing status.]
```

### Required Fields Checklist

- [ ] Version number matches project manifest and assembly
- [ ] Theme name is present and reflects the actual scope
- [ ] At least one Highlights section with plain-language description
- [ ] Design Boundaries section with at least two entries
- [ ] Built With section lists all notable dependencies
- [ ] Release Artifact section with exact filename and SHA-256
- [ ] Signing status is stated (even if unsigned or self-signed)

### Prohibited Content

- Do not claim production readiness in a release note without a security review on record.
- Do not omit Design Boundaries because "there are no limits." There are always limits.
- Do not write a release note as a commit log. Group by meaning, not by change.

---

## 4. Artifact Naming Convention

Installer and release artifacts follow this naming pattern:

```
[AppName]-[MAJOR.MINOR.PATCH.0]-[platform].[ext]
```

Examples:
```
FilingCabinet-1.3.1.0-win-x64.msi
Aegis-0.1.2.0-win-x64.msix
```

Rules:
- **AppName** is a single PascalCase word matching the project identifier in the manifest.
- **Version** is the four-part Windows version including the trailing `.0`.
- **Platform** is `win-x64` for all standard Windows x64 releases. Add `win-arm64` when ARM64 is validated.
- **Extension** reflects the actual installer format (`msi`, `msix`, `exe`).
- File names are case-sensitive for hashing purposes. Use the exact name in the release document.

---

## 5. Artifact Integrity

Every release artifact requires a SHA-256 hash recorded in the release document.

Minimum requirement: **SHA-256**, uppercase hex, no separators.

Preferred for security-sensitive releases: **SHA-256 + BLAKE3**.

The hash must be computed from the final artifact file, not from the publish directory before packaging. Re-running the installer build must reproduce the same binary hash if the inputs have not changed.

### Where to Record Hashes

1. **In the release document** — the primary and most visible location.
2. **In the project manifest** — under `release.installer.sha256`.
3. **In the release checklist** (if maintained separately) — under the per-version verification block.

Never publish only a hash without also naming the exact artifact file the hash covers.

### Self-Referential Packaged Documentation

If release documentation is bundled inside the signed or hashed installer, the packaged copy of the release note must not be the canonical place for the final artifact hash when writing that hash would change the artifact being hashed.

For self-referential installers, the canonical post-build hash record is the source-tree release note, the project manifest, the release checklist, and any release evidence bundle created after the final artifact is built. The copy of the release note inside the installer may either omit the final artifact hash or state that the final hash is recorded externally in the manifest, checklist, and evidence bundle.

This is not a mismatch or withdrawal condition when the manifest, checklist, source release note, and evidence bundle agree and the final artifact verifies. Prefer a release evidence folder with `filehash.txt` for public releases or any release where the installer contains its own documentation snapshot.

---

## 6. Build Verification Record

Every release must have a verification record: a short, factual statement of what was tested and when.

The verification record belongs in:
- The project manifest (`release.verified`)
- The release checklist (per-version section)

### Minimum Verification Record

```
Build result:    [Project].vcxproj / dotnet build completed [Date]
Test result:     [TestRunner] passed [N] tests on [Date]
Install result:  Installed, launched ([window title]), uninstalled successfully on [Date]
Data safety:     [Data file] was not modified or deleted by install/uninstall on [Date]
Signing:         [Self-signed / code-signed / unsigned] on [Date]
```

### What Must Be Recorded Per Release

| Check | Minimum Evidence |
|---|---|
| Build completed | "Release x64 build completed on [date]" |
| Tests passed | "passed N tests" with test runner name |
| Install works | "installed and launched on [date]" with window title |
| Uninstall is safe | "uninstalled successfully; [data file] not deleted" |
| Upgrade is safe | "existing data preserved after upgrade" (if applicable) |
| Signing status | Explicit statement — never implicit |

### Test Count Is Meaningful

Record the test count in the verification block. If the test count drops between releases, it should be noticed and explained. If tests were removed for legitimate reasons, document why.

---

## 7. Project Manifest

Every project maintains a machine-readable project descriptor file.

Accepted formats: `[ProjectName].manifest.json` or `[ProjectName].manifest.toml`

The manifest is the single source of truth for:
- Current version
- Latest release artifact name and hash
- Last verified date and test result
- Build and deploy automation strings
- Documentation index
- External dependency list

The manifest must be updated as part of the release, not as an afterthought. It should never describe a version that has not been released.

### Release Status Values

Use `release.status` to distinguish local verification from public distribution:

| Status | Meaning | Release gate result |
|---|---|---|
| `draft` | Planned, not built | Not releasable |
| `candidate` | Built and under verification | Not ready yet |
| `local-verified` | Packaged, hashed, signed or explicitly unsigned, and verified locally; not publicly distributed | Valid for private/local release records |
| `published` | Public artifact is available to users | Valid for public release records |
| `superseded` | Replaced by a newer release | Historical record only |
| `withdrawn` | Retracted after publication or local distribution | Blocked; see withdrawal process |

Do not use `published` for a package that only exists as a local validation artifact. Local verification is useful evidence, but it is not public distribution.

### Minimum Manifest Fields

```json
{
  "project": {
    "id": "projectname",
    "version": "X.Y.Z"
  },
  "release": {
    "version": "X.Y.Z",
    "name": "AppName vX.Y.Z — Theme Name",
    "date": "YYYY-MM-DD",
    "installer": {
      "path": "artifacts/installer/[filename]",
      "runtime": "win-x64",
      "package_version": "X.Y.Z.0",
      "size_bytes": 0,
      "sha256": "HASH"
    },
    "verified": {
      "date": "YYYY-MM-DD",
      "tests": "[runner] passed N tests",
      "installer_build": "[script] completed"
    }
  },
  "documentation": {
    "release_notes": "docs/[release note filename]"
  }
}
```

---

## 8. Documentation Delivery

Release documentation must travel with the application.

**During build:** Copy the `docs/` folder into the publish output directory alongside the application binaries.

**In the installer:** Include the `docs/` folder in the installed package so an operator who has only the installed application can access release notes and core docs without the source repository.

**Minimum docs that ship:**
- The release note for the current version
- The trust or security model document (if the application handles sensitive data)
- Any integrity validation matrix or verification model

Documentation files are text files. They add negligible size and are the most durable part of the release artifact.

### Evidence Folder Convention

A mature project captures release evidence in a durable proof bundle alongside the documentation. This is not required for every release but is strongly recommended for public releases and any release that makes a security claim.

```
release-evidence/
  v1.0.0/
    build.log
    test.log
    install-check.txt
    uninstall-check.txt
    filehash.txt
```

Evidence files are created at release time and never modified afterward. The `filehash.txt` must record the artifact filename, size in bytes, and SHA-256 hash. Evidence folders complement — but do not replace — the verification record in the manifest and checklist.

---

## 9. Supporting Document Types

A mature project accumulates a small set of supporting documents. These are not roadmap items — they are living references that describe what the project is, how it works, and why it makes the decisions it makes.

| Document Type | Purpose | When to Create |
|---|---|---|
| Release notes (`vX.Y.Z`) | What shipped, what it does, the artifact hash | Every release |
| Release checklist | Pre-release gate with per-version verification blocks | Before the first public release |
| Project manifest | Machine-readable project state and release record | Project start |
| Trust / security model | How the application handles sensitive data and who it trusts | Before any security-relevant release |
| Vault / data format notes | Storage schema, versioning policy, upgrade path | When the data format stabilizes |
| Integrity validation matrix | What "healthy" state looks like; how to detect and repair drift | When a repair or verification workflow exists |
| Threat model | Attack surface, trust boundaries, known limitations | Before any security claim |
| Dependency provenance | Exact versions, sources, build flags for each external dependency | Before any public release |
| Build reproducibility guide | Clean-clone build steps, required tools, exact versions | Before sharing with other developers |

Supporting documents do not need to be comprehensive at creation. They should be **honest about their current scope** and updated as the project evolves. An incomplete trust model that says what it covers is more useful than no trust model.

---

## 10. Release Checklist

The release checklist is a living gate document. It does not change between releases — the same sections apply every time. New per-version verification blocks are appended to it.

### Pre-Release Gates (Apply Every Release)

**Build**
- [ ] Clean clone builds successfully
- [ ] All package dependencies restore without manual intervention
- [ ] Required tool versions are documented
- [ ] Release and Debug configurations are both validated
- [ ] Target platform(s) are explicitly listed (x64 / ARM64 / both)

**Tests**
- [ ] Full test suite passes
- [ ] Test count is recorded
- [ ] No tests were removed without explanation
- [ ] If crypto or vault operations exist: primitive, fixture, and negative path tests pass
- [ ] Manual UI smoke test is performed and recorded

**Data Safety**
- [ ] First-run behavior creates expected data structures
- [ ] Upgrade from previous version preserves existing data
- [ ] Uninstall does not silently delete user data
- [ ] If a vault or data format version check exists: version enforcement is tested

**Security / Trust**
- [ ] README and release note state audit/review status accurately
- [ ] Security-relevant behavior changes are documented
- [ ] Dependency changes (especially cryptographic) are documented
- [ ] Known gaps and limitations are updated in the manifest or threat model

**Artifacts**
- [ ] Installer or package artifact is produced with expected filename
- [ ] SHA-256 hash is recorded in the release document
- [ ] Signing status is documented
- [ ] Release document is in `docs/` and included in the build output

### Per-Version Verification Block

Append one of these blocks to the checklist for each release:

```
## v[X.Y.Z] [Platform] Verification

* Package target: `[path/to/installer]`
* Package size: `[N]` bytes
* SHA-256: `[HASH]`
* Signing: [self-signed CN=... / code-signed by ... / unsigned]
* Build result: Release [platform] build completed on [date]
* Test result: [runner] passed [N] tests on [date]
* Install result: installed, launched with title `[window title]`, uninstalled successfully on [date]
* Data safety: `[data path]` not deleted by uninstall on [date]
* Public release: [planned / not planned for this version]
```

---

## 11. Release Blockers

A release is blocked — regardless of feature completeness — if any of the following are true:

- A test that was passing in the previous release now fails without a recorded explanation
- The installer artifact hash in the release document does not match the artifact file
- The installer deletes or overwrites user data without explicit operator approval
- The release note claims production readiness without a security review on record
- A breaking data format change is not documented and does not include an upgrade path
- An external cryptographic dependency was changed without updating the dependency provenance record
- The manifest version does not match the installer version

### Release Blocker Severity Reference

| Blocker | Severity | Override Allowed | Required Action |
|---------|----------|-----------------|-----------------|
| Installer artifact hash mismatch | Critical | No | Rebuild or correct the release document — never adjust a hash to match |
| Test regression (passing test now fails) | High | With recorded explanation | Link to issue; explain in per-version checklist block |
| Manifest version does not match installer version | Critical | No | Fix the manifest before release |
| Release note not written | Critical | No | Write the release note |
| Installer deletes or overwrites user data | Critical | No | Data safety is non-negotiable |
| Unsigned installer (when not disclosed) | High | Yes | Must be stated explicitly in release note and manifest |
| Production readiness claim without security review | Critical | No | Perform the review or remove the claim |
| Breaking data format change without upgrade path | High | With explicit operator warning | Document migration in release note; see Section 15 |
| Cryptographic dependency changed without provenance update | High | No | Update Dependency Provenance before release |
| Release note omits Design Boundaries | High | No | Design Boundaries section is required |

---

## 12. Release Cadence Principles

There is no fixed release schedule. Releases are driven by scope completion, not calendars.

**A release is ready when its theme is fully implemented.**
If the release was named "Vault Reliability and Trust Release," it should not ship until the trust and reliability work is complete. Partial themes produce confusing releases.

**Patches may be released at any time.**
If a patch is isolated and verified, waiting for a feature release is not required and not preferred. Ship the patch.

**Minor releases absorb related work.**
If two feature areas are closely enough related that they belong in the same release theme, include them. If they are independent, consider two releases.

**A release that takes more than a few sessions to develop should have at least a draft release note written before coding begins.**
Writing the release note first forces the scope to be explicit before any time is spent building.

**Documentation lag is a release blocker.**
If the release note, manifest, and checklist are not ready, the release is not ready. These are not optional paperwork — they are part of what makes a release a release.

---

## 13. Reference: Filing Cabinet Lineage

This standard was derived from the Filing Cabinet release history. The following practices were established in Filing Cabinet and should be considered validated:

| Practice | First Established | Evidence |
|---|---|---|
| Release theme naming | v1.0.0 | "Initial Stable Release", "Preview and Recall Release", etc. |
| Design Boundaries as a required section | v1.1.0 | Explicit list of intentional exclusions in every release note |
| SHA-256 in release document | v1.1.0 | `FilingCabinet-1.1.0.0-win-x64.msi` hash in v1.1.0 note |
| `docs/` folder in publish output | v1.0.0 | Docs folder present in `artifacts/publish/win-x64/docs/` |
| Machine-readable manifest | v1.4.x | `Filing Cabinet.manifest.json` with full release and verification record |
| Test count in verification record | v1.0.0 | "passed N tests" recorded per version |
| Repair log as trust artifact | v1.2.0 | `catalog/repair-log.jsonl` logged and surfaced in UI |
| Headless CLI verification | v1.2.0+ | `FilingCabinet.Cli.exe verify --fail-on medium` |
| Trust and verification model document | v1.2.0 | `Filing Cabinet — Trust and Verification Model.md` |
| Integrity validation matrix | v1.2.0 | `Filing Cabinet — Vault Integrity Validation Matrix.md` |

The Aegis project extended this model with:

| Practice | Evidence |
|---|---|
| Per-version verification blocks in release checklist | `Aegis - Release Checklist.md` v0.1.0 through v0.1.2 |
| Explicit release blockers section | Aegis release checklist Blockers section |
| Test path override in services | `SetKeyringPathForTesting`, `SetSettingsPathForTesting` |
| 3:12 test ratio enforcement | `.agents/rules.md` |

---

## 14. Withdrawn Releases

A release may be withdrawn after publication if any of the following are true:

- The artifact hash in the release document is incorrect
- The installer damages, deletes, or corrupts user data
- The release note made a security claim that is not supported by a review on record
- A critical defect was discovered after publication that makes the release unsafe to use

### Withdrawal Procedure

1. Update `release.status` to `"withdrawn"` in the project manifest
2. Write a Withdrawn Release document using the template at `templates/Withdrawn-Release.md`
3. Record the reason, impact, and post-withdrawal review findings in the document
4. Annotate the original release note at the top: do not delete it
5. If a replacement release is planned, document it in the withdrawal record
6. Add a process change to the release checklist to prevent recurrence

### Withdrawn Release Documents

The Withdrawn Release document must record:
- The exact reason for withdrawal
- Which users are affected and how
- Remediation instructions for anyone who installed the release
- A post-withdrawal review: root cause, detection method, process gap, and the change made to prevent it

Do not delete the original release note. The historical record must be preserved.

---

## 15. Data Migration Contract

When a release changes the persistent data format — schema version, storage structure, file format, or field types — it must document a migration contract before the release ships.

A migration contract is not optional. An undocumented breaking data change is a release blocker (see Section 11).

### Required Contract Elements

| Element | Description |
|---------|-------------|
| Previous and new schema versions | The version identifiers the application reads and writes |
| Changed fields | Every field added, removed, renamed, or changed in type |
| Migration trigger | What causes migration to run (startup, explicit command, installer) |
| Migration steps | Exact operations, in order, including what happens to existing data |
| Pre-migration backup | The application must back up data before migrating — failure to back up must abort the migration |
| Rollback procedure | How to restore the previous version's data if migration fails or the upgrade is reversed |
| Failure behavior | What the application does at each possible failure point — must not silently swallow failures |
| Operator guidance | What the operator needs to know and do before upgrading |

### Migration Rules

- **Backup before mutate.** The application creates a backup of the data file before running any migration step. If the backup fails, migration is aborted.
- **Fail explicitly.** A failed migration surfaces a clear error message with the backup path. It does not silently leave data in an intermediate state.
- **Version markers are required.** The data format must include a machine-readable version identifier. The application refuses to open data from a version it does not understand.
- **Downgrade behavior must be stated.** If downgrading the application after migration is unsupported, this must be documented and surfaced to the operator.

Use the template at `templates/Data-Migration-Contract.md`.

---

## 16. Changelog Policy

Four documents serve distinct purposes in this standard. They should not be conflated.

| Document | Purpose | Audience | Cadence |
|----------|---------|---------|---------|
| `CHANGELOG.md` | Chronological version history — what changed, when | Future developers, historians | Updated each release |
| Release note | What this specific release means — written for someone deciding whether to install | Operators, end users | Written before or during the final build |
| Project manifest | Machine-readable canonical state and release record | Tooling, auditors | Updated as part of every release |
| Release checklist | Verification gate — evidence that pre-release gates were checked | Developers, release managers | Appended per release |

**CHANGELOG.md is chronological.** It lists versions newest-first with a brief summary of changes. It does not explain why — that is the release note's job.

**Release notes are explanatory.** They explain what changed, why it matters, and what the operator can now do. They are written for a human reader, not for a git log parser. They are not a commit log.

**The manifest is canonical.** It is the source of truth for version, artifact hash, and verification record. When any document conflicts with the manifest, the manifest governs (if the manifest is correct — otherwise, the manifest is the thing to fix).

**The checklist is evidentiary.** It records that a human checked the gates. It is not a living document of project state — it is a record that verification happened.

---

## 17. SBOM and Artifact Provenance

For any public release, consider generating a Software Bill of Materials (SBOM). An SBOM records every component in the release artifact with its version, source, and license.

Recommended formats: CycloneDX (JSON or XML) or SPDX. Both are supported by the .NET toolchain:

```powershell
dotnet CycloneDX --json --output artifacts\sbom\AppName-1.0.0-cyclonedx.json
```

### When SBOM is Required

An SBOM is not required by this standard. It is strongly recommended when:
- The release is distributed publicly
- The release includes components with viral licenses (GPL, AGPL)
- The release is used in a regulated environment
- A dependency provenance document alone is insufficient for the distribution context

### Checklist Gates (when applicable)

- [ ] SBOM generated for this release
- [ ] SBOM stored at `artifacts/sbom/AppName-X.Y.Z-cyclonedx.json`
- [ ] SBOM reviewed for unexpected components or license conflicts
- [ ] SBOM included in release artifacts (alongside installer)

### Relationship to Dependency Provenance

The SBOM and Dependency Provenance document (`templates/Dependency-Provenance.md`) serve different purposes. The Dependency Provenance document is human-readable and focused on build reproducibility and change tracking. The SBOM is machine-readable and focused on supply chain transparency. Both can coexist; the SBOM does not replace the Dependency Provenance document.

---

*This document is a working standard. It should be updated when a new practice is validated in a real release.*
