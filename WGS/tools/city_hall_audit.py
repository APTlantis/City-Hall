#!/usr/bin/env python3
"""Audit City Hall standard directories for SFDS/WGS documentation shape."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path


IGNORED_DIRS = {".git", ".idea", ".vscode", "__pycache__"}
WORKSPACE_PORTFOLIOS = ["WDS", "BASIC", "CTS", "DATA", "DRS"]
REQUIRED_TOP_LEVEL = [
    "README.md",
    "Adoption-Guide.md",
    "Validation-Checklist.md",
    "CHANGELOG.md",
]
SCHEMA_VERSION = "wgs.audit.v1"


@dataclass
class Finding:
    standard: str
    level: str
    message: str


def load_manifest(path: Path) -> tuple[dict, str | None]:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle), None
    except Exception as exc:  # pragma: no cover - diagnostic path
        return {}, f"manifest parse failed: {exc}"


def version_in_changelog(changelog: Path, version: str) -> bool:
    if not changelog.exists() or not version:
        return False
    text = changelog.read_text(encoding="utf-8", errors="replace")
    return f"## {version}" in text or f"## [{version}]" in text


def audit_standard(directory: Path) -> list[Finding]:
    findings: list[Finding] = []
    name = directory.name
    manifest_path = directory / f"{name}.manifest.toml"

    if not manifest_path.exists():
        findings.append(Finding(name, "FAIL", f"missing entity-named manifest {manifest_path.name}"))
        return findings

    manifest, manifest_error = load_manifest(manifest_path)
    if manifest_error:
        findings.append(Finding(name, "FAIL", manifest_error))
        return findings

    for rel_path in REQUIRED_TOP_LEVEL:
        if not (directory / rel_path).exists():
            findings.append(Finding(name, "FAIL", f"missing {rel_path}"))

    artifacts = manifest.get("artifacts", {})
    spec_rel = artifacts.get("specification", "")
    if not spec_rel:
        findings.append(Finding(name, "FAIL", "manifest does not declare artifacts.specification"))
    elif not (directory / spec_rel).exists():
        findings.append(Finding(name, "FAIL", f"declared specification is missing: {spec_rel}"))

    examples_rel = artifacts.get("examples", "examples")
    if examples_rel:
        examples_dir = directory / examples_rel
        if not examples_dir.exists():
            findings.append(Finding(name, "WARN", f"examples directory is missing: {examples_rel}"))
        elif not any(item.is_file() for item in examples_dir.rglob("*")):
            findings.append(Finding(name, "WARN", f"examples directory has no files: {examples_rel}"))

    templates_rel = artifacts.get("templates", "")
    if templates_rel:
        templates_dir = directory / templates_rel
        if not templates_dir.exists():
            findings.append(Finding(name, "WARN", f"templates directory is declared but missing: {templates_rel}"))

    schema_rel = artifacts.get("schema", "")
    if schema_rel:
        schema_path = directory / schema_rel
        if not schema_path.exists():
            findings.append(Finding(name, "FAIL", f"declared schema is missing: {schema_rel}"))
        elif schema_path.suffix == ".json":
            try:
                json.loads(schema_path.read_text(encoding="utf-8"))
            except Exception as exc:
                findings.append(Finding(name, "FAIL", f"declared JSON schema does not parse: {schema_rel}: {exc}"))

    for rel_path in artifacts.get("validators", []):
        if rel_path and not (directory / rel_path).exists():
            findings.append(Finding(name, "WARN", f"declared validator is missing: {rel_path}"))

    for key in ["adoption_guide", "validation_checklist", "changelog"]:
        rel_path = artifacts.get(key, "")
        if rel_path and not (directory / rel_path).exists():
            findings.append(Finding(name, "FAIL", f"declared {key} is missing: {rel_path}"))

    for rel_path in artifacts.get("reference_examples", []):
        if rel_path and not (directory / rel_path).exists():
            findings.append(Finding(name, "WARN", f"declared reference example is missing: {rel_path}"))

    for rel_path in artifacts.get("governance_notes", []):
        if rel_path and not (directory / rel_path).exists():
            findings.append(Finding(name, "WARN", f"declared governance note is missing: {rel_path}"))

    adopter_artifacts = manifest.get("adopter_artifacts", {})
    for key in ["schemas", "manifest_templates", "document_templates"]:
        for rel_path in adopter_artifacts.get(key, []):
            if rel_path and not (directory / rel_path).exists():
                findings.append(Finding(name, "WARN", f"declared adopter {key[:-1]} is missing: {rel_path}"))

    version = str(manifest.get("standard", {}).get("version", ""))
    changelog = directory / str(artifacts.get("changelog", "CHANGELOG.md"))
    if version and not version_in_changelog(changelog, version):
        findings.append(Finding(name, "FAIL", f"manifest version {version} is not recorded in changelog"))

    return findings


def standard_directories(root: Path) -> list[Path]:
    directories = []
    for item in root.iterdir():
        manifest_path = item / f"{item.name}.manifest.toml"
        if not item.is_dir() or item.name in IGNORED_DIRS or not manifest_path.exists():
            continue
        manifest, error = load_manifest(manifest_path)
        if not error and "standard" in manifest:
            directories.append(item)
    return sorted(directories, key=lambda path: path.name.lower())


def render_markdown(root: Path, findings_by_standard: dict[str, list[Finding]]) -> str:
    lines = [
        "# City Hall Standards Audit",
        "",
        f"- Root: `{root}`",
        f"- Audit scopes inspected: {len(findings_by_standard)}",
        "",
        "| Scope | Status | Findings |",
        "| --- | --- | --- |",
    ]
    for standard, findings in findings_by_standard.items():
        if not findings:
            lines.append(f"| {standard} | pass | None |")
            continue
        status = "fail" if any(f.level == "FAIL" for f in findings) else "warn"
        message = "<br>".join(f"{f.level}: {f.message}" for f in findings)
        lines.append(f"| {standard} | {status} | {message} |")
    lines.append("")
    return "\n".join(lines)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def jsonl_level(level: str) -> str:
    return {
        "FAIL": "error",
        "WARN": "warning",
        "INFO": "info",
    }.get(level.upper(), "info")


def finding_id(finding: Finding) -> str:
    digest = hashlib.sha256(f"{finding.standard}|{finding.level}|{finding.message}".encode("utf-8")).hexdigest()
    return digest[:16]


def rule_id(message: str) -> str:
    token = "".join(char.lower() if char.isalnum() else "-" for char in message.split(":", 1)[0])
    return "wgs." + "-".join(part for part in token.split("-") if part)


def standard_suite_record(root: Path, directory: Path, findings: list[Finding], run_id: str, generated_at: str) -> dict:
    manifest_path = directory / f"{directory.name}.manifest.toml"
    manifest, error = load_manifest(manifest_path) if manifest_path.exists() else ({}, "manifest missing")
    artifacts = manifest.get("artifacts", {}) if not error else {}
    required = REQUIRED_TOP_LEVEL[:]
    specification = artifacts.get("specification", "")
    if specification:
        required.append(str(specification))
    present = [rel_path for rel_path in required if (directory / rel_path).exists()]
    missing = [rel_path for rel_path in required if not (directory / rel_path).exists()]
    examples_rel = artifacts.get("examples", "examples")
    examples_present: list[str] = []
    if examples_rel and (directory / examples_rel).exists():
        examples_present = [
            str(path.relative_to(directory))
            for path in sorted((directory / examples_rel).rglob("*"))
            if path.is_file()
        ]
    return {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "record_type": "standard_suite_coverage",
        "workspace_root": str(root),
        "path": str(directory),
        "generated_at": generated_at,
        "standard": directory.name,
        "status": str(manifest.get("standard", {}).get("status", "unknown")),
        "maturity": str(manifest.get("standard", {}).get("maturity", "unknown")),
        "required_artifacts_present": present,
        "required_artifacts_missing": missing,
        "validators_registered": artifacts.get("validators", []) if isinstance(artifacts.get("validators", []), list) else [],
        "examples_present": examples_present,
        "finding_count": len(findings),
    }


def jsonl_records(root: Path, findings_by_standard: dict[str, list[Finding]]) -> list[dict]:
    generated_at = now_iso()
    run_id = generated_at.replace(":", "").replace("-", "").replace("Z", "Z")
    records: list[dict] = []
    standard_names = {path.name for path in standard_directories(root)}
    for standard, findings in findings_by_standard.items():
        if standard in standard_names:
            records.append(standard_suite_record(root, root / standard, findings, run_id, generated_at))
        for finding in findings:
            records.append(
                {
                    "schema_version": SCHEMA_VERSION,
                    "run_id": run_id,
                    "record_type": "audit_finding",
                    "workspace_root": str(root),
                    "path": str(root / standard) if standard in standard_names else standard,
                    "generated_at": generated_at,
                    "finding_id": finding_id(finding),
                    "rule_id": rule_id(finding.message),
                    "severity": jsonl_level(finding.level),
                    "message": finding.message,
                    "evidence": {"scope": finding.standard, "level": finding.level},
                    "recommended_action": finding.message,
                }
            )
    return records


def render_jsonl(records: list[dict]) -> str:
    return "\n".join(json.dumps(record, sort_keys=True) for record in records)


def windows_path(value: str) -> Path:
    """Resolve a manifest's absolute Windows path without changing its meaning."""
    return Path(value)


