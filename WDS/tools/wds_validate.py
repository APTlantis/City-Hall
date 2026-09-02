#!/usr/bin/env python3
"""Validate a WDS site manifest for required governance, deployment, and quality fields."""

from __future__ import annotations

import argparse
import json
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path


TOOL = "wds-validate"
VERSION = "0.1.0"
REQUIRED_FIELDS = [
    ("site", "id"),
    ("site", "title"),
    ("site", "status"),
    ("governance", "standard"),
    ("governance", "workspace_standard"),
    ("deployment", "environment"),
    ("deployment", "rollback"),
    ("routes", "required"),
    ("metadata", "title"),
    ("metadata", "description"),
]
VALID_SITE_STATUS = {"draft", "preview", "published", "maintained", "archived"}
VALID_ENVIRONMENTS = {"local", "preview", "production", "archived", "internal"}


@dataclass
class Finding:
    code: str
    message: str
    path: str


def load_manifest(path: Path) -> tuple[dict, list[Finding]]:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle), []
    except Exception as exc:
        return {}, [Finding("manifest-parse-error", f"Manifest could not be parsed: {exc}", str(path))]


def value_at(data: dict, section: str, field: str):
    value = data.get(section, {}).get(field)
    if value == "":
        return None
    return value


def validate(path: Path) -> list[Finding]:
    if not path.exists():
        return [Finding("input-missing", f"Site manifest is missing: {path}", str(path))]
    data, findings = load_manifest(path)
    if findings:
        return findings
    for section, field in REQUIRED_FIELDS:
        if value_at(data, section, field) is None:
            findings.append(Finding("missing-field", f"Missing required field: {section}.{field}", f"{path}:{section}.{field}"))
    status = value_at(data, "site", "status")
    if status and status not in VALID_SITE_STATUS:
        findings.append(Finding("invalid-site-status", f"Unsupported site.status: {status}", f"{path}:site.status"))
    environment = value_at(data, "deployment", "environment")
    if environment and environment not in VALID_ENVIRONMENTS:
        findings.append(Finding("invalid-environment", f"Unsupported deployment.environment: {environment}", f"{path}:deployment.environment"))
    routes = value_at(data, "routes", "required")
    if routes is not None and (not isinstance(routes, list) or not routes):
        findings.append(Finding("invalid-routes", "routes.required must be a non-empty array.", f"{path}:routes.required"))
    if status in {"published", "maintained"} and environment != "production":
        findings.append(Finding("publication-environment", "published or maintained sites should use deployment.environment = production.", f"{path}:deployment.environment"))
    if status in {"published", "maintained"} and not value_at(data, "metadata", "canonical"):
        findings.append(Finding("missing-canonical", "published or maintained sites must record metadata.canonical.", f"{path}:metadata.canonical"))
    return findings


def render_json(findings: list[Finding]) -> str:
    return json.dumps(
        {
            "status": "ok" if not findings else "error",
            "tool": TOOL,
            "version": VERSION,
            "data": {"findings_count": len(findings)},
            "errors": [asdict(finding) for finding in findings],
            "warnings": [],
        },
        indent=2,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = validate(args.manifest)
    if args.json:
        print(render_json(findings))
    elif findings:
        print("WDS validation failed:")
        for finding in findings:
            print(f"- {finding.path}: {finding.message}")
    else:
        print("WDS validation passed.")
    return 0 if not findings else 4


if __name__ == "__main__":
    raise SystemExit(main())
