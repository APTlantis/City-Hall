#!/usr/bin/env python3
"""Back up root governance records inside the active WGS suite.

The snapshot is explicitly non-authoritative. Run without --apply to compare
hashes; --apply refreshes the controlled backup and its SHA-256 inventory.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from datetime import datetime, timezone
from pathlib import Path

try:
    import tomli_w
except ModuleNotFoundError:
    import toml_write


FILES = ("AGENTS.md", "Development.manifest.toml", "INDEX.md")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path("D:/"))
    parser.add_argument("--snapshot-root", type=Path, default=Path("D:/.city_hall/WGS/workspace-root-snapshot"))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    workspace = args.workspace_root.resolve()
    snapshot = args.snapshot_root.resolve()
    records = []
    changed = False
    for name in FILES:
        source = workspace / name
        target = snapshot / name
        if not source.is_file():
            raise SystemExit(f"Missing root governance file: {source}")
        source_hash = sha256(source)
        target_hash = sha256(target) if target.exists() else ""
        state = "current" if source_hash == target_hash else "refresh-needed"
        print(f"{name}: {state}")
        changed |= state != "current"
        records.append({"name": name, "source": str(source), "sha256": source_hash, "size_bytes": source.stat().st_size})
        if args.apply and state != "current":
            snapshot.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    if args.apply:
        metadata = {
            "snapshot": {
                "authoritative": False,
                "purpose": "Version-controlled recovery copy of D drive root governance records.",
                "source_root": str(workspace),
                "refreshed_utc": datetime.now(timezone.utc).isoformat(),
                "files": records,
            }
        }
        snapshot.mkdir(parents=True, exist_ok=True)
        if "tomli_w" in globals():
            rendered = tomli_w.dumps(metadata)
        else:
            rendered = toml_write.dumps(metadata)
        (snapshot / "SNAPSHOT.toml").write_bytes(rendered.encode("utf-8"))
        (snapshot / "README.md").write_text(
            "# Workspace Root Governance Snapshot\n\n"
            "This directory is a version-controlled recovery copy of `D:\\AGENTS.md`, "
            "`D:\\Development.manifest.toml`, and `D:\\INDEX.md`. The files at the drive root "
            "remain authoritative. Refresh this snapshot with `snapshot_root_governance.py --apply`; "
            "do not edit snapshot copies directly.\n",
            encoding="utf-8", newline="\n",
        )
    return 1 if changed and not args.apply else 0


if __name__ == "__main__":
    raise SystemExit(main())