def placeholder_values(value: object, location: str = "") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            findings.extend(placeholder_values(child, f"{location}.{key}" if location else str(key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(placeholder_values(child, f"{location}[{index}]"))
    elif isinstance(value, str):
        lowered = value.lower()
        tokens = ["yyyy-mm-dd", "example-project", "example-directory", "000-example", "replace with"]
        if any(token in lowered for token in tokens):
            findings.append(f"placeholder value at {location}: {value}")
    return findings


def audit_governance_links(scope: str, manifest: dict) -> list[Finding]:
    findings: list[Finding] = []
    governance = manifest.get("governance", {})
    declared = [governance.get("primary_standard_path", "")]
    declared.extend(governance.get("additional_standard_paths", []))
    release_path = governance.get("release_standard_path", "")
    if release_path:
        declared.append(release_path)
    for value in declared:
        if not value:
            findings.append(Finding(scope, "FAIL", "empty canonical standard path"))
        elif not windows_path(str(value)).exists():
            findings.append(Finding(scope, "FAIL", f"canonical standard link does not resolve: {value}"))
    return findings


def entity_manifest_path(directory: Path) -> Path:
    return directory / f"{directory.name}.manifest.toml"


def canonical_entity_manifests(directory: Path) -> list[Path]:
    records: list[Path] = []
    for path in directory.glob("*.manifest.toml"):
        manifest, error = load_manifest(path)
        if error:
            continue
        if manifest.get("manifest", {}).get("manifest_type") in {"directory", "project"}:
            records.append(path)
    return records


def audit_local_authority(directory: Path, scope: str) -> list[Finding]:
    findings: list[Finding] = []
    expected = entity_manifest_path(directory)
    if not expected.is_file():
        findings.append(Finding(scope, "FAIL", f"missing entity-named manifest {expected.name}"))
    fixed = [directory / "directory.manifest.toml", directory / "project.manifest.toml"]
    for path in fixed:
        if path.exists() and path != expected:
            findings.append(Finding(scope, "FAIL", f"superseded fixed-name manifest remains: {path.name}"))
    authorities = canonical_entity_manifests(directory)
    if len(authorities) > 1:
        findings.append(Finding(scope, "FAIL", "multiple local entity authorities: " + ", ".join(path.name for path in authorities)))
    return findings


def same_path(left: str, right: Path) -> bool:
    try:
        return windows_path(str(left)).resolve() == right.resolve()
    except Exception:
        return False


def audit_manifest_common(directory: Path, manifest: dict, expected_parent: Path) -> list[Finding]:
    scope = str(directory)
    findings = audit_local_authority(directory, scope)
    expected_name = entity_manifest_path(directory).name
    if manifest.get("manifest", {}).get("canonical_name") != expected_name:
        findings.append(Finding(scope, "FAIL", f"canonical_name is not {expected_name}"))
    domain = manifest.get("directory") or manifest.get("paths", {})
    recorded = domain.get("path") if "directory" in manifest else domain.get("root")
    if not recorded or not same_path(str(recorded), directory):
        findings.append(Finding(scope, "FAIL", f"manifest path does not match physical path: {recorded}"))
    parent = manifest.get("relationships", {}).get("parent", "")
    if not parent or not same_path(str(parent), expected_parent):
        findings.append(Finding(scope, "FAIL", f"manifest parent does not match: {parent}"))
    findings.extend(audit_governance_links(scope, manifest))
    for message in placeholder_values(manifest):
        findings.append(Finding(scope, "FAIL", message))
    return findings


def audit_project(project_dir: Path, expected_parent: Path) -> list[Finding]:
    scope = str(project_dir)
    findings: list[Finding] = []
    manifest_path = entity_manifest_path(project_dir)
    for filename in ["AGENTS.md", manifest_path.name, "Project-README.md"]:
        if not (project_dir / filename).is_file():
            findings.append(Finding(scope, "FAIL", f"missing {filename}"))
    if not manifest_path.exists():
        return findings + audit_local_authority(project_dir, scope)
    manifest, error = load_manifest(manifest_path)
    if error:
        return findings + [Finding(scope, "FAIL", error)]
    findings.extend(audit_manifest_common(project_dir, manifest, expected_parent))

    project = manifest.get("project", {})
    entity = manifest.get("entity", {})
    if project.get("version") in {None, "", "unverified", "0.0.0"}:
        findings.append(Finding(scope, "FAIL", f"unreconciled project version: {project.get('version')}"))
    if project.get("stage") == "existing-unverified" or entity.get("status") == "unverified":
        findings.append(Finding(scope, "FAIL", "unreconciled lifecycle classification"))
    verification = manifest.get("verification", {})
    if not verification:
        findings.append(Finding(scope, "FAIL", "missing verification boundary"))
    if entity.get("status") == "release-ready" and not all(
        verification.get(field) for field in ["build_verified", "tests_verified", "artifact_verified", "release_verified"]
    ):
        findings.append(Finding(scope, "FAIL", "release-ready status is not supported by complete verification"))

    for child_name in manifest.get("relationships", {}).get("child_projects", []):
        child = project_dir / str(child_name)
        if not child.is_dir():
            findings.append(Finding(scope, "FAIL", f"registered child project is missing: {child_name}"))
        else:
            findings.extend(audit_project(child, project_dir))
    for child_name in manifest.get("relationships", {}).get("child_containers", []):
        child = project_dir / str(child_name)
        findings.extend(audit_directory_entity(child, project_dir, compare_children=False))
    return findings


def audit_directory_entity(directory: Path, expected_parent: Path, compare_children: bool = True) -> list[Finding]:
    scope = str(directory)
    findings: list[Finding] = []
    manifest_path = entity_manifest_path(directory)
    for filename in ["AGENTS.md", manifest_path.name]:
        if not (directory / filename).is_file():
            findings.append(Finding(scope, "FAIL", f"missing {filename}"))
    if not manifest_path.exists():
        return findings + audit_local_authority(directory, scope)
    manifest, error = load_manifest(manifest_path)
    if error:
        return findings + [Finding(scope, "FAIL", error)]
    findings.extend(audit_manifest_common(directory, manifest, expected_parent))

    if compare_children:
        registered = set(manifest.get("structure", {}).get("children", []))
        physical = {item.name for item in directory.iterdir() if item.is_dir() and item.name not in IGNORED_DIRS}
        for child in sorted(registered - physical, key=str.lower):
            findings.append(Finding(scope, "FAIL", f"registered child is missing: {child}"))
        for child in sorted(physical - registered, key=str.lower):
            findings.append(Finding(scope, "FAIL", f"physical child is not registered: {child}"))
    return findings


def audit_holding(directory: Path, expected_parent: Path) -> list[Finding]:
    findings = audit_directory_entity(directory, expected_parent, compare_children=True)
    manifest_path = entity_manifest_path(directory)
    if manifest_path.exists():
        manifest, error = load_manifest(manifest_path)
        if not error and not manifest.get("policy", {}).get("exclude_from_active_reporting", False):
            findings.append(Finding(str(directory), "FAIL", "holding is not excluded from active reporting"))
    return findings


def audit_portfolio(
    workspace_root: Path,
    portfolio_name: str,
    directory: Path | None = None,
) -> list[Finding]:
    directory = directory or workspace_root / portfolio_name
    findings: list[Finding] = []
    if not directory.is_dir():
        return [Finding(portfolio_name, "FAIL", f"portfolio directory is missing: {directory}")]
    manifest_path = entity_manifest_path(directory)
    findings.extend(audit_directory_entity(directory, workspace_root, compare_children=True))
    if not manifest_path.exists():
        return findings
    manifest, error = load_manifest(manifest_path)
    if error:
        return findings

    registered = set(manifest.get("structure", {}).get("children", []))
    classification = manifest.get("classification", {})
    classified: dict[str, str] = {}
    for class_name, names in classification.items():
        if class_name in {"artifacts", "root_artifacts"}:
            continue
        for child in names:
            child = str(child)
            if child in classified:
                findings.append(Finding(portfolio_name, "FAIL", f"child has multiple classifications: {child}"))
            classified[child] = class_name
    for child in sorted(registered - set(classified), key=str.lower):
        findings.append(Finding(portfolio_name, "FAIL", f"registered child lacks classification: {child}"))
    for child in sorted(set(classified) - registered, key=str.lower):
        findings.append(Finding(portfolio_name, "FAIL", f"classified child is not registered: {child}"))

    for child, class_name in sorted(classified.items(), key=lambda item: item[0].lower()):
        child_dir = directory / child
        if class_name in {"projects", "project_groups", "datasets"}:
            findings.extend(audit_project(child_dir, directory))
        elif class_name in {"external_sources", "containers", "services", "caches", "runtimes"}:
            findings.extend(audit_directory_entity(child_dir, directory, compare_children=False))
        elif class_name == "archives":
            findings.extend(audit_holding(child_dir, directory))

    governance_shortcuts = sorted(path.name for path in directory.glob("*.lnk"))
    if governance_shortcuts:
        findings.append(Finding(portfolio_name, "FAIL", "portfolio-root Windows shortcuts are forbidden: " + ", ".join(governance_shortcuts)))
    return findings


def audit_workspace(workspace_root: Path) -> dict[str, list[Finding]]:
    findings: dict[str, list[Finding]] = {}
    root_findings: list[Finding] = []
    for filename in ["AGENTS.md", "INDEX.md", "Development.manifest.toml"]:
        if not (workspace_root / filename).is_file():
            root_findings.append(Finding("workspace", "FAIL", f"missing root file {filename}"))
    development_path = workspace_root / "Development.manifest.toml"
    development: dict = {}
    if development_path.exists():
        development, error = load_manifest(development_path)
        if error:
            root_findings.append(Finding("workspace", "FAIL", error))
        else:
            if development.get("manifest", {}).get("canonical_name") != "Development.manifest.toml":
                root_findings.append(Finding("workspace", "FAIL", "drive manifest canonical_name is incorrect"))
            for message in placeholder_values(development):
                root_findings.append(Finding("workspace", "FAIL", message))
            for root in development.get("roots", []):
                path = windows_path(str(root.get("path", "")))
                manifest = windows_path(str(root.get("manifest", "")))
                if not path.exists():
                    root_findings.append(Finding("workspace", "FAIL", f"registered root is missing: {path}"))
                if not manifest.exists():
                    root_findings.append(Finding("workspace", "FAIL", f"registered root manifest is missing: {manifest}"))
    findings["workspace:root"] = root_findings
    registered_portfolios = [
        root for root in development.get("roots", []) if root.get("kind") == "portfolio"
    ]
    if registered_portfolios:
        for root in registered_portfolios:
            portfolio_name = str(root.get("id") or windows_path(str(root.get("path", ""))).name)
            portfolio_path = windows_path(str(root.get("path", "")))
            findings[f"portfolio:{portfolio_name}"] = audit_portfolio(
                workspace_root,
                portfolio_name,
                portfolio_path,
            )
    else:
        for portfolio in WORKSPACE_PORTFOLIOS:
            findings[f"portfolio:{portfolio}"] = audit_portfolio(workspace_root, portfolio)
    for root in development.get("roots", []):
        path = windows_path(str(root.get("path", "")))
        if root.get("kind") in {"shared-infrastructure", "reference-library", "shared-runtime"} and path.exists():
            findings[f"foundation:{path.name}"] = audit_directory_entity(path, workspace_root, compare_children=True)
            manifest, error = load_manifest(entity_manifest_path(path))
            if not error:
                classification = manifest.get("classification", {})
                for names in classification.values():
                    for child_name in names:
                        child = path / str(child_name)
                        if entity_manifest_path(child).exists():
                            findings[f"foundation:{path.name}"].extend(audit_directory_entity(child, path, compare_children=False))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="City Hall workspace root.")
    parser.add_argument("--workspace-root", type=Path, help="Also audit the governed development workspace and portfolios.")
    parser.add_argument("--entity-root", type=Path, action="append", default=[], help="Audit an additional project or directory entity root.")
    parser.add_argument("--format", choices=["markdown", "jsonl"], default="markdown")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        print(f"Root does not exist: {root}", file=sys.stderr)
        return 2

    findings_by_standard = {
        directory.name: audit_standard(directory)
        for directory in standard_directories(root)
    }
    if args.workspace_root:
        workspace_root = args.workspace_root.resolve()
        if not workspace_root.exists():
            print(f"Workspace root does not exist: {workspace_root}", file=sys.stderr)
            return 2
        findings_by_standard.update(audit_workspace(workspace_root))
    for entity_root in args.entity_root:
        directory = entity_root.resolve()
        manifest_path = entity_manifest_path(directory)
        manifest, error = load_manifest(manifest_path) if manifest_path.exists() else ({}, "manifest missing")
        if error:
            findings_by_standard[f"entity:{directory}"] = [Finding(str(directory), "FAIL", error)]
        elif manifest.get("manifest", {}).get("manifest_type") == "project":
            findings_by_standard[f"entity:{directory}"] = audit_project(directory, directory.parent)
        else:
            findings_by_standard[f"entity:{directory}"] = audit_directory_entity(directory, directory.parent, compare_children=True)
    if args.format == "jsonl":
        print(render_jsonl(jsonl_records(root, findings_by_standard)))
    else:
        print(render_markdown(root, findings_by_standard))

    has_failures = any(
        finding.level == "FAIL"
        for findings in findings_by_standard.values()
        for finding in findings
    )
    return 1 if has_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
