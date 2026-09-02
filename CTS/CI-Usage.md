# CTS CI Usage

## Purpose

This note shows how to use CTS validation support in local automation or CI.

## Local Contract Check

```powershell
python CTS\tools\cts_validate.py CTS\examples\Manifest-Audit-Command-Contract.md
python CTS\tools\cts_validate.py CTS\examples\manifest-audit-output-ok.json --json
```

## GitHub Actions Shape

```yaml
name: cts-contract-check

on:
  pull_request:
    paths:
      - "CTS/**"
      - "docs/**/*Command-Contract*.md"
      - "examples/**/*.json"

jobs:
  cts:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate command contracts
        shell: pwsh
        run: python CTS\tools\cts_validate.py CTS\examples\Manifest-Audit-Command-Contract.md
```

## Expectations

- CI should fail when command-contract required sections are missing.
- CI should fail when JSON envelope examples omit `status`, `tool`, or `version`.
- CI should preserve command output as release evidence when validating a tool release.
