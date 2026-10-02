# Entity-Named Live Manifest Migration — 2026-07-08

## Decision

Every governed directory uses the exact containing directory name plus `.manifest.toml`. `Development.manifest.toml` remains the drive-root exception.

Examples:

- `D:\CTS\CTS.manifest.toml`
- `D:\CTS\CloneCratesio\CloneCratesio.manifest.toml`
- `D:\.dpw\.dpw.manifest.toml`

## Preservation

Conflicting live entity-named, generic, and historical records were moved to `Legacy-Live-Manifests-20260708` with their workspace-relative paths preserved. No legacy record is a parallel local authority.

The migration tool promoted 63 current governed records, reconciled project version/lifecycle metadata from explicit local evidence, added verification boundaries, normalized paths and inheritance, and updated local document references.

## Canonical-link policy

Standards and templates resolve through manifest paths and Markdown links to `D:\.city_hall`. Six portfolio-root Windows shortcuts were removed. Project artifacts that happen to use `.lnk` files are not governance dependencies.

## Holdings

WDS, CTS, and DRS holding roots now have entity manifests and instructions. Their children remain preserved and excluded from active reporting until explicitly reactivated.

## Foundation roots

`.dpw`, `.library`, and `.sonar` were reclassified and normalized. The former `.agents` root was absent during migration and is intentionally not registered.

## Verification boundary

Metadata reconciliation does not imply code, build, test, artifact, or release readiness. Project manifests record those checks separately. No project was promoted to `release-ready` by this migration.
