"""Check a named deployed route inventory and preserve bounded smoke evidence."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.parse import urljoin
from route_check import check_url
from accessibility_smoke import read_source, check_html


def check(base_url, routes, timeout):
    if not routes or len(set(routes)) != len(routes):
        raise ValueError('nonempty unique route inventory required')
    results = []
    for route in routes:
        url = urljoin(base_url.rstrip('/') + '/', route.lstrip('/'))
        status, error = check_url(url, timeout)
        findings = []
        if status is not None and 200 <= status < 400:
            try:
                findings = [finding.__dict__ for finding in check_html(read_source(url, timeout))]
            except Exception as exc:
                error = str(exc)
        results.append({'route': route, 'url': url, 'status': status, 'error': error, 'html_findings': findings,
                        'ok': status is not None and 200 <= status < 400 and not error and not findings})
    return {'observed_at': datetime.now(timezone.utc).isoformat(), 'base_url': base_url,
            'denominator': len(results), 'routes': results,
            'result': 'pass' if all(r['ok'] for r in results) else 'fail',
            'boundary': 'HTTP and HTML smoke only; rendered focus, keyboard traversal, contrast, DNS/tunnel ownership and full accessibility require separate evidence.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base_url')
    parser.add_argument('routes', nargs='+')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timeout', type=float, default=10)
    args = parser.parse_args()
    result = check(args.base_url, args.routes, args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps({'result': result['result'], 'denominator': result['denominator']}))
    raise SystemExit(4 if result['result'] == 'fail' else 0)
