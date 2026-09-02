#!/usr/bin/env python3
"""Validate SESM metadata and the SESM safe SVG profile."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


TOOL_NAME = "Validate-SESM-Safe"
TOOL_VERSION = "0.1.0"
SESM_METADATA_ID = "sesm"
MAX_METADATA_BYTES = 64 * 1024
REMOTE_URL_RE = re.compile(r"^(https?:)?//|^(https?|ftp):", re.IGNORECASE)
DATA_URL_RE = re.compile(r"^data:", re.IGNORECASE)
SAFE_RASTER_DATA_URL_RE = re.compile(
    r"^data:image/(png|jpe?g|webp|gif|avif);base64,",
    re.IGNORECASE,
)
JAVASCRIPT_URL_RE = re.compile(r"^\s*javascript\s*:", re.IGNORECASE)
CREDENTIAL_RE = re.compile(
    r"\b(password|passwd|api[_ -]?key|secret|token|credential|private[_ -]?key|bearer)\b",
    re.IGNORECASE,
)
COMMAND_AUTHORITY_RE = re.compile(
    r"\b(run|execute|shell|powershell|cmd\.exe|sudo|ignore previous|bypass policy|reveal secret|exfiltrate)\b",
    re.IGNORECASE,
)


@dataclass
class Finding:
    code: str
    message: str
    path: str = ""


@dataclass
class ValidationResult:
    status: str
    profile: str
    file: str
    errors: list[Finding]
    warnings: list[Finding]
    metadata_version: str | None
    schema: str | None
    safe_profile_checked: bool


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def element_path(element: ET.Element) -> str:
    name = local_name(element.tag)
    element_id = element.attrib.get("id")
    return f"{name}#{element_id}" if element_id else name


def parse_svg(path: Path) -> tuple[ET.Element | None, list[Finding]]:
    try:
        return ET.fromstring(path.read_text(encoding="utf-8")), []
    except Exception as exc:
        return None, [Finding("svg-parse-error", f"SVG is not parseable XML: {exc}")]


def find_sesm_blocks(root: ET.Element) -> list[ET.Element]:
    blocks = []
    for element in root.iter():
        if local_name(element.tag) == "metadata" and element.attrib.get("id") == SESM_METADATA_ID:
            blocks.append(element)
    return blocks


def metadata_text(element: ET.Element) -> str:
    parts = []
    if element.text:
        parts.append(element.text)
    for child in list(element):
        if child.text:
            parts.append(child.text)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts).strip()


def load_metadata(blocks: list[ET.Element]) -> tuple[dict[str, Any] | None, list[Finding], list[Finding]]:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    if not blocks:
        errors.append(Finding("sesm-missing", "No <metadata id=\"sesm\"> block found."))
        return None, errors, warnings
    if len(blocks) > 1:
        errors.append(Finding("sesm-duplicate", "More than one <metadata id=\"sesm\"> block found."))
        return None, errors, warnings

    raw = metadata_text(blocks[0])
    if len(raw.encode("utf-8")) > MAX_METADATA_BYTES:
        errors.append(Finding("sesm-oversized", f"SESM metadata exceeds {MAX_METADATA_BYTES} bytes."))
    try:
        data = json.loads(raw)
    except Exception as exc:
        errors.append(Finding("sesm-json-invalid", f"SESM metadata is not valid JSON: {exc}"))
        return None, errors, warnings
    if not isinstance(data, dict):
        errors.append(Finding("sesm-not-object", "SESM metadata must be a JSON object."))
        return None, errors, warnings
    if "sesm_version" not in data:
        errors.append(Finding("sesm-version-missing", "SESM metadata must include sesm_version."))
    return data, errors, warnings


def validate_schema(data: dict[str, Any], schema_path: Path | None) -> list[Finding]:
    if schema_path is None:
        return []
    if not schema_path.exists():
        return [Finding("schema-missing", f"Schema not found: {schema_path}")]

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [Finding("schema-invalid", f"Schema is not valid JSON: {exc}", str(schema_path))]

    try:
        import jsonschema  # type: ignore
    except Exception:
        return structural_validate(data)

    wrapper = {
        "type": "asset",
        "asset_type": "svg",
        "slug": data.get("asset", {}).get("id", "sesm-asset"),
        "source": {"format": "svg", "content": ""},
        "sesm": data,
    }
    validator = jsonschema.Draft202012Validator(schema)
    findings = []
    for error in sorted(validator.iter_errors(wrapper), key=lambda item: list(item.path)):
        path = ".".join(str(part) for part in error.absolute_path)
        findings.append(Finding("schema-validation", error.message, path))
    return findings


def structural_validate(data: dict[str, Any]) -> list[Finding]:
    findings = []
    version = data.get("sesm_version")
    if version not in {"0.2.0", "0.3.0"}:
        findings.append(Finding("schema-version", "sesm_version must be 0.2.0 or 0.3.0.", "sesm_version"))
    asset = data.get("asset")
    if asset is not None:
        if not isinstance(asset, dict):
            findings.append(Finding("schema-asset", "asset must be an object.", "asset"))
        else:
            if not asset.get("id"):
                findings.append(Finding("schema-asset-id", "asset.id is recommended for validation.", "asset.id"))
            if not asset.get("role"):
                findings.append(Finding("schema-asset-role", "asset.role is required when asset is present.", "asset.role"))
    return findings


def check_safe_profile(root: ET.Element, data: dict[str, Any] | None) -> tuple[list[Finding], list[Finding]]:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    for element in root.iter():
        name = local_name(element.tag)
        path = element_path(element)
        if name == "script":
            errors.append(Finding("svg-script", "SESM-safe SVGs must not contain <script>.", path))
        if name == "text":
            style = element.attrib.get("style", "").lower()
            hidden = (
                element.attrib.get("display") == "none"
                or element.attrib.get("visibility") == "hidden"
                or "display:none" in style.replace(" ", "")
                or "visibility:hidden" in style.replace(" ", "")
                or "opacity:0" in style.replace(" ", "")
            )
            text = "".join(element.itertext()).strip()
            if hidden and text:
                warnings.append(Finding("hidden-text", "Hidden text with content should be reviewed.", path))
        for attr, value in element.attrib.items():
            attr_name = local_name(attr)
            value_text = str(value)
            if attr_name.startswith("on"):
                errors.append(Finding("svg-event-handler", f"Event handler attribute is forbidden: {attr_name}", path))
            if JAVASCRIPT_URL_RE.match(value_text):
                errors.append(Finding("javascript-url", "javascript: URLs are forbidden.", path))
            if attr_name in {"href", "src", "xlink:href"} or attr.endswith("}href"):
                if DATA_URL_RE.match(value_text):
                    if not SAFE_RASTER_DATA_URL_RE.match(value_text):
                        warnings.append(Finding("embedded-data-reference", f"Embedded data reference should be reviewed: {value_text}", path))
                elif REMOTE_URL_RE.match(value_text):
                    warnings.append(Finding("remote-reference", f"Remote reference should be reviewed: {value_text}", path))
            elif REMOTE_URL_RE.search(value_text) or DATA_URL_RE.search(value_text):
                warnings.append(Finding("remote-reference", f"Remote URL should be reviewed: {value_text}", path))

    if data is not None:
        data_text = json.dumps(data, sort_keys=True)
        if CREDENTIAL_RE.search(data_text):
            errors.append(Finding("credential-request", "SESM metadata appears to mention credentials or secrets."))
        if COMMAND_AUTHORITY_RE.search(data_text):
            errors.append(Finding("agent-command-authority", "SESM metadata appears to request command authority or policy bypass."))
    return errors, warnings


def validate_file(path: Path, schema_path: Path | None, safe_profile: bool) -> ValidationResult:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    if not path.exists():
        return ValidationResult(
            status="error",
            profile="sesm-unverified",
            file=str(path),
            errors=[Finding("input-missing", f"Input file not found: {path}")],
            warnings=[],
            metadata_version=None,
            schema=str(schema_path) if schema_path else None,
            safe_profile_checked=safe_profile,
        )

    root, parse_errors = parse_svg(path)
    errors.extend(parse_errors)
    metadata_version = None
    if root is None:
        return ValidationResult("error", "sesm-unverified", str(path), errors, warnings, None, str(schema_path) if schema_path else None, safe_profile)

    metadata, metadata_errors, metadata_warnings = load_metadata(find_sesm_blocks(root))
    errors.extend(metadata_errors)
    warnings.extend(metadata_warnings)
    if metadata is not None:
        metadata_version = str(metadata.get("sesm_version")) if metadata.get("sesm_version") is not None else None
        errors.extend(validate_schema(metadata, schema_path))

    if safe_profile:
        safe_errors, safe_warnings = check_safe_profile(root, metadata)
        errors.extend(safe_errors)
        warnings.extend(safe_warnings)

    if errors:
        profile = "sesm-unsafe" if safe_profile else "sesm-unverified"
        status = "error"
    elif safe_profile and warnings:
        profile = "sesm-unverified"
        status = "warning"
    elif safe_profile:
        profile = "sesm-safe"
        status = "ok"
    else:
        profile = "sesm-valid"
        status = "ok" if not warnings else "warning"

    return ValidationResult(status, profile, str(path), errors, warnings, metadata_version, str(schema_path) if schema_path else None, safe_profile)


def print_human(result: ValidationResult) -> None:
    print(f"{TOOL_NAME} {TOOL_VERSION}")
    print(f"File: {result.file}")
    print(f"Status: {result.status}")
    print(f"Profile: {result.profile}")
    if result.metadata_version:
        print(f"SESM version: {result.metadata_version}")
    for finding in result.errors:
        location = f" ({finding.path})" if finding.path else ""
        print(f"ERROR {finding.code}{location}: {finding.message}")
    for finding in result.warnings:
        location = f" ({finding.path})" if finding.path else ""
        print(f"WARN {finding.code}{location}: {finding.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path, help="SVG file to validate.")
    parser.add_argument("--schema", type=Path, default=Path(__file__).with_name("svg_asset.schema.json"))
    parser.add_argument("--safe-profile", action="store_true", help="Check the SESM safe SVG profile.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    result = validate_file(args.svg, args.schema, args.safe_profile)
    if args.json:
        print(json.dumps(asdict(result), indent=2))
    else:
        print_human(result)

    if result.status == "ok":
        return 0
    if result.status == "warning":
        return 0
    return 4 if any(error.code != "input-missing" for error in result.errors) else 3


if __name__ == "__main__":
    raise SystemExit(main())
