#!/usr/bin/env python3
"""Run a simple WDS route availability check against a base URL."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


TOOL = "wds-route-check"
VERSION = "0.1.0"


@dataclass
class RouteResult:
    route: str
    url: str
    status_code: int | None
    ok: bool
    error: str = ""


def check_url(url: str, timeout: float) -> tuple[int | None, str]:
    request = Request(url, headers={"User-Agent": f"{TOOL}/{VERSION}"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.status, ""
    except HTTPError as exc:
        return exc.code, str(exc)
    except URLError as exc:
        return None, str(exc.reason)
    except Exception as exc:
        return None, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_url")
    parser.add_argument("routes", nargs="+")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results: list[RouteResult] = []
    for route in args.routes:
        url = urljoin(args.base_url.rstrip("/") + "/", route.lstrip("/"))
        status, error = check_url(url, args.timeout)
        results.append(RouteResult(route, url, status, status is not None and 200 <= status < 400, error))
    failed = [result for result in results if not result.ok]
    if args.json:
        print(json.dumps({"status": "ok" if not failed else "error", "tool": TOOL, "version": VERSION, "data": {"routes": [asdict(result) for result in results]}, "errors": [], "warnings": []}, indent=2))
    else:
        for result in results:
            label = "OK" if result.ok else "FAIL"
            detail = result.status_code if result.status_code is not None else result.error
            print(f"{label} {result.route} {detail}")
    return 0 if not failed else 4


if __name__ == "__main__":
    raise SystemExit(main())
