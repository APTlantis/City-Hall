"""Execute a bounded suite evaluation and preserve its inputs, denominator and findings."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'SFDS/tools'))
from sfds_validate import discover_suites, validate_suite


def evaluate(root):
    targets = discover_suites(root)
    if not targets:
        raise ValueError('no governed suites; denominator would be zero')
    inputs = []
    for suite in targets:
        manifest = suite / f'{suite.name}.manifest.toml'
        inputs.append({'path': str(manifest.relative_to(root)), 'sha256': hashlib.sha256(manifest.read_bytes()).hexdigest()})
    results = [validate_suite(suite) for suite in targets]
    return {'executed_at': datetime.now(timezone.utc).isoformat(), 'run_performed': True,
            'scope': 'registered suite structure; not adopter or application runtime conformance',
            'inputs': inputs, 'denominator': len(targets),
            'passed': sum(not result['errors'] for result in results),
            'observed_findings': [{'suite': result['suite'], 'errors': result['errors'], 'warnings': result['warnings']} for result in results],
            'result': 'fail' if any(result['errors'] for result in results) else 'pass'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = evaluate(args.root.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Named evidence is never silently overwritten.
    with args.output.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps({'result': result['result'], 'denominator': result['denominator'], 'passed': result['passed']}))
    raise SystemExit(1 if result['result'] == 'fail' else 0)
