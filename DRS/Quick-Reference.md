# DRS Quick Reference

Use this sheet while preparing, reviewing, or releasing a desktop application. It condenses the active **Desktop Application Release Standard**; the full specification remains authoritative: [Desktop Application Release Standard.md](Desktop%20Application%20Release%20Standard.md).

## Use DRS When

DRS governs desktop release readiness and evidence: versioning, manifests, release notes, artifact naming and hashes, test/install/upgrade/uninstall verification, documentation delivery, distribution, signing posture, and withdrawals.

It does **not** govern project intent (PPS), workspace placement (WGS), CLI output contracts (CTS), website deployments (WDS), or dataset provenance. ARHS supplies publishable release hash manifests; AAMHS supplies archive-preservation hashing and detached signatures.

## Release Truth: Three Records Must Agree

| Record | Job |
| --- | --- |
| Release note | Human promise: what shipped, why it matters, and its intentional boundaries. |
| Project manifest | Machine record: canonical version, artifact, verification, docs, and channel. |
| Final artifact SHA-256 | Binds those records to the exact package. |

If they conflict, the release is broken. Compute SHA-256 from the final package, in uppercase hex with no separators; record the exact filename and hash in the release note and manifest. Attach an ARHS `.hashmanifest.toml` for publishable artifacts. If a package bundles its own release note, keep the canonical final hash externally in the source release note, manifest, checklist, and evidence bundle so packaging does not change the artifact being hashed.

## Before Building

- Name the release and write a truthful draft note before or with the final build; a release theme is a scope commitment.
- Make the manifest the version source of truth. `project.version`, `release.version`, application/package version, artifact name, note, and checklist must agree.
- Use SemVer `MAJOR.MINOR.PATCH`; Windows package versions are `MAJOR.MINOR.PATCH.0` (trailing `.0` unless an emergency same-patch re-release requires otherwise).
- Copy and maintain the project manifest, release note, and release checklist. Add trust/security and threat documents before security claims; add dependency provenance before public release; add a migration contract before persistent-format changes.

## Release Note and Manifest Minimum

Release note: theme, plain-language highlights, at least two **Design Boundaries**, notable build/runtime dependencies, exact artifact filename, SHA-256, and explicit distribution/signing/provenance. It is not a commit log and must not claim production readiness without a review on record.

Manifest: current version; release status and date; installer path, runtime, four-part package version, size, SHA-256, optional BLAKE3, signing; verification date/build/test count/install/data/upgrade evidence; documentation paths; distribution channel and signing authority. Never describe an unreleased version as released.

| Status | Meaning |
| --- | --- |
| `draft` | Planned, not built |
| `candidate` | Built, under verification |
| `local-verified` | Locally packaged, hashed, signed or explicitly unsigned, and verified; not public |
| `published` | Public artifact available |
| `superseded` | Historical, replaced |
| `withdrawn` | Retracted; blocked pending withdrawal record |

## Artifact, Channel, and Trust Boundaries

Name packages `[AppName]-[MAJOR.MINOR.PATCH.0]-[platform].[ext]`—normally `win-x64`; add `win-arm64` only after validation. State distribution and signing as separate facts.

| Release shape | Default path | Required truthfulness |
| --- | --- | --- |
| Public Windows GUI | MSIX through Microsoft Store | Store signs the accepted package; reserve and exactly use Partner Center identity before submission. |
| Development/test Windows GUI | Sideload MSIX | Self-signed development certificate; explicitly non-production. |
| Direct public Windows installer | MSI/EXE only with documented reason | CA-backed or Trusted Signing where appropriate. |
| Internal Windows utility | Simplest fit | State `unsigned-internal` or self-signed truthfully. |
| Cross-platform GUI | Store MSIX for Windows; native/ecosystem packages elsewhere | Record platform-specific provenance. |

`winapp` helps with local MSIX packaging and development certificates; `msstore` helps Store submission. Neither replaces release verification. Rebuild and create fresh ARHS evidence after the final Store candidate is accepted—identity, assets, or structure changes alter the package.

## Gates: Do Not Publish If Any Fail

- Build and full tests pass; record runner and count. Explain removed/regressed tests.
- Manually smoke the UI; install, launch (record title), uninstall, and verify user data survives. Test upgrade preservation when applicable.
- Package exists with exact expected name, nonzero size, recorded hash, and explicit signing/distribution posture.
- Release note, manifest, checklist, and packaged documentation agree; `docs/` ships beside installed binaries (current release note plus applicable trust/integrity docs).
- No data-format change ships without version markers, a pre-migration backup, explicit failure behavior, rollback/downgrade posture, and an operator-facing migration contract.
- Do not claim production/security readiness without the supporting review record. Update dependency provenance for security-relevant changes.

For public or security-sensitive releases, preserve an immutable `release-evidence/vX.Y.Z/` bundle with build/test/install/uninstall/hash records; it complements but never replaces the manifest and checklist.

## Quick Gate Commands

Run from the adopter project root with PowerShell 7+:

```powershell
pwsh -File D:\.city_hall\DRS\drs.ps1 verify-manifest
python D:\.city_hall\DRS\tools\drs_integrity_check.py <ProjectName.manifest.toml> --json
pwsh -File D:\.city_hall\DRS\drs.ps1 check-release
```

Use `drs.ps1 hash <artifact>` for SHA-256; add `--blake3` only when a trusted BLAKE3 utility is installed. Exit `0` means no blocking DRS failure, `1` means blocked/invalid/missing, and `2` means bad invocation/context. Validators support judgment; they do not prove installation, launch, user-data safety, or public distribution.

## Withdrawals and Scope Changes

Withdraw if the recorded hash is wrong, the installer harms user data, a security claim lacks review evidence, or a critical unsafe defect appears. Set `release.status = "withdrawn"`, preserve and annotate the original note, create the withdrawal record, give remediation, record impact/root cause/process gap, and add the prevention change to the checklist.

## Source Map

- Full rules: [Desktop Application Release Standard.md](Desktop%20Application%20Release%20Standard.md)
- Adoption and gates: [Adoption-Guide.md](Adoption-Guide.md), [Validation-Checklist.md](Validation-Checklist.md), [Release-Gating Workflow](docs/Release-Gating-Workflow.md)
- Templates: [project manifest](templates/ProjectName.manifest.toml), [release note](templates/Release-Note.md), [release checklist](templates/Release-Checklist.md), [migration contract](templates/Data-Migration-Contract.md), [withdrawal record](templates/Withdrawn-Release.md)
- Supporting evidence: [trust/security](templates/Trust-Security-Model.md), [threat model](templates/Threat-Model.md), [dependency provenance](templates/Dependency-Provenance.md), [build guide](templates/Build-Reproducibility-Guide.md), [integrity matrix](templates/Integrity-Validation-Matrix.md)
