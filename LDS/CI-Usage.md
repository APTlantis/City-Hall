# LDS CI Usage

## Purpose

This note shows how to run LDS interface-note checks in local automation or CI.

## Local Validation

```powershell
python LDS\tools\lds_validate.py LDS\examples\ManifestQuery.Core-Library-Interface-Note.md
python LDS\tools\lds_validate.py LDS\examples\HashSuite.Core-Library-Interface-Note.md --json
```

## GitHub Actions Shape

```yaml
name: lds-interface-note-check

on:
  pull_request:
    paths:
      - "LDS/**"
      - "**/*Library-Interface-Note.md"

jobs:
  lds:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate LDS interface notes
        shell: pwsh
        run: python LDS\tools\lds_validate.py LDS\examples\ManifestQuery.Core-Library-Interface-Note.md LDS\examples\HashSuite.Core-Library-Interface-Note.md
```

## Runner Expectations

- CI should fail when required interface-note sections are missing.
- CI should fail when template placeholders remain.
- CI should preserve validator output as review evidence when a library claims `interface-stable`, `versioned`, or `reference`.
