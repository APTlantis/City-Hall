# CTS Command Versioning And Migration Notes

## Purpose

This note records the recommended migration policy for CTS-governed command contracts.

## Compatibility Defaults

- Patch releases may fix help text, examples, or diagnostics without changing command behavior.
- Minor releases may add optional flags, additive JSON fields, new warning codes, or new examples.
- Major releases are required for breaking changes to stable command names, flags, exit-code meanings, stdout/stderr behavior, or stable JSON field names and types.

## Migration Notes

When a breaking change is unavoidable, record:

- old command, flag, field, or exit-code behavior;
- new behavior;
- replacement command or migration path;
- first version where the replacement is available;
- planned removal version;
- examples before and after the change.

## Deprecation Pattern

1. Mark the command or field as deprecated in the command contract.
2. Keep the old behavior working for at least one minor release when practical.
3. Emit a machine-readable warning in JSON mode.
4. Provide an automation-safe replacement example.
5. Remove only in a major release or explicitly documented compatibility break.
