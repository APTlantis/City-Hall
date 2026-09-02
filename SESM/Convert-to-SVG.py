# =========================================================
# Script Name: Convert-to-SVG.py
# Description: Convert images (PNG, JPG, WEBP, etc.) to SVG.
#              Default: embed raster inside SVG as base64 (preserves appearance).
#              Optional: monochrome vector tracing using OpenCV contours if available.
# Author: APTlantis Team
# Creation Date: 2025-08-20
# Last Modified: 2026-05-27
# 
# Dependencies:
# - Python 3.x
# - Pillow (PIL)
# - Optional: opencv-python (for trace mode)
# 
# Usage examples:
#   python Convert-to-SVG.py --input "C:\\path\\to\\image.png"
#   python Convert-to-SVG.py --input "C:\\Users\\Administrator\\Desktop\\AptlantisLogos\\png" --mode embed
#   python Convert-to-SVG.py --input "C:\\path\\to\\image.jpg" --mode trace --threshold auto --simplify 2.5 --blur 3 --min-area 15
#   python Convert-to-SVG.py --input "C:\\path\\to\\image.webp" --mode embed --output-dir "C:\\out"
# =========================================================

import os
import io
import sys
import base64
import argparse
from typing import Optional, Tuple, Union

try:
    from PIL import Image  # type: ignore
    _PIL_AVAILABLE = True
except Exception:
    Image = None  # type: ignore
    _PIL_AVAILABLE = False

# Optional import for tracing
try:
    import cv2  # type: ignore
    _CV2_AVAILABLE = True
except Exception:
    _CV2_AVAILABLE = False

SUPPORTED_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.tif', '.tiff'}


def ensure_dir(path: str) -> None:
    if path and not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def make_output_path(input_path: str, output_dir: Optional[str]) -> str:
    base, _ = os.path.splitext(os.path.basename(input_path))
    out_dir = output_dir if output_dir else os.path.dirname(input_path)
    ensure_dir(out_dir)
    return os.path.join(out_dir, base + '.svg')


def pil_load_rgba(path: str) -> Image.Image:
    # Use PIL to load first frame; convert to RGBA for consistent embedding
    if not _PIL_AVAILABLE:
        raise RuntimeError("Pillow is required for embedding raster images. Install with: pip install Pillow")
    try:
        img = Image.open(path)
        if getattr(img, "is_animated", False):
            img.seek(0)
        if img.mode not in ("RGBA", "RGB"):
            img = img.convert("RGBA")
        return img
    except Exception as e:
        raise RuntimeError(f"Pillow failed to load image: {e}")


