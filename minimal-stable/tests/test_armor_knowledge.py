from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "armor-knowledge.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def make_vault(tmp_path: Path) -> Path:
    vault = tmp_path / "armor-vault"
    (vault / "01-Knowledge" / "Products").mkdir(parents=True)
    (vault / "03-Records").mkdir(parents=True)
    return vault


def write_knowledge(vault: Path, name: str, content: str) -> Path:
    path = vault / "01-Knowledge" / "Products" / name
    path.write_text(content, encoding="utf-8")
    return path


def test_check_missing_authority_is_warning_not_error(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(vault, "power-track.md", "# Power Track\n")

    completed = run_cli("check", "--vault", str(vault))

    assert completed.returncode == 0
    assert "[missing_authority]" in completed.stdout
    assert "Errors: 0" in completed.stdout
    assert "Warnings: 1" in completed.stdout


def test_check_invalid_authority_is_error(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(
        vault,
        "power-track.md",
        '---\nauthority: "ssot"\n---\n# Power Track\n',
    )

    completed = run_cli("check", "--vault", str(vault))

    assert completed.returncode == 1
    assert "[invalid_authority]" in completed.stdout


def test_verified_without_provenance_is_warning(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(
        vault,
        "power-track.md",
        '---\nauthority: "verified"\n---\n# Power Track\n',
    )

    completed = run_cli("check", "--vault", str(vault))

    assert completed.returncode == 0
    assert "[provenance_not_declared]" in completed.stdout


def test_source_ref_satisfies_provenance_advisory(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(
        vault,
        "power-track.md",
        '---\nauthority: "canonical"\nsource_ref: "03-Records/spec.md"\n---\n# Power Track\n',
    )

    completed = run_cli("check", "--vault", str(vault))

    assert completed.returncode == 0
    assert "provenance_not_declared" not in completed.stdout
    assert "Findings: none" in completed.stdout


def test_duplicate_titles_are_warning_when_not_multiple_canonical(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(vault, "one.md", '---\nauthority: "working"\n---\n# Power Track System\n')
    write_knowledge(vault, "two.md", '---\nauthority: "verified"\nsource_ref: "spec.md"\n---\n# Power Track System\n')

    completed = run_cli("check", "--vault", str(vault))

    assert completed.returncode == 0
    assert completed.stdout.count("[duplicate_title]") == 2


def test_multiple_canonical_pages_with_same_title_are_errors(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(vault, "one.md", '---\nauthority: "canonical"\nsource_ref: "one.md"\n---\n# Power Track\n')
    write_knowledge(vault, "two.md", '---\nauthority: "canonical"\nsource_ref: "two.md"\n---\n# Power Track\n')

    completed = run_cli("check", "--vault", str(vault))

    assert completed.returncode == 1
    assert completed.stdout.count("[canonical_title_collision]") == 2


def test_check_json_is_machine_readable_and_scoped_to_knowledge(tmp_path: Path):
    vault = make_vault(tmp_path)
    write_knowledge(vault, "knowledge.md", '---\nauthority: "working"\n---\n# Knowledge\n')
    (vault / "03-Records" / "ignored.md").write_text(
        '---\nauthority: "invalid"\n---\n# Ignored Record\n',
        encoding="utf-8",
    )

    completed = run_cli("check", "--vault", str(vault), "--json")

    assert completed.returncode == 0
    payload = json.loads(completed.stdout)
    assert payload["scope"] == "01-Knowledge"
    assert payload["summary"]["knowledge_files"] == 1
    assert payload["summary"]["errors"] == 0


def test_check_requires_vault_root(tmp_path: Path):
    completed = run_cli("check", "--vault", str(tmp_path / "missing"))

    assert completed.returncode == 2
    assert "vault root does not exist" in completed.stderr


def test_diff_previews_change_without_writing_files(tmp_path: Path):
    current = tmp_path / "current.md"
    candidate = tmp_path / "candidate.md"
    current.write_text("# Product\nVoltage: 12V\n", encoding="utf-8")
    candidate.write_text("# Product\nVoltage: 24V\n", encoding="utf-8")

    completed = run_cli("diff", str(current), str(candidate))

    assert completed.returncode == 0
    assert "-Voltage: 12V" in completed.stdout
    assert "+Voltage: 24V" in completed.stdout
    assert current.read_text(encoding="utf-8") == "# Product\nVoltage: 12V\n"
    assert candidate.read_text(encoding="utf-8") == "# Product\nVoltage: 24V\n"


def test_diff_reports_no_changes(tmp_path: Path):
    current = tmp_path / "current.md"
    candidate = tmp_path / "candidate.md"
    content = "# Product\nVoltage: 24V\n"
    current.write_text(content, encoding="utf-8")
    candidate.write_text(content, encoding="utf-8")

    completed = run_cli("diff", str(current), str(candidate))

    assert completed.returncode == 0
    assert completed.stdout.strip() == "No changes."
