# CTS JSON Data Payload Guidance

## Purpose

`CommandOutput.schema.json` defines the reusable CTS output envelope.
This guidance defines how command-specific `data` payloads should be shaped so automation consumers can rely on them.

## Recommended Data Shapes

Use one of these shapes for `data`:

| Shape | Use when | Example |
| --- | --- | --- |
| object | One command result with named fields | `{ "files_checked": 12, "valid": true }` |
| array of objects | A list of homogeneous records | `[{ "path": "a.toml", "status": "ok" }]` |
| object with `items` | A list plus summary metadata | `{ "summary": {...}, "items": [...] }` |

Avoid scalar `data` values for stable commands.
If the result is a single value, wrap it in an object with a named field.

## Stable Field Rules

- Fields documented in the command contract are automation-stable.
- Additive fields are allowed in minor versions.
- Removing, renaming, or changing the type of a stable field requires a breaking-change note.
- Use `null` for known-but-unavailable values.
- Omit fields only when the contract says they are optional.

## Error Payloads

In machine-readable mode, failures should still use the CTS envelope:

```json
{
  "status": "error",
  "tool": "example-tool",
  "version": "1.2.0",
  "errors": [
    {
      "code": "input-missing",
      "message": "Input file was not found.",
      "path": "config.toml"
    }
  ]
}
```

Normal progress, debug text, and human-readable warnings must not appear in stdout when JSON output is requested.
