# HashSuite.Core Library Interface Note

Example status: second independent library validation example for LDS v0.2.0.

## Public API Surface

`HashSuite.Core` exposes:

- `HashAlgorithmId` for supported algorithm labels.
- `HashManifestReader.read(path)` for loading an AAMHS hash manifest.
- `HashVerifier.verify_file(entry, base_path)` for checking file size and SHA-256.
- `SignaturePolicy.describe(manifest)` for reporting detached signature expectations.

The API is library-only and has no direct command surface.

## Stability Level

`interface-stable`

The public surface is stable enough for an AAMHS validator and a future archive dashboard to consume.

## Versioning / Breaking-Change Policy

Semver is used.
Changing algorithm identifiers, verifier return shape, or manifest reader error types is breaking.
Adding new optional algorithms is minor when existing identifiers keep their meaning.

## Extension Contracts

Future hash algorithms implement a `HashProvider` contract:

- algorithm id;
- digest length when fixed;
- streaming update function;
- final uppercase string encoder.

## Known Consumers

- `aamhs-validate` reference validator.
- Future archive integrity dashboard.

## Companion Crates

| Crate | Standard |
| --- | --- |
| `hash-suite-cli` | CTS |

## Known Gaps

- This example validates LDS independence from CTS/AAMHS; it is not yet tied to a committed crate in this repository.
