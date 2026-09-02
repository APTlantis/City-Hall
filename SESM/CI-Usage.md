# SESM CI Usage

## Purpose

Use SESM CI checks to keep fixtures, safe-profile validation, and JSON output behavior stable.

## Local Checks

```powershell
python SESM/tests/run_tests.py
python SESM/Validate-SESM-Safe.py SESM/fixtures/valid/basic-safe.svg --safe-profile --json
python SESM/Validate-SESM-Safe.py SESM/fixtures/invalid/script.svg --safe-profile --json
```

## JSON Report Capture

```powershell
New-Item -ItemType Directory -Force SESM/reports | Out-Null
python SESM/Validate-SESM-Safe.py SESM/fixtures/valid/basic-safe.svg --safe-profile --json |
  Set-Content SESM/reports/basic-safe.validation.json
```

Generated reports should be committed only when they represent a named review packet or compatibility baseline.

## GitHub Actions Example

```yaml
name: sesm-validation

on:
  pull_request:
    paths:
      - "SESM/**"

jobs:
  validate:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run SESM tests
        shell: pwsh
        run: python SESM/tests/run_tests.py
      - name: Capture JSON validation output
        shell: pwsh
        run: python SESM/Validate-SESM-Safe.py SESM/fixtures/valid/basic-safe.svg --safe-profile --json
```
