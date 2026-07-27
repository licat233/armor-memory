from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit-v72-dependencies.py"
SPEC = importlib.util.spec_from_file_location("audit_v72_dependencies", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def invoke(args: list[str]) -> int:
    old = sys.argv
    try:
        sys.argv = [str(SCRIPT_PATH), *args]
        return MODULE.main()
    finally:
        sys.argv = old


def test_dependency_reference_detection(tmp_path: Path, capsys: pytest.CaptureFixture[str]):
    scan_dir = tmp_path / "scan"
    write_text(scan_dir / "AGENTS.md", "See 00-Core and enterprise/README.md")

    invoke(["--scan-dir", str(scan_dir)])
    out = capsys.readouterr().out
    payload = json.loads(out)
    assert payload["matches"][0]["matches"] == ["00-Core", "enterprise/"]


def test_output_file_written(tmp_path: Path):
    scan_dir = tmp_path / "scan"
    output = tmp_path / "report.json"
    write_text(scan_dir / "config.yaml", "path: 05-Projects")

    invoke(["--scan-dir", str(scan_dir), "--output", str(output)])
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["matches"][0]["matches"] == ["05-Projects"]


def test_missing_scan_directory_fails(tmp_path: Path):
    with pytest.raises(SystemExit):
        invoke(["--scan-dir", str(tmp_path / "missing")])


def test_non_likely_files_are_skipped(tmp_path: Path, capsys: pytest.CaptureFixture[str]):
    scan_dir = tmp_path / "scan"
    write_text(scan_dir / "notes.txt", "00-Core")

    invoke(["--scan-dir", str(scan_dir)])
    payload = json.loads(capsys.readouterr().out)
    assert payload["matches"] == []

