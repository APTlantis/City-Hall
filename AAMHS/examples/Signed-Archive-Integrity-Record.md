# Signed Archive Integrity Record

## Archive

- Archive id: `aamhs-signed-example`
- Title: Signed AAMHS Example Archive
- Date: 2026-07-30
- Maintainer: Aptlantis

## Hash Manifest

- Manifest: `Example-Hash-Manifest.toml`
- Primary hash: SHA-256
- Additional hashes: none in this minimal example

## Detached Signature Policy

Detached signatures are used when archive material is distributed outside the trusted workspace or when the archive is a long-term preservation checkpoint.

Example signature files:

| File | Signature | Tool | Identity |
| --- | --- | --- | --- |
| `sample-archive/payload.txt` | `sample-archive/payload.txt.sig` | `gpg --detach-sign` | `archive-operator@example.local` |

## Verification Procedure

1. Verify file hashes:

```powershell
python AAMHS\tools\aamhs_validate.py AAMHS\examples\Example-Hash-Manifest.toml
```

2. Verify signature files are present:

```powershell
python AAMHS\tools\aamhs_signature_check.py AAMHS\examples\Example-Hash-Manifest.toml
```

3. Verify cryptographic signatures with the signing tool and trusted keyring:

```powershell
gpg --verify sample-archive\payload.txt.sig sample-archive\payload.txt
```

## Trust Limits

This record shows the canonical evidence shape.
It does not include a real detached signature because the example payload is only a minimal fixture.
