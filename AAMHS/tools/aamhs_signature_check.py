#!/usr/bin/env python3
"""Check that detached signature files declared by an AAMHS manifest are present."""

from __future__ import annotations

import argparse
import json
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path


TOOL = "aamhs-signature-check"
VERSION = "0.1.0"


@dataclass
class Finding:
    code: str
    message: str
    path: str


def check(manifest_path: Path) -> list[Finding]:
    try:
        with manifest_path.open("rb") as handle:
            manifest = tomllib.load(handle)
    except Exception as exc:
        return [Finding("manifest-parse-error", f"Hash manifest could not be parsed: {exc}", str(manifest_path))]
    signatures = manifest.get("signatures", {})
    if not signatures.get("detached_signatures_used", False):
        return []
    base = manifest_path.parent
    findings: list[Finding] = []
    for index, entry in enumerate(signatures.get("files", [])):
        rel = entry.get("path", "")
        if not rel:
            findings.append(Finding("missing-signature-path", "Signature entry is missing path.", f"signatures.files[{index}]"))
            continue
        if not (base / rel).exists():
            findings.append(Finding("signature-missing", f"Detached signature file is missing: {rel}", f"signatures.files[{index}]"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = check(args.manifest)
    payload = {"status": "ok" if not findings else "error", "tool": TOOL, "version": VERSION, "data": {"findings_count": len(findings)}, "errors": [asdict(finding) for finding in findings], "warnings": []}
    if args.json:
        print(json.dumps(payload, indent=2))
    elif findings:
        print("AAMHS signature check failed:")
        for finding in findings:
            print(f"- {finding.path}: {finding.message}")
    else:
        print("AAMHS signature check passed.")
    return 0 if not findings else 4


if __name__ == "__main__":
    raise SystemExit(main())
