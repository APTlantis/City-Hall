"""Emit SESM metadata only after schema and safe-profile validation succeed."""
import argparse
import importlib
import json
from pathlib import Path
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
validator = importlib.import_module('Validate-SESM-Safe')


def ingest(path):
    try:
        import jsonschema
    except ImportError as exc:
        raise ValueError('full JSON Schema validation unavailable; install SESM/requirements-ingestion.txt') from exc
    # Validate and extract the same bytes, avoiding a validate/reopen race.
    raw = path.read_bytes()
    with tempfile.TemporaryDirectory() as temp:
        snapshot = Path(temp) / 'input.svg'
        snapshot.write_bytes(raw)
        result = validator.validate_file(snapshot, ROOT / 'svg_asset.schema.json', True)
    if result.profile != 'sesm-safe' or result.status != 'ok':
        raise ValueError(f'ingestion rejected: {result.profile}; {result.errors}; {result.warnings}')
    xml = ET.fromstring(raw)
    metadata = next(e for e in xml.iter() if e.tag.split('}')[-1] == 'metadata' and e.get('id') == 'sesm')
    return json.loads(metadata.text or '')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('svg', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps({'status': 'ok', 'data': ingest(args.svg)}, indent=2))
    except (OSError, ValueError, ET.ParseError) as exc:
        print(json.dumps({'status': 'error', 'error': str(exc)}))
        raise SystemExit(4)
