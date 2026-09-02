#!/usr/bin/env python3
"""Promote fixed-name workspace manifests to entity-named canonical records.

The migration is deliberately conservative:
- conflicting entity-named and other legacy manifests are moved to a dated
  City Hall archive before promotion;
- one canonical manifest remains in each governed directory;
- project lifecycle/version fields are reconciled from explicit local evidence;
- AGENTS.md and Project-README.md references are updated mechanically.

Run without --apply for a dry run.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import tomllib
from dataclasses import dataclass
from pathlib import Path

import tomli_w


PORTFOLIOS = ("WDS", "BASIC", "CTS", "DATA", "DRS")
PRUNE = {
    ".git", ".idea", ".vscode", "node_modules", "target", "bin", "obj",
    "dist", "build", ".next", "__pycache__", "vendor",
}
FIXED_NAMES = ("directory.manifest.toml", "project.manifest.toml")


@dataclass(frozen=True)
class ProjectTruth:
    version: str
    status: str
    stage: str
    stability: str
    active: bool
    evidence: str


TRUTH: dict[str, ProjectTruth] = {
    "WDS/aptlantis-one": ProjectTruth("0.1.0", "active", "active", "experimental", True, "package.json"),
    "WDS/aptlantis-two": ProjectTruth("not-versioned", "active", "active", "experimental", True, "registered child projects"),
    "WDS/aptlantis-two/aptlantis": ProjectTruth("0.1.0", "active", "active", "experimental", True, "package.json"),
    "WDS/aptlantis-two/webserver": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "source layout"),
    "WDS/linux-genealogy": ProjectTruth("0.1.0", "active", "active", "mostly-stable", True, "legacy manifest and generated site/data"),
    "WDS/portfolio-website": ProjectTruth("0.1.0", "active", "active", "experimental", True, "package.json and README.md"),
    "BASIC/QB-7Zip": ProjectTruth("not-versioned", "experimental", "concept", "experimental", False, "legacy manifest and source archive"),
    "BASIC/QB-Veracrypt": ProjectTruth("not-versioned", "experimental", "concept", "experimental", False, "legacy manifest and source archive"),
    "BASIC/QB-Winget": ProjectTruth("1.0.0", "active", "active", "mostly-stable", True, "README.md, executable, and legacy manifest"),
    "CTS/AnalyzeProjects": ProjectTruth("0.1.0", "active", "active", "experimental", True, "README.md and implementation"),
    "CTS/AptlantisLogos": ProjectTruth("1.0", "paused", "production", "stable", False, "README.md, generators, and legacy manifest"),
    "CTS/CloneCratesio": ProjectTruth("1.0.0", "paused", "production", "stable", False, "README.md, Go module, and legacy manifest"),
    "CTS/ConversionTools": ProjectTruth("1.0.0", "active", "active", "mostly-stable", True, "README.md and legacy manifest"),
    "CTS/DatasetPipelines": ProjectTruth("0.1.0", "active", "active", "mostly-stable", True, "registered pipeline children and legacy manifest"),
    "CTS/DatasetPipelines/TinyLlama-HolyC": ProjectTruth("0.1.0", "active", "active", "experimental", True, "Cargo.toml"),
    "CTS/DatasetPipelines/Winget": ProjectTruth("not-versioned", "active", "active", "experimental", True, "Go module and pipeline files"),
    "CTS/FH-RefToolkit": ProjectTruth("1.0.0", "paused", "production", "stable", False, "pyproject.toml, README.md, and FlathubRefs legacy manifest"),
    "CTS/LangThemeGenerator": ProjectTruth("0.1.0", "active", "active", "mostly-stable", True, "README.md and legacy manifest"),
    "CTS/Llama": ProjectTruth("0.1.0", "active", "active", "experimental", True, "child pipelines and legacy manifest"),
    "CTS/Llama/create-dataset": ProjectTruth("0.1.0", "active", "active", "experimental", True, "Cargo.toml"),
    "CTS/Llama/layer-one": ProjectTruth("not-versioned", "active", "active", "experimental", True, "Python generators and JSONL outputs"),
    "CTS/UTILITIES": ProjectTruth("not-versioned", "active", "active", "experimental", True, "seven registered child utilities"),
    "CTS/UTILITIES/appstream_to_jsonl": ProjectTruth("not-versioned", "paused", "prototype", "experimental", False, "README.md and legacy manifest"),
    "CTS/UTILITIES/dir_mapper": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "package.json and README.md"),
    "CTS/UTILITIES/extract_winget_manifests": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "local implementation"),
    "CTS/UTILITIES/JSON-JSONL": ProjectTruth("not-versioned", "active", "active", "experimental", True, "Go module"),
    "CTS/UTILITIES/platform_views": ProjectTruth("0.1.0", "active", "active", "experimental", True, "Cargo.toml and README.md"),
    "CTS/UTILITIES/search_and_copy": ProjectTruth("not-versioned", "active", "active", "experimental", True, "Go module"),
    "CTS/UTILITIES/svg_metadata": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "local implementation"),
    "DATA/crates.io": ProjectTruth("snapshot-series", "reference", "reference", "stable", False, "January-April 2026 snapshot directories"),
    "DATA/node.js": ProjectTruth("snapshot-series", "reference", "reference", "stable", False, "generated output tree"),
    "DATA/winget": ProjectTruth("snapshot-series", "active", "active", "mostly-stable", True, "catalog snapshots and WingetExport child"),
    "DATA/winget/WingetExport": ProjectTruth("1.0.0", "active", "active", "mostly-stable", True, "package.json and README.md"),
    "DRS/AptlantisConsole": ProjectTruth("1.0.8", "active", "active", "stable", True, "package.json, README.md, and legacy manifest"),
    "DRS/Chat": ProjectTruth("0.1.0", "blocked", "blocked", "mostly-stable", True, "package.json, README.md, tests, and documented installer gate"),
    "DRS/ChromeArchivalPlugin": ProjectTruth("1.0.0", "active", "active", "mostly-stable", True, "README.md and legacy manifest"),
    "DRS/ClipboardFilter": ProjectTruth("2.0.0", "active", "active", "mostly-stable", True, "README.md and legacy manifest"),
    "DRS/CommandWizard": ProjectTruth("1.0.0", "paused", "production", "stable", False, "README.md, tests, packaged release evidence, and legacy manifest"),
    "DRS/DataVisualizers": ProjectTruth("0.1.0", "experimental", "prototype", "experimental", False, "package.json and starter README"),
    "DRS/Partitioning": ProjectTruth("not-versioned", "active", "active", "experimental", True, "README.md, engine, tests, and installer layout"),
    "DRS/Structra": ProjectTruth("1.0.0", "active", "active", "mostly-stable", True, "package.json, README.md, and workflow tests"),
    "DRS/Tauri-IT": ProjectTruth("0.1.0", "active", "active", "stable", True, "nested it-tools workspace and legacy manifest"),
    "DRS/WinTrim": ProjectTruth("0.1.0", "active", "concept", "experimental", True, "README-Rules.md and legacy manifest"),
    "DRS/WSL": ProjectTruth("not-versioned", "active", "active", "experimental", True, "ten registered distro workspaces"),
    "DRS/WSL/antix": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "workspace contents"),
    "DRS/WSL/brunson": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "workspace contents"),
    "DRS/WSL/cbpp": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "workspace contents"),
    "DRS/WSL/clear-43540-live-server": ProjectTruth("43540", "active", "active", "experimental", True, "Clear Linux source image workspace"),
    "DRS/WSL/clearlinux": ProjectTruth("not-versioned", "active", "active", "experimental", True, "PROCESS.md and build material"),
    "DRS/WSL/crunchbang": ProjectTruth("not-versioned", "active", "active", "experimental", True, "build and packaging material"),
    "DRS/WSL/feren": ProjectTruth("not-versioned", "active", "active", "experimental", True, "README.md and image inspection material"),
    "DRS/WSL/nitrux": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "workspace contents"),
    "DRS/WSL/peppermint": ProjectTruth("not-versioned", "experimental", "prototype", "experimental", False, "workspace contents"),
    "DRS/WSL/solus": ProjectTruth("not-versioned", "active", "active", "experimental", True, "rootfs and packaging material"),
}


def load(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def dump(path: Path, data: dict) -> None:
    path.write_bytes(tomli_w.dumps(data, multiline_strings=True).encode("utf-8"))


def relative_key(workspace: Path, directory: Path) -> str:
    return directory.relative_to(workspace).as_posix()


def governed_directories(workspace: Path) -> list[tuple[Path, Path]]:
    found: list[tuple[Path, Path]] = []
    for portfolio in PORTFOLIOS:
        root = workspace / portfolio
        for current, dirs, files in os.walk(root):
            dirs[:] = [name for name in dirs if name not in PRUNE]
            fixed = next((name for name in FIXED_NAMES if name in files), None)
            if fixed:
                found.append((Path(current), Path(current) / fixed))
    return sorted(found, key=lambda item: (len(item[0].parts), str(item[0]).lower()))


def archive_path(archive_root: Path, workspace: Path, source: Path) -> Path:
    return archive_root / source.relative_to(workspace)


def replace_doc_references(directory: Path, old_name: str, new_name: str, apply: bool) -> None:
    for doc_name in ("AGENTS.md", "Project-README.md"):
        path = directory / doc_name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        updated = text.replace(old_name, new_name)
        if updated != text:
            print(f"UPDATE {path}: {old_name} -> {new_name}")
            if apply:
                path.write_text(updated, encoding="utf-8", newline="\n")


def reconcile_manifest(
    workspace: Path,
    directory: Path,
    manifest: dict,
    canonical_name: str,
    archived: list[Path],
) -> dict:
    manifest.setdefault("manifest", {})["canonical_name"] = canonical_name
    manifest["manifest"]["last_updated"] = "2026-07-08"
    key = relative_key(workspace, directory)
    entity = manifest.setdefault("entity", {})
    entity["id"] = re.sub(r"[^a-z0-9]+", "-", directory.name.lower()).strip("-")
    if canonical_name != f"{directory.name}.manifest.toml":
        raise ValueError(f"unexpected canonical filename for {directory}")

    structure = manifest.setdefault("structure", {})
    required = structure.get("required_files", [])
    structure["required_files"] = [
        canonical_name if item in FIXED_NAMES or item == "DIRECTORY.manifest.toml" else item
        for item in required
    ]
    structure["required_child_project_files"] = [
        "AGENTS.md", "[EntityName].manifest.toml", "Project-README.md"
    ] if "required_child_project_files" in structure else structure.get("required_child_project_files", [])

    agent = manifest.setdefault("agent", {})
    for field in ("read_first", "authoritative_docs"):
        values = agent.get(field, [])
        agent[field] = [
            canonical_name if item in FIXED_NAMES or item == "DIRECTORY.manifest.toml" else item
            for item in values
        ]

    migration = manifest.setdefault("migration", {})
    migration["archived_manifests"] = [str(path) for path in archived]
    migration.pop("legacy_manifests", None)

    if "project" in manifest:
        truth = TRUTH.get(key)
        if not truth:
            raise ValueError(f"missing ProjectTruth entry for {key}")
        entity["status"] = truth.status
        manifest["project"]["stage"] = truth.stage
        manifest["project"]["version"] = truth.version
        lifecycle = manifest.setdefault("lifecycle", {})
        lifecycle["state"] = truth.status
        lifecycle["last_reviewed"] = "2026-07-08"
        state = manifest.setdefault("state", {})
        state["stability"] = truth.stability
        state["active_development"] = truth.active
        state["known_gaps"] = [
            "Current build, test, artifact, and release posture were not executed during the governance migration."
        ]
        manifest["verification"] = {
            "level": "metadata-reconciled",
            "evidence": truth.evidence,
            "reviewed": "2026-07-08",
            "build_verified": False,
            "tests_verified": False,
            "artifact_verified": False,
            "release_verified": False,
        }
    else:
        manifest.setdefault("lifecycle", {})["last_reviewed"] = "2026-07-08"

    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path("D:/"))
    parser.add_argument(
        "--archive-root",
        type=Path,
        default=Path("D:/.city_hall/WGS/migration-notes/Legacy-Live-Manifests-20260708"),
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    workspace = args.workspace_root.resolve()
    archive_root = args.archive_root.resolve()
    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"Mode: {mode}")

    operations = 0
    for directory, fixed in governed_directories(workspace):
        canonical_name = f"{directory.name}.manifest.toml"
        canonical = directory / canonical_name
        to_archive = [
            path for path in directory.glob("*.manifest.toml")
            if path.name not in {fixed.name, canonical_name}
        ]
        if canonical.exists() and canonical != fixed:
            to_archive.append(canonical)
        to_archive = sorted(set(to_archive), key=lambda path: path.name.lower())
        archived_records: list[Path] = []

        for source in to_archive:
            destination = archive_path(archive_root, workspace, source)
            print(f"ARCHIVE {source} -> {destination}")
            archived_records.append(destination)
            operations += 1
            if args.apply:
                destination.parent.mkdir(parents=True, exist_ok=True)
                if destination.exists():
                    raise FileExistsError(destination)
                shutil.move(str(source), str(destination))

        print(f"PROMOTE {fixed} -> {canonical}")
        operations += 1
        if args.apply:
            if canonical.exists() and canonical != fixed:
                raise FileExistsError(canonical)
            shutil.move(str(fixed), str(canonical))
            manifest = reconcile_manifest(
                workspace,
                directory,
                load(canonical),
                canonical_name,
                archived_records,
            )
            dump(canonical, manifest)
        replace_doc_references(directory, fixed.name, canonical_name, args.apply)

    print(f"Operations: {operations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
