# Workspace Governance Audit — 2026-07-07

- Command: `python D:\.city_hall\WGS\tools\city_hall_audit.py --root D:\.city_hall --workspace-root D:\`
- Exit code: `0`
- Audit scopes: 21
- Failures: 0
- Warnings: 2

## Result

All 15 detected City Hall standard suites passed. The drive root and the WDS, BASIC, CTS, DATA, and DRS portfolio scopes passed structural validation.

The two warnings are intentional registered migration items:

- `D:\CTS\Command Tool Standard.md`
- `D:\DRS\Desktop Application Release Standard.md`

Canonical authority for those standards is under `D:\.city_hall`. The portfolio copies remain registered as legacy evidence pending manual disposition.

## Workspace checks covered

- Root `AGENTS.md`, `INDEX.md`, and `Development.manifest.toml`
- Portfolio `AGENTS.md` and `directory.manifest.toml`
- Physical versus registered direct children
- Exactly one declared classification per governed child
- Required project/group files
- Registered nested project-group children
- Manifest physical paths and parent relationships
- Canonical standard-link resolution
- Placeholder detection
- Registration of known non-canonical standard copies

## Interpretation boundary

This is a governance-structure verdict. It does not establish that every project's code, build, tests, artifact, version, or release posture has been independently verified. Those gaps remain explicit in project manifests and `Project-README.md` files.
