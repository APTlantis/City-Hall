#!/usr/bin/env python3
"""Validate SFDS-governed standard suite shape."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path


REQUIRED_SECTIONS = ("standard", "governance", "artifacts", "lifecycle")
REQUIRED_STANDARD_FIELDS = ("id", "title", "abbreviation", "status", "maturity", "version")
REQUIRED_GOVERNANCE_FIELDS = ("meta_standard", "scope")
REQUIRED_ARTIFACT_FIELDS = ("specification", "adoption_guide", "validation_checklist", "changelog")
REQUIRED_LIFECYCLE_FIELDS = ("created", "last_updated", "maintainer")

STATUS_VALUES = {
    "concept",
    "draft",
    "planned",
    "candidate-active",
    "active",
    "stable",
    "deprecated",
    "retired",
}
MATURITY_VALUES = {"concept", "draft", "candidate", "stable", "reference-candidate", "reference"}
PROMOTION_STATES = {
    "draft",
    "candidate-active-library-copy",
    "active-library-copy",
    "promoted",
    "deprecated",
}


def _as_list(value: object) -> list[object]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _load_manifest(path: Path) -> tuple[dict[str, object] | None, str | None]:
    try:
        return tomllib.loads(path.read_text(encoding="utf-8")), None
    except FileNotFoundError:
        return None, f"manifest missing: {path}"
    except tomllib.TOMLDecodeError as exc:
        return None, f"manifest TOML parse failed: {exc}"


def _relative_exists(base: Path, value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False
    return (base / value).exists()


def validate_suite(path: Path) -> dict[str, object]:
    suite = path.resolve()
    manifest_candidates = sorted(suite.glob("*.manifest.toml"))
    errors: list[str] = []
    warnings: list[str] = []

    if not suite.exists() or not suite.is_dir():
        return {"suite": str(path), "status": "fail", "errors": [f"suite directory missing: {path}"], "warnings": []}

    if not manifest_candidates:
        return {"suite": str(suite), "status": "fail", "errors": ["no suite manifest found"], "warnings": []}

    expected_manifest = suite / f"{suite.name}.manifest.toml"
    manifest_path = expected_manifest if expected_manifest.exists() else manifest_candidates[0]
    if manifest_path != expected_manifest:
        warnings.append(f"using manifest {manifest_path.name}; expected {expected_manifest.name}")

    manifest, manifest_error = _load_manifest(manifest_path)
    if manifest_error:
        return {"suite": str(suite), "status": "fail", "errors": [manifest_error], "warnings": warnings}
    assert manifest is not None

    for section in REQUIRED_SECTIONS:
        if section not in manifest or not isinstance(manifest[section], dict):
            errors.append(f"missing [{section}] section")

    standard = manifest.get("standard", {})
    governance = manifest.get("governance", {})
    artifacts = manifest.get("artifacts", {})
    lifecycle = manifest.get("lifecycle", {})
    promotion = manifest.get("promotion", {})

    if isinstance(standard, dict):
        for field in REQUIRED_STANDARD_FIELDS:
            if not standard.get(field):
                errors.append(f"missing [standard].{field}")
        status = standard.get("status")
        maturity = standard.get("maturity")
        if status and status not in STATUS_VALUES:
            warnings.append(f"[standard].status uses unregistered value: {status}")
        if maturity and maturity not in MATURITY_VALUES:
            warnings.append(f"[standard].maturity uses unregistered value: {maturity}")
        abbreviation = standard.get("abbreviation")
        if isinstance(abbreviation, str) and abbreviation.lower() != suite.name.lower():
            warnings.append(f"[standard].abbreviation does not match directory name: {abbreviation}")

    if isinstance(governance, dict):
        for field in REQUIRED_GOVERNANCE_FIELDS:
            if not governance.get(field):
                errors.append(f"missing [governance].{field}")
        if governance.get("meta_standard") != "SFDS":
            errors.append("[governance].meta_standard must be SFDS")

    if isinstance(artifacts, dict):
        for field in REQUIRED_ARTIFACT_FIELDS:
            if not artifacts.get(field):
                errors.append(f"missing [artifacts].{field}")
            elif not _relative_exists(suite, artifacts[field]):
                errors.append(f"[artifacts].{field} does not resolve: {artifacts[field]}")

        optional_paths = []
        optional_paths.extend(_as_list(artifacts.get("schema")))
        optional_paths.extend(_as_list(artifacts.get("templates")))
        optional_paths.extend(_as_list(artifacts.get("examples")))
        optional_paths.extend(_as_list(artifacts.get("validators")))
        optional_paths.extend(_as_list(artifacts.get("governance_notes")))
        optional_paths.extend(_as_list(artifacts.get("reference_examples")))
        for value in optional_paths:
            if isinstance(value, str) and value and not value.startswith("../") and not _relative_exists(suite, value):
                errors.append(f"declared artifact does not resolve: {value}")

    if isinstance(lifecycle, dict):
        for field in REQUIRED_LIFECYCLE_FIELDS:
            if not lifecycle.get(field):
                errors.append(f"missing [lifecycle].{field}")

    if isinstance(promotion, dict):
        state = promotion.get("promotion_state")
        if state and state not in PROMOTION_STATES:
            warnings.append(f"[promotion].promotion_state uses unregistered value: {state}")

    if not (suite / "README.md").exists():
        errors.append("README.md missing")
    if artifacts and isinstance(artifacts, dict):
        spec = artifacts.get("specification")
        if isinstance(spec, str) and spec:
            readme = suite / "README.md"
            if readme.exists() and spec not in readme.read_text(encoding="utf-8", errors="replace"):
                warnings.append(f"README.md does not mention declared specification: {spec}")

    status = "fail" if errors else "warn" if warnings else "ok"
    return {"suite": str(suite), "manifest": str(manifest_path), "status": status, "errors": errors, "warnings": warnings}


def discover_suites(root: Path) -> list[Path]:
    suites: list[Path] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        manifest_path = child / f"{child.name}.manifest.toml"
        manifest, _ = _load_manifest(manifest_path)
        if not manifest:
            continue
        standard = manifest.get("standard")
        governance = manifest.get("governance")
        if isinstance(standard, dict) and isinstance(governance, dict) and governance.get("meta_standard") == "SFDS":
            suites.append(child)
    return suites


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SFDS standard suite shape.")
    parser.add_argument("suites", nargs="*", help="Standard suite directories to validate.")
    parser.add_argument("--root", default=".", help="Root used when no suite directories are provided.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    targets = [Path(s) for s in args.suites] if args.suites else discover_suites(Path(args.root))
    results = [validate_suite(target) for target in targets]
    has_failures = any(result["status"] == "fail" for result in results)

    if args.json:
        print(json.dumps({"status": "fail" if has_failures else "ok", "results": results}, indent=2))
    else:
        for result in results:
            print(f"{result['status'].upper()} {result['suite']}")
            for error in result["errors"]:
                print(f"  error: {error}")
            for warning in result["warnings"]:
                print(f"  warning: {warning}")

    return 1 if has_failures else 0


if __name__ == "__main__":
    sys.exit(main())
