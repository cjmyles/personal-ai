#!/usr/bin/env python3
"""Explicit, preview-first sync of Codex global instructions; never commits."""
import argparse
import difflib
import os
from pathlib import Path
import shutil
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("direction", choices=("capture", "apply"))
    parser.add_argument("--write", action="store_true", help="Perform the previewed copy")
    parser.add_argument("--live", type=Path, help="Override live file (also useful for tests)")
    parser.add_argument("--tracked", type=Path, help="Override tracked file (also useful for tests)")
    args = parser.parse_args()
    live = args.live or Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "AGENTS.md"
    tracked = args.tracked or Path(__file__).resolve().parents[1] / "global" / "AGENTS.md"
    source, destination = (live, tracked) if args.direction == "capture" else (tracked, live)
    if not source.is_file():
        parser.error(f"Source does not exist: {source}")
    if destination.is_symlink():
        parser.error(f"Refusing to overwrite a symlink: {destination}")
    incoming = source.read_bytes()
    previous = destination.read_bytes() if destination.exists() else b""
    if destination.exists() and previous == incoming:
        print("Already synchronised.")
        return
    print("".join(difflib.unified_diff(
        previous.decode("utf-8").splitlines(keepends=True),
        incoming.decode("utf-8").splitlines(keepends=True),
        fromfile=str(destination), tofile=str(source))), end="")
    if not args.write:
        print("\nPreview only. Add --write to copy; no Git commit or push is automatic.")
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        backup_dir = Path(tempfile.mkdtemp(prefix="codex-instructions-backup-"))
        shutil.copy2(destination, backup_dir / "AGENTS.md")
        print(f"\nBackup: {backup_dir / 'AGENTS.md'}")
    shutil.copyfile(source, destination)
    if destination.read_bytes() != incoming:
        raise RuntimeError("Verification failed")
    print(f"Verified: {destination}")


if __name__ == "__main__":
    main()
