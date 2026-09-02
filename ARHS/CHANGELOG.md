# APTlantis Release Hashing Standard Changelog

## 0.3.0 - 2026-08-20

- Promoted ARHS into `D:\.city_hall\ARHS` as the active candidate release-hash standard.
- Aligned the required release hash suite with ReleaseHasher: SHA256, BLAKE3-256, and KT128.
- Made `.hashmanifest.toml` the canonical adopter artifact for release hash evidence.
- Added release distribution and signing/provenance boundaries, including Microsoft Store MSIX signing, self-signed development sideloads, CLI/package ecosystem provenance, and internal utility defaults.
- Clarified that ArchiveHasher and `manifest-signer.exe` belong to AAMHS archive-preservation signing workflows, not normal release signing.

## 0.2.1 - 2026-06-11

- Added a release hash record template.
- Added a filled ARHS release hash record example showing SHA256, BLAKE3, KangarooTwelve, artifact metadata, commands, and verification status.
- Updated suite manifest references for ARHS templates and examples.
- Added a lightweight release hash record schema.

## 0.2.0 - 2026-06-11

- Promoted ARHS to candidate maturity.
- Added hash record requirements, verification rules, release blockers, and relationship guidance for DRS, CTS, WDS, DDS, and AAMHS.
- Clarified that ARHS is the minimum release-artifact hash rule while AAMHS governs richer archive preservation records.

## 0.1.0 - 2026-06-10

- Initial draft.
