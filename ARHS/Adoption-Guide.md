# APTlantis Release Hashing Standard Adoption Guide

## When To Adopt

Any Aptlantis project that produces software release artifacts, such as MSIX packages, installers, portable binaries, archives, datasets, virtual machine images, or software collections.

## Required Steps

1. Read the specification.
2. Read `ARHS.manifest.toml` to understand the suite boundary.
3. Generate a `.hashmanifest.toml` for the final release artifact with ReleaseHasher or an equivalent documented command.
4. Ensure the manifest includes SHA256, BLAKE3-256, and KT128 entries.
5. Publish the hash manifest alongside the release artifact.
6. Record known gaps (e.g. lack of tooling for a specific environment).
7. Ensure the release document and hash record name the same final artifact.
8. Record the distribution channel and signing/provenance authority when the artifact is public.
9. Use AAMHS when the artifact is being preserved as part of a long-term archive.

## Distribution Defaults

| Software type | Distribution | Signing or provenance |
| --- | --- | --- |
| Windows GUI application | MSIX submitted through Microsoft Store | Microsoft signs the Store package |
| Windows GUI development build | MSIX sideload | Self-signed development certificate; non-production |
| Cross-platform CLI | GitHub releases or package ecosystem | Platform-appropriate signing or ecosystem provenance |
| Windows CLI | ZIP, portable binary, or package manager | Authenticode optional unless the channel requires it |
| Rust/Python/Go/etc. tool | crates.io, PyPI, Go modules, GitHub, or equivalent | Ecosystem provenance plus release hash evidence |
| Internal utility | Simplest appropriate channel | Self-sign only when useful |

## Manifest Model

`ARHS.manifest.toml` describes this standard.
Adopter manifests, schemas, and document templates describe the projects or artifacts governed by this standard.
