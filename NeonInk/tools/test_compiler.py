"""Behavioral tests for conversion, validation and read-only freshness."""
import copy
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from compile_neonink import ROOT, compile_source, contrast, oklch, to_linear_srgb


class CompilerTests(unittest.TestCase):
    def test_known_colors(self):
        for value, expected in [('#000000',(0,0,0)),('#FFFFFF',(1,0,0)),('#FF0000',(0.627955,0.257683,29.233885))]:
            actual=oklch(value)
            for a,b in zip(actual,expected):self.assertAlmostEqual(a,b,places=5)
        self.assertEqual(contrast('#000000','#FFFFFF'),21)

    def test_reverse_conversion(self):
        for value in ['#22D3EE','#F43F5E','#050816','#FFFFFF','#818CF8']:
            channels=to_linear_srgb(oklch(value))
            encoded=[12.92*x if x<=0.0031308 else 1.055*x**(1/2.4)-0.055 for x in channels]
            reconstructed='#'+''.join(f'{round(v*255):02X}' for v in encoded)
            self.assertEqual(value,reconstructed)

    def mutated(self, old, new):
        with tempfile.TemporaryDirectory() as directory:
            source=Path(directory)/'tokens.toml'
            content=(ROOT/'spec/tokens/NeonInk.Tokens.toml').read_text()
            self.assertIn(old,content)
            source.write_text(content.replace(old,new,1))
            with self.assertRaises((ValueError,KeyError)):
                compile_source(source)

    def test_bad_reference(self):
        self.mutated('canvas = "background-void"','canvas = "missing"')

    def test_color_disagreement(self):
        self.mutated('hex = "#050816"','hex = "#FFFFFF"')

    def test_contrast_regression(self):
        self.mutated('text = "text-primary"','text = "background-void"')

    def test_scale_order(self):
        self.mutated('["seq-1", "seq-2", "seq-3", "seq-4", "seq-5"]','["seq-5", "seq-2", "seq-3", "seq-4", "seq-1"]')

    def test_freshness_never_repairs(self):
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)/'missing'
            command=[sys.executable,str(ROOT/'tools/compile_neonink.py'),'--output',str(output)]
            self.assertNotEqual(subprocess.run(command+['--check'],capture_output=True).returncode,0)
            self.assertFalse(output.exists())
            self.assertEqual(subprocess.run(command,capture_output=True).returncode,0)
            self.assertEqual(subprocess.run(command+['--check'],capture_output=True).returncode,0)
            target=output/'NeonInk.Tokens.css';target.write_bytes(b'stale')
            self.assertNotEqual(subprocess.run(command+['--check'],capture_output=True).returncode,0)
            self.assertEqual(target.read_bytes(),b'stale')


if __name__=='__main__':unittest.main()
