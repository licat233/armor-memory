from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "migrate-lifecycle-neutral.py"
SPEC = importlib.util.spec_from_file_location("migrate_lifecycle_neutral", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def make_vault(tmp_path: Path) -> Path:
    vault = tmp_path / "armor-vault"
    (vault / "02-Projects").mkdir(parents=True)
    (vault / "03-Records" / "Published" / "Articles").mkdir(parents=True)
    (vault / "03-Records" / "Published" / "Social-Media").mkdir(parents=True)
    return vault


def run_cli(vault: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--vault", str(vault), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def test_dry_run_does_not_move_active(tmp_path: Path):
    vault = make_vault(tmp_path)
    active = vault / "02-Projects" / "Active"
    (active / "armor-website").mkdir(parents=True)

    completed = run_cli(vault)

    assert completed.returncode == 0
    assert "DRY-RUN" in completed.stdout
    assert active.exists()
    assert not (vault / "02-Projects" / "Projects").exists()


def test_apply_renames_active_when_destination_absent(tmp_path: Path):
    vault = make_vault(tmp_path)
    active_project = vault / "02-Projects" / "Active" / "armor-website"
    active_project.mkdir(parents=True)
    (active_project / "note.md").write_text("hello", encoding="utf-8")

    completed = run_cli(vault, "--apply")

    assert completed.returncode == 0
    assert not (vault / "02-Projects" / "Active").exists()
    migrated = vault / "02-Projects" / "Projects" / "armor-website" / "note.md"
    assert migrated.read_text(encoding="utf-8") == "hello"


def test_apply_merges_non_colliding_projects(tmp_path: Path):
    vault = make_vault(tmp_path)
    (vault / "02-Projects" / "Active" / "project-a").mkdir(parents=True)
    (vault / "02-Projects" / "Projects" / "project-b").mkdir(parents=True)

    completed = run_cli(vault, "--apply")

    assert completed.returncode == 0
    assert (vault / "02-Projects" / "Projects" / "project-a").is_dir()
    assert (vault / "02-Projects" / "Projects" / "project-b").is_dir()
    assert not (vault / "02-Projects" / "Active").exists()


def test_collision_fails_before_any_move(tmp_path: Path):
    vault = make_vault(tmp_path)
    active = vault / "02-Projects" / "Active"
    projects = vault / "02-Projects" / "Projects"
    (active / "same-project").mkdir(parents=True)
    (active / "other-project").mkdir(parents=True)
    (projects / "same-project").mkdir(parents=True)

    completed = run_cli(vault, "--apply")

    assert completed.returncode == 2
    assert "migration collision" in completed.stderr
    assert (active / "same-project").is_dir()
    assert (active / "other-project").is_dir()
    assert not (projects / "other-project").exists()


def test_published_records_are_preserved(tmp_path: Path):
    vault = make_vault(tmp_path)
    article = vault / "03-Records" / "Published" / "Articles" / "legacy.md"
    social = vault / "03-Records" / "Published" / "Social-Media" / "legacy-social.md"
    article.write_text("article", encoding="utf-8")
    social.write_text("social", encoding="utf-8")
    (vault / "02-Projects" / "Active" / "project-a").mkdir(parents=True)

    completed = run_cli(vault, "--apply")

    assert completed.returncode == 0
    assert article.read_text(encoding="utf-8") == "article"
    assert social.read_text(encoding="utf-8") == "social"


def test_missing_projects_root_fails(tmp_path: Path):
    vault = tmp_path / "armor-vault"
    vault.mkdir()

    completed = run_cli(vault)

    assert completed.returncode == 2
    assert "projects directory not found" in completed.stderr


def test_missing_vault_environment_is_rejected(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("ARMOR_VAULT_ROOT", raising=False)
    with pytest.raises(ValueError, match="ARMOR_VAULT_ROOT is required"):
        MODULE.resolve_vault_root(None)
