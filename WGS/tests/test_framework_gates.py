import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'DRS/tools'))
sys.path.insert(0, str(ROOT / 'SFDS/tools'))
sys.path.insert(0, str(ROOT / 'WGS/tools'))
from drs_integrity_check import validate
from release_evidence import check_evidence, STAGES
from promotion_review import review
from city_hall_audit import audit_catalog
sys.path.insert(0, str(ROOT / 'AAS/tools'))
sys.path.insert(0, str(ROOT / 'WDS/tools'))
from evaluate_suite_snapshot import evaluate
import deployment_gate


class Gates(unittest.TestCase):
    def test_evaluation_requires_nonzero_denominator(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                evaluate(Path(temp))
        result = evaluate(ROOT)
        self.assertTrue(result['run_performed'])
        self.assertEqual(result['denominator'], 16)
        self.assertEqual(len(result['observed_findings']), 16)

    def test_deployment_checks_http_and_html(self):
        with patch.object(deployment_gate, 'check_url', return_value=(200, '')), patch.object(deployment_gate, 'read_source', return_value='<html lang="en"><title>Test</title><meta name="description" content="Test"></html>'):
            self.assertEqual(deployment_gate.check('https://example.invalid', ['/'], 1)['result'], 'pass')
        with patch.object(deployment_gate, 'check_url', return_value=(404, 'missing')):
            self.assertEqual(deployment_gate.check('https://example.invalid', ['/'], 1)['result'], 'fail')
        with patch.object(deployment_gate, 'check_url', return_value=(200, '')), patch.object(deployment_gate, 'read_source', return_value='<img src="test">'):
            self.assertEqual(deployment_gate.check('https://example.invalid', ['/'], 1)['result'], 'fail')
        with self.assertRaises(ValueError):
            deployment_gate.check('https://example.invalid', [], 1)

    def test_powershell_check_release_blocks_pending(self):
        import shutil
        shell = shutil.which('pwsh')
        if not shell:
            self.skipTest('PowerShell unavailable')
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'Test.manifest.toml').write_bytes((ROOT / 'DRS/templates/ProjectName.manifest.toml').read_bytes())
            result = subprocess.run([shell, '-NoProfile', '-File', str(ROOT / 'DRS/drs.ps1'), 'check-release', '-PythonExecutable', sys.executable], cwd=root, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Release-stage evidence failed', result.stdout)

    def test_pending_and_missing_stage_records_block(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertTrue(check_evidence(root, {}))
            record = root / 'evidence.toml'
            record.write_bytes((ROOT / 'DRS/templates/Release-Stage-Evidence.toml').read_bytes())
            manifest = {'release': {'version': 'REPLACE', 'installer': {'sha256': 'REPLACE'}, 'verified': {'stage_evidence': record.name}}}
            errors = check_evidence(root, manifest)
            self.assertTrue(all(any(name in e for e in errors) for name in STAGES))

    def test_complete_stage_record_and_mutated_artifact(self):
        import hashlib
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'app.bin').write_bytes(b'test artifact')
            digest = hashlib.sha256(b'test artifact').hexdigest()
            (root / 'observed.log').write_text('Synthetic regression evidence; not production proof.')
            text = f'version = "1.0.0"\nartifact_sha256 = "{digest}"\n'
            for stage in STAGES:
                text += f'[stages.{stage}]\nstatus = "pass"\ndate = "2026-10-02"\nlog = "observed.log"\n'
            (root / 'evidence.toml').write_text(text)
            manifest = root / 'Test.manifest.toml'
            manifest.write_text(f'[release]\nversion = "1.0.0"\n[release.installer]\npath = "app.bin"\nsha256 = "{digest}"\nsigning = "unsigned"\n[release.verified]\nstage_evidence = "evidence.toml"\n')
            self.assertEqual(validate(manifest, root, True)['errors'], [])
            (root / 'app.bin').write_bytes(b'mutated')
            self.assertTrue(validate(manifest, root, True)['errors'])
            (root / 'observed.log').unlink()
            self.assertTrue(validate(manifest, root, True)['errors'])

    def test_missing_promotion_and_teaching_adopters_block(self):
        self.assertTrue(review(ROOT / 'CTS', ROOT / 'SFDS/templates/Promotion-Review.toml')['errors'])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'log').write_text('Synthetic regression fixture')
            record = root / 'review.toml'
            text = 'version = "0.2.1"\ntarget = "stable"\ndate = "2026-10-02"\nreviewer = "Fixture"\napproved = true\n'
            for project in ('One', 'Two'):
                text += f'[[adopters]]\nproject = "{project}"\nproduction = true\nteaching = false\ndate = "2026-10-02"\nadoption_record = "log"\nschema_log = "log"\nschema_errors = 0\nruntime_log = "log"\nruntime_result = "pass"\n'
            record.write_text(text)
            self.assertEqual(review(ROOT / 'CTS', record)['errors'], [])
            record.write_text(text.replace('teaching = false', 'teaching = true'))
            self.assertTrue(review(ROOT / 'CTS', record)['errors'])

    def test_catalog_drift_is_not_a_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'catalog.json'
            data = json.loads((ROOT / 'WGS/catalog/city-hall.json').read_text())
            self.assertEqual(audit_catalog(ROOT, ROOT / 'WGS/catalog/city-hall.json'), [])
            data['components'][0]['version'] = 'stale'
            path.write_text(json.dumps(data))
            self.assertTrue(audit_catalog(ROOT, path))
            path.write_text('{')
            self.assertTrue(audit_catalog(ROOT, path))

    def test_ingestion_rejects_unsafe_vectors_before_metadata_output(self):
        helper = ROOT / 'SESM/tools/ingest_sesm.py'
        for name in ('script.svg', 'event-handler.svg', 'javascript-url.svg', 'bad-json.svg'):
            result = subprocess.run([sys.executable, '-B', str(helper), str(ROOT / 'SESM/fixtures/invalid' / name)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 4, result.stderr)
            self.assertNotIn('data', json.loads(result.stdout))
        result = subprocess.run([sys.executable, '-B', str(helper), str(ROOT / 'SESM/fixtures/valid/basic-safe.svg')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('data', json.loads(result.stdout))

    def test_ingestion_fails_closed_without_schema_engine(self):
        # Isolated bundled runtime deliberately cannot see the temporary test dependencies.
        result = subprocess.run([sys.executable, '-I', '-B', str(ROOT / 'SESM/tools/ingest_sesm.py'), str(ROOT / 'SESM/fixtures/valid/basic-safe.svg')], capture_output=True, text=True)
        if result.returncode == 0:
            self.skipTest('schema engine already installed in isolated runtime')
        self.assertEqual(result.returncode, 4)
        self.assertIn('full JSON Schema validation unavailable', result.stdout)
        self.assertNotIn('data', json.loads(result.stdout))


if __name__ == '__main__':
    unittest.main()
