# ManifestQuery.Core Library Interface Note

Example status: completed public API validation example for LDS v0.2.0.

## Public API Surface

`ManifestQuery.Core` exposes:

- `ManifestLoader.load(path)` for reading a TOML manifest into a typed record.
- `ManifestIndex.from_roots(paths)` for building an in-memory index of entity manifests.
- `ManifestQuery.find_by_standard(standard)` for locating projects governed by a standard.
- `ManifestQuery.find_by_lifecycle(state)` for lifecycle filtering.

The API is intentionally read-only.

## Stability Level

`interface-stable`

The public surface is small enough for independent consumers to build against without expecting churn.

## Versioning / Breaking-Change Policy

Semver is used.
Removing methods, changing return types, or renaming query fields requires a major version.
Adding optional filters or additive record fields is a minor version.

## Extension Contracts

No plugin interface exists.
Future storage backends must implement a read-only `ManifestStore` contract with deterministic iteration order.

## Known Consumers

- `manifest-audit` CLI, governed by CTS.
- Standards-health report generator, governed by WGS/AAS.

## Companion Crates

| Crate | Standard |
| --- | --- |
| `manifest-query-cli` | CTS |

## Known Gaps

- This example validates LDS shape; it is not yet tied to a committed crate in this repository.
