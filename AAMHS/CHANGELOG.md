# AAMHS Changelog

## Unreleased

- Clarified that ArchiveHasher and `manifest-signer.exe` are archive-preservation hashing and detached-signing tools.
- Clarified that AAMHS signatures do not replace Microsoft Store signing, Authenticode signing, or package-ecosystem provenance for release distribution.
- Updated ARHS relationship language to point to release hash manifests instead of generic minimum release hashes.
- Refined `HashManifest.schema.toml` with item-level fields, allowed hash algorithms, and signature fields.
- Added a concrete hash manifest example with computed SHA-256.
- Added lightweight hash and detached-signature validator scripts.
- Clarified ARHS/AAMHS quick boundary guidance.
- Recorded update cadence in the suite manifest.
- Added JSON Schema mapping, CI usage guidance, and signed archive integrity record example.

## 1.0.3 - 2026-06-11

- Added a filled archive integrity record example.
- Clarified practical AAMHS record shape for archive coverage, hash suites, signature policy notes, validation procedure, and known limits.
- Added a lightweight hash manifest schema.

## 1.0.2 - 2026-06-11

- Clarified the boundary between ARHS release-artifact hashing and AAMHS archive preservation integrity records.
- Added hash manifest requirements, integrity record requirements, signature policy expectations, validation rules, and archive blockers.

## 1.0.1 - 2026-06-10

- Added SFDS two-layer suite metadata to the AAMHS standard manifest.
- Added an AAMHS suite map example.
- Clarified README, adoption, and validation language for suite conformance versus archive integrity readiness.

## 1.0.0 - 2026-06-10

- Added WGS/SFDS standard root and normalization wrapper.
- Preserved existing AAMHS source documents as references.
