#!/usr/bin/env python3
"""Validate PPS proposal manifest fields and emit structured diagnostics."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path


TOOL = "pps-validate"
VERSION = "0.1.1"
STATUS_VALUES = {"sketch", "draft", "ready", "approved", "deferred", "rejected", "archived"}
READINESS_VALUES = {"sketch", "ready-for-review", "approved-for-build", "blocked", "deferred"}
PERSONA_VALUES = {"solo-maintainer", "operator", "agent", "reviewer", "adopter", "maintainer"}
RESPONSIBILITY_POSTURE_VALUES = {"personal", "shared", "adoptable"}
REQUIRED_FIELDS = [
    ("proposal", "id"),
    ("proposal", "status"),
    ("proposal", "created"),
    ("proposal", "responsibility_posture"),
    ("project", "name"),
    ("project", "type"),
    ("project", "mission"),
    ("criteria", "success"),
    ("criteria", "failure"),
    ("constraints", "technical"),
    ("constraints", "scope"),
]


@dataclass
class Finding:
    code: str
    message: str
    path: str


def load(path: Path) -> tuple[dict, list[Finding]]:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle), []
    except Exception as exc:
        return {}, [Finding("manifest-parse-error", f"Proposal manifest could not parse: {exc}", str(path))]


def validate(path: Path) -> list[Finding]:
    if not path.exists():
        return [Finding("input-missing", f"Input path is missing: {path}", str(path))]
    data, findings = load(path)
    if findings:
        return findings
    for section, field in REQUIRED_FIELDS:
        value = data.get(section, {}).get(field)
        if value is None or value == "":
            findings.append(Finding("missing-field", f"Missing required field: {section}.{field}", f"{path}:{section}.{field}"))
    status = data.get("proposal", {}).get("status")
    if status and status not in STATUS_VALUES:
        findings.append(Finding("unknown-status", f"proposal.status is not registered: {status}", f"{path}:proposal.status"))
    readiness = data.get("proposal", {}).get("readiness")
    if readiness and readiness not in READINESS_VALUES:
        findings.append(Finding("unknown-readiness", f"proposal.readiness is not registered: {readiness}", f"{path}:proposal.readiness"))
    responsibility_posture = data.get("proposal", {}).get("responsibility_posture")
    if responsibility_posture and responsibility_posture not in RESPONSIBILITY_POSTURE_VALUES:
        findings.append(Finding("unknown-responsibility-posture", f"proposal.responsibility_posture is not registered: {responsibility_posture}", f"{path}:proposal.responsibility_posture"))
    personas = data.get("proposal", {}).get("operational_personas", [])
    if personas and isinstance(personas, list):
        unknown = sorted(str(item) for item in personas if item not in PERSONA_VALUES)
        if unknown:
            findings.append(Finding("unknown-operational-persona", "Unknown operational persona(s): " + ", ".join(unknown), f"{path}:proposal.operational_personas"))
    return findings


def to_json(findings: list[Finding]) -> str:
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
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings: list[Finding] = []
    for path in args.paths:
        findings.extend(validate(path))
    print(to_json(findings) if args.json else ("PPS validation passed." if not findings else "\n".join(f"{f.path}: {f.message}" for f in findings)))
    return 0 if not findings else 4


if __name__ == "__main__":
    sys.exit(main())
