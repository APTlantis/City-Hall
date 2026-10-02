# APTlantis Release Hashing Standard (ARHS)

![Standard](https://img.shields.io/badge/standard-ARHS%20v0.3-blue)
![Manifest](https://img.shields.io/badge/manifest-TOML-orange)
![Integrity](https://img.shields.io/badge/integrity-SHA256%20%7C%20BLAKE3--256%20%7C%20KT128-green)
![Status](https://img.shields.io/badge/status-candidate-lightgrey)

A standard for ensuring the long-term integrity, verification, and cryptographic diversity of Aptlantis release artifacts. ARHS defines the required release hash manifest that must accompany publishable release artifacts.

ARHS conforms to SFDS at the standard-suite governance layer. SFDS describes how this documentation suite is indexed, validated, and normalized; ARHS remains authoritative for cryptographic hashing rules for APTlantis release artifacts.

This promoted copy in `D:\.city_hall\ARHS` is the active candidate standard. The City Hall copy remains historical workshop material unless explicitly updated or cited as lineage.

ARHS is the release-artifact hash rule. AAMHS is the richer archive preservation integrity and detached-signature standard. DRS, CTS, WDS, DDS, LDS, and ecosystem-specific standards decide how an artifact is distributed.

---

## What This Standard Covers

| Area | Summary |
|------|---------|
| Algorithms | Required release hash algorithms (`SHA256`, `BLAKE3-256`, `KT128`) |
| Cryptographic Diversity | Avoiding dependence on a single algorithm family |
| Manifest | `.hashmanifest.toml` release hash manifests compatible with ReleaseHasher |
| Verification | Manual and automated verification of final released artifacts |

## Distribution and Signing Boundary

ARHS does not sign artifacts and does not decide the distribution channel. Release records must name both the distribution path and the signing or provenance authority.

| Software type | Distribution | Signing or provenance |
| --- | --- | --- |
| Windows GUI application | MSIX submitted through Microsoft Store | Microsoft signs the Store package |
| Windows GUI development build | MSIX sideload | Self-signed development certificate; non-production |
| Cross-platform CLI | GitHub releases or package ecosystem | Platform-appropriate signing or ecosystem provenance |
| Windows CLI | ZIP, portable binary, or package manager | Authenticode optional unless the channel requires it |
| Rust/Python/Go/etc. tool | crates.io, PyPI, Go modules, GitHub, or equivalent | Ecosystem provenance plus release hash evidence |
| Internal utility | Simplest appropriate channel | Self-sign only when useful |

ArchiveHasher and `manifest-signer.exe` belong to AAMHS archive-preservation workflows. Their detached PGP and SLH-DSA signatures do not replace Microsoft Store signing, Authenticode signing, or package-ecosystem provenance for release distribution.

---

## Document Suite

ARHS follows the SFDS two-layer model:

- `ARHS.manifest.toml` describes the ARHS standard suite.

### Core

| File | Purpose |
|------|---------|
| [`APTlantis Release Hashing Standard.md`](APTlantis%20Release%20Hashing%20Standard.md) | The full hashing standard. Read this first. |
| [`ARHS.manifest.toml`](ARHS.manifest.toml) | Machine-readable standard manifest. |
| [`Adoption-Guide.md`](Adoption-Guide.md) | How an APTlantis project adopts ARHS. |
| [`Validation-Checklist.md`](Validation-Checklist.md) | Manual validation checklist. |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history for ARHS. |

### Examples

| File | Purpose |
|----------|---------|
| [`examples/sample-hashes.txt`](examples/sample-hashes.txt) | Example of a text file containing the required hashes for a release artifact. |

---

## Quick Start

### For Projects Adopting ARHS

1. Review the [Specification](APTlantis%20Release%20Hashing%20Standard.md) and [Adoption Guide](Adoption-Guide.md).
2. Use ReleaseHasher, or an equivalent documented command, to generate a `.hashmanifest.toml` for each final release artifact.
3. Publish the hash manifest alongside the release artifact.
4. Run through the [Validation Checklist](Validation-Checklist.md) to ensure compliance.

---

## Core Principles

**Verification is Long-Term.**
Software releases are artifacts worthy of preservation. Verification information should remain useful and trustworthy for years or decades after publication.

**Algorithmic Independence.**
Relying on a single cryptographic family creates a single point of failure. ARHS enforces diversity by requiring algorithms from different lineages (SHA-2, BLAKE, Keccak).

**Baseline Compatibility + Modern Performance.**
SHA256 ensures universal compatibility, while BLAKE3-256 and KT128 provide high-performance verification for large files with independent cryptographic lineage.
