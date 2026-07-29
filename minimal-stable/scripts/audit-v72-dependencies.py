#!/usr/bin/env python3
"""Scan likely agent and config files for ARMOR V7.2 references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


LIKELY_FILE_NAMES = {"AGENTS.md", "CLAUDE.md", "HERMES.md", "SOUL.md", "MEMORY.md"}
LIKELY_SUFFIXES = {".yaml", ".yml", ".json", ".toml", ".md", ".sh", ".py"}
DEPENDENCY_MARKERS = (
    "enterprise/",
    "00-Core",
    "01-Facts",
    "02-Rules",
    "03-Insights",
    "05-Projects",
    "06-Records",
    "90-Drafts",
    "93-Proposals",
    "94-Review-Queues",
)


def scan_paths(root_paths: list[Path]) -> dict[str, object]:
    results: list[dict[str, object]] = []
    scanned_files = 0

    for root in root_paths:
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if path.name not in LIKELY_FILE_NAMES and path.suffix.lower() not in LIKELY_SUFFIXES:
                continue
            scanned_files += 1
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            matches = [marker for marker in DEPENDENCY_MARKERS if marker in text]
            if matches:
                results.append(
                    {
                        "path": str(path),
                        "matches": sorted(set(matches)),
                    }
                )

    return {
        "scanned_roots": [str(path) for path in root_paths],
        "scanned_files": scanned_files,
        "matches": results,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit local files for ARMOR V7.2 dependency references.")
    parser.add_argument("--scan-dir", action="append", required=True, help="Directory to scan; may be used multiple times")
    parser.add_argument("--output", help="Optional output JSON path")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    roots = [Path(entry).expanduser() for entry in args.scan_dir]
    for root in roots:
        if not root.exists():
            parser.error(f"scan directory does not exist: {root}")
        if not root.is_dir():
            parser.error(f"scan directory is not a directory: {root}")

    report = scan_paths(roots)
    payload = json.dumps(report, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).expanduser().write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
