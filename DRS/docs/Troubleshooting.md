# DRS Troubleshooting

## Purpose

This note records common `drs.ps1` failures, expected operator action, PowerShell compatibility, and script trust guidance.

## PowerShell Compatibility

`drs.ps1` is intended for PowerShell 7 or newer on Windows.

Recommended runtime:

```powershell
pwsh --version
```

Expected result: PowerShell 7.x.

Windows PowerShell 5.1 is not the preferred runtime for DRS automation because DRS adopter projects and CI snippets assume modern PowerShell behavior.

## Script Trust

Before using `drs.ps1` as a release gate:

- Keep the DRS suite in a trusted workspace location or pin it in source control.
- Review local changes to `drs.ps1` before relying on a release check.
- Prefer a signed script for distribution-grade workflows.
- If the script is unsigned, record that trust decision in release evidence or operator notes.

Check script signature:

```powershell
Get-AuthenticodeSignature D:\.city_hall\DRS\drs.ps1
```

Unsigned local use is acceptable for a single-operator workspace when the script path and repository state are trusted.
Shared or public release workflows should sign the script or pin its exact source revision.

## Common Failures

| Symptom | Likely cause | Next action |
| --- | --- | --- |
| `No *.manifest.toml found` | Command was run outside the adopter project root. | Run from the project root or copy the DRS manifest template first. |
| `Multiple manifest files found` | More than one project manifest is in the current directory. | Run from the specific project root or temporarily isolate the intended manifest. |
| `Version mismatch` | `project.version`, `release.version`, or package version drifted. | Update the manifest so the project and release version fields agree. |
| `SHA-256 format invalid` | Hash is missing, lowercase, truncated, or includes separators. | Recompute with `drs hash <artifact>` and paste the uppercase value. |
| `SHA-256 hash mismatch` | Artifact changed after the release note or manifest was updated. | Recompute the hash and update both manifest and release note, or rebuild the intended artifact. |
| `Release note not found` | `documentation.release_notes` points to a missing path. | Fix the manifest path or add the missing release note. |
| `Design Boundaries section missing` | Release note does not follow the DRS template. | Add the required section before publishing. |
| `docs/ not found in publish output` | Build did not package release documentation. | Update build or installer packaging scripts to include required docs. |
| `BLAKE3 verification skipped` | Manifest has `blake3`, but no local `b3sum` or `blake3` executable is available. | Install a trusted BLAKE3 tool or treat SHA-256 as the verified minimum. |

## Expected Command Outcomes And Exit Codes

| Command | Ready outcome | Blocked outcome | Exit code |
| --- | --- | --- | ---: |
| `drs validate` | All required fields are present. | Required fields are missing or empty. | 0 or 1 |
| `drs verify-manifest` | Footer reports no failures. | Footer reports failures or release status blocks readiness. | 0 or 1 |
| `drs check-release` | Footer reports `Release is READY` or `READY (with warnings)`. | Footer reports `Release is BLOCKED`. | 0 or 1 |
| `drs hash <path>` | SHA-256 and file size are printed. | Artifact path is missing or cannot be read. | 0 or 1 |
| `drs hash <path> --blake3` | SHA-256 is printed; BLAKE3 is printed when a tool is available. | Missing artifact, or BLAKE3 unavailable when the operator requires it. | 0 or 1 |
| invalid command or missing required argument | Help or usage is printed. | Invocation must be corrected. | 2 |

Warnings are not automatic release blockers unless the release tier or operator policy says they are.
For security-sensitive and distribution-grade releases, resolve or explicitly record every warning before publishing.
