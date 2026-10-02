# AAMHS CI Usage

## Purpose

This note shows how to generate and validate AAMHS hash-manifest evidence in local automation or CI.

## Local Validation

```powershell
python AAMHS\tools\aamhs_validate.py AAMHS\examples\Example-Hash-Manifest.toml
python AAMHS\tools\aamhs_signature_check.py AAMHS\examples\Example-Hash-Manifest.toml
```

## Hash Manifest Generation Shape

Generate hashes as close as possible to the archived bytes:

```powershell
$file = Get-Item .\archive\payload.bin
$hash = (Get-FileHash $file.FullName -Algorithm SHA256).Hash
@"
[[files]]
path = "archive/payload.bin"
size_bytes = $($file.Length)
sha256 = "$hash"
"@
```

For multi-file archives, sort entries by path before writing the manifest so review diffs remain stable.

## GitHub Actions Shape

```yaml
name: aamhs-archive-check

on:
  pull_request:
    paths:
      - "archive/**"
      - "**/*Hash-Manifest.toml"

jobs:
  aamhs:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate archive hash manifest
        shell: pwsh
        run: python AAMHS\tools\aamhs_validate.py AAMHS\examples\Example-Hash-Manifest.toml
      - name: Check detached signature references
        shell: pwsh
        run: python AAMHS\tools\aamhs_signature_check.py AAMHS\examples\Example-Hash-Manifest.toml
```

CI should preserve validation output as archive evidence when the archive snapshot is promoted or published.
