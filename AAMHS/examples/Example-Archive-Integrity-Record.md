# Archive Integrity Record

## Archive

- Archive ID: `city-hall-standards-snapshot-2026-06-11`
- Archive title: City Hall standards snapshot
- Coverage: Standard-suite source documents, manifests, templates, examples, and validation records
- Created: `2026-06-11`

## Hash Suite

- Primary: SHA256
- Additional: BLAKE3, KangarooTwelve
- Manifest: `hashes/city-hall-standards-snapshot-2026-06-11.hashes.toml`

## Files

| Path | Size bytes | SHA256 | BLAKE3 | KangarooTwelve |
| --- | ---: | --- | --- | --- |
| `SFDS/Standards Framework Development Standard.md` | `42120` | `example-sha256-sfds` | `example-blake3-sfds` | `example-k12-sfds` |
| `DRS/Documentation Release Standard.md` | `38642` | `example-sha256-drs` | `example-blake3-drs` | `example-k12-drs` |
| `WGS/Workspace Governance Standard.md` | `44518` | `example-sha256-wgs` | `example-blake3-wgs` | `example-k12-wgs` |

## Signatures

- Detached signatures used: no
- Signature policy note: This example records hash integrity only. Production archives should record detached signature status when signing is used.

## Validation Procedure

```powershell
python WGS/tools/city_hall_audit.py --root D:\010-CITY-HALL
Get-FileHash SFDS\Standards Framework Development Standard.md -Algorithm SHA256
b3sum SFDS\Standards Framework Development Standard.md
k12sum SFDS\Standards Framework Development Standard.md
```

## Verification Result

- Result: partial
- Verified on: `2026-06-11`
- Known limits: Example hash values are placeholders that demonstrate record shape. A production archive integrity record must use actual computed hashes.
