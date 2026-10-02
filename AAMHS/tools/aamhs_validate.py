#!/usr/bin/env python3
"""Validate an AAMHS hash manifest and verify recorded SHA-256 hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path


TOOL = "aamhs-validate"
VERSION = "0.1.0"


@dataclass
class Finding:
    code: str
    message: str
    path: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def validate(manifest_path: Path) -> list[Finding]:
    try:
        with manifest_path.open("rb") as handle:
            manifest = tomllib.load(handle)
    except Exception as exc:
        return [Finding("manifest-parse-error", f"Hash manifest could not be parsed: {exc}", str(manifest_path))]
    findings: list[Finding] = []
    for section in ["archive", "hash_suite", "files"]:
        if section not in manifest:
            findings.append(Finding("missing-section", f"Missing section: {section}", str(manifest_path)))
    files = manifest.get("files", [])
    if not isinstance(files, list) or not files:
        findings.append(Finding("missing-files", "Hash manifest must include at least one [[files]] entry.", str(manifest_path)))
        return findings
    base = manifest_path.parent
    for index, entry in enumerate(files):
        label = f"files[{index}]"
        rel = entry.get("path")
        expected_sha = str(entry.get("sha256", "")).upper()
        if not rel:
            findings.append(Finding("missing-path", "File entry is missing path.", label))
            continue
        file_path = (base / rel).resolve()
        if not file_path.exists():
            findings.append(Finding("file-missing", f"Listed file is missing: {rel}", label))
            continue
        size = entry.get("size_bytes")
        if size is not None and int(size) != file_path.stat().st_size:
            findings.append(Finding("size-mismatch", f"Size mismatch for {rel}: expected {size}, got {file_path.stat().st_size}", label))
        if not expected_sha:
            findings.append(Finding("missing-sha256", f"Missing sha256 for {rel}", label))
            continue
        actual_sha = sha256(file_path)
        if actual_sha != expected_sha:
            findings.append(Finding("sha256-mismatch", f"SHA-256 mismatch for {rel}: expected {expected_sha}, got {actual_sha}", label))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = validate(args.manifest)
    payload = {"status": "ok" if not findings else "error", "tool": TOOL, "version": VERSION, "data": {"findings_count": len(findings)}, "errors": [asdict(finding) for finding in findings], "warnings": []}
    if args.json:
        print(json.dumps(payload, indent=2))
    elif findings:
        print("AAMHS validation failed:")
        for finding in findings:
            print(f"- {finding.path}: {finding.message}")
    else:
        print("AAMHS validation passed.")
    return 0 if not findings else 4


if __name__ == "__main__":
    raise SystemExit(main())
