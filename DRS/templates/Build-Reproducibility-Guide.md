# [AppName] — Build Reproducibility Guide

**Version:** [AppName] v[X.Y.Z]
**Last updated:** [YYYY-MM-DD]

This guide provides the exact steps required to build [AppName] from a clean clone of the repository and produce a byte-comparable installer artifact. Anyone with the listed prerequisites should be able to follow these steps without contacting the original developer.

---

## Prerequisites

### Required Tools

| Tool | Minimum Version | Where to Get It | Notes |
|------|----------------|-----------------|-------|
| [e.g. .NET SDK] | [e.g. 9.0.100] | [e.g. dotnet.microsoft.com/download] | [e.g. Includes the runtime] |
| [e.g. Visual Studio 2022] | [e.g. 17.12] | [e.g. visualstudio.microsoft.com] | [e.g. Workloads: .NET Desktop Development] |
| [e.g. WiX Toolset] | [e.g. 5.0.1] | [e.g. wixtoolset.org] | [e.g. Required for MSI build] |
| [e.g. PowerShell] | [e.g. 7.4] | [e.g. github.com/PowerShell/PowerShell] | [e.g. Used by build scripts] |

### Required Visual Studio Workloads

* [e.g. .NET desktop development]
* [e.g. Desktop development with C++] (if applicable)

### System Requirements

* Operating system: [e.g. Windows 10 22H2 or later, x64]
* Architecture: [e.g. x64]
* Disk space: [e.g. ~4 GB for SDK, build tools, and dependencies]

---

## Clone and Restore

```powershell
# Clone the repository
git clone [repository-url] AppName
Set-Location AppName

# Restore NuGet packages
dotnet restore
```

If a `packages.lock.json` is present, restore with lock file enforcement:

```powershell
dotnet restore --locked-mode
```

---

## Build

### Application (Release configuration)

```powershell
dotnet build -c Release
```

Expected output: `Build succeeded. 0 Warning(s). 0 Error(s).`

### Publish (self-contained, win-x64)

```powershell
dotnet publish src/[AppName]/[AppName].csproj `
  -c Release `
  -r win-x64 `
  --self-contained false `
  -o artifacts/publish/win-x64
```

[Adjust flags to match the actual publish configuration used in production.]

---

## Run Tests

```powershell
dotnet test -c Release --logger "console;verbosity=normal"
```

Expected: all tests pass. Record the test count. If any test fails, the build is not releasable.

---

## Build the Installer

```powershell
.\scripts\Build-Installer.ps1 -Version "X.Y.Z.0" -PublishDir "artifacts/publish/win-x64"
```

[Replace with the actual build script name, path, and parameters.]

Expected output: `artifacts/installer/AppName-X.Y.Z.0-win-x64.msi`

---

## Verify the Artifact

Compute and record the SHA-256 hash:

```powershell
Get-FileHash "artifacts/installer/AppName-X.Y.Z.0-win-x64.msi" -Algorithm SHA256
```

The hash must match the value in:
1. The release note (`docs/AppName vX.Y.Z.md`)
2. The project manifest (`AppName.manifest.toml`, field `release.installer.sha256`)

If the hashes do not match, do not publish.

---

## Known Build Environment Differences

[Document any known cases where the build environment affects output — e.g. linker version differences on ARM64, SDK patch version differences, etc.]

* [e.g. "The installer size may differ by a few bytes between WiX 5.0.0 and 5.0.1 due to cabinet compression changes."]
* [e.g. "Building on a machine with a different .NET SDK patch version may produce a slightly different binary hash."]

---

## Troubleshooting

### `packages.lock.json` is out of date

Run `dotnet restore` without `--locked-mode`, inspect the diff, and update the lock file if the changes are expected.

### Build script fails with access denied

Ensure PowerShell is running as the current user (not elevated). The build script does not require administrator rights.

### WiX cannot find heat.exe / wix.exe

Verify WiX is installed and its tools are on `$env:PATH`. Run `wix --version` to confirm.

---

## Version History of This Guide

| Version | Change | Date |
|---------|--------|------|
| v[X.Y.Z] | Initial guide | [YYYY-MM-DD] |
