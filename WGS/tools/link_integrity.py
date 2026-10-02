#!/usr/bin/env python3
"""Check local Markdown links in governed documentation folders."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "#")


def normalize_target(raw: str) -> str:
    target = raw.strip()
    if not target:
        return target
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith("<"):
        target = target.split()[0]
    return unquote(target)


def check_file(path: Path) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in LINK_PATTERN.finditer(line):
            target = normalize_target(match.group(1))
            if not target or target.startswith(IGNORED_PREFIXES):
                continue
            target_path, _, _anchor = target.partition("#")
            if not target_path:
                continue
            candidate = Path(target_path)
            if not candidate.is_absolute():
                candidate = path.parent / candidate
            if not candidate.exists():
                findings.append(
                    {
                        "file": str(path),
                        "line": line_number,
                        "target": target,
                        "message": "local Markdown link target does not resolve",
                    }
                )
    return findings


def check_roots(roots: list[Path], include_templates: bool = False) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for root in roots:
        paths = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for path in paths:
            if any(part in {".git", "__pycache__", "node_modules"} for part in path.parts):
                continue
            if not include_templates and any(part.lower() == "templates" for part in path.parts):
                continue
            findings.extend(check_file(path))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local Markdown links.")
    parser.add_argument("paths", nargs="+", help="Markdown files or directories to inspect.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--include-templates", action="store_true", help="Also inspect template directories.")
    args = parser.parse_args()

    findings = check_roots([Path(path) for path in args.paths], include_templates=args.include_templates)
    status = "fail" if findings else "ok"
    if args.json:
        print(json.dumps({"status": status, "findings": findings}, indent=2))
    else:
        print(status)
        for finding in findings:
            print(f"{finding['file']}:{finding['line']} {finding['target']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
