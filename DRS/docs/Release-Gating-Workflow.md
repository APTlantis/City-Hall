# DRS Release Gating Workflow

## Purpose

This workflow shows how to use DRS checks as a continuous release gate without replacing human release review.

## Gate Order

1. Fill or update the project manifest.
2. Generate artifact hashes with `drs.ps1 hash`.
3. Update the release note and optional JSON-LD metadata.
4. Run manifest verification.
5. Run integrity checks.
6. Run the full release check.

```powershell
pwsh -File DRS/drs.ps1 verify-manifest
python DRS/tools/drs_integrity_check.py ProjectName.manifest.toml --json
pwsh -File DRS/drs.ps1 check-release
```

## CI Meaning

| Gate | Blocks release when |
| --- | --- |
| `verify-manifest` | Required release fields are missing or inconsistent. |
| `drs_integrity_check.py` | Declared SHA-256 or BLAKE3 does not match the artifact, or signing metadata is absent. |
| `check-release` | Artifact, release note, checklist, or required publishing evidence is missing. |

BLAKE3 absence is a warning when the manifest does not declare a BLAKE3 hash.
Signing absence is an error; an explicit `unsigned` statement is allowed but remains a warning.
