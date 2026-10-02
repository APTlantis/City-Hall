#!/usr/bin/env python3
"""Scaffold and register an entity-named governed child.

Dry-run is the default. --apply creates the child and updates the parent's
entity manifest. Existing targets are never overwritten.
"""

from __future__ import annotations

import argparse
import re
import tomllib
from datetime import date
from pathlib import Path

try:
    import tomli_w
except ModuleNotFoundError:
    import toml_write


CLASSIFICATION = {
    "project": "projects",
    "project-group": "project_groups",
    "dataset": "datasets",
    "reference": "external_sources",
    "container": "containers",
    "archive": "archives",
}
PROJECT_KINDS = {"project", "project-group", "dataset"}
STANDARD_PATHS = {
    name: f"D:\\.city_hall\\{name}\\README.md"
    for name in ["WGS", "PPS", "LDS", "CTS", "DRS", "WDS", "ARHS", "AAMHS", "SESM"]
}
READMAP_TEMPLATE = Path(__file__).resolve().parents[1] / "templates" / "PROJECT-READMAP.toml"


def load(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def write_toml(path: Path, value: dict) -> None:
    if "tomli_w" in globals():
        rendered = tomli_w.dumps(value, multiline_strings=True)
    else:
        rendered = toml_write.dumps(value)
    path.write_bytes(rendered.encode("utf-8"))


def entity_manifest(directory: Path) -> Path:
    return directory / f"{directory.name}.manifest.toml"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def render_readmap(target: Path) -> str:
    text = READMAP_TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "{{PROJECT_NAME}}": target.name,
        "{{PROJECT_MANIFEST}}": entity_manifest(target).name,
        "{{GENERATED_BY}}": "WGS tools/governance_scaffold.py",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def project_manifest(target: Path, parent: Path, kind: str, standard: str, description: str) -> dict:
    today = date.today().isoformat()
    return {
        "manifest": {
            "schema": "APTlantis Entity Manifest", "schema_version": "2.4",
            "manifest_type": "project", "canonical_name": entity_manifest(target).name,
            "last_updated": today, "maintainer": "Herb",
        },
        "entity": {
            "id": slug(target.name), "title": target.name, "kind": "dataset" if kind == "dataset" else "project",
            "class": kind, "status": "experimental", "description": description, "tags": [],
        },
        "project": {
            "type": kind, "portfolio_class": kind, "stage": "concept", "version": "not-versioned",
        },
        "governance": {
            "primary_standard": standard, "primary_standard_path": STANDARD_PATHS[standard],
            "additional_standards": ["WGS", "PPS"],
            "additional_standard_paths": [STANDARD_PATHS["WGS"], STANDARD_PATHS["PPS"]],
            "inherits_from": f"..\\{entity_manifest(parent).name}",
        },
        "lifecycle": {"state": "experimental", "created": today, "last_reviewed": today, "maintainer": "Herb"},
        "paths": {"root": str(target)},
        "documentation": {"project_readme": "Project-README.md", "project_readmap": "PROJECT-READMAP.toml", "readme": "README.md"},
        "relationships": {"parent": str(parent), "child_projects": []},
        "state": {
            "stability": "experimental", "active_development": False,
            "known_gaps": ["Implementation, build, test, artifact, and release evidence have not been established."],
        },
        "migration": {"archived_manifests": []},
        "agent": {
            "read_first": ["AGENTS.md", entity_manifest(target).name, "PROJECT-READMAP.toml", "Project-README.md"],
            "authoritative_docs": [entity_manifest(target).name, "PROJECT-READMAP.toml", "Project-README.md", "AGENTS.md"],
            "safe_to_modify": True, "notes": "Concept scaffold; verify evidence before changing lifecycle claims.",
        },
        "structure": {"required_files": ["AGENTS.md", entity_manifest(target).name, "PROJECT-READMAP.toml", "Project-README.md"]},
        "verification": {
            "level": "scaffold-only", "evidence": "operator-supplied scaffold metadata", "reviewed": today,
            "build_verified": False, "tests_verified": False, "artifact_verified": False, "release_verified": False,
        },
    }


def directory_manifest(target: Path, parent: Path, kind: str, standard: str, description: str) -> dict:
    today = date.today().isoformat()
    status = "archived" if kind == "archive" else "planned"
    return {
        "manifest": {
            "schema": "APTlantis Entity Manifest", "schema_version": "2.4",
            "manifest_type": "directory", "canonical_name": entity_manifest(target).name,
            "last_updated": today, "maintainer": "Herb",
        },
        "entity": {
            "id": slug(target.name), "title": target.name, "kind": "directory", "class": kind,
            "status": status, "description": description, "tags": [],
        },
        "directory": {
            "path": str(target), "role": description, "portfolio_class": "container",
            "health": "unreviewed", "allows_project_groups": kind == "container",
        },
        "governance": {
            "primary_standard": standard, "primary_standard_path": STANDARD_PATHS[standard],
            "additional_standards": ["WGS"], "additional_standard_paths": [STANDARD_PATHS["WGS"]],
            "inherits_from": f"..\\{entity_manifest(parent).name}", "requires_child_manifests": True,
            "allowed_child_types": ["project", "project-group", "container"],
        },
        "lifecycle": {"state": status, "created": today, "last_reviewed": today, "maintainer": "Herb"},
        "structure": {"required_files": ["AGENTS.md", entity_manifest(target).name], "children": [], "reserved_directories": []},
        "classification": {"projects": [], "project_groups": [], "containers": [], "archives": []},
        "relationships": {"parent": str(parent)},
        "policy": {
            "allow_project_creation": kind == "container", "allow_agent_scaffolding": kind == "container",
            "requires_manual_review_for_moves": True, "exclude_from_active_reporting": kind == "archive",
        },
        "migration": {"archived_manifests": [], "known_gaps": ["Child topology and operating policy require review."]},
        "agent": {
            "read_first": ["AGENTS.md", entity_manifest(target).name],
            "authoritative_docs": [entity_manifest(target).name, "AGENTS.md"],
            "safe_to_modify": kind != "archive", "notes": "New governed directory scaffold.",
        },
    }


def update_parent(parent_manifest: dict, name: str, kind: str) -> None:
    structure = parent_manifest.setdefault("structure", {})
    children = structure.setdefault("children", [])
    if name in children:
        raise ValueError(f"parent already registers child: {name}")
    children.append(name)
    children.sort(key=str.lower)
    classification = parent_manifest.setdefault("classification", {})
    bucket = classification.setdefault(CLASSIFICATION[kind], [])
    bucket.append(name)
    bucket.sort(key=str.lower)
    parent_manifest.setdefault("manifest", {})["last_updated"] = date.today().isoformat()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--kind", choices=sorted(CLASSIFICATION), required=True)
    parser.add_argument("--standard", choices=sorted(STANDARD_PATHS), default="WGS")
    parser.add_argument("--description", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    parent = args.parent.resolve()
    parent_manifest_path = entity_manifest(parent)
    if not parent_manifest_path.is_file():
        raise SystemExit(f"Parent entity manifest is missing: {parent_manifest_path}")
    if any(part in {".", ".."} for part in Path(args.name).parts) or Path(args.name).name != args.name:
        raise SystemExit("--name must be one directory name")
    target = parent / args.name
    if target.exists():
        raise SystemExit(f"Target already exists: {target}")

    parent_manifest = load(parent_manifest_path)
    update_parent(parent_manifest, args.name, args.kind)
    manifest = (
        project_manifest(target, parent, args.kind, args.standard, args.description)
        if args.kind in PROJECT_KINDS
        else directory_manifest(target, parent, args.kind, args.standard, args.description)
    )
    files = ["AGENTS.md", entity_manifest(target).name]
    if args.kind in PROJECT_KINDS:
        files.extend(["PROJECT-READMAP.toml", "Project-README.md"])
    print(f"{'CREATE' if args.apply else 'WOULD CREATE'} {target}")
    print("Files: " + ", ".join(files))
    print(f"{'UPDATE' if args.apply else 'WOULD UPDATE'} {parent_manifest_path}")
    if not args.apply:
        return 0

    target.mkdir(parents=False)
    write_toml(entity_manifest(target), manifest)
    standard_link = STANDARD_PATHS[args.standard].replace("\\", "/")
    (target / "AGENTS.md").write_text(
        f"# {args.name} Instructions\n\nInherit `{parent / 'AGENTS.md'}` and `D:\\AGENTS.md`.\n\n"
        f"Read `{entity_manifest(target).name}` first. Canonical standard: [{args.standard}]({standard_link}).\n",
        encoding="utf-8", newline="\n",
    )
    if args.kind in PROJECT_KINDS:
        (target / "PROJECT-READMAP.toml").write_text(render_readmap(target), encoding="utf-8", newline="\n")
        (target / "Project-README.md").write_text(
            f"# {args.name}\n\n## Purpose\n\n{args.description}\n\n## Governance\n\n"
            f"- [{entity_manifest(target).name}]({entity_manifest(target).name})\n"
            "- [PROJECT-READMAP.toml](PROJECT-READMAP.toml)\n"
            f"- [AGENTS.md](AGENTS.md)\n\n## Current state\n\n"
            "Concept scaffold only. Build, tests, artifacts, and release posture are unverified.\n",
            encoding="utf-8", newline="\n",
        )
    write_toml(parent_manifest_path, parent_manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
