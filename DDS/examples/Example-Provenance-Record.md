# Provenance Record

## Sources

- Source name: Example public domain text notes
- Source location: `data/raw/example-notes/`
- Collection date or range: 2026-06-10
- Collector: Herb

## Collection Method

Files were copied from a local public-domain source folder into a raw dataset staging directory.

## Transformations

- Step: Normalize line endings.
- Tool or script: `normalize-lines.ps1`
- Output: `data/working/example-notes-normalized/`

## Removed or Filtered Records

- Rule: Remove empty files.
- Count: 3
- Reason: Empty files do not contribute usable examples.

## License Notes

Source material is public domain. Public release remains blocked until license status is reviewed against the original source notes.

## Validation

- Checks performed: file count, UTF-8 decode, empty file scan.
- Result: passed with 3 empty files removed.
- Date: 2026-06-10

## Splits

- Method: deterministic hash split by filename.
- Seed: not applicable.
- Counts: train 80, validation 10, test 10.

## Integrity

- Artifact: `example-notes-v0.1.0.zip`
- Hash algorithm: SHA-256
- Hash: `TBD`

## Known Limitations

Small example dataset. Not representative enough for model evaluation.

## Review

- Maintainer: Herb
- Last reviewed: 2026-06-10

