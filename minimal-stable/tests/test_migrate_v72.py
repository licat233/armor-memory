from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "migrate-v72.py"
SPEC = importlib.util.spec_from_file_location("migrate_v72", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def run_cli(*args: str) -> int:
    return MODULE.main.__wrapped__(*args)  # type: ignore[attr-defined]


def invoke(args: list[str]) -> int:
    old = sys.argv
    try:
        sys.argv = [str(SCRIPT_PATH), *args]
        return MODULE.main()
    finally:
        sys.argv = old


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def test_dry_run_performs_no_writes(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "01-Facts" / "Products" / "fact.md", "hello")

    assert invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"]) == 0
    assert not target.exists()
    assert (report / "inventory.json").exists()


def test_known_folder_mapping(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "01-Facts" / "Products" / "item.md", "hello")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    proposed = read_csv_rows(report / "proposed-moves.csv")
    assert proposed[0]["target_rel"] == "01-Knowledge/Products/item.md"


def test_drafts_remain_unresolved_when_ambiguous(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "90-Drafts" / "draft.md", "draft")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    unresolved = read_csv_rows(report / "unresolved.csv")
    assert unresolved[0]["source_rel"] == "90-Drafts/draft.md"


def test_existing_target_conflict(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "01-Facts" / "Products" / "item.md", "hello")
    write_text(target / "01-Knowledge" / "Products" / "item.md", "existing")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--apply"])
    conflicts = read_csv_rows(report / "conflicts.csv")
    assert conflicts[0]["source_rel"] == "01-Facts/Products/item.md"


def test_sha256_verification_and_copy_record(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "05-Projects" / "Alpha" / "plan.md", "content")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--apply"])
    copied = read_csv_rows(report / "copied-files.csv")
    assert copied[0]["source_sha256"] == copied[0]["target_sha256"]


def test_resume_behavior(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "05-Projects" / "Alpha" / "plan.md", "content")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--apply"])
    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--apply"])
    summary = (report / "summary.md").read_text(encoding="utf-8")
    assert "Resumed: `1`" in summary


def test_malformed_source_path(tmp_path: Path):
    source = tmp_path / "missing"
    target = tmp_path / "target"
    report = tmp_path / "report"
    with pytest.raises(SystemExit):
        invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])


def test_target_inside_source_rejection(tmp_path: Path):
    source = tmp_path / "source"
    target = source / "target"
    source.mkdir()
    with pytest.raises(SystemExit):
        invoke(["--source", str(source), "--target", str(target), "--report-dir", str(tmp_path / "report"), "--dry-run"])


def test_source_inside_target_rejection(tmp_path: Path):
    target = tmp_path / "target"
    source = target / "source"
    source.mkdir(parents=True)
    with pytest.raises(SystemExit):
        invoke(["--source", str(source), "--target", str(target), "--report-dir", str(tmp_path / "report"), "--dry-run"])


def test_symlink_handling(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "01-Facts" / "Products" / "real.md", "hello")
    os_target = source / "01-Facts" / "Products" / "real.md"
    (source / "01-Facts" / "Products" / "link.md").symlink_to(os_target)

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    ignored = read_csv_rows(report / "ignored.csv")
    assert any(row["source_rel"].endswith("link.md") for row in ignored)


def test_hidden_files_are_ignored(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / ".hidden.md", "hidden")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    ignored = read_csv_rows(report / "ignored.csv")
    assert ignored[0]["source_rel"] == ".hidden.md"


def test_markdown_link_extraction(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "05-Projects" / "Alpha" / "plan.md", "See [[01-Facts/Product]] and 02-Rules/SEO")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    links = read_csv_rows(report / "link-audit.csv")
    markers = {row["legacy_reference"] for row in links}
    assert "01-Facts" in markers
    assert "02-Rules" in markers


def test_legacy_metadata_detection(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(
        source / "01-Facts" / "Products" / "fact.md",
        "---\nmemory_layer: \"facts\"\nauthor_agent: \"Codex\"\n---\nbody",
    )

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    metadata = read_csv_rows(report / "metadata-cleanup.csv")
    fields = {row["field_name"] for row in metadata}
    assert "memory_layer" in fields
    assert "author_agent" in fields


def test_no_automatic_deletion_and_no_source_modification(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "05-Projects" / "Alpha" / "plan.md", "original")

    before = (source / "05-Projects" / "Alpha" / "plan.md").read_text(encoding="utf-8")
    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--apply"])
    after = (source / "05-Projects" / "Alpha" / "plan.md").read_text(encoding="utf-8")
    assert before == after
    assert (source / "05-Projects" / "Alpha" / "plan.md").exists()


def test_inventory_json_contains_stats(tmp_path: Path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    report = tmp_path / "report"
    write_text(source / "01-Facts" / "Products" / "fact.md", "hello")

    invoke(["--source", str(source), "--target", str(target), "--report-dir", str(report), "--dry-run"])
    payload = json.loads((report / "inventory.json").read_text(encoding="utf-8"))
    assert payload["stats"]["proposed"] == 1

