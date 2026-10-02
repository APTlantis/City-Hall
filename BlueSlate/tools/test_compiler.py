"""Behavioral regression checks for source validation and read-only freshness."""
import tempfile
import unittest
from pathlib import Path
from compile_blueslate import ROOT, compile_tokens, load_tokens, render


class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'tokens.toml'
        self.original = (ROOT/'spec/tokens/BlueSlate.Tokens.toml').read_text(encoding='utf-8')
        self.source.write_text(self.original, encoding='utf-8')
        self.output = self.root/'generated'

    def test_repeatable_and_read_only_check(self):
        compile_tokens(self.source, self.output)
        before = {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.output.iterdir()}
        compile_tokens(self.source, self.output, check=True)
        self.assertEqual(before, {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.output.iterdir()})
        self.assertEqual(render(load_tokens(self.source)), render(load_tokens(self.source)))

    def test_stale_target_fails_without_repairing(self):
        compile_tokens(self.source, self.output)
        for name in render(load_tokens(self.source)):
            with self.subTest(name=name):
                p = self.output/name
                original = p.read_bytes()
                p.write_bytes(original+b'corruption')
                with self.assertRaisesRegex(ValueError, 'stale'):
                    compile_tokens(self.source, self.output, check=True)
                self.assertEqual(p.read_bytes(), original+b'corruption')
                p.write_bytes(original)

    def test_missing_target_does_not_create_directory(self):
        with self.assertRaisesRegex(ValueError, 'Missing'):
            compile_tokens(self.source, self.output, check=True)
        self.assertFalse(self.output.exists())

    def test_unknown_and_cyclic_references(self):
        for value, message in [('{semantic.content.missing}', 'Unknown'), ('{semantic.content.primary}', 'Cyclic'), ('{framework.tailwind.primary}', 'canonical'), ('{semantic.surface}', 'table')]:
            with self.subTest(value=value):
                self.source.write_text(self.original.replace('primary = "{palette.off-white}"', f'primary = "{value}"'), encoding='utf-8')
                with self.assertRaisesRegex(ValueError, message):
                    compile_tokens(self.source, self.output)
                self.assertFalse(self.output.exists())

    def test_invalid_toml_and_theme_rejected(self):
        for content in [self.original+'\n[meta]\nversion = "9.0.0"', self.original.replace('dark-only', 'light'), self.original.replace('#050913', 'not-hex')]:
            self.source.write_text(content, encoding='utf-8')
            with self.assertRaises(ValueError):
                compile_tokens(self.source, self.output)
            self.assertFalse(self.output.exists())

    def test_custom_source_and_output(self):
        self.source.write_text(self.original.replace('#050913', '#050914').replace('version = "0.5.0"', 'version = "0.5.1"'), encoding='utf-8')
        compile_tokens(self.source, self.output)
        self.assertIn('#050914', (self.output/'BlueSlate.Tokens.css').read_text())
        self.assertIn('v0.5.1', (self.output/'BlueSlate.Tokens.css').read_text())
        # Conversion accuracy is independently checked by Test-ColorConversions.js.


if __name__ == '__main__':
    unittest.main()