def image_to_svg_embed(input_path: str, output_path: str, png_compress_level: int = 6) -> None:
    # Load image, encode as PNG in-memory, embed into SVG as base64
    img = pil_load_rgba(input_path)
    width, height = img.size

    buf = io.BytesIO()
    # Save as PNG to preserve transparency uniformly
    img.save(buf, format='PNG', compress_level=png_compress_level)
    data_b64 = base64.b64encode(buf.getvalue()).decode('ascii')

    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" \n     xmlns:xlink="http://www.w3.org/1999/xlink" \n     version="1.1" width="%d" height="%d" viewBox="0 0 %d %d">' % (width, height, width, height))
    svg.append('  <image x="0" y="0" width="%d" height="%d" xlink:href="data:image/png;base64,%s"/>' % (width, height, data_b64))
    svg.append('</svg>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg))


def _threshold_image(gray: 'cv2.Mat', threshold: str | int) -> Tuple['cv2.Mat', int]:  # type: ignore
    # Helper: apply threshold; supports 'auto' (Otsu) or specific integer
    if isinstance(threshold, str):
        thr_str = threshold.strip().lower()
        if thr_str == 'auto':
            # Otsu's method
            _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            return bw, 0
        else:
            try:
                tval = int(threshold)
            except Exception:
                tval = 128
    else:
        tval = int(threshold)
    _, bw = cv2.threshold(gray, tval, 255, cv2.THRESH_BINARY)
    return bw, tval


def image_to_svg_trace(
    input_path: str,
    output_path: str,
    threshold: str | int = 'auto',
    simplify: float = 2.0,
    invert: bool = False,
    fill_color: str = '#000000',
    blur: int = 0,
    min_area: float = 10.0
) -> None:
    if not _CV2_AVAILABLE:
        raise RuntimeError("Trace mode requires opencv-python. Install with: pip install opencv-python")

    # Read with OpenCV
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise RuntimeError(f"Failed to read image: {input_path}")

    height, width = img.shape[:2]

    # Build grayscale; respect alpha if present by premultiplying over white
    if img.ndim == 3 and img.shape[2] == 4:  # BGRA
        b, g, r, a = cv2.split(img)
        alpha = a.astype('float32') / 255.0
        rgb = cv2.merge([b, g, r]).astype('float32')
        white = 255.0
        composite = (rgb * alpha[..., None] + white * (1.0 - alpha[..., None])).astype('uint8')
        gray = cv2.cvtColor(composite, cv2.COLOR_BGR2GRAY)
    elif img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # Apply Gaussian Blur if specified
    if blur > 0:
        if blur % 2 == 0:
            blur += 1  # Kernel size must be odd
        gray = cv2.GaussianBlur(gray, (blur, blur), 0)

    bw, used_threshold = _threshold_image(gray, threshold)

    if invert:
        bw = 255 - bw

    # Find contours using RETR_CCOMP to extract parent contours and their internal holes
    contours, hierarchy = cv2.findContours(bw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    path_elements = []
    if hierarchy is not None and len(contours) > 0:
        hierarchy_flat = hierarchy[0]
        for i in range(len(contours)):
            # If contour is a parent (external boundary, parent_idx == -1)
            if hierarchy_flat[i][3] == -1:
                # Check minimum area
                if cv2.contourArea(contours[i]) < min_area:
                    continue

                # Simplify parent contour
                approx = cv2.approxPolyDP(contours[i], simplify, True) if simplify > 0 else contours[i]
                if len(approx) < 3:
                    continue

                # Construct SVG path definition
                d_parts = []
                pts = approx.reshape(-1, 2)
                x0, y0 = pts[0]
                d_parts.append(f"M {x0} {y0}")
                for x, y in pts[1:]:
                    d_parts.append(f"L {x} {y}")
                d_parts.append("Z")

                # Traversal through children of this parent contour (holes)
                child_idx = hierarchy_flat[i][2]
                while child_idx != -1:
                    # Filter child contour by minimum area
                    if cv2.contourArea(contours[child_idx]) >= min_area:
                        approx_child = cv2.approxPolyDP(contours[child_idx], simplify, True) if simplify > 0 else contours[child_idx]
                        if len(approx_child) >= 3:
                            cpts = approx_child.reshape(-1, 2)
                            cx0, cy0 = cpts[0]
                            d_parts.append(f"M {cx0} {cy0}")
                            for cx, cy in cpts[1:]:
                                d_parts.append(f"L {cx} {cy}")
                            d_parts.append("Z")
                    # Move to next child contour sibling
                    child_idx = hierarchy_flat[child_idx][0]

                d_attr = " ".join(d_parts)
                path_elements.append(f'<path d="{d_attr}" fill="{fill_color}" fill-rule="evenodd" stroke="none"/>')

    svg_lines = []
    svg_lines.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    svg_lines.append('<svg xmlns="http://www.w3.org/2000/svg" \n     xmlns:xlink="http://www.w3.org/1999/xlink" \n     version="1.1" width="%d" height="%d" viewBox="0 0 %d %d">' % (width, height, width, height))

    if not path_elements:
        # Fallback: if no contours detected, embed raster instead of saving an empty SVG
        img_pil = pil_load_rgba(input_path)
        buf = io.BytesIO()
        img_pil.save(buf, format='PNG', compress_level=6)
        data_b64 = base64.b64encode(buf.getvalue()).decode('ascii')
        svg_lines.append('  <!-- No contours detected; embedding raster fallback -->')
        svg_lines.append('  <image x="0" y="0" width="%d" height="%d" xlink:href="data:image/png;base64,%s"/>' % (width, height, data_b64))
    else:
        svg_lines.extend("  " + p for p in path_elements)

    svg_lines.append('</svg>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg_lines))


def process_path(
    input_path: str,
    output_dir: Optional[str],
    mode: str,
    threshold: str | int,
    simplify: float,
    invert: bool,
    overwrite: bool,
    blur: int = 0,
    min_area: float = 10.0
) -> int:
    if os.path.isfile(input_path):
        ext = os.path.splitext(input_path)[1].lower()
        if ext not in SUPPORTED_EXTS:
            print(f"Skipping unsupported file: {input_path}")
            return 0
        out_path = make_output_path(input_path, output_dir)
        if (not overwrite) and os.path.exists(out_path):
            print(f"Skipping (exists): {out_path}")
            return 0
        run_conversion(input_path, out_path, mode, threshold, simplify, invert, blur, min_area)
        print(f"Converted: {input_path} -> {out_path}")
        return 1

    # Directory processing
    count = 0
    for root, _, files in os.walk(input_path):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in SUPPORTED_EXTS:
                continue
            src = os.path.join(root, fname)
            out_path = make_output_path(src, output_dir)
            if (not overwrite) and os.path.exists(out_path):
                print(f"Skipping (exists): {out_path}")
                continue
            run_conversion(src, out_path, mode, threshold, simplify, invert, blur, min_area)
            print(f"Converted: {src} -> {out_path}")
            count += 1
    return count


def run_conversion(
    src: str,
    dst: str,
    mode: str,
    threshold: str | int,
    simplify: float,
    invert: bool,
    blur: int = 0,
    min_area: float = 10.0
) -> None:
    chosen_mode = mode.lower()
    if chosen_mode == 'auto':
        chosen_mode = 'trace' if _CV2_AVAILABLE else 'embed'
    if chosen_mode == 'embed':
        image_to_svg_embed(src, dst)
    elif chosen_mode == 'trace':
        image_to_svg_trace(src, dst, threshold=threshold, simplify=simplify, invert=invert, blur=blur, min_area=min_area)
    else:
        raise ValueError("Invalid mode. Use one of: auto, embed, trace")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Convert images (PNG/JPG/WEBP/etc.) to SVG. Default embeds the raster; optional trace mode vectorizes (monochrome).')
    parser.add_argument('--input', required=True, help='Input file or directory')
    parser.add_argument('--output-dir', default=None, help='Output directory (defaults to alongside source files)')
    parser.add_argument('--mode', choices=['auto', 'embed', 'trace'], default='auto', help='Conversion mode: auto (trace if OpenCV present, else embed), embed (base64 image), trace (vector contours)')
    parser.add_argument('--threshold', default='auto', help='Threshold for trace: integer [0-255] or "auto" (Otsu)')
    parser.add_argument('--simplify', type=float, default=2.0, help='Polygon simplification epsilon for trace (pixels). Use 0 to disable.')
    parser.add_argument('--invert', action='store_true', help='Invert the thresholded bitmap before tracing')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing .svg files')
    parser.add_argument('--blur', type=int, default=0, help='Gaussian blur kernel size (odd integer). Use 0 to disable.')
    parser.add_argument('--min-area', type=float, default=10.0, help='Minimum contour area (pixels) to include. Default is 10.0.')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    in_path = os.path.expandvars(os.path.expanduser(args.input))
    out_dir = os.path.expandvars(os.path.expanduser(args.output_dir)) if args.output_dir else None

    if not os.path.exists(in_path):
        print(f"Error: input path not found: {in_path}")
        return 1

    try:
        cnt = process_path(
            in_path,
            out_dir,
            args.mode,
            args.threshold,
            args.simplify,
            args.invert,
            args.overwrite,
            args.blur,
            args.min_area
        )
        print(f"Done. Created {cnt} SVG file(s).")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 2


if __name__ == '__main__':
    sys.exit(main())
