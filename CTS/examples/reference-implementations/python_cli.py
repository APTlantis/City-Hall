#!/usr/bin/env python3
"""Tiny CTS-style Python command example."""

from __future__ import annotations

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    payload = {
        "status": "ok",
        "tool": "python-cts-example",
        "version": "0.1.0",
        "data": {"greeting": "hello"},
        "warnings": [],
        "errors": [],
    }
    print(json.dumps(payload, indent=2) if args.json else "hello")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
