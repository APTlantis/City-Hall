# Aptlantis Archive Multi-Hash Standard

## Status

Candidate v1.0.3.

## Scope

AAMHS governs archive hash suites, manifest formats, detached signatures, validation procedures, and archival integrity records.

## Does Not Govern

AAMHS does not govern UI design, project proposals, workspace root layout, dataset licensing, release distribution channels, or platform/package signing.

## Required Archive Artifacts

- Hash manifest.
- Archive integrity record.
- Hash suite declaration.
- Signature policy when signatures are used.
- Validation procedure.
- Preservation notes.

## Relationship to ARHS

ARHS defines release hash manifest requirements for release artifacts.
AAMHS governs richer archive preservation records.

Use ARHS when publishing a release artifact.
Use AAMHS when preserving archives, collections, datasets, evidence bundles, or release snapshots that need long-term verification, detached signatures, validation procedures, and preservation notes.

Quick boundary:

| Use case | Standard |
| --- | --- |
| Single release artifact hash manifest | ARHS |
| Archive, collection, evidence bundle, or snapshot with multiple files | AAMHS |
| Detached signature policy for preserved archive material | AAMHS |
| Long-term revalidation procedure for preserved bytes | AAMHS |

## Hash Manifest Requirements

AAMHS hash manifests should record:

- Archive id and title.
- Artifact filenames.
- File sizes when known.
- Hash suite used.
- Hash values.
- Hash generation date.
- Tool names or commands.
- Maintainer or operator.
- Related release, dataset, or archive records.
- Expected update cadence.

## Integrity Record Requirements

An archive integrity record should answer:

- What archive or collection is being preserved?
- Which files are covered?
- Which hash suite was used?
- Were signatures used?
- How can the archive be verified later?
- What known gaps, missing files, or validation limits exist?

## Signature Policy

Detached signatures are optional unless required by the archive context.
When signatures are used, the record must identify:

- Signature file.
- Signing tool.
- Signing identity or key reference.
- Verification procedure.
- Trust limitations.

ArchiveHasher and `manifest-signer.exe` are the current Aptlantis AAMHS tooling references for archive hashing and detached manifest signing. Their PGP and SLH-DSA signatures are archive-preservation evidence. They do not replace Microsoft Store signing for Store MSIX packages, Authenticode signing for direct Windows binaries, or provenance supplied by package ecosystems such as crates.io, PyPI, Go modules, or GitHub releases.

## Validation Rules

Validation must confirm:

- Every listed file exists or is intentionally marked missing.
- Every listed hash matches the file bytes.
- The hash suite is declared.
- Signature verification is documented when signatures are used.
- Preservation notes identify known gaps or environmental assumptions.

## Archive Blockers

An archive is blocked from AAMHS-ready status when:

- Hash manifest is missing.
- Archive integrity record is missing.
- Hash suite is not declared.
- Listed files cannot be identified.
- Any required hash mismatches.
- Signature policy is unclear when signatures are claimed.
- Preservation notes omit known gaps.
