# SFDS CI Usage

## Purpose

Use the SFDS validator as a lightweight structural check for standard-suite changes.
It checks the suite manifest, required files, registered artifact paths, and SFDS vocabulary.

## Local Check

```powershell
python SFDS/tools/sfds_validate.py SFDS WGS DRS CTS WDS PPS SESM AAMHS LDS --json
```

Run the full WGS audit after the SFDS check when validating a broad City Hall documentation change:

```powershell
python WGS/tools/city_hall_audit.py --root .
```

## GitHub Actions Example

```yaml
name: standards-suite-validation

on:
  pull_request:
    paths:
      - "**/*.manifest.toml"
      - "**/*.md"
      - "**/*.schema.toml"
      - "**/*.schema.json"
      - "**/tools/**"

jobs:
  sfds:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Validate standard suites
        shell: pwsh
        run: python SFDS/tools/sfds_validate.py SFDS WGS DRS CTS WDS PPS SESM AAMHS LDS --json
      - name: Run City Hall audit
        shell: pwsh
        run: python WGS/tools/city_hall_audit.py --root .
```

## Exit Codes

| Exit code | Meaning |
| --- | --- |
| `0` | No blocking SFDS errors were found. Warnings may still require reviewer judgment. |
| `1` | One or more standard suites failed structural validation. |

Warnings are intentionally non-blocking so existing standards can preserve proven domain practice while SFDS normalization continues.
