# DRS CI Usage

## Purpose

This note shows how to run `drs.ps1` from local automation or CI without changing the DRS release contract.
CI may support a release, but DRS still treats the manifest, release note, checklist, and artifact hash as the release authority.

## Local Automation Snippet

Run from a DRS adopter project root after the release manifest and docs have been updated:

```powershell
$drs = "D:\.city_hall\DRS\drs.ps1"

& $drs verify-manifest
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $drs hash artifacts\installer\AppName-1.0.0.0-win-x64.msi
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $drs check-release
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
```

For security-sensitive releases, add BLAKE3 when a local `b3sum` or `blake3` executable is installed:

```powershell
& $drs hash artifacts\installer\AppName-1.0.0.0-win-x64.msi --blake3
```

## GitHub Actions Shape

```yaml
name: drs-release-check

on:
  workflow_dispatch:
  pull_request:
    paths:
      - "**/*.manifest.toml"
      - "docs/**"
      - "artifacts/installer/**"

jobs:
  drs:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Verify release manifest
        shell: pwsh
        run: D:\.city_hall\DRS\drs.ps1 verify-manifest
      - name: Check release gate
        shell: pwsh
        run: D:\.city_hall\DRS\drs.ps1 check-release
```

Adjust the DRS path for hosted CI. In a public repository, vendor the DRS suite, install it from a trusted location, or pin it as a submodule.

## CI Expectations

- CI should fail on `drs.ps1` failures.
- CI should preserve build, test, and hash logs as release evidence.
- CI should not publish artifacts unless the manifest, release note, checklist, and artifact hash already agree.
- CI should not silently change release metadata after `check-release` passes.

## Exit Codes

`drs.ps1` uses these process exit codes for automation:

| Exit code | Meaning |
| ---: | --- |
| 0 | Command completed and no blocking DRS failure was found. |
| 1 | DRS found a release-blocking failure, missing artifact, or invalid release state. |
| 2 | Command usage or invocation context is wrong, such as missing arguments or no manifest in the current directory. |

Automation should treat any non-zero exit as a failed release gate.
When a command prints `Release is BLOCKED`, the release must not be published.
