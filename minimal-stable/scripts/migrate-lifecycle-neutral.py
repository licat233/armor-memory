#!/usr/bin/env python3
"""One-time migration from lifecycle-named project paths to neutral paths.

This tool intentionally migrates only the deterministic project-root rename:

    02-Projects/Active/ -> 02-Projects/Projects/

Legacy 03-Records/Published content is preserved. Under older routing rules that
location may contain both true publication evidence and content that was merely
created for publication, so bulk-moving it would risk rewriting historical
meaning.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MigrationPlan:
    vault_root: Path
    source: Path
    destination: Path
    moves: tuple[tuple[Path, Path], ...]
    mode: str


def resolve_vault_root(explicit: str | None) -> Path:
    raw = explicit or os.environ.get("ARMOR_VAULT_ROOT")
    if not raw:
        raise ValueError("ARMOR_VAULT_ROOT is required unless --vault is provided")
    root = Path(raw).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"vault root does not exist or is not a directory: {root}")
    projects_root = root / "02-Projects"
    if not projects_root.is_dir():
        raise ValueError(f"projects directory not found: {projects_root}")
    return root


def build_plan(vault_root: Path) -> MigrationPlan:
    projects_root = vault_root / "02-Projects"
    source = projects_root / "Active"
    destination = projects_root / "Projects"

    if not source.exists():
        return MigrationPlan(vault_root, source, destination, (), "noop")
    if not source.is_dir():
        raise ValueError(f"expected directory but found non-directory: {source}")

    if not destination.exists():
        return MigrationPlan(vault_root, source, destination, ((source, destination),), "rename")
    if not destination.is_dir():
        raise ValueError(f"expected directory but found non-directory: {destination}")

    source_children = sorted(source.iterdir(), key=lambda path: path.name)
    collisions = [child.name for child in source_children if (destination / child.name).exists()]
    if collisions:
        joined = ", ".join(collisions)
        raise ValueError(f"migration collision in 02-Projects/Projects: {joined}")

    moves = tuple((child, destination / child.name) for child in source_children)
    return MigrationPlan(vault_root, source, destination, moves, "merge")


def print_plan(plan: MigrationPlan, apply: bool) -> None:
    action = "APPLY" if apply else "DRY-RUN"
    print(f"ARMOR lifecycle-neutral migration [{action}]")
    print(f"Vault: {plan.vault_root}")
    print("Scope: 02-Projects/Active -> 02-Projects/Projects")
    print("Preserved: 03-Records/Published (no bulk move)")

    if plan.mode == "noop":
        print("Result: no Active directory; nothing to migrate")
        return

    print(f"Mode: {plan.mode}")
    for source, destination in plan.moves:
        print(f"MOVE {source} -> {destination}")


def apply_plan(plan: MigrationPlan) -> None:
    if plan.mode == "noop":
        return

    if plan.mode == "rename":
        source, destination = plan.moves[0]
        source.rename(destination)
        return

    plan.destination.mkdir(parents=True, exist_ok=True)
    for source, destination in plan.moves:
        shutil.move(str(source), str(destination))

    try:
        plan.source.rmdir()
    except OSError as exc:
        raise RuntimeError(f"migration moved project entries but could not remove empty source directory: {plan.source}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Migrate ARMOR Vault project paths to lifecycle-neutral naming.")
    parser.add_argument("--vault", help="Vault root. Defaults to ARMOR_VAULT_ROOT.")
    parser.add_argument("--apply", action="store_true", help="Apply the migration. Without this flag, only show the plan.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        vault_root = resolve_vault_root(args.vault)
        plan = build_plan(vault_root)
        print_plan(plan, args.apply)
        if args.apply:
            apply_plan(plan)
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
