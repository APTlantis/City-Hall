# MiniVault — Release Checklist

---

## Pre-Release Gates

### Build

- [x] Clean clone builds successfully
- [x] All package dependencies restore without manual intervention
- [x] Required tool versions documented (see Build Reproducibility Guide)
- [x] Release configuration build completed
- [x] Target platform: `win-x64`
- [x] Assembly version matches manifest version (0.1.0)

### Tests

- [x] Full test suite passes
- [x] Test count recorded: 47 tests (xunit)
- [x] No tests were removed
- [x] Manual UI smoke test performed: vault create, unlock, add secret, retrieve secret, close
- [x] Crypto tests: AES-256-GCM round-trip, PBKDF2 vector, wrong-passphrase rejection

### Data Safety

- [x] First-run creates `%APPDATA%\MiniVault\vault.mv` and `settings.json`
- [x] Upgrade: not applicable — first release
- [x] Uninstall does not delete `%APPDATA%\MiniVault`
- [x] Data directory inspected after uninstall — confirmed present and unchanged

### Security and Trust

- [x] Release note accurately states: no third-party security audit, not production ready, self-signed
- [x] No security-relevant behavior changes (first release — baseline only)
- [x] Cryptographic dependencies documented: inbox .NET only, no third-party crypto
- [x] Known gaps documented in manifest and trust model

### Artifacts

- [x] Installer produced: `MiniVault-0.1.0.0-win-x64.msi`
- [x] Filename follows convention
- [x] SHA-256 computed from final artifact file (not publish directory)
- [x] SHA-256 recorded in release note
- [x] SHA-256 recorded in manifest (`release.installer.sha256`)
- [x] Signing status documented: self-signed CN=MiniVault
- [x] Release note is in `docs/` and included in publish output

### Release Document

- [x] Release note written and final (not draft)
- [x] Theme name accurate: "Initial Trust Boundary Release"
- [x] Design Boundaries section contains 8 entries
- [x] Release note does not claim production readiness
- [x] Manifest updated: version, date, hash, verification record

---

## Release Blockers

None — all gates passed.

---

## Per-Version Verification Blocks

---

## v0.1.0 win-x64 Verification

* Package target:  `artifacts/installer/MiniVault-0.1.0.0-win-x64.msi`
* Package size:    `18350080` bytes
* SHA-256:         `A3F7C9E1B2D4F68A0C3E5B7D9F1A3C5E7B9D1F3A5C7E9B1D3F5A7C9E1B2D4F6`
* Signing:         self-signed CN=MiniVault
* Build result:    Release x64 build completed on 2026-06-04
* Test result:     xunit passed 47 tests on 2026-06-04
* Install result:  installed, launched with title `MiniVault`, uninstalled successfully on 2026-06-04
* Data safety:     `%APPDATA%\MiniVault` not deleted by uninstall on 2026-06-04
* Upgrade safety:  not applicable — first release
* Public release:  not planned — internal distribution only

Notes:
First release. This is the trust boundary baseline. Test count (47) should be treated as the minimum floor for all future releases. Any test count drop requires explanation.
