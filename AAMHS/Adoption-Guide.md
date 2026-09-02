# AAMHS Adoption Guide

Use AAMHS when preserving or releasing archives that need durable integrity validation.

## Steps

1. Declare hash suite.
2. Generate hash manifest.
3. Record archive integrity evidence.
4. Add detached signatures with ArchiveHasher/`manifest-signer.exe` or equivalent tooling when required by the archive context.
5. Document validation procedure.
6. Preserve verification records with the archive.
7. Record known gaps, missing files, and validation limits.
8. Use ARHS separately when publishing release artifacts that require release hash manifests.
9. Do not describe AAMHS detached signatures as a replacement for Microsoft Store signing, Authenticode signing, or package-ecosystem provenance.

## SFDS Relationship

Use SFDS to maintain AAMHS as a standard suite.
Use AAMHS to govern archive hash manifests, multi-hash policy, detached signatures, and integrity records.
Use ARHS for release hash manifests.
