# [AppName] — Dependency Provenance

**Version:** [AppName] v[X.Y.Z]
**Last updated:** [YYYY-MM-DD]

This document records the exact version, source, and purpose of every external dependency. It is updated whenever a dependency is added, removed, or upgraded.

Purpose: anyone reproducing the build should be able to locate and verify every input. Changes to cryptographic dependencies require explicit recording here and must be reflected in the release note.

---

## Runtime Dependencies

Dependencies that ship with or are required to run the installed application.

| Package | Version | Source | License | Purpose | Verified |
|---------|---------|--------|---------|---------|---------|
| [e.g. Microsoft.Extensions.DependencyInjection] | [e.g. 9.0.0] | [e.g. nuget.org] | [e.g. MIT] | [e.g. Dependency injection container] | [YYYY-MM-DD] |
| | | | | | |

---

## Build-Time Dependencies

Dependencies required to build but not shipped with the application.

| Package | Version | Source | License | Purpose | Verified |
|---------|---------|--------|---------|---------|---------|
| [e.g. WiX Toolset] | [e.g. 5.0.1] | [e.g. wixtoolset.org] | [e.g. MS-RL] | [e.g. MSI installer generation] | [YYYY-MM-DD] |
| | | | | | |

---

## Framework and Runtime

| Component | Version | Source | Notes |
|-----------|---------|--------|-------|
| [e.g. .NET SDK] | [e.g. 9.0.100] | [e.g. dotnet.microsoft.com] | [e.g. Build and publish] |
| [e.g. Windows Desktop Runtime] | [e.g. 9.0.0] | [e.g. dotnet.microsoft.com] | [e.g. Required on target machine] |
| [e.g. Target Framework] | [e.g. net9.0-windows] | — | [e.g. Minimum Windows 10 build 19041] |

---

## Cryptographic Dependencies

Any dependency involved in cryptographic operations receives a separate entry here. This section must be updated whenever a cryptographic dependency changes — including version bumps.

| Package | Version | Algorithm(s) Used | Key Sizes | Purpose | Changed in This Release |
|---------|---------|------------------|-----------|---------|------------------------|
| [e.g. System.Security.Cryptography] | [e.g. inbox .NET 9] | [e.g. AES-256-GCM, PBKDF2-SHA256] | [e.g. 256-bit] | [e.g. Vault encryption and key derivation] | [Yes / No] |

If no cryptographic dependencies are used: "This application uses no external cryptographic dependencies. It relies on inbox .NET cryptographic APIs only."

---

## Dependency Change Log

Record every dependency change here — additions, removals, and version changes.

| Date | Package | Change | Reason | Release |
|------|---------|--------|--------|---------|
| [YYYY-MM-DD] | [Package name] | [Added / Removed / Updated vX.Y → vX.Z] | [Why this change was made] | [vX.Y.Z] |

---

## Verification Notes

* **Source verification:** [How packages are authenticated — e.g. "NuGet packages are restored from nuget.org with package signature verification enabled."]
* **Lock file policy:** [e.g. "packages.lock.json is committed and enforced in CI. Builds fail if the lock file is out of date."]
* **Private feeds:** [e.g. "No private NuGet feeds are used." or list them]
* **Pinning policy:** [e.g. "All production dependencies are pinned to exact versions. No floating version ranges."]
