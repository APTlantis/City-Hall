import datetime
import json
import re
import xml.etree.ElementTree as ET
import sys
import argparse
from pathlib import Path

TARGET_SIZE = 300  # logical render size (px)
PROJECT = "aptlantis"
GENERATOR = "aptlantis-svg-asset-worker"

SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)

def load_overrides(overrides_path: Path, verbose=False):
    if overrides_path.exists():
        try:
            with open(overrides_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Remove example if it exists
                data.pop("_example", None)
                if verbose:
                    print(f"Loaded {len(data)} overrides from {overrides_path.name}")
                return data
        except Exception as e:
            print(f"Error loading overrides from {overrides_path}: {e}")
    else:
        if verbose:
            print(f"Overrides file not found at {overrides_path}; proceeding without overrides.")
    return {}

def parse_svg_length(value):
    if value is None:
        return None
    text = str(value).strip()
    match = re.match(r"^([0-9]*\.?[0-9]+)", text)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None

def get_viewbox(root):
    # Keep existing viewBox if it's there
    viewbox = root.get("viewBox")
    if viewbox:
        return viewbox

    # Fallback to computing from width and height
    width = parse_svg_length(root.get("width"))
    height = parse_svg_length(root.get("height"))

    if width is not None and height is not None:
        return f"0 0 {width} {height}"
    
    return f"0 0 {TARGET_SIZE} {TARGET_SIZE}"

def strip_editor_junk(root):
    # Remove any attribute containing inkscape or sodipodi in its key
    for key in list(root.attrib.keys()):
        if any(junk in key for junk in ["inkscape", "sodipodi"]):
            del root.attrib[key]

def deep_merge(dict1, dict2):
    """
    Recursively merge dict2 into dict1 in place.
    """
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            deep_merge(dict1[key], value)
        else:
            dict1[key] = value
    return dict1

def detect_nipc_theme(svg_text: str):
    """
    Scan the SVG XML text for NIPC colors and construct a semantic theme block.
    """
    # Find all hex color codes (e.g. #0B0F1A)
    hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}\b', svg_text))
    # Normalize to lowercase
    hex_colors = {c.lower() for c in hex_colors}

    nipc_map = {
        "#050816": "void",
        "#0b0f1a": "base",
        "#111827": "panel",
        "#22d3ee": "info",
        "#a78bfa": "process",
        "#f472b6": "featured",
        "#34d399": "success",
        "#facc15": "important",
        "#f43f5e": "critical",
        "#f97316": "code_heat",
        "#e5e7eb": "text",
        "#94a3b8": "muted"
    }

    detected_tokens = {}
    for hc in hex_colors:
        if hc in nipc_map:
            detected_tokens[nipc_map[hc]] = hc.upper()

    if not detected_tokens:
        return None

    theme_block = {
        "id": "neon-ink",
        "name": "Neon Ink",
        "version": "0.1.0",
        "palette_contract": "nipc-0.1",
        "mode": "dark",
        "tokens": detected_tokens,
        "semantic_families": {
            "clarity-orientation": ["info", "structure", "navigation", "reference", "orientation"],
            "trust-validation": ["success", "verified", "stable", "reproducible", "available"],
            "attention-learning-anchor": ["important", "note", "caution", "decision", "memory-anchor"],
            "risk-constraint": ["critical", "error", "blocked", "constraint", "deprecated"],
            "process-transformation": ["process", "pipeline", "transform", "automation", "orchestration"],
            "creation-build-code": ["code-heat", "build", "operation", "artifact-output", "tooling"],
            "discovery-creative-featured": ["featured", "creative", "discovery", "spotlight", "human-note"],
            "research-experimental": ["experimental", "research", "prototype", "hypothesis", "unstable"],
            "canonical-archive-neutral": ["canonical", "archive", "muted", "unknown", "baseline"]
        }
    }

    # Add accent color info if detected
    if "code_heat" in detected_tokens:
        theme_block["accent"] = {
            "name": "code-heat",
            "hex": "#F97316",
            "semantic_role": "code-heat",
            "semantic_family": "creation-build-code",
            "psychological_intent": "signal-hands-on-code-build-work"
        }
    elif "info" in detected_tokens:
        theme_block["accent"] = {
            "name": "info",
            "hex": "#22D3EE",
            "semantic_role": "info",
            "semantic_family": "clarity-orientation",
            "psychological_intent": "understanding-reference-guidance"
        }
    elif "featured" in detected_tokens:
        theme_block["accent"] = {
            "name": "featured",
            "hex": "#F472B6",
            "semantic_role": "featured",
            "semantic_family": "discovery-creative-featured",
            "psychological_intent": "featured-creative-spotlight"
        }

    # State tracking based on tokens present
    if "critical" in detected_tokens:
        theme_block["state"] = {
            "name": "error",
            "intensity": 3,
            "glow": "intense",
            "priority": "high"
        }
    elif "important" in detected_tokens:
        theme_block["state"] = {
            "name": "warning",
            "intensity": 2,
            "glow": "soft",
            "priority": "high"
        }
    elif "success" in detected_tokens:
        theme_block["state"] = {
            "name": "verified",
            "intensity": 1,
            "glow": "none",
            "priority": "medium"
        }
    else:
        theme_block["state"] = {
            "name": "active",
            "intensity": 2,
            "glow": "soft",
            "priority": "medium"
        }

    return theme_block

