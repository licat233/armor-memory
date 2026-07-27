from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ROUTE_WRAPPER = REPO_ROOT / ".agent" / "skills" / "armor-memory" / "scripts" / "route.sh"
PYTHON_ROUTER = REPO_ROOT / "minimal-stable" / "scripts" / "armor-route.py"
AGENTS_DOC = REPO_ROOT / "AGENTS.md"
CLAUDE_DOC = REPO_ROOT / "CLAUDE.md"
HERMES_DOC = REPO_ROOT / "HERMES.md"
SKILL_DOC = REPO_ROOT / ".agent" / "skills" / "armor-memory" / "SKILL.md"


def run_command(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=False)


def test_route_wrapper_exists():
    assert ROUTE_WRAPPER.exists()


def test_route_wrapper_points_to_python_router():
    contents = ROUTE_WRAPPER.read_text()
    assert "minimal-stable/scripts/armor-route.py" in contents
    assert 'exec python3 \\' in contents


def test_wrapper_output_matches_direct_router():
    wrapper = run_command(
        str(ROUTE_WRAPPER),
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

