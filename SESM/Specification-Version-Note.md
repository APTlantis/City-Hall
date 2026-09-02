# SESM Specification Version Note

## Purpose

This note reconciles the current SESM suite version with the historical primary specification filename.

## Canonical Pointer

The current SESM suite version is `0.3.0`, as declared in `SESM.manifest.toml`, `README.md`, and `CONFORMANCE.md`.

The primary specification file remains:

```text
SESM-v0.2.md
```

That filename is preserved for continuity with the original SESM draft lineage.
For the public-review candidate suite, treat `SESM-v0.2.md` plus the registered governance notes as the canonical SESM `0.3.0` specification packet.

## Public-Review Packet

Use this packet when evaluating SESM `0.3.0`:

- `SESM-v0.2.md`
- `SAFE-PROFILE.md`
- `CONFORMANCE.md`
- `VALIDATOR-RULES.md`
- `THREAT-MODEL.md`
- `PRIVACY.md`
- `SECURITY.md`
- `REFERENCE-IMPLEMENTATION.md`
- `Specification-Version-Note.md`

## Compatibility Meaning

The embedded `sesm_version` field identifies the metadata profile inside an SVG.
The suite version identifies the documentation, validator, fixtures, and governance packet.

SESM `0.3.0` validators intentionally continue to accept historical `0.2.0` metadata where it remains structurally compatible.
New examples and public-review fixtures should use `sesm_version: "0.3.0"` unless they are specifically testing cross-version compatibility.
