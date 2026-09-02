#!/usr/bin/env python3
"""Validate LDS Library Interface Note markdown for required sections."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


TOOL = "lds-validate"
VERSION = "0.1.0"
REQUIRED_SECTIONS = [
    "Public API Surface",
    "Stability Level",
    "Versioning / Breaking-Change Policy",
    "Extension Contracts",
    "Known Consumers",
    "Companion Crates",
    "Known Gaps",
]
STABILITY_LEVELS = {"experimental", "interface-stable", "versioned", "reference"}


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


def validate(path: Path) -> list[Finding]:
    if not path.exists():
        return [Finding("input-missing", f"Interface note is missing: {path}", str(path))]
    text = path.read_text(encoding="utf-8", errors="replace")
    present = headings(text)
    findings: list[Finding] = []
    for section in REQUIRED_SECTIONS:
        if section not in present:
            findings.append(Finding("missing-section", f"Missing section: {section}", str(path)))
    if not any(f"`{level}`" in text or level in text for level in STABILITY_LEVELS):
        findings.append(Finding("missing-stability-level", "No recognized LDS stability level found.", str(path)))
    if "{{" in text or "}}" in text:
        findings.append(Finding("unfilled-placeholder", "Template placeholders remain in interface note.", str(path)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notes", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings: list[Finding] = []
    for note in args.notes:
        findings.extend(validate(note))
    payload = {"status": "ok" if not findings else "error", "tool": TOOL, "version": VERSION, "data": {"findings_count": len(findings)}, "errors": [asdict(finding) for finding in findings], "warnings": []}
    if args.json:
        print(json.dumps(payload, indent=2))
    elif findings:
        print("LDS validation failed:")
        for finding in findings:
            print(f"- {finding.path}: {finding.message}")
    else:
        print("LDS validation passed.")
    return 0 if not findings else 4


if __name__ == "__main__":
    raise SystemExit(main())
