# SESM Conformance Harness

## Purpose

This note shows the smallest repeatable conformance harness for SESM adopters.
It uses the reference validator and fixture corpus without requiring a separate test framework.

## Fixture Smoke Test

Run from the repository root:

```powershell
python SESM\Validate-SESM-Safe.py SESM\fixtures\valid\basic-safe.svg --safe-profile --json
python SESM\Validate-SESM-Safe.py SESM\fixtures\valid\full-metadata.svg --safe-profile --json
python SESM\Validate-SESM-Safe.py SESM\fixtures\warning\remote-reference.svg --safe-profile --json
python SESM\Validate-SESM-Safe.py SESM\fixtures\invalid\script.svg --safe-profile --json
```

Expected outcomes:

| Fixture | Expected status | Expected profile |
| --- | --- | --- |
| `fixtures/valid/basic-safe.svg` | `ok` | `sesm-safe` |
| `fixtures/valid/full-metadata.svg` | `ok` | `sesm-safe` |
| `fixtures/warning/remote-reference.svg` | `warning` | `sesm-unverified` |
| `fixtures/invalid/script.svg` | `error` | `sesm-unsafe` |

## Compatibility Fixture Check

```powershell
python SESM\Validate-SESM-Safe.py SESM\fixtures\compatibility\v0.2-basic.svg --safe-profile --json
python SESM\Validate-SESM-Safe.py SESM\fixtures\compatibility\v0.3-basic.svg --safe-profile --json
```

Both fixtures should parse and validate.
The `0.2.0` fixture exists to prove historical profile compatibility.
The `0.3.0` fixture exists to show the current public-review profile shape.

## Full Reference Tests

The existing unit and integration suite remains the reference implementation check:

```powershell
python SESM\tests\run_tests.py
```

Use the smoke harness when an adopter wants a lightweight sanity check.
Use the full test suite when changing SESM tools, schemas, or validator rules.
