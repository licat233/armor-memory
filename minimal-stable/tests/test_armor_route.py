from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "armor-route.py"
SPEC = importlib.util.spec_from_file_location("armor_route", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_active_project_has_highest_priority():
    result = MODULE.route_task("write a website article", project="Alpha")
    assert result.path == "02-Projects/Active/Alpha/"
    assert result.reason == "explicit active project"


def test_workspace_routes_work_product():
    result = MODULE.route_task("write a website article", workspace="website")
    assert result.path == "02-Projects/Workspaces/Website/"


def test_record_type_routes_to_records():
    result = MODULE.route_task("save a customer email", record_type="email")
    assert result.path == "03-Records/Emails/"


def test_knowledge_type_routes_to_knowledge():
    result = MODULE.route_task("remember this product characteristic", knowledge_type="product")
    assert result.path == "01-Knowledge/Products/"


def test_research_source_routes_to_sources():
    result = MODULE.route_task("gather competitor sources", research_kind="source")
    assert result.path == "04-Research/Sources/"


def test_fallback_infers_marketing_workspace():
    result = MODULE.route_task("prepare a marketing campaign")
    assert result.path == "02-Projects/Workspaces/Marketing/"


def test_unresolved_task_goes_to_inbox():
    result = MODULE.route_task("hello there")
    assert result.path == "90-Inbox/"
    assert result.reason == "routing unresolved"
