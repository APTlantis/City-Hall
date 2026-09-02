# Aptlantis Archive Multi-Hash Standard (AAMHS)

![Standard](https://img.shields.io/badge/archive%20standard-AAMHS%20v1.0.3-blue)
![Manifest](https://img.shields.io/badge/manifest-TOML-orange)
![Integrity](https://img.shields.io/badge/integrity-multi--hash-green)
![Signatures](https://img.shields.io/badge/signatures-detached-purple)
![Status](https://img.shields.io/badge/status-active-lightgrey)

AAMHS defines long-term archive verification and integrity validation for Aptlantis archival systems.

AAMHS is the preservation integrity standard. ARHS defines release-artifact hash manifests; AAMHS adds archive manifests, validation records, detached signature policy, and preservation notes.

ArchiveHasher and `manifest-signer.exe` are AAMHS archive-preservation tools. `archive-hasher` computes preservation hash manifests; `manifest-signer.exe` signs manifests for archive evidence with detached PGP and optional SLH-DSA workflows. These signatures do not replace Microsoft Store signing, Authenticode signing, or package-ecosystem provenance for release distribution.

## Document Suite

| File | Purpose |
| --- | --- |
| `Aptlantis Archive Multi-Hash Standard.md` | Primary AAMHS specification wrapper. |
| `AAMHS.manifest.toml` | Standard manifest. |
| `HashManifest.schema.toml` | TOML-oriented hash manifest schema. |
| `HashManifest.schema.json` | JSON Schema mapping for broader tool compatibility. |
| `templates/Archive-Integrity-Record.md` | Archive integrity record template. |
| `templates/Hash-Manifest.toml` | Hash manifest template. |
| `CI-Usage.md` | Local and CI automation snippets for AAMHS validation. |
| `tools/aamhs_validate.py` | Reference hash manifest validator and SHA-256 verifier. |
| `tools/aamhs_signature_check.py` | Detached-signature presence checker. |
| `examples/Example-Hash-Manifest.toml` | Concrete hash manifest with computed SHA-256. |
| `examples/Signed-Archive-Integrity-Record.md` | Canonical signed archive integrity record shape. |
| `Adoption-Guide.md` | AAMHS adoption procedure. |
| `Validation-Checklist.md` | Archive integrity checklist. |
| `CHANGELOG.md` | AAMHS version history. |

Existing source material remains in `references/APTlantis Release Hashing Standard.md` and `D:\010-CITY-HALL\AADR\AptlantisEcosystem\Standards\AAMHS v1.0.md`.

## SFDS Suite Model

`AAMHS.manifest.toml` describes AAMHS as a standard suite.
The templates in `templates/` describe hash manifests and archive integrity records governed by AAMHS.
