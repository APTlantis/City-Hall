#!/usr/bin/env python3
"""Lint CTS command contracts for stability risks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Finding:
    code: str
    message: str
    path: str


RISK_PATTERNS = {
    "unstable-output": re.compile(r"\b(output may change|subject to change|experimental json)\b", re.I),
    "ambiguous-exit-code": re.compile(r"\b(non[- ]?zero|various exit codes|implementation-defined exit)\b", re.I),
    "stdout-progress-risk": re.compile(r"\b(progress bar|spinner|interactive prompt)\b", re.I),
}


def lint(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    findings: list[Finding] = []
    for code, pattern in RISK_PATTERNS.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append(Finding(code, f"Potential CTS stability risk near line {line}.", f"{path}:{line}"))
    if "--json" in text and "stderr" not in text.lower():
        findings.append(Finding("json-progress-channel", "Contract mentions --json but does not state where progress output goes.", str(path)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings: list[Finding] = []
    for path in args.paths:
        findings.extend(lint(path))
    payload = {
        "status": "ok" if not findings else "warning",
        "tool": "cts-lint-contract",
        "version": "0.1.0",
        "data": {"findings_count": len(findings)},
        "warnings": [asdict(finding) for finding in findings],
        "errors": [],
    }
    print(json.dumps(payload, indent=2) if args.json else ("CTS contract lint passed." if not findings else "\n".join(f"{f.path}: {f.message}" for f in findings)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
