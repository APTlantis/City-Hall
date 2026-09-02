# CTS Progress Output Compatibility

## Purpose

Progress output is useful for humans and risky for automation.
This note keeps progress reporting compatible with CTS machine output.

## Rules

- `--json` output must write one final JSON envelope to stdout.
- Progress messages during `--json` mode should go to stderr or a log file.
- Do not interleave progress bars, spinners, prompts, or colored text with JSON stdout.
- For long-running commands, prefer JSONL event mode only when explicitly documented.
- If a command supports JSONL progress, each line must be a complete JSON object with `event`, `tool`, and `version`.

## Example JSONL Event

```json
{"event":"progress","tool":"example-command","version":"1.0.0","data":{"current":3,"total":10}}
```

JSONL progress is a separate mode. It is not the same as the final CTS JSON envelope.
