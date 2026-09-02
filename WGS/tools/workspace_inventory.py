#!/usr/bin/env python3
"""Report workspace registration and filesystem drift without rewriting files."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import tomllib
from pathlib import Path


IGNORED = {".git", ".idea", ".vscode", "__pycache__", "node_modules"}
SCHEMA_VERSION = "wgs.audit.v1"


def load(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def inspect_root(path: Path, manifest_path: Path) -> dict:
    result = {"path": str(path), "manifest": str(manifest_path), "status": "pass", "findings": []}
    if not path.is_dir():
        result["status"] = "fail"; result["findings"].append("root missing"); return result
    if not manifest_path.is_file():
        result["status"] = "fail"; result["findings"].append("manifest missing"); return result
    try:
        manifest = load(manifest_path)
    except Exception as exc:
        result["status"] = "fail"; result["findings"].append(f"manifest parse failed: {exc}"); return result
    registered = set(manifest.get("structure", {}).get("children", []))
    physical = {item.name for item in path.iterdir() if item.is_dir() and item.name not in IGNORED}
    missing = sorted(registered - physical, key=str.lower)
    extra = sorted(physical - registered, key=str.lower)
    if missing:
        result["findings"].append("registered but missing: " + ", ".join(missing))
    if extra:
        result["findings"].append("physical but unregistered: " + ", ".join(extra))
    authorities = []
    for candidate in path.glob("*.manifest.toml"):
        try:
            data = load(candidate)
            if data.get("manifest", {}).get("manifest_type") in {"directory", "project"}:
                authorities.append(candidate.name)
        except Exception:
            pass
    if len(authorities) != 1:
        result["findings"].append("local entity authorities: " + (", ".join(authorities) or "none"))
    if result["findings"]:
        result["status"] = "drift"
    result["registered_children"] = len(registered)
    result["physical_children"] = len(physical)
    return result


def markdown(results: list[dict]) -> str:
    lines = ["# Workspace Inventory Report", "", "| Root | Status | Registered | Physical | Findings |", "| --- | --- | ---: | ---: | --- |"]
    for item in results:
        lines.append(
            f"| `{item['path']}` | {item['status']} | {item.get('registered_children', 0)} | "
            f"{item.get('physical_children', 0)} | {'; '.join(item['findings']) or 'None'} |"
        )
    lines.append("")
    return "\n".join(lines)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def coverage_status(item: dict) -> str:
    findings = item.get("findings", [])
    if "manifest missing" in findings:
        return "missing"
    authorities = [
        finding for finding in findings
        if finding.startswith("local entity authorities:")
    ]
    if authorities and not authorities[0].endswith(Path(item["manifest"]).name):
        return "duplicate"
    return "present"


def jsonl_records(results: list[dict], workspace_root: Path) -> list[dict]:
    generated_at = now_iso()
    run_id = generated_at.replace(":", "").replace("-", "").replace("Z", "Z")
    records: list[dict] = []
    for item in results:
        root_path = Path(item["path"])
        manifest_path = Path(item["manifest"])
        status = coverage_status(item)
        records.append(
            {
                "schema_version": SCHEMA_VERSION,
                "run_id": run_id,
                "record_type": "workspace_entity",
                "workspace_root": str(workspace_root),
                "path": str(root_path),
                "generated_at": generated_at,
                "entity_name": root_path.name,
                "entity_type": "directory",
                "lifecycle": "unknown",
                "governing_standards": ["WGS"],
                "manifest_path": str(manifest_path) if manifest_path.is_file() else "",
                "readme_path": str(root_path / "README.md") if (root_path / "README.md").is_file() else "",
                "inventory_status": item["status"],
                "registered_children": item.get("registered_children", 0),
                "physical_children": item.get("physical_children", 0),
            }
        )
        records.append(
            {
                "schema_version": SCHEMA_VERSION,
                "run_id": run_id,
                "record_type": "manifest_coverage",
                "workspace_root": str(workspace_root),
                "path": str(root_path),
                "generated_at": generated_at,
                "expected_manifest_path": str(manifest_path),
                "actual_manifest_path": str(manifest_path) if manifest_path.is_file() else "",
                "coverage_status": status,
                "naming_status": "canonical" if status == "present" else "unknown",
                "parent_registered": True,
                "findings": item.get("findings", []),
            }
        )
    return records


def render_jsonl(records: list[dict]) -> str:
    return "\n".join(json.dumps(record, sort_keys=True) for record in records)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path("D:/"))
    parser.add_argument("--format", choices=["markdown", "json", "jsonl"], default="markdown")
    args = parser.parse_args()
    workspace = args.workspace_root.resolve()
    development = load(workspace / "Development.manifest.toml")
    results = [
        inspect_root(Path(root["path"]), Path(root["manifest"]))
        for root in development.get("roots", [])
        if root.get("kind") != "standards-registry"
    ]
    if args.format == "json":
        print(json.dumps(results, indent=2))
    elif args.format == "jsonl":
        print(render_jsonl(jsonl_records(results, workspace)))
    else:
        print(markdown(results))
    return 1 if any(item["status"] != "pass" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
