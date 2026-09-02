"""Validate the Blue Slate Bootstrap 5.3 profile without requiring Bootstrap itself."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOKENS = ROOT / "spec" / "tokens" / "BlueSlate.Tokens.json"
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
    if tokens["version"] != "0.3.0":
        raise SystemExit("Expected Blue Slate tokens version 0.3.0")
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
    normal_text_pairs = (("#e7ece3", "#050913"), ("#cbd6d1", "#050913"), ("#b2c0c3", "#0b1728"), ("#65f2ff", "#050913"))
    indicator_pairs = (("#00d8ff", "#050913"), ("#30d58c", "#0b1728"), ("#ff884d", "#0b1728"), ("#ff5c74", "#0b1728"))
    if any(contrast(*pair) < 4.5 for pair in normal_text_pairs):
        raise SystemExit("A normal-text profile pair does not meet 4.5:1 contrast")
    if any(contrast(*pair) < 3 for pair in indicator_pairs):
        raise SystemExit("A non-text indicator profile pair does not meet 3:1 contrast")
    print(f"Validated {len(properties)} Bootstrap 5.3 custom properties and profile contrast thresholds against Blue Slate 0.3.0 roles/aliases.")


if __name__ == "__main__":
    main()
