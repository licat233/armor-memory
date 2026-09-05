from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
ROUTE_WRAPPER = REPO_ROOT / ".agent" / "skills" / "armor-memory" / "scripts" / "route.sh"
PYTHON_ROUTER = REPO_ROOT / "minimal-stable" / "scripts" / "armor-route.py"
AGENTS_DOC = REPO_ROOT / "AGENTS.md"
CLAUDE_DOC = REPO_ROOT / "CLAUDE.md"
HERMES_DOC = REPO_ROOT / "HERMES.md"
SKILL_DOC = REPO_ROOT / ".agent" / "skills" / "armor-memory" / "SKILL.md"


def run_command(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=False)


def run_wrapper(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env is not None:
        merged_env.update(env)
    return subprocess.run(
        [str(ROUTE_WRAPPER), *args],
        text=True,
        capture_output=True,
        check=False,
        env=merged_env,
    )


def test_route_wrapper_exists():
    assert ROUTE_WRAPPER.exists()


def test_route_wrapper_points_to_python_router():
    contents = ROUTE_WRAPPER.read_text()
    assert "minimal-stable/scripts/armor-route.py" in contents
    assert "ARMOR_ARCH_ROOT" in contents
    assert "resolve_script_path()" in contents


def test_wrapper_output_matches_direct_router():
    wrapper = run_wrapper(
        "--object",
        "work-product",
        "--domain",
        "website",
        "--artifact",
        "article",
        "--project",
        "armor-website",
    )
    direct = run_command(
        sys.executable,
        str(PYTHON_ROUTER),
        "--object",
        "work-product",
        "--domain",
        "website",
        "--artifact",
        "article",
        "--project",
        "armor-website",
    )
    assert wrapper.returncode == 0
    assert direct.returncode == 0
    assert wrapper.stdout == direct.stdout


def test_wrapper_works_from_real_repository_path():
    completed = run_wrapper("--object", "record", "--record-type", "journal", "--year", "2026")
    assert completed.returncode == 0
    assert completed.stdout.splitlines()[0] == "03-Records/Journal/2026/"


def test_wrapper_works_through_symbolic_link(tmp_path: Path):
    link_root = tmp_path / "skill link"
    link_root.symlink_to(REPO_ROOT / ".agent" / "skills" / "armor-memory", target_is_directory=True)
    linked_wrapper = link_root / "scripts" / "route.sh"
    completed = subprocess.run(
        [str(linked_wrapper), "--object", "record", "--record-type", "journal", "--year", "2026"],
        text=True,
        capture_output=True,
        check=False,
        env=os.environ.copy(),
    )
    assert completed.returncode == 0
    assert completed.stdout.splitlines()[0] == "03-Records/Journal/2026/"


def test_armor_arch_root_overrides_path_discovery(tmp_path: Path):
    fake_repo = tmp_path / "fake repo"
    router_dir = fake_repo / "minimal-stable" / "scripts"
    router_dir.mkdir(parents=True)
    router_path = router_dir / "armor-route.py"
    router_path.write_text(
        "#!/usr/bin/env python3\nprint('override-path/')\nprint('record')\nprint('override')\n",
        encoding="utf-8",
    )
    completed = run_wrapper(
        "--object",
        "record",
        "--record-type",
        "meeting",
        env={"ARMOR_ARCH_ROOT": str(fake_repo)},
    )
    assert completed.returncode == 0
    assert completed.stdout.splitlines()[0] == "override-path/"


def test_missing_router_produces_clear_error(tmp_path: Path):
    missing_repo = tmp_path / "missing repo"
    missing_repo.mkdir()
    completed = run_wrapper(
        "--object",
        "record",
        "--record-type",
        "meeting",
        env={"ARMOR_ARCH_ROOT": str(missing_repo)},
    )
    assert completed.returncode == 1
    assert "ERROR: ARMOR Router not found:" in completed.stderr
    assert "Set ARMOR_ARCH_ROOT" in completed.stderr


def test_default_output_remains_relative():
    completed = run_wrapper("--object", "record", "--record-type", "journal", "--year", "2026")
    assert completed.returncode == 0
    assert completed.stdout.splitlines()[0] == "03-Records/Journal/2026/"


def test_absolute_output_uses_armor_vault_root():
    completed = run_wrapper(
        "--absolute",
        "--object",
        "record",
        "--record-type",
        "journal",
        "--year",
        "2026",
        env={"ARMOR_VAULT_ROOT": "/Users/licat/armor-vault"},
    )
    assert completed.returncode == 0
    assert completed.stdout.splitlines()[0] == "/Users/licat/armor-vault/03-Records/Journal/2026/"


def test_absolute_output_requires_armor_vault_root(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("ARMOR_VAULT_ROOT", raising=False)
    completed = run_wrapper("--absolute", "--object", "record", "--record-type", "journal", "--year", "2026")
    assert completed.returncode == 1
    assert "ARMOR_VAULT_ROOT is required with --absolute" in completed.stderr


def test_paths_with_spaces_work_via_symlink(tmp_path: Path):
    link_root = tmp_path / "armor memory skill"
    link_root.symlink_to(REPO_ROOT / ".agent" / "skills" / "armor-memory", target_is_directory=True)
    linked_wrapper = link_root / "scripts" / "route.sh"
    completed = subprocess.run(
        [
            str(linked_wrapper),
            "--absolute",
            "--object",
            "work-product",
            "--domain",
            "website",
            "--artifact",
            "article",
            "--project",
            "Armor Website",
        ],
        text=True,
        capture_output=True,
        check=False,
        env={**os.environ, "ARMOR_VAULT_ROOT": "/Users/licat/armor-vault"},
    )
    assert completed.returncode == 0
    assert completed.stdout.splitlines()[0] == "/Users/licat/armor-vault/02-Projects/Workspaces/Website/Articles/"


def test_wrapper_forwards_router_arguments_unchanged():
    wrapper = run_wrapper("--object", "work-product", "--domain", "website", "--artifact", "article", "--project", "Armor Website")
    direct = run_command(
        sys.executable,
        str(PYTHON_ROUTER),
        "--object",
        "work-product",
        "--domain",
        "website",
        "--artifact",
        "article",
        "--project",
        "Armor Website",
    )
    assert wrapper.returncode == 0
    assert direct.returncode == 0
    assert wrapper.stdout == direct.stdout


def test_wrapper_rejects_absolute_with_json():
    completed = run_wrapper(
        "--absolute",
        "--json",
        "--object",
        "record",
        "--record-type",
        "journal",
        "--year",
        "2026",
        env={"ARMOR_VAULT_ROOT": "/Users/licat/armor-vault"},
    )
    assert completed.returncode == 1
    assert "--absolute cannot currently be combined with --json" in completed.stderr


def test_agents_md_references_shared_skill():
    contents = AGENTS_DOC.read_text()
    assert ".agent/skills/armor-memory/SKILL.md" in contents
    assert ".agent/skills/armor-memory/scripts/route.sh" in contents


def test_claude_md_references_shared_skill():
    contents = CLAUDE_DOC.read_text()
    assert ".agent/skills/armor-memory/SKILL.md" in contents
    assert ".agent/skills/armor-memory/scripts/route.sh" in contents


def test_hermes_md_references_shared_skill():
    contents = HERMES_DOC.read_text()
    assert ".agent/skills/armor-memory/SKILL.md" in contents
    assert ".agent/skills/armor-memory/scripts/route.sh" in contents


def test_skill_exists_and_mentions_protocol():
    contents = SKILL_DOC.read_text()
    assert "references/CLASSIFICATION-PROTOCOL.md" in contents
    assert "scripts/route.sh" in contents
