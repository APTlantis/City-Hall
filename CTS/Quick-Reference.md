# CTS Quick Reference

Use this sheet while building, changing, reviewing, or releasing a command-line tool. It condenses the active **Command Tool Standard**; the full specification remains authoritative: [Command Tool Standard.md](Command%20Tool%20Standard.md).

## Use CTS When

CTS governs command-line tools, automation utilities, command contracts, streams, exit codes, structured output, destructive-command safety, and CLI distribution evidence.

It does **not** govern desktop GUI release packaging (DRS), websites (WDS), workspace placement (WGS), project intent (PPS), release hash manifests (ARHS), or archive-preservation signatures (AAMHS).

## The Contract Before Stability

A public command is not stable until its command contract documents:

- purpose, invocation, inputs, normal stdout, diagnostic stderr, exit codes, and examples;
- machine-readable mode and its automation-safe fields, when offered;
- stability of command names, flags, fields, and exit-code behavior; and
- preview, confirmation, and recovery behavior when it can delete, overwrite, move, publish, mutate, or revoke.

Use [templates/Command-Contract.md](templates/Command-Contract.md). Keep `--help` and version output accurate.

| Stability | What consumers may assume |
| --- | --- |
| `experimental` | May change without compatibility guarantees. |
| `documented` | Has a contract, examples, and exit-code behavior. |
| `stable` | Scripts may rely on its name, flags, documented fields, and exit codes. |
| `deprecated` | Still works; replacement and removal plan are documented. |

Public automation should use only `stable` commands.

## Output and Exit-Code Rules

| Surface | Rule |
| --- | --- |
| Normal interactive data | stdout |
| Diagnostics, warnings, progress, errors | stderr |
| `--json` / machine mode | Explicitly requested; stdout contains only the documented JSON result. |
| `--quiet` | Must not hide failures. |
| `--verbose` | Must not alter the machine-readable data shape. |
| JSONL progress | Separate, explicitly documented event mode; every line is complete JSON with `event`, `tool`, and `version`. |

Use the shared JSON envelope unless a command-specific schema is better documented. Its required fields are `status` (`ok`, `warning`, or `error`), `tool`, and `version`; `data`, `warnings`, and structured `errors` are optional. Prefer a named object, an array of records, or `{ summary, items }` for stable `data`; do not make automation rely on undocumented fields.

| Exit code | Meaning |
| ---: | --- |
| 0 | Success |
| 1 | General failure |
| 2 | Invalid usage or arguments |
| 3 | Missing input, path, or resource |
| 4 | Validation failure |
| 5 | External dependency unavailable |
| 10+ | Tool-specific; document it in the contract |

## Compatibility and Safety

Treat these as breaking changes for a stable command: renaming/removing a command or flag; changing an exit code’s meaning; moving normal data between stdout and stderr; renaming/removing/changing the type of a stable field; changing destructive defaults; or adding a network requirement to an offline command.

Use a major version, a clear compatibility note, or an explicit migration path. For deprecation: document it, retain it for at least one minor release when practical, emit a machine-readable warning, give an automation-safe replacement, then remove only in a major or explicitly documented break.

For mutating commands: make impact visible before mutation, offer `--dry-run` for automation when feasible, require or document confirmation, and state recovery/rollback. Never make an automation consumer scrape prose logs to detect a failure.

## Release Minimum

- Project manifest, command contract, release checklist, `--help`, version output, and error examples exist and agree.
- Test success, invalid usage, missing input, validation failure, stream separation, and automation examples.
- Record the distribution channel: GitHub/package ecosystem, Windows ZIP/portable/package manager, or internal.
- For publishable binary or archive artifacts, create an ARHS `.hashmanifest.toml` and record signing/provenance when public.
- ArchiveHasher and `manifest-signer.exe` are AAMHS preservation tools; they are not normal CLI release signing.

Release is blocked by inaccurate help, undocumented or mismatched exit behavior, progress in JSON stdout, unannounced stable-field changes, unreliable script failure detection, unsafe destructive behavior, unworkable automation examples, or missing distribution/hash evidence.

## Fast Checks and Escalation

Start with [Validation-Checklist.md](Validation-Checklist.md), [templates/CLI-Release-Checklist.md](templates/CLI-Release-Checklist.md), and the full [Adoption-Guide.md](Adoption-Guide.md). The lightweight validators check contract shape and JSON examples—not arbitrary CLI runtime behavior:

```powershell
python D:\.city_hall\CTS\tools\cts_validate.py <command-contract.md>
python D:\.city_hall\CTS\tools\cts_validate.py <output-example.json> --json
python D:\.city_hall\CTS\tools\cts_lint_contract.py <command-contract.md>
```

If a change affects a stable interface, destructive behavior, distribution, or release evidence, stop treating it as a small implementation edit: update the contract, compatibility/migration note, examples, manifest, checklist, and release evidence together.

## Source Map

- Full rules: [Command Tool Standard.md](Command%20Tool%20Standard.md)
- Output envelope: [CommandOutput.schema.json](CommandOutput.schema.json)
- Payload, progress, versioning: [JSON guidance](JSON-Data-Payload-Guidance.md), [progress compatibility](Progress-Output-Compatibility.md), [migration notes](Command-Versioning-Migration-Notes.md)
- Adoption and validation: [Adoption-Guide.md](Adoption-Guide.md), [Validation-Checklist.md](Validation-Checklist.md), [CI-Usage.md](CI-Usage.md)
