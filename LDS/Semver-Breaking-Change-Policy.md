# LDS Semver And Breaking-Change Policy Template

## Purpose

Use this template when an LDS-governed library claims `versioned` or `reference` stability.

## Versioning Scheme

- Scheme: Semver.
- Current version:
- Minimum supported runtime or toolchain:
- Rust MSRV, when applicable:

## Breaking Changes

The following are breaking changes:

- removing a public function, type, trait, interface, module, or exported field;
- renaming a public API item;
- changing public return types or error types;
- changing trait or interface requirements;
- changing default behavior that stable consumers rely on;
- raising MSRV or runtime requirements beyond the documented support policy.

## Non-Breaking Changes

The following are non-breaking when existing behavior remains valid:

- adding optional public functions;
- adding optional fields;
- adding trait implementations for existing types;
- improving diagnostics without changing error type contracts;
- adding support for a newer runtime while preserving the current minimum.

## Migration Record

For each breaking change, record:

- old API;
- new API;
- first version where replacement is available;
- removal version;
- consumer impact;
- migration example;
- changelog entry.

## Rust MSRV Note

For Rust crates, raising MSRV is a compatibility-impacting change.
Patch releases should not raise MSRV.
Minor releases may raise MSRV only when the policy allows it and the changelog records the new minimum.
Major releases may raise MSRV with explicit migration notes.
