import unittest
import tempfile
import sys
import os
from pathlib import Path
from PIL import Image, ImageDraw

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
import importlib
convert_module = importlib.import_module("Convert-to-SVG")

class TestConvertToSvg(unittest.TestCase):
    def setUp(self):
        # Create a temp directory for input/output files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.dir_path = Path(self.temp_dir.name)
        
        # Create a dummy test image: A black square with a white hole in the center
        # Background is white. Shape is black. Hole is white.
        self.img_path = self.dir_path / "test_shape.png"
        img = Image.new("RGBA", (100, 100), "white")
        draw = ImageDraw.Draw(img)
        # Black outer square
        draw.rectangle([20, 20, 80, 80], fill="black")
        # White inner hole
        draw.rectangle([40, 40, 60, 60], fill="white")
        img.save(self.img_path, format="PNG")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_image_to_svg_embed(self):
        out_svg = self.dir_path / "embed_output.svg"
        convert_module.image_to_svg_embed(str(self.img_path), str(out_svg))
        
        self.assertTrue(out_svg.exists())
        content = out_svg.read_text(encoding="utf-8")
        
        # Should contain image tag with base64 data
        self.assertIn("<image", content)
        self.assertIn("data:image/png;base64,", content)
        self.assertIn('width="100"', content)
        self.assertIn('height="100"', content)

    def test_image_to_svg_trace_monochrome_hierarchy(self):
        # Skip if cv2 (OpenCV) is not available
        if not convert_module._CV2_AVAILABLE:
            self.skipTest("OpenCV is not available, skipping vector tracing test.")

        out_svg = self.dir_path / "trace_output.svg"
        
        # We trace with invert=True since the shape is black on a white background.
        # This will threshold white background to 0 (black) and shape to 255 (white)
        # with its inner hole thresholded to 0 (black).
        convert_module.image_to_svg_trace(
            str(self.img_path),
            str(out_svg),
            threshold="auto",
            simplify=0.0, # Disable simplification to get exact rect coords
            invert=True,
            fill_color="#FF0000",
            blur=0,
            min_area=5.0
        )

        self.assertTrue(out_svg.exists())
        content = out_svg.read_text(encoding="utf-8")
        
        # Verify evenodd fill rule is present
        self.assertIn('fill-rule="evenodd"', content)
        self.assertIn('fill="#FF0000"', content)

        # Count the number of 'M' commands in path d-attributes.
        # A square with a hole should have 2 sub-paths, hence 2 'M' commands.
        self.assertTrue(content.count("M") >= 2, f"Expected at least 2 'M' commands for shape with hole, got: {content.count('M')}")

    def test_image_to_svg_trace_min_area_filter(self):
        if not convert_module._CV2_AVAILABLE:
            self.skipTest("OpenCV is not available.")

        # Create image with tiny speck (noise)
        noise_img_path = self.dir_path / "noise_shape.png"
        img = Image.new("RGBA", (100, 100), "white")
        draw = ImageDraw.Draw(img)
        # Main solid square (60x60 area = 3600)
        draw.rectangle([20, 20, 80, 80], fill="black")
        # Tiny noise pixel (1x2 area = 2)
        draw.rectangle([5, 5, 6, 7], fill="black")
        img.save(noise_img_path, format="PNG")

        out_svg = self.dir_path / "noise_output.svg"
        
        # Trace with min_area = 10. This should filter out the noise pixel but keep the main square.
        convert_module.image_to_svg_trace(
            str(noise_img_path),
            str(out_svg),
            threshold="auto",
            simplify=0.0,
            invert=True,
            min_area=10.0
        )
        
        content = out_svg.read_text(encoding="utf-8")
        
        # The main square contour is a 4-point rectangle, the noise is 4-point.
        # Since noise is filtered, we should have exactly 1 path element
        self.assertEqual(content.count("<path"), 1)

    def test_run_conversion_fallback(self):
        # Even if trace is requested, if OpenCV is missing, it should fall back to embed
        # (We simulate this by temporarily patching _CV2_AVAILABLE to False)
        orig_cv2 = convert_module._CV2_AVAILABLE
        try:
            convert_module._CV2_AVAILABLE = False
            out_svg = self.dir_path / "fallback_output.svg"
            
            # This should fall back to base64 embedding
            convert_module.run_conversion(
                str(self.img_path),
                str(out_svg),
                mode="auto",
                threshold="auto",
                simplify=2.0,
                invert=False
            )
            
            self.assertTrue(out_svg.exists())
            content = out_svg.read_text(encoding="utf-8")
            self.assertIn("<image", content) # Fallback is active
        finally:
            convert_module._CV2_AVAILABLE = orig_cv2

if __name__ == "__main__":
    unittest.main()
