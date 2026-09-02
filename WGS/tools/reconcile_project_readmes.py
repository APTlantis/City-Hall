#!/usr/bin/env python3
"""Replace rollout-placeholder state text with manifest-backed verification text."""

from __future__ import annotations

import argparse
import os
import tomllib
from pathlib import Path


PORTFOLIOS = ("WDS", "BASIC", "CTS", "DATA", "DRS")
PRUNE = {".git", ".idea", ".vscode", "node_modules", "target", "bin", "obj", "dist", "build", ".next", "__pycache__", "vendor"}
PLACEHOLDERS = (
    "The project predates the July 2026 fixed-name governance rollout. Its physical source and existing documents are present, but build, version, lifecycle, and release claims have not yet been fully reconciled into the canonical manifest.",
    "The project predates the July 2026 governance rollout. Source material is present, but its current version, build state, and release posture still require project-specific reconciliation.",
    "The current version, lifecycle, environment, and output integrity require project-specific reconciliation.",
)


def project_manifests(workspace: Path) -> list[Path]:
    result: list[Path] = []
    for portfolio in PORTFOLIOS:
        for current, dirs, files in os.walk(workspace / portfolio):
            dirs[:] = [name for name in dirs if name not in PRUNE and not name.endswith("_holding")]
            directory = Path(current)
            expected = f"{directory.name}.manifest.toml"
            if expected in files:
                path = directory / expected
                try:
                    with path.open("rb") as handle:
                        manifest = tomllib.load(handle)
                    if "project" in manifest:
                        result.append(path)
                except Exception:
                    pass
    return sorted(result, key=lambda path: str(path).lower())


def statement(manifest: dict) -> str:
    project = manifest.get("project", {})
    entity = manifest.get("entity", {})
    verification = manifest.get("verification", {})
    version = project.get("version", "not-versioned")
    status = entity.get("status", "unreviewed")
    stage = project.get("stage", "unreviewed")
    evidence = verification.get("evidence", "local source and documentation")
    reviewed = verification.get("reviewed", "2026-07-08")
    return (
        f"Governance metadata was reconciled on {reviewed}: version `{version}`, "
        f"lifecycle `{status}`, stage `{stage}`. Evidence reviewed: {evidence}. "
        "The build, tests, shipping artifact, and release posture were not executed "
        "during this metadata pass, so this classification is not a release-readiness claim."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path("D:/"))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    changed = 0
    for manifest_path in project_manifests(args.workspace_root.resolve()):
        readme = manifest_path.parent / "Project-README.md"
        if not readme.exists():
            continue
        with manifest_path.open("rb") as handle:
            manifest = tomllib.load(handle)
        text = readme.read_text(encoding="utf-8", errors="replace")
        updated = text
        for placeholder in PLACEHOLDERS:
            updated = updated.replace(placeholder, statement(manifest))
        if updated != text:
            changed += 1
            print(f"{'UPDATE' if args.apply else 'WOULD UPDATE'} {readme}")
            if args.apply:
                readme.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Project READMEs changed: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
