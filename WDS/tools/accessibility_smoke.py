#!/usr/bin/env python3
"""Run a lightweight WDS accessibility and metadata smoke check for one HTML page."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.request import Request, urlopen


TOOL = "wds-accessibility-smoke"
VERSION = "0.1.0"


@dataclass
class Finding:
    code: str
    message: str


def read_source(source: str, timeout: float) -> str:
    path = Path(source)
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    request = Request(source, headers={"User-Agent": f"{TOOL}/{VERSION}"})
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def check_html(html: str) -> list[Finding]:
    findings: list[Finding] = []
    if not re.search(r"<html\b[^>]*\blang=", html, re.IGNORECASE):
        findings.append(Finding("missing-html-lang", "The html element should include a lang attribute."))
    if not re.search(r"<title>[^<]+</title>", html, re.IGNORECASE):
        findings.append(Finding("missing-title", "A non-empty title element is required."))
    if not re.search(r"<meta\b[^>]*name=[\"']description[\"'][^>]*content=[\"'][^\"']+[\"']", html, re.IGNORECASE):
        findings.append(Finding("missing-description", "A meta description is required for public pages."))
    for match in re.finditer(r"<img\b([^>]*)>", html, re.IGNORECASE):
        attrs = match.group(1)
        if not re.search(r"\balt=", attrs, re.IGNORECASE):
            findings.append(Finding("missing-img-alt", "Image is missing alt text."))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="HTML file path or URL.")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = check_html(read_source(args.source, args.timeout))
    if args.json:
        print(json.dumps({"status": "ok" if not findings else "error", "tool": TOOL, "version": VERSION, "data": {"findings_count": len(findings)}, "errors": [asdict(finding) for finding in findings], "warnings": []}, indent=2))
    elif findings:
        print("WDS accessibility smoke check failed:")
        for finding in findings:
            print(f"- {finding.code}: {finding.message}")
    else:
        print("WDS accessibility smoke check passed.")
    return 0 if not findings else 4


if __name__ == "__main__":
    raise SystemExit(main())
