#!/usr/bin/env python3
"""Inventory and safe-copy migration workflow from ARMOR V7.2 to Minimal Stable."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path


DEFAULT_REPORT_FILES = {
    "inventory": "inventory.json",
    "moves": "proposed-moves.csv",
    "conflicts": "conflicts.csv",
    "unresolved": "unresolved.csv",
    "ignored": "ignored.csv",
    "summary": "summary.md",
    "metadata": "metadata-cleanup.csv",
    "links": "link-audit.csv",
    "copied": "copied-files.csv",
}

LEGACY_METADATA_FIELDS = (
    "memory_layer",
    "permission_class",
    "write_policy",
    "retrieval_scope",
    "freshness_class",
    "proposal_type",
    "review_owner",
    "author_agent",
    "confidence",
)

DEPENDENCY_PATH_MARKERS = (
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

AUTO_MAP_PREFIXES = {
    "01-Facts": Path("01-Knowledge"),
    "02-Rules": Path("01-Knowledge/Rules"),
    "03-Insights": Path("01-Knowledge/Insights"),
    "04-Research": Path("04-Research"),
    "05-Projects": Path("02-Projects"),
    "06-Records": Path("03-Records"),
    "99-Archive": Path("99-Archive/V7.2"),
}

ARCHIVE_ONLY_PREFIXES = {"00-Core", "70-Schemas", "92-Logs"}
IGNORE_PREFIXES = {"80-Indexes", "81-Dashboards"}
REVIEW_PREFIXES = {"90-Drafts", "91-Inbox", "93-Proposals", "94-Review-Queues"}
MARKDOWN_EXTENSIONS = {".md", ".markdown"}


@dataclass
class FileRecord:
    source_rel: str
    source_abs: str
    size: int
    sha256: str
    status: str
    reason: str
    target_rel: str | None = None
    file_type: str = "file"
    metadata_fields: list[str] = field(default_factory=list)
    legacy_references: list[str] = field(default_factory=list)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_safe_paths(source: Path, target: Path) -> None:
    if not source.exists():
        raise ValueError(f"source path does not exist: {source}")
    if not source.is_dir():
        raise ValueError(f"source path is not a directory: {source}")

    source_real = source.resolve()
    target_real = target.resolve(strict=False)

    if source_real == target_real:
        raise ValueError("source and target must be different directories")
    if is_relative_to(target_real, source_real):
        raise ValueError("target must not be inside source")
    if is_relative_to(source_real, target_real):
        raise ValueError("source must not be inside target")


def is_relative_to(path: Path, base: Path) -> bool:
    try:
        path.relative_to(base)
        return True
    except ValueError:
        return False


def parse_frontmatter_legacy_fields(path: Path) -> list[str]:
    if path.suffix.lower() not in MARKDOWN_EXTENSIONS:
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---", 4)
    if end == -1:
        return []
    frontmatter = text[4:end].splitlines()
    found: list[str] = []
    for line in frontmatter:
        if ":" not in line:
            continue
        key = line.split(":", 1)[0].strip()
        if key in LEGACY_METADATA_FIELDS:
            found.append(key)
    return found


def extract_legacy_links(path: Path) -> list[str]:
    if path.suffix.lower() not in MARKDOWN_EXTENSIONS:
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    found: list[str] = []
    for marker in DEPENDENCY_PATH_MARKERS:
        if marker in text:
            found.append(marker)
    return sorted(set(found))


def determine_route(source_rel: Path) -> tuple[str, str, Path | None]:
    top = source_rel.parts[0]

    if top in AUTO_MAP_PREFIXES:
        target_base = AUTO_MAP_PREFIXES[top]
        remainder = Path(*source_rel.parts[1:]) if len(source_rel.parts) > 1 else Path()
        return ("proposed", "deterministic mapping", target_base / remainder)

    if top in REVIEW_PREFIXES:
        return ("unresolved", f"{top} requires individual review", None)

    if top in ARCHIVE_ONLY_PREFIXES:
        return ("ignored", f"{top} is archive-only in first-pass migration", None)

    if top in IGNORE_PREFIXES:
        return ("ignored", f"{top} is excluded from default migration", None)

    return ("ignored", "top-level folder is outside the default mapping", None)


def iter_source_files(source: Path) -> list[Path]:
    results: list[Path] = []
    for path in source.rglob("*"):
        if path.is_dir():
            continue
        results.append(path)
    return sorted(results)


def build_inventory(source: Path) -> tuple[list[FileRecord], dict[str, int]]:
    records: list[FileRecord] = []
    stats = {
        "proposed": 0,
        "unresolved": 0,
        "ignored": 0,
        "conflicts": 0,
        "copied": 0,
        "resumed": 0,
    }

    for path in iter_source_files(source):
        rel = path.relative_to(source)

        if any(part.startswith(".") for part in rel.parts):
            records.append(
                FileRecord(
                    source_rel=rel.as_posix(),
                    source_abs=str(path),
                    size=path.stat().st_size,
                    sha256=sha256_file(path),
                    status="ignored",
                    reason="hidden path is excluded from first-pass migration",
                    file_type="hidden",
                )
            )
            stats["ignored"] += 1
            continue

        if path.is_symlink():
            records.append(
                FileRecord(
                    source_rel=rel.as_posix(),
                    source_abs=str(path),
                    size=0,
                    sha256="",
                    status="ignored",
                    reason="symlink is excluded from first-pass migration",
                    file_type="symlink",
                )
            )
            stats["ignored"] += 1
            continue

        status, reason, target_rel = determine_route(rel)
        metadata_fields = parse_frontmatter_legacy_fields(path)
        legacy_refs = extract_legacy_links(path)
        record = FileRecord(
            source_rel=rel.as_posix(),
            source_abs=str(path),
            size=path.stat().st_size,
            sha256=sha256_file(path),
            status=status,
            reason=reason,
            target_rel=target_rel.as_posix() if target_rel else None,
            metadata_fields=metadata_fields,
            legacy_references=legacy_refs,
        )
        records.append(record)
        stats[status] += 1

    return records, stats


def load_resume_manifest(report_dir: Path) -> dict[str, dict[str, str]]:
    manifest_path = report_dir / DEFAULT_REPORT_FILES["copied"]
    if not manifest_path.exists():
        return {}
    with manifest_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {row["source_rel"]: row for row in reader}


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_reports(report_dir: Path, records: list[FileRecord], stats: dict[str, int], source: Path, target: Path) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)

    inventory_rows = []
    proposed_rows = []
    conflict_rows = []
    unresolved_rows = []
    ignored_rows = []
    metadata_rows = []
    link_rows = []

    for record in records:
        inventory_rows.append(
            {
                "source_rel": record.source_rel,
                "source_abs": record.source_abs,
                "size": record.size,
                "sha256": record.sha256,
                "status": record.status,
                "reason": record.reason,
                "target_rel": record.target_rel,
                "file_type": record.file_type,
                "metadata_fields": record.metadata_fields,
                "legacy_references": record.legacy_references,
            }
        )
        row = {
            "source_rel": record.source_rel,
            "target_rel": record.target_rel or "",
            "reason": record.reason,
            "sha256": record.sha256,
        }
        if record.status == "proposed":
            proposed_rows.append(row)
        elif record.status == "conflict":
            conflict_rows.append(row)
        elif record.status == "unresolved":
            unresolved_rows.append(row)
        elif record.status == "ignored":
            ignored_rows.append(row)

        for field_name in record.metadata_fields:
            metadata_rows.append({"source_rel": record.source_rel, "field_name": field_name})
        for marker in record.legacy_references:
            link_rows.append({"source_rel": record.source_rel, "legacy_reference": marker})

    (report_dir / DEFAULT_REPORT_FILES["inventory"]).write_text(
        json.dumps(
            {
                "source": str(source),
                "target": str(target),
                "stats": stats,
                "files": inventory_rows,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    write_csv(report_dir / DEFAULT_REPORT_FILES["moves"], ["source_rel", "target_rel", "reason", "sha256"], proposed_rows)
    write_csv(report_dir / DEFAULT_REPORT_FILES["conflicts"], ["source_rel", "target_rel", "reason", "sha256"], conflict_rows)
    write_csv(report_dir / DEFAULT_REPORT_FILES["unresolved"], ["source_rel", "target_rel", "reason", "sha256"], unresolved_rows)
    write_csv(report_dir / DEFAULT_REPORT_FILES["ignored"], ["source_rel", "target_rel", "reason", "sha256"], ignored_rows)
    write_csv(report_dir / DEFAULT_REPORT_FILES["metadata"], ["source_rel", "field_name"], metadata_rows)
    write_csv(report_dir / DEFAULT_REPORT_FILES["links"], ["source_rel", "legacy_reference"], link_rows)

    summary = "\n".join(
        [
            "# Migration Summary",
            "",
            f"- Source: `{source}`",
            f"- Target: `{target}`",
            f"- Proposed files: `{stats['proposed']}`",
            f"- Unresolved files: `{stats['unresolved']}`",
            f"- Ignored files: `{stats['ignored']}`",
            f"- Conflicts: `{stats['conflicts']}`",
            f"- Copied: `{stats['copied']}`",
            f"- Resumed: `{stats['resumed']}`",
        ]
    )
    (report_dir / DEFAULT_REPORT_FILES["summary"]).write_text(summary + "\n", encoding="utf-8")


def append_copy_rows(report_dir: Path, rows: list[dict[str, str]]) -> None:
    path = report_dir / DEFAULT_REPORT_FILES["copied"]
    file_exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["source_rel", "target_rel", "source_sha256", "target_sha256", "status"],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)


def apply_copy(
    source: Path,
    target: Path,
    report_dir: Path,
    records: list[FileRecord],
    stats: dict[str, int],
) -> None:
    resume_manifest = load_resume_manifest(report_dir)
    copy_rows: list[dict[str, str]] = []

    for record in records:
        if record.status != "proposed" or not record.target_rel:
            continue

        source_path = source / record.source_rel
        target_path = target / record.target_rel
        target_path.parent.mkdir(parents=True, exist_ok=True)

        existing_resume = resume_manifest.get(record.source_rel)
        if existing_resume:
            if target_path.exists() and sha256_file(target_path) == record.sha256:
                stats["resumed"] += 1
                continue

        if target_path.exists():
            record.status = "conflict"
            record.reason = "target already exists"
            stats["proposed"] -= 1
            stats["conflicts"] += 1
            continue

        before_hash = sha256_file(source_path)
        shutil.copy2(source_path, target_path)
        after_hash = sha256_file(target_path)
        if before_hash != after_hash:
            raise RuntimeError(f"hash mismatch after copying {record.source_rel}")

        copy_rows.append(
            {
                "source_rel": record.source_rel,
                "target_rel": record.target_rel,
                "source_sha256": before_hash,
                "target_sha256": after_hash,
                "status": "copied",
            }
        )
        stats["copied"] += 1

    if copy_rows:
        append_copy_rows(report_dir, copy_rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inventory and migrate an ARMOR V7.2 vault to Minimal Stable.")
    parser.add_argument("--source", required=True, help="Path to the V7.2 vault")
    parser.add_argument("--target", required=True, help="Path to the Minimal Stable vault")
    parser.add_argument("--report-dir", required=True, help="Directory for dry-run and apply reports")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Generate reports without writing to either vault")
    mode.add_argument("--apply", action="store_true", help="Copy files according to deterministic mappings")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    source = Path(args.source).expanduser()
    target = Path(args.target).expanduser()
    report_dir = Path(args.report_dir).expanduser()

    try:
        ensure_safe_paths(source, target)
    except ValueError as exc:
        parser.error(str(exc))

    records, stats = build_inventory(source)
    write_reports(report_dir, records, stats, source, target)

    if args.apply:
        target.mkdir(parents=True, exist_ok=True)
        apply_copy(source, target, report_dir, records, stats)
        write_reports(report_dir, records, stats, source, target)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
