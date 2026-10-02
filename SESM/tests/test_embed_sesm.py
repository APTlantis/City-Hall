import unittest
import json
import tempfile
import sys
from pathlib import Path

# Add parent directory to path so we can import Embed-SESM.py
sys.path.insert(0, str(Path(__file__).parent.parent))
import importlib
embed_module = importlib.import_module("Embed-SESM")

class TestEmbedSesm(unittest.TestCase):
    def test_deep_merge(self):
        d1 = {
            "sesm_version": "0.3.0",
            "asset": {
                "id": "my-asset",
                "role": "logo",
                "tags": ["original"]
            },
            "theme": {
                "mode": "dark",
                "tokens": {
                    "base": "#0B0F1A"
                }
            }
        }
        d2 = {
            "asset": {
                "title": "New Title",
                "tags": ["override"]
            },
            "theme": {
                "mode": "light",
                "tokens": {
                    "info": "#22D3EE"
                }
            },
            "extra": {
                "custom": True
            }
        }
        merged = embed_module.deep_merge(d1, d2)
        
        # Verify nested structures are merged recursively
        self.assertEqual(merged["asset"]["id"], "my-asset")
        self.assertEqual(merged["asset"]["title"], "New Title")
        # Tags was overwritten because it is a list, not a dict
        self.assertEqual(merged["asset"]["tags"], ["override"])
        self.assertEqual(merged["theme"]["mode"], "light")
        self.assertEqual(merged["theme"]["tokens"]["base"], "#0B0F1A")
        self.assertEqual(merged["theme"]["tokens"]["info"], "#22D3EE")
        self.assertTrue(merged["extra"]["custom"])

    def test_detect_nipc_theme(self):
        # Case 1: SVG containing code-heat and critical colors
        svg_text = """<svg viewBox="0 0 100 100">
            <rect fill="#0B0F1A" width="100" height="100"/>
            <circle fill="#F97316" r="10" cx="50" cy="50"/>
            <path stroke="#F43F5E" d="M0 0 L10 10"/>
        </svg>"""
        
        theme = embed_module.detect_nipc_theme(svg_text)
        self.assertIsNotNone(theme)
        self.assertEqual(theme["id"], "neon-ink")
        self.assertEqual(theme["tokens"]["base"], "#0B0F1A")
        self.assertEqual(theme["tokens"]["code_heat"], "#F97316")
        self.assertEqual(theme["tokens"]["critical"], "#F43F5E")
        self.assertEqual(theme["accent"]["name"], "code-heat")
        self.assertEqual(theme["state"]["name"], "error") # critical -> error state
        
        # Case 2: SVG containing only info color
        svg_text_info = """<svg>
            <circle fill="#22D3EE" r="10"/>
        </svg>"""
        theme_info = embed_module.detect_nipc_theme(svg_text_info)
        self.assertIsNotNone(theme_info)
        self.assertEqual(theme_info["tokens"]["info"], "#22D3EE")
        self.assertEqual(theme_info["accent"]["name"], "info")
        self.assertEqual(theme_info["state"]["name"], "active") # default active state

    def test_validate_sesm_block_manual_fallback(self):
        # Test basic validation without schema path (triggers manual validation)
        block_ok = {
            "sesm_version": "0.3.0",
            "asset": {
                "id": "my-logo",
                "role": "logo"
            }
        }
        valid, errs = embed_module.validate_sesm_block(block_ok, Path("nonexistent.schema.json"))
        self.assertTrue(valid)
        self.assertEqual(len(errs), 0)

        # Invalid block: missing role, unknown role, bad version
        block_bad = {
            "sesm_version": "0.1.0",
            "asset": {
                "id": "my-logo",
                "role": "not-a-role"
            }
        }
        valid, errs = embed_module.validate_sesm_block(block_bad, Path("nonexistent.schema.json"))
        self.assertFalse(valid)
        self.assertTrue(any("sesm_version" in e for e in errs))
        self.assertTrue(any("role" in e for e in errs))

    def test_process_svg_and_legacy_mapping(self):
        # Create a temp SVG file
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        
        # Write dummy SVG content
        svg_content = """<?xml version="1.0" encoding="utf-8"?>
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <rect fill="#0B0F1A" width="100" height="100"/>
            <circle fill="#22D3EE" r="10" cx="50" cy="50"/>
        </svg>"""
        tmp_path.write_text(svg_content, encoding="utf-8")

        try:
            # Setup overrides including legacy ai mapping
            slug = tmp_path.stem
            overrides = {
                slug: {
                    "sesm": {
                        "asset": {
                            "role": "icon"
                        }
                    },
                    "ai": {
                        "summary": "Legacy AI Summary",
                        "tags": ["imported-tag"]
                    }
                }
            }

            # Process SVG
            valid = embed_module.process_svg(tmp_path, overrides, Path("nonexistent.schema.json"), verbose=True)
            self.assertTrue(valid)

            # Read back processed SVG and extract SESM metadata
            block = embed_module.extract_sesm_block(tmp_path)
            self.assertIsNotNone(block)
            self.assertEqual(block["sesm_version"], "0.3.0")
            self.assertEqual(block["asset"]["role"], "icon") # overridden from logo to icon
            self.assertEqual(block["llm"]["summary"], "Legacy AI Summary") # mapped from ai.summary
            self.assertIn("imported-tag", block["asset"]["tags"]) # mapped from ai.tags
            self.assertEqual(block["theme"]["tokens"]["base"], "#0B0F1A") # NIPC base token detected
            self.assertEqual(block["theme"]["tokens"]["info"], "#22D3EE") # NIPC info token detected
            
        finally:
            # Clean up temp file
            if tmp_path.exists():
                tmp_path.unlink()

if __name__ == "__main__":
    unittest.main()
