#!/usr/bin/env python3
"""Companion DRS integrity checks for BLAKE3 and signing metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


def load(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def blake3_hash(path: Path) -> str | None:
    tool = shutil.which("b3sum") or shutil.which("blake3")
    if not tool:
        return None
    result = subprocess.run([tool, str(path)], check=False, capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return result.stdout.split()[0].upper()


def validate(manifest_path: Path, root: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    manifest = load(manifest_path)
    release = manifest.get("release", {})
    installer = release.get("installer", {})
    artifact_rel = installer.get("path", "")
    artifact = root / artifact_rel if artifact_rel else None

    signing = str(installer.get("signing", "")).strip()
    if not signing:
        errors.append("release.installer.signing is required")
    elif signing.lower() == "unsigned":
        warnings.append("installer is explicitly unsigned")

    expected_sha256 = str(installer.get("sha256", "")).upper()
    if expected_sha256 and artifact and artifact.exists():
        actual_sha256 = hashlib.sha256(artifact.read_bytes()).hexdigest().upper()
        if actual_sha256 != expected_sha256:
            errors.append("release.installer.sha256 does not match artifact")
    elif expected_sha256 and artifact:
        warnings.append(f"artifact not found for hash verification: {artifact_rel}")

    expected_blake3 = str(installer.get("blake3", "")).upper()
    if expected_blake3:
        if artifact and artifact.exists():
            actual_blake3 = blake3_hash(artifact)
            if actual_blake3 is None:
                warnings.append("BLAKE3 value is declared but no b3sum/blake3 executable is available")
            elif actual_blake3 != expected_blake3:
                errors.append("release.installer.blake3 does not match artifact")
        else:
            warnings.append(f"BLAKE3 declared but artifact not found: {artifact_rel}")

    return {
        "status": "error" if errors else "warning" if warnings else "ok",
        "manifest": str(manifest_path),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check DRS release integrity metadata.")
    parser.add_argument("manifest")
    parser.add_argument("--root", default=".", help="Project root used to resolve artifact paths.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = validate(Path(args.manifest), Path(args.root))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["status"])
        for error in result["errors"]:
            print(f"error: {error}")
        for warning in result["warnings"]:
            print(f"warning: {warning}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
