# [AppName] — Release Checklist

This checklist is a living gate document. The pre-release gates are permanent — they apply to every release. Do not remove sections; do not mark gates as N/A without a recorded explanation.

Append one Per-Version Verification Block at the bottom of this file for each release.

---

## Pre-Release Gates

These gates apply to every release. Every unchecked item is a release blocker.

### Build

- [ ] Clean clone builds successfully — no uncommitted files, no manual setup required
- [ ] All package dependencies restore without manual intervention (`dotnet restore` or equivalent)
- [ ] Required tool versions are documented in the Build Reproducibility Guide
- [ ] Release configuration build completed (not just Debug)
- [ ] Target platform(s) are explicitly listed: `win-x64` / `win-arm64` / both
- [ ] Assembly version matches the manifest version

### Tests

- [ ] Full test suite passes
- [ ] Test count is recorded (see Per-Version Verification Block)
- [ ] No tests were removed without an explanation recorded in this checklist
- [ ] Manual UI smoke test performed and recorded (launch, exercise primary workflow, close)
- [ ] If crypto or vault operations exist: primitive tests, fixture tests, and negative-path tests pass

### Data Safety

- [ ] First-run behavior creates the expected data structures
- [ ] Upgrade from the previous release preserves existing data
- [ ] Uninstall does not silently delete user data
- [ ] Uninstall was tested and the data path was inspected afterward
- [ ] If a vault or data format version check exists: version enforcement is tested
- [ ] If a data format change was made: a Data Migration Contract document exists and was reviewed

### Network Behavior (offline apps)

- [ ] No unexpected outbound connections observed during launch and primary workflow
- [ ] If the application is claimed to be fully offline: verified with network monitoring during smoke test

### Security and Trust

- [ ] README and release note state audit/review status accurately
- [ ] Security-relevant behavior changes are documented
- [ ] Dependency changes (especially cryptographic) are documented in Dependency Provenance
- [ ] Known gaps and limitations are current in the manifest or threat model

### Artifacts

- [ ] Installer artifact is produced with the exact expected filename
- [ ] Filename follows the convention: `[AppName]-[MAJOR.MINOR.PATCH.0]-win-x64.[ext]`
- [ ] SHA-256 hash is computed from the final artifact (not the publish directory)
- [ ] SHA-256 hash is recorded in the release note
- [ ] SHA-256 hash is recorded in the project manifest (`release.installer.sha256`)
- [ ] ARHS `.hashmanifest.toml` is generated for publishable artifacts
- [ ] Distribution channel is documented explicitly
- [ ] Signing/provenance status is documented explicitly — never implicit
- [ ] Release note is in `docs/` and included in the build publish output
- [ ] `docs/` folder is present in the publish output and installer package
- [ ] Current release note is present inside the installed application's `docs/` folder (verified after install)
- [ ] Trust/security model document is present in `docs/` if the application handles sensitive data

### Release Document

- [ ] Release note is written (not a draft — final prose)
- [ ] Theme name accurately reflects what shipped
- [ ] Design Boundaries section contains at least two entries
- [ ] Release note does not claim production readiness without a security review on record
- [ ] Project manifest is updated (version, release date, hash, verification record)

---

## Release Blockers

A release is blocked regardless of feature completeness if any of the following are true:

- A test that was passing in the previous release now fails without a recorded explanation
- The installer artifact hash in the release document does not match the artifact file
- The installer deletes or overwrites user data without explicit operator approval
- The release note claims production readiness without a security review on record
- A breaking data format change is not documented and does not include an upgrade path
- An external cryptographic dependency was changed without updating Dependency Provenance
- The manifest version does not match the installer version
- The release note has not been written

---

## Per-Version Verification Blocks

Append one block per release. Newest at the bottom. Do not edit past blocks.

---

## v[X.Y.Z] [Platform] Verification

* Package target:  `[path/to/AppName-X.Y.Z.0-win-x64.msi]`
* Package size:    `[N]` bytes
* SHA-256:         `[UPPERCASE HEX HASH]`
* Distribution:    [microsoft-store-msix / msix-sideload-dev / direct-msi-exe / internal]
* Signing:         [microsoft-store-signed / self-signed-development / ca-signed / unsigned-internal / other clear statement]
* Build result:    Release x64 build completed on [YYYY-MM-DD]
* Test result:     [runner] passed [N] tests on [YYYY-MM-DD]
* Install result:  installed, launched with title `[window title]`, uninstalled successfully on [YYYY-MM-DD]
* Data safety:     `[data path]` not deleted by uninstall on [YYYY-MM-DD]
* Upgrade safety:  [existing data preserved after upgrade from vX.Y.Z / not applicable]
* Public release:  [planned / not planned for this version]

Notes:
[Any deviations from standard gates, explanations for removed tests, or other context worth recording.]
