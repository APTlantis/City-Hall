"""Check prospective maturity-promotion evidence; never change maturity automatically."""
import argparse
from datetime import date
import json
from pathlib import Path
import tomllib
from sfds_validate import validate_suite


def review(suite, record):
    errors = list(validate_suite(suite)['errors'])
    try:
        data = tomllib.loads(record.read_text(encoding='utf-8'))
        manifest = tomllib.loads((suite / f'{suite.name}.manifest.toml').read_text(encoding='utf-8'))
        if data.get('version') != manifest['standard']['version']:
            errors.append('review version must match the suite version')
        if data.get('target') not in ('stable', 'reference'):
            errors.append('target must be stable or reference')
        if not data.get('reviewer') or data.get('approved') is not True:
            errors.append('named reviewer approval is required')
        date.fromisoformat(data.get('date', ''))
        adopters = data.get('adopters', [])
        identities = set()
        for adopter in adopters:
            identity = adopter.get('project', '')
            if not identity or identity in identities:
                errors.append('adopters must have distinct project identities')
            identities.add(identity)
            if adopter.get('production') is not True or adopter.get('teaching') is not False:
                errors.append(f'{identity}: non-teaching production adoption required')
            for key in ('adoption_record', 'runtime_log', 'schema_log'):
                path = (record.parent / adopter.get(key, '')).resolve()
                if not path.is_file() or path.stat().st_size == 0:
                    errors.append(f'{identity}: nonempty {key} required')
            if adopter.get('schema_errors') != 0 or isinstance(adopter.get('schema_errors'), bool):
                errors.append(f'{identity}: schema_errors must be zero')
            if adopter.get('runtime_result') != 'pass':
                errors.append(f'{identity}: runtime_result must be pass')
            date.fromisoformat(adopter.get('date', ''))
        if len(identities) < 2:
            errors.append('two independent non-teaching production adopters required')
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f'invalid promotion record: {exc}')
    return {'status': 'error' if errors else 'ok', 'errors': errors,
            'boundary': 'Checks recorded claims and files. Reviewer must verify independence, schema results and runtime semantics. No automatic promotion.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('suite', type=Path)
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    result = review(args.suite, args.record)
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result['errors'] else 0)
