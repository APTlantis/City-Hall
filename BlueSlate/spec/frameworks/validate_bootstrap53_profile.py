"""Validate the Blue Slate Bootstrap 5.3 profile without requiring Bootstrap itself."""
from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOKENS = ROOT / "generated" / "BlueSlate.Tokens.json"
CSS = ROOT / "starter-packs" / "bootstrap53" / "aptlantis-blue-slate.bootstrap53.css"
PROFILE = ROOT / "spec" / "frameworks" / "BlueSlate.Bootstrap53.md"
SAMPLE = ROOT / "starter-packs" / "bootstrap53" / "sample-surface.html"

# These families are documented in the profile as Bootstrap-required aliases.
ALIAS_PATTERNS = (
    r"--bs-(blue|indigo|purple|pink|red|orange|yellow|green|teal|cyan)$",
    r"--bs-(black|white|gray|gray-dark|gray-[1-9]00)$",
    r"--bs-.*-rgb$",
    r"--bs-(primary|secondary|success|info|warning|danger|light|dark)-(text-emphasis|bg-subtle|border-subtle)$",
)

# Every non-alias Bootstrap variable belongs to one canonical semantic group.
ROLE_PATTERNS = (
    r"--bs-(primary|secondary|success|info|warning|danger|light|dark)$",
    r"--bs-(secondary|tertiary)-color$",
    r"--bs-(secondary|tertiary)-bg$",
    r"--bs-(font|body|emphasis|heading|link|code|highlight|border|box-shadow|focus-ring|form)-.*$",
    r"--bs-(gradient|border-width|border-style|border-color|border-color-translucent|border-radius|border-radius-sm|border-radius-lg|border-radius-xl|border-radius-xxl|border-radius-2xl|border-radius-pill|box-shadow|box-shadow-sm|box-shadow-lg|box-shadow-inset)$",
)


def matches(patterns: tuple[str, ...], name: str) -> bool:
    return any(re.fullmatch(pattern, name) for pattern in patterns)


def contrast(hex_a: str, hex_b: str) -> float:
    def luminance(value: str) -> float:
        channels = [int(value[index : index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    first, second = sorted((luminance(hex_a), luminance(hex_b)), reverse=True)
    return (first + 0.05) / (second + 0.05)


def main() -> None:
    tokens = json.loads(TOKENS.read_text(encoding="utf-8"))
    source = tomllib.loads((ROOT / "spec/tokens/BlueSlate.Tokens.toml").read_text(encoding="utf-8-sig"))
    if tokens["version"] != source["meta"]["version"] or tokens.get("canonicalSource") != "BlueSlate.Tokens.toml":
        raise SystemExit("Generated token version/source differs from the canonical TOML")
    for section in ("palette", "semantic", "foundation", "typography"):
        if section not in tokens:
            raise SystemExit(f"Missing token section: {section}")
    profile_text = PROFILE.read_text(encoding="utf-8")
    if "Bootstrap compatibility aliases" not in profile_text:
        raise SystemExit("Bootstrap compatibility aliases are not documented")
    sample_text = SAMPLE.read_text(encoding="utf-8")
    required_sample_markers = ("card", "navbar", "table", "badge", "btn-primary", "disabled", "is-valid", "is-invalid", "alert", "progress", "<code>")
    missing_markers = [marker for marker in required_sample_markers if marker not in sample_text]
    if missing_markers:
        raise SystemExit("Bootstrap starter example is missing: " + ", ".join(missing_markers))
    properties = set(re.findall(r"(--bs-[a-z0-9-]+)\s*:", CSS.read_text(encoding="utf-8")))
    unmapped = sorted(name for name in properties if not matches(ALIAS_PATTERNS, name) and not matches(ROLE_PATTERNS, name))
    if unmapped:
        raise SystemExit("Unmapped Bootstrap properties: " + ", ".join(unmapped))
    css_text = CSS.read_text(encoding="utf-8")
    values = dict(re.findall(r"(--bs-[a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;", css_text))
    normal_text_pairs = tuple((values[a], values[b]) for a, b in (("--bs-body-color", "--bs-body-bg"), ("--bs-link-color", "--bs-body-bg"), ("--bs-heading-color", "--bs-tertiary-bg")))
    indicator_pairs = tuple((values[name], values["--bs-body-bg"]) for name in ("--bs-primary", "--bs-success", "--bs-warning", "--bs-danger"))
    if any(contrast(*pair) < 4.5 for pair in normal_text_pairs):
        raise SystemExit("A normal-text profile pair does not meet 4.5:1 contrast")
    if any(contrast(*pair) < 3 for pair in indicator_pairs):
        raise SystemExit("A non-text indicator profile pair does not meet 3:1 contrast")
    print(f"Validated {len(properties)} legacy Bootstrap 5.3 property names, specimen markers, and 7 opaque CSS contrast pairs. This is not a rendered-state or full semantic mapping audit.")


if __name__ == "__main__":
    main()