def validate_sesm_block(sesm_block, schema_path: Path, verbose=False):
    # Try using jsonschema
    try:
        import jsonschema
        if schema_path and schema_path.exists():
            with open(schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
            sesm_schema = schema.get("properties", {}).get("sesm", {})
            jsonschema.validate(instance=sesm_block, schema=sesm_schema)
            if verbose:
                print("  [Valid] Complies with JSON Schema draft 2020-12.")
            return True, []
        else:
            if verbose:
                print("  [Warning] Schema path not found; using structural validation fallback.")
    except ImportError:
        if verbose:
            print("  [Warning] jsonschema library not found; using structural validation fallback.")
    except Exception as e:
        return False, [f"JSON Schema error: {e}"]

    # Fallback manual validation
    errors = []
    if not isinstance(sesm_block, dict):
        return False, ["SESM block must be a JSON object"]
    
    if sesm_block.get("sesm_version") not in {"0.2.0", "0.3.0"}:
        errors.append(f"Invalid or missing sesm_version (expected '0.2.0' or '0.3.0', got '{sesm_block.get('sesm_version')}')")
    
    if "asset" in sesm_block:
        asset = sesm_block["asset"]
        if not isinstance(asset, dict):
            errors.append("asset must be an object")
        else:
            if "id" not in asset:
                errors.append("asset.id is required")
            if "role" not in asset:
                errors.append("asset.role is required")
            elif asset["role"] not in [
                "logo", "icon", "theme-board", "dataset-card", "dataset-header",
                "pipeline-panel", "stats-panel", "navigation-card", "graph-node",
                "graph-panel", "status-badge", "download-card", "schema-card",
                "archive-summary", "landing-hero", "page-header", "decorative", "unknown"
            ]:
                errors.append(f"Unknown asset.role: {asset['role']}")
                
    if "theme" in sesm_block:
        theme = sesm_block["theme"]
        if not isinstance(theme, dict):
            errors.append("theme must be an object")
        else:
            if "mode" in theme and theme["mode"] not in ["light", "dark"]:
                errors.append("theme.mode must be 'light' or 'dark'")
            if "accent" in theme:
                accent = theme["accent"]
                if not isinstance(accent, dict):
                    errors.append("theme.accent must be an object")
                elif "hex" in accent:
                    if not re.match(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$", accent["hex"]):
                        errors.append(f"Invalid theme.accent.hex color format: {accent['hex']}")
            if "state" in theme:
                state = theme["state"]
                if not isinstance(state, dict):
                    errors.append("theme.state must be an object")
                elif "name" in state and state["name"] not in [
                    "idle", "running", "active", "featured", "complete", "verified",
                    "warning", "error", "archived", "experimental", "deprecated"
                ]:
                    errors.append(f"Unknown theme.state.name: {state['name']}")
                    
    if "provenance" in sesm_block:
        prov = sesm_block["provenance"]
        if not isinstance(prov, dict):
            errors.append("provenance must be an object")
        else:
            if "generated" in prov and not isinstance(prov["generated"], bool):
                errors.append("provenance.generated must be a boolean")
                
    return len(errors) == 0, errors

def extract_sesm_block(path: Path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        for child in root:
            tag = child.tag.split("}")[-1]
            if tag == "metadata" and child.get("id") == "sesm":
                text = (child.text or "").strip()
                if text.startswith("<![CDATA["):
                    text = text[len("<![CDATA["):]
                if text.endswith("]]>"):
                    text = text[:-len("]]>")]
                text = text.strip()
                return json.loads(text)
    except Exception:
        return None
    return None

def process_svg(path: Path, overrides, schema_path: Path, verbose=False):
    # 1. Read raw SVG file first (for color parsing and metadata preservation)
    with open(path, "r", encoding="utf-8") as f:
        svg_text = f.read()

    tree = ET.parse(path)
    root = tree.getroot()
    slug = path.stem

    # Remove existing metadata blocks
    for child in list(root):
        if isinstance(child.tag, str) and child.tag.split("}")[-1] == "metadata":
            root.remove(child)

    # Clean editor junk
    strip_editor_junk(root)

    # Handle viewBox and normalize dimensions
    viewbox = get_viewbox(root)
    root.set("viewBox", viewbox)
    root.set("width", str(TARGET_SIZE))
    root.set("height", str(TARGET_SIZE))

    # Construct default SESM block
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    derived_title = slug.replace("apt-", "").replace("-logo", "").replace(".", " ").title() + " Logo"
    derived_ecosystem = slug.replace("apt-", "").replace("-logo", "").split(".")[0]

    sesm_block = {
        "sesm_version": "0.3.0",
        "asset": {
            "id": slug,
            "role": "logo",
            "title": derived_title,
            "ecosystem": derived_ecosystem,
            "tags": [derived_ecosystem, "logo", "branding"]
        },
        "ui": {
            "dimensions": {
                "width": float(TARGET_SIZE),
                "height": float(TARGET_SIZE),
                "viewBox": viewbox
            }
        },
        "provenance": {
            "generated": True,
            "generator": {
                "name": GENERATOR,
                "version": "0.2.0",
                "language": "python"
            },
            "generated_at": timestamp
        }
    }

    # Run NIPC theme detection heuristics
    detected_theme = detect_nipc_theme(svg_text)
    if detected_theme:
        sesm_block["theme"] = detected_theme
        if verbose:
            print(f"  Detected NeonInk palette contract colors. Theme metadata auto-populated.")

    # Apply override if available (deep merging)
    override = overrides.get(slug) or overrides.get(path.name)
    if override:
        if "sesm" in override:
            sesm_block = deep_merge(sesm_block, override["sesm"])
        
        # Legacy mappings (ai summary/tags)
        if "ai" in override and isinstance(override["ai"], dict):
            ai = override["ai"]
            if "summary" in ai:
                if "llm" not in sesm_block:
                    sesm_block["llm"] = {}
                if "summary" not in sesm_block["llm"]:
                    sesm_block["llm"]["summary"] = ai["summary"]
            if "tags" in ai and isinstance(ai["tags"], list):
                seen = set(sesm_block["asset"].get("tags", []))
                merged_tags = list(sesm_block["asset"].get("tags", []))
                for t in ai["tags"]:
                    if t not in seen:
                        merged_tags.append(t)
                        seen.add(t)
                sesm_block["asset"]["tags"] = merged_tags

    # Validate the built block
    valid, errs = validate_sesm_block(sesm_block, schema_path, verbose)
    if not valid:
        print(f"  [Validation Error] {path.name} failed verification:")
        for err in errs:
            print(f"    - {err}")

    # Inject placeholder for CDATA
    metadata = ET.Element("metadata", id="sesm")
    metadata.text = "__SESM_CDATA_PLACEHOLDER__"
    root.insert(0, metadata)

    # Convert XML to string
    xml_str = ET.tostring(root, encoding="unicode")

    # Replace placeholder with standard CDATA format
    cdata_str = f"<![CDATA[\n{json.dumps(sesm_block, indent=2)}\n]]>"
    xml_str = xml_str.replace("__SESM_CDATA_PLACEHOLDER__", cdata_str)

    # Write SVG file back
    with open(path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n' + xml_str + '\n')

    return valid

def main(argv=None):
    parser = argparse.ArgumentParser(description="Embed structured semantic metadata inside SVG assets.")
    parser.add_argument("--input-dir", "-i", default=str(Path(__file__).parent / "svg"), help="Directory containing SVG assets.")
    parser.add_argument("--overrides", "-o", default=str(Path(__file__).parent / "svg-metadata.overrides.json"), help="Path to metadata overrides file.")
    parser.add_argument("--schema", "-s", default=str(Path(__file__).parent / "svg_asset.schema.json"), help="Path to validation JSON Schema.")
    parser.add_argument("--validate-only", action="store_true", help="Only validate existing embedded metadata, without modifications.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable detailed logging output.")

    args = parser.parse_args(argv)

    svg_dir = Path(args.input_dir)
    overrides_path = Path(args.overrides)
    schema_path = Path(args.schema)

    if not svg_dir.exists():
        print(f"Error: Directory {svg_dir} does not exist.")
        return 1

    if args.validate_only:
        print(f"Validating SVGs in {svg_dir}...")
        all_valid = True
        svg_files = list(svg_dir.glob("*.svg"))
        if not svg_files:
            print("No SVG files found.")
            return 0
        
        for svg in svg_files:
            block = extract_sesm_block(svg)
            if not block:
                print(f"{svg.name}: [FAIL] Missing or invalid <metadata id=\"sesm\"> block.")
                all_valid = False
                continue
            
            valid, errs = validate_sesm_block(block, schema_path, args.verbose)
            if valid:
                if args.verbose:
                    print(f"{svg.name}: [OK]")
            else:
                print(f"{svg.name}: [FAIL]")
                for e in errs:
                    print(f"  - {e}")
                all_valid = False
        
        if all_valid:
            print("All assets validated successfully.")
            return 0
        else:
            print("Some assets failed validation.")
            return 2

    overrides = load_overrides(overrides_path, args.verbose)

    print(f"Processing and embedding metadata in {svg_dir}...")
    svg_files = list(svg_dir.glob("*.svg"))
    if not svg_files:
        print("No SVG files found.")
        return 0

    failed_count = 0
    for svg in svg_files:
        if args.verbose:
            print(f"Processing {svg.name}...")
        valid = process_svg(svg, overrides, schema_path, args.verbose)
        if not valid:
            failed_count += 1
            
    print(f"Done processing {len(svg_files)} SVGs.")
    if failed_count > 0:
        print(f"Warning: {failed_count} SVGs failed validation checks.")
        return 3
    return 0

if __name__ == "__main__":
    sys.exit(main())
