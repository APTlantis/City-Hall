# LDS Breaking-Change Cycle Example

## Purpose

This example simulates a breaking-change cycle for an LDS-governed library.

## Library

- Library: `ManifestQuery.Core`
- Previous version: `0.3.0`
- New version: `1.0.0`
- Stability before change: `interface-stable`
- Stability after change: `versioned`

## Breaking Change

Old API:

```text
ManifestQuery.find_by_status(status)
```

New API:

```text
ManifestQuery.find_by_lifecycle(state)
```

## Reason

WGS uses lifecycle terminology across project and entity manifests.
The old `status` name blurred lifecycle state with health, maturity, and release status.

## Migration

- Add `find_by_lifecycle(state)` in `0.4.0`.
- Keep `find_by_status(status)` as deprecated through `0.4.x`.
- Emit deprecation warning in developer docs.
- Remove `find_by_status(status)` in `1.0.0`.
- Record migration in changelog and interface note.

## Validation

The breaking-change record is acceptable under LDS because:

- old and new API names are recorded;
- migration window is documented;
- consumer impact is stated;
- version bump is explicit;
- known consumers can update before removal.
