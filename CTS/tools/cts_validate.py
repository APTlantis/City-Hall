#!/usr/bin/env python3
"""Validate CTS command contracts and JSON output envelope examples."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


TOOL = "cts-validate"
VERSION = "0.1.0"
REQUIRED_SECTIONS = [
    "Purpose",
    "Usage",
    "Inputs",
    "Outputs",
    "Human Output",
    "Machine Output",
    "Diagnostics",
    "Exit Codes",
    "Stability",
    "Examples",
    "Human Use",
    "Automation Use",
]
REQUIRED_EXIT_CODES = {"0", "1", "2", "3", "4", "5"}


@dataclass
class Finding:
    code: str
    message: str
    path: str


def headings(text: str) -> set[str]:
    found = set()
    for line in text.splitlines():
        match = re.match(r"^#{2,6}\s+(.+?)\s*$", line)
        if match:
            found.add(match.group(1).strip())
    return found


def exit_codes(text: str) -> set[str]:
    codes = set()
    in_exit_section = False
    for line in text.splitlines():
        heading = re.match(r"^#{2,6}\s+(.+?)\s*$", line)
        if heading:
            in_exit_section = heading.group(1).strip() == "Exit Codes"
            continue
        if in_exit_section:
            match = re.match(r"^\|\s*(\d+)\s*\|", line)
            if match:
                codes.add(match.group(1))
    return codes


def validate_contract(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    present = headings(text)
    for section in REQUIRED_SECTIONS:
        if section not in present:
            findings.append(Finding("missing-section", f"Missing section: {section}", str(path)))
    codes = exit_codes(text)
    if not codes:
        findings.append(Finding("missing-exit-code-table", "No exit-code rows found.", str(path)))
    else:
        missing = sorted(REQUIRED_EXIT_CODES - codes, key=int)
        if missing:
            findings.append(Finding("missing-standard-exit-code", "Missing standard exit code(s): " + ", ".join(missing), str(path)))
    if "--json" in text and "Machine Output" not in present:
        findings.append(Finding("json-undocumented", "Contract mentions --json but lacks Machine Output section.", str(path)))
    return findings


def validate_json_envelope(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        data: Any = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [Finding("json-parse-error", f"JSON does not parse: {exc}", str(path))]
    if not isinstance(data, dict):
        return [Finding("json-not-object", "CTS output envelope must be a JSON object.", str(path))]
    for field in ["status", "tool", "version"]:
        if field not in data:
            findings.append(Finding("missing-envelope-field", f"Missing required field: {field}", str(path)))
    if data.get("status") not in {"ok", "warning", "error"}:
        findings.append(Finding("invalid-status", "status must be ok, warning, or error.", str(path)))
    for field in ["warnings", "errors"]:
        if field in data and not isinstance(data[field], list):
            findings.append(Finding("invalid-array-field", f"{field} must be an array when present.", str(path)))
    for index, error in enumerate(data.get("errors", []) if isinstance(data.get("errors", []), list) else []):
        if not isinstance(error, dict) or "code" not in error or "message" not in error:
            findings.append(Finding("invalid-error-object", f"errors[{index}] must include code and message.", str(path)))
    return findings


def render_json(findings: list[Finding]) -> str:
    status = "ok" if not findings else "error"
    payload = {
        "status": status,
        "tool": TOOL,
        "version": VERSION,
        "data": {"findings_count": len(findings)},
        "errors": [asdict(finding) for finding in findings],
        "warnings": [],
    }
    return json.dumps(payload, indent=2)


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return "CTS validation passed."
    lines = ["CTS validation failed:"]
    for finding in findings:
        lines.append(f"- {finding.path}: {finding.code}: {finding.message}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Command contract Markdown or JSON envelope examples.")
    parser.add_argument("--json", action="store_true", help="Emit CTS JSON output envelope.")
    args = parser.parse_args()

    findings: list[Finding] = []
    for path in args.paths:
        if not path.exists():
            findings.append(Finding("input-missing", f"Input path is missing: {path}", str(path)))
            continue
        if path.suffix.lower() == ".json":
            findings.extend(validate_json_envelope(path))
        else:
            findings.extend(validate_contract(path))

    print(render_json(findings) if args.json else render_human(findings))
    return 0 if not findings else 4


if __name__ == "__main__":
    raise SystemExit(main())
