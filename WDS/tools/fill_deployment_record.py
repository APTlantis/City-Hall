#!/usr/bin/env python3
"""Fill a WDS deployment record from simple CI metadata."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


TEMPLATE = """# Deployment Record

## Site

- Site: {site}
- Environment: {environment}
- URL: {url}
- Commit: {commit}
- Build artifact: {artifact}
- Generated at: {generated_at}

## Validation

- Manifest validation: {manifest_validation}
- Route check: {route_check}
- Accessibility smoke check: {accessibility_check}

## Rollback

{rollback}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", required=True)
    parser.add_argument("--environment", default="preview")
    parser.add_argument("--url", default="")
    parser.add_argument("--commit", default="")
    parser.add_argument("--artifact", default="")
    parser.add_argument("--manifest-validation", default="not recorded")
    parser.add_argument("--route-check", default="not recorded")
    parser.add_argument("--accessibility-check", default="not recorded")
    parser.add_argument("--rollback", default="Redeploy the previous known-good build.")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    text = TEMPLATE.format(**vars(args), generated_at=generated_at)
    Path(args.output).write_text(text, encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
