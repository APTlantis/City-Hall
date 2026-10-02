import importlib
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))
validator = importlib.import_module("Validate-SESM-Safe")


class TestValidateSesmSafe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parent.parent
        cls.schema = cls.root / "svg_asset.schema.json"

    def validate(self, rel_path):
        return validator.validate_file(self.root / rel_path, self.schema, True)

    def test_valid_basic_safe_fixture(self):
        result = self.validate("fixtures/valid/basic-safe.svg")
        self.assertEqual(result.status, "ok")
        self.assertEqual(result.profile, "sesm-safe")
        self.assertEqual(result.metadata_version, "0.3.0")

    def test_valid_full_metadata_fixture(self):
        result = self.validate("fixtures/valid/full-metadata.svg")
        self.assertEqual(result.status, "ok")
        self.assertEqual(result.profile, "sesm-safe")

    def test_rejects_script(self):
        result = self.validate("fixtures/invalid/script.svg")
        self.assertEqual(result.status, "error")
        self.assertTrue(any(error.code == "svg-script" for error in result.errors))

    def test_rejects_event_handler(self):
        result = self.validate("fixtures/invalid/event-handler.svg")
        self.assertEqual(result.status, "error")
        self.assertTrue(any(error.code == "svg-event-handler" for error in result.errors))

    def test_rejects_javascript_url(self):
        result = self.validate("fixtures/invalid/javascript-url.svg")
        self.assertEqual(result.status, "error")
        self.assertTrue(any(error.code == "javascript-url" for error in result.errors))

    def test_rejects_duplicate_metadata(self):
        result = self.validate("fixtures/invalid/duplicate-metadata.svg")
        self.assertEqual(result.status, "error")
        self.assertTrue(any(error.code == "sesm-duplicate" for error in result.errors))

    def test_rejects_bad_json(self):
        result = self.validate("fixtures/invalid/bad-json.svg")
        self.assertEqual(result.status, "error")
        self.assertTrue(any(error.code == "sesm-json-invalid" for error in result.errors))

    def test_warns_on_remote_reference(self):
        result = self.validate("fixtures/warning/remote-reference.svg")
        self.assertEqual(result.status, "warning")
        self.assertEqual(result.profile, "sesm-unverified")
        self.assertTrue(any(warning.code == "remote-reference" for warning in result.warnings))


if __name__ == "__main__":
    unittest.main()
