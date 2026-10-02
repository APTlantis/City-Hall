#!/usr/bin/env python3
"""Compare two TOML manifests and report changed fields."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def flatten(value: Any, prefix: str = "") -> dict[str, Any]:
    if isinstance(value, dict):
        output: dict[str, Any] = {}
        for key, child in value.items():
            child_prefix = f"{prefix}.{key}" if prefix else str(key)
            output.update(flatten(child, child_prefix))
        return output
    return {prefix: value}


def diff(old: dict[str, Any], new: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    old_flat = flatten(old)
    new_flat = flatten(new)
    old_keys = set(old_flat)
    new_keys = set(new_flat)
    return {
        "added": [{"field": key, "value": new_flat[key]} for key in sorted(new_keys - old_keys)],
        "removed": [{"field": key, "value": old_flat[key]} for key in sorted(old_keys - new_keys)],
        "changed": [
            {"field": key, "old": old_flat[key], "new": new_flat[key]}
            for key in sorted(old_keys & new_keys)
            if old_flat[key] != new_flat[key]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare two TOML manifests.")
    parser.add_argument("old_manifest")
    parser.add_argument("new_manifest")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    old_path = Path(args.old_manifest)
    new_path = Path(args.new_manifest)
    result = diff(load(old_path), load(new_path))
    has_changes = any(result[key] for key in result)

    if args.json:
        print(json.dumps({"status": "changed" if has_changes else "same", **result}, indent=2, sort_keys=True))
    else:
        print("changed" if has_changes else "same")
        for section in ("added", "removed", "changed"):
            if not result[section]:
                continue
            print(section + ":")
            for item in result[section]:
                print("  " + item["field"])

    return 1 if has_changes else 0


if __name__ == "__main__":
    sys.exit(main())
