# APTlantis Release Hashing Standard

## Status

Candidate v0.3.0. Promoted active candidate copy in `D:\.city_hall\ARHS`.

## Scope

Every Aptlantis release artifact SHALL be accompanied by a release hash manifest. The purpose of this manifest is to provide integrity verification, long-term confidence, and independence from any single cryptographic algorithm or vendor ecosystem.

The APTlantis project views software releases as artifacts worthy of preservation. Verification information should remain useful and trustworthy for years or decades after publication.

## Required Hash Algorithms

All release hash manifests MUST include the following hash entries:

* SHA256
* BLAKE3-256
* KT128

KT128 means a 128-byte KangarooTwelve XOF digest encoded as base64. BLAKE3-256 means the 32-byte BLAKE3 digest encoded as lowercase hexadecimal. SHA256 is encoded as lowercase hexadecimal in ARHS `.hashmanifest.toml` records for compatibility with ReleaseHasher; delivery standards may additionally require uppercase SHA-256 in release notes or legacy manifests.

## Relationship to DRS, CTS, WDS, DDS, LDS, and AAMHS

ARHS governs release artifact hash requirements.

DRS, CTS, WDS, DDS, and LDS govern release readiness and distribution posture for their project classes.
AAMHS governs long-term archive integrity records, richer preservation hash manifests, and detached archive signatures.

When a release artifact is published, ARHS defines the minimum hash set that must accompany it.
When an archive is preserved for long-term integrity validation, AAMHS may add additional manifest, signature, and preservation requirements.

## Distribution and Signing Policy

Release records must distinguish distribution from signing or provenance. The distribution channel decides the appropriate signing authority:

| Software type | Distribution | Signing or provenance |
| --- | --- | --- |
| Windows GUI application | MSIX submitted through Microsoft Store | Microsoft signs the Store package |
| Windows GUI development build | MSIX sideload | Self-signed development certificate; non-production |
| Cross-platform CLI | GitHub releases or package ecosystem | Platform-appropriate signing or ecosystem provenance |
| Windows CLI | ZIP, portable binary, or package manager | Authenticode optional unless the channel requires it |
| Rust/Python/Go/etc. tool | crates.io, PyPI, Go modules, GitHub, or equivalent | Ecosystem provenance plus release hash evidence |
| Internal utility | Simplest appropriate channel | Self-sign only when useful |

ARHS does not sign release artifacts. It may record the distribution channel and signing/provenance authority so readers understand who vouches for the artifact. ArchiveHasher and `manifest-signer.exe` are AAMHS archive-preservation tools; their detached PGP and SLH-DSA signatures do not replace Microsoft Store signing, Authenticode signing, or package-ecosystem provenance.

## Rationale

### SHA256: Universal Compatibility

SHA256 remains the most widely recognized and supported cryptographic hash algorithm in software distribution.

Benefits include:

* Native support across Windows, Linux, and macOS
* Compatibility with security scanners and CI/CD systems
* Broad recognition by users and organizations
* Long-established industry adoption

SHA256 serves as the baseline verification method that virtually every user can validate without installing additional tooling.

### BLAKE3-256: High-Performance Modern Hashing

BLAKE3-256 represents the current state of the art in practical hashing performance while using a fixed 32-byte release digest.

Benefits include:

* Extremely high throughput
* Parallel processing support
* Excellent performance on modern CPUs
* Strong cryptographic design
* Growing ecosystem adoption

BLAKE3-256 is particularly valuable when verifying large artifacts such as ISO images, archives, datasets, virtual machine images, and software collections.

### KT128: Independent Cryptographic Lineage

KT128 is the ARHS release-manifest profile for KangarooTwelve: a 128-byte XOF digest encoded as base64. KangarooTwelve is a high-performance derivative of the Keccak family, the basis of SHA-3.

Benefits include:

* Distinct design lineage from SHA-2 and BLAKE families
* Excellent performance characteristics
* Strong security margins
* Modern sponge-based construction
* Long-term cryptographic diversity

KT128 provides algorithmic independence, reducing reliance on any single family of cryptographic designs.

## Defense Through Diversity

The selected algorithms intentionally originate from different cryptographic families:

| Algorithm      | Family         |
| -------------- | -------------- |
| SHA256 | SHA-2 |
| BLAKE3-256 | BLAKE |
| KT128 | Keccak / SHA-3 |

This approach improves long-term resilience by avoiding dependence on a single algorithm family.

The goal is not merely redundancy, but cryptographic diversity.

## Post-Quantum Considerations

Current research indicates that cryptographic hash functions remain significantly more resistant to quantum attacks than traditional public-key cryptography.

The selected algorithms provide strong security margins while maintaining practical performance. Aptlantis considers SHA256, BLAKE3-256, and KT128 an appropriate balance between compatibility, performance, and future resilience.

## Future Direction

Aptlantis may supplement release hashes with cryptographic signatures when a distribution channel or archive context requires them.

Hashes verify that a file has not changed.

Signatures or ecosystem provenance verify who published it.

Both play an important role in long-term software preservation and provenance.

## Release Hash Manifest Requirements

Every release hash manifest must include:

- Release project name.
- Release version.
- Artifact filename.
- Artifact path or URI.
- Artifact size in bytes.
- `SHA256` hash.
- `BLAKE3-256` hash.
- `KT128` hash.
- Distribution channel when known.
- Signing or provenance authority when known.
- Tool names or commands used when practical.

The hash record must name the exact artifact file the hashes cover.
Do not publish loose hashes without filenames.

The canonical adopter artifact is a `.hashmanifest.toml` compatible with ReleaseHasher:

```toml
[release]
name = "FileCabinet"
version = "0.1.0.0"
artifact = "FileCabinet-0.1.0.0-win-x64.msix"
path = "D:\\DRS\\File Cabinet\\artifacts\\installer\\FileCabinet-0.1.0.0-win-x64.msix"
size_bytes = 123456
distribution = "microsoft-store-msix"
signing = "microsoft-store-signed"

[[hash]]
algorithm = "SHA256"
value = "<32-byte lowercase hex>"

[[hash]]
algorithm = "BLAKE3-256"
value = "<32-byte lowercase hex>"

[[hash]]
algorithm = "KT128"
value = "<128-byte KangarooTwelve XOF digest, base64>"
```

## Verification Rules

Verification must confirm:

- All required algorithms are present.
- Hashes are formatted consistently.
- The artifact file exists.
- Each recorded hash matches the artifact bytes.
- The release note, manifest, or publication record points to the same artifact name.
- Distribution and signing/provenance are named when the artifact is publicly distributed.

If any hash mismatches, the release artifact is not verified.

## Release Blockers

An APTlantis release artifact is blocked when:

- SHA256 is missing.
- BLAKE3-256 is missing.
- KT128 is missing.
- A recorded hash does not match the artifact.
- The hash record does not identify the exact artifact filename.
- The release document and hash record disagree about artifact name or version.
- Hashes were computed before final packaging.
- A public release omits its distribution channel or signing/provenance authority.

## Required Artifacts

- Specification (`APTlantis Release Hashing Standard.md`).
- `ARHS.manifest.toml` for the standard suite.
- Adoption guide (`Adoption-Guide.md`).
- Validation checklist (`Validation-Checklist.md`).
- Changelog (`CHANGELOG.md`).

## Validation

Conformance is checked by verifying that any released artifact provides a valid `.hashmanifest.toml` with SHA256, BLAKE3-256, and KT128 entries, and that these hashes match the final artifact.
