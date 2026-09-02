#!/usr/bin/env python3
"""Normalize canonical entity-manifest filenames, paths, and inheritance.

This tool only rewrites manifests whose filename exactly matches the containing
directory name plus `.manifest.toml`. Run without --apply for a dry run.
"""

from __future__ import annotations

import argparse
import os
import re
import tomllib
from pathlib import Path

import tomli_w


PRUNE = {
    ".git", ".idea", ".vscode", "node_modules", "target", "bin", "obj",
    "dist", "build", ".next", "__pycache__", "vendor", "$RECYCLE.BIN",
    "System Volume Information", "migration-notes",
}
PORTFOLIOS = {"WDS", "BASIC", "CTS", "DATA", "DRS"}


def load(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def dump(path: Path, value: dict) -> None:
    path.write_bytes(tomli_w.dumps(value, multiline_strings=True).encode("utf-8"))


def normalize_string(value: str) -> str:
    if re.match(r"^[A-Za-z]:\\", value):
        while "\\\\" in value:
            value = value.replace("\\\\", "\\")
    return value


def normalize_values(value: object) -> object:
    if isinstance(value, dict):
        return {key: normalize_values(child) for key, child in value.items()}
    if isinstance(value, list):
        return [normalize_values(child) for child in value]
    if isinstance(value, str):
        return normalize_string(value)
    return value


def entity_manifests(workspace: Path) -> list[Path]:
    manifests: list[Path] = []
    for root_name in PORTFOLIOS:
        root = workspace / root_name
        for current, dirs, files in os.walk(root):
            dirs[:] = [
                name for name in dirs
                if name not in PRUNE and not name.endswith("_holding")
            ]
            directory = Path(current)
            expected = f"{directory.name}.manifest.toml"
            if expected in files:
                manifests.append(directory / expected)
    return sorted(manifests, key=lambda path: str(path).lower())


def expected_parent_reference(workspace: Path, directory: Path) -> str:
    if directory.parent == workspace:
        return "D:\\Development.manifest.toml"
    return f"..\\{directory.parent.name}.manifest.toml"


def normalize_manifest(workspace: Path, path: Path) -> tuple[dict, list[str]]:
    original = load(path)
    manifest = normalize_values(original)
    changes: list[str] = []
    canonical = path.name
    if manifest.setdefault("manifest", {}).get("canonical_name") != canonical:
        manifest["manifest"]["canonical_name"] = canonical
        changes.append("canonical_name")
    manifest["manifest"]["last_updated"] = "2026-07-08"

    directory = path.parent
    domain = manifest.get("directory") or manifest.get("paths")
    path_key = "path" if "directory" in manifest else "root"
    expected_path = str(directory)
    if domain is not None and domain.get(path_key) != expected_path:
        domain[path_key] = expected_path
        changes.append(path_key)

    governance = manifest.setdefault("governance", {})
    expected_inheritance = expected_parent_reference(workspace, directory)
    if governance.get("inherits_from") != expected_inheritance:
        governance["inherits_from"] = expected_inheritance
        changes.append("inherits_from")

    structure = manifest.setdefault("structure", {})
    required = structure.get("required_files", [])
    normalized_required = [
        canonical if item in {"directory.manifest.toml", "project.manifest.toml", "DIRECTORY.manifest.toml"} else item
        for item in required
    ]
    if normalized_required != required:
        structure["required_files"] = normalized_required
        changes.append("required_files")
    if "required_child_project_files" in structure:
        desired = ["AGENTS.md", "[EntityName].manifest.toml", "Project-README.md"]
        if structure["required_child_project_files"] != desired:
            structure["required_child_project_files"] = desired
            changes.append("required_child_project_files")

    agent = manifest.setdefault("agent", {})
    for field in ("read_first", "authoritative_docs"):
        values = agent.get(field, [])
        updated = [
            canonical if item in {"directory.manifest.toml", "project.manifest.toml", "DIRECTORY.manifest.toml"} else item
            for item in values
        ]
        if updated != values:
            agent[field] = updated
            changes.append(f"agent.{field}")

    if manifest != original and not changes:
        changes.append("path-separator normalization")
    return manifest, changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path("D:/"))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    workspace = args.workspace_root.resolve()
    changed = 0
    for path in entity_manifests(workspace):
        manifest, changes = normalize_manifest(workspace, path)
        if changes:
            changed += 1
            print(f"{'UPDATE' if args.apply else 'WOULD UPDATE'} {path}: {', '.join(changes)}")
            if args.apply:
                dump(path, manifest)
    print(f"Manifests changed: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
