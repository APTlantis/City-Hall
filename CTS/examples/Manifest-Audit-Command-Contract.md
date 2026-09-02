# manifest-audit Contract

## Purpose

Check standard-suite manifests for required sections and missing local artifact references.

## Usage

```text
manifest-audit [root] [--json]
```

## Inputs

- Arguments: optional root path; defaults to current directory.
- Options: `--json` emits machine-readable output.
- Environment: none.
- Files: `*/CTS.manifest.toml`.

## Outputs

### Human Output

Summary of manifests checked, missing sections, missing artifact paths, and final result.

### Machine Output

With `--json`, stdout contains one JSON object:

- `root`
- `manifests_checked`
- `errors`
- `warnings`
- `status`

### Diagnostics

Unreadable files, parse errors, and filesystem diagnostics go to stderr.

## Exit Codes

| Code | Meaning |
| --- | --- |
| 0 | All checked manifests passed. |
| 1 | General failure. |
| 2 | Invalid arguments. |
| 3 | Root path missing. |
| 4 | One or more manifests failed validation. |
| 5 | TOML parser or required external dependency unavailable. |

## Stability

- Command name: stable after first release.
- Flag names: `--json` is stable.
- Machine-readable fields: additive changes allowed in minor releases.
- Breaking-change policy: field removals require a major version.

## Examples

### Human Use

```text
manifest-audit D:\010-CITY-HALL
```

### Automation Use

```text
manifest-audit D:\010-CITY-HALL --json
```
