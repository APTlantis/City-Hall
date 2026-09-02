"""Small TOML writer for WGS tooling.

This is intentionally narrow: it supports the scalar, list, table, and
array-of-table shapes emitted by the WGS scaffold/snapshot tools.
"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime


def _key(value: str) -> str:
    return value if value.replace("_", "").replace("-", "").isalnum() else repr(value)


def _string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _value(value) -> str:
    if isinstance(value, str):
        return _string(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (date, datetime)):
        return _string(value.isoformat())
    if isinstance(value, list):
        return "[" + ", ".join(_value(item) for item in value) + "]"
    if value is None:
        return '""'
    raise TypeError(f"Unsupported TOML value: {type(value).__name__}")


def _emit_table(lines: list[str], table: Mapping, prefix: list[str]) -> None:
    scalars = []
    nested = []
    arrays = []
    for key, value in table.items():
        if isinstance(value, Mapping):
            nested.append((key, value))
        elif isinstance(value, list) and value and all(isinstance(item, Mapping) for item in value):
            arrays.append((key, value))
        else:
            scalars.append((key, value))

    if prefix:
        lines.append(f"[{'.'.join(_key(part) for part in prefix)}]")
    for key, value in scalars:
        lines.append(f"{_key(key)} = {_value(value)}")
    if scalars and (nested or arrays):
        lines.append("")

    for index, (key, value) in enumerate(nested):
        _emit_table(lines, value, [*prefix, key])
        if index != len(nested) - 1 or arrays:
            lines.append("")

    for key, values in arrays:
        for item in values:
            lines.append(f"[[{'.'.join(_key(part) for part in [*prefix, key])}]]")
            _emit_table(lines, item, [])
            lines.append("")


def dumps(data: Mapping) -> str:
    lines: list[str] = []
    _emit_table(lines, data, [])
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines) + "\n"
