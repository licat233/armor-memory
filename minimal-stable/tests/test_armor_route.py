from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "armor-route.py"
SPEC = importlib.util.spec_from_file_location("armor_route", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def test_work_product_website_article_workspace():
    result = MODULE.route_request(object_type="work-product", domain="website", artifact="article")
    assert result.path == "02-Projects/Workspaces/Website/Articles/"


def test_work_product_website_article_project():
    result = MODULE.route_request(
        object_type="work-product",
        domain="website",
        artifact="article",
        project="armor-website",
    )
    assert result.path == "02-Projects/Active/armor-website/Content/Articles/"


def test_work_product_website_landing_page_workspace():
    result = MODULE.route_request(object_type="work-product", domain="website", artifact="landing-page")
    assert result.path == "02-Projects/Workspaces/Website/Landing-Pages/"


def test_work_product_website_case_study_workspace():
    result = MODULE.route_request(object_type="work-product", domain="website", artifact="case-study")
    assert result.path == "02-Projects/Workspaces/Website/Case-Studies/"


def test_work_product_content_blog_post_workspace():
    result = MODULE.route_request(object_type="work-product", domain="content", artifact="blog-post")
    assert result.path == "02-Projects/Workspaces/Content/Blog-Posts/"


def test_work_product_content_report_workspace():
    result = MODULE.route_request(object_type="work-product", domain="content", artifact="report")
    assert result.path == "02-Projects/Workspaces/Content/Reports/"


def test_work_product_content_case_study_project():
    result = MODULE.route_request(
        object_type="work-product",
        domain="content",
        artifact="case-study",
        project="Q4 Content",
    )
    assert result.path == "02-Projects/Active/q4-content/Content/Case-Studies/"


def test_work_product_marketing_campaign_workspace():
    result = MODULE.route_request(object_type="work-product", domain="marketing", artifact="campaign")
    assert result.path == "02-Projects/Workspaces/Marketing/Campaigns/"


def test_work_product_marketing_email_sequence_project():
    result = MODULE.route_request(
        object_type="work-product",
        domain="marketing",
        artifact="email-sequence",
        project="Launch 2026",
    )
    assert result.path == "02-Projects/Active/launch-2026/Marketing/Email-Sequences/"


def test_work_product_marketing_social_copy_workspace():
    result = MODULE.route_request(object_type="work-product", domain="marketing", artifact="social-copy")
    assert result.path == "02-Projects/Workspaces/Marketing/Social-Copy/"


def test_work_product_products_manual_workspace():
    result = MODULE.route_request(
        object_type="work-product",
        domain="products",
        artifact="product-manual",
        entity="Armor Pro Panel",
    )
    assert result.path == "02-Projects/Workspaces/Products/armor-pro-panel/Documentation/"


def test_work_product_products_manual_project():
    result = MODULE.route_request(
        object_type="work-product",
        domain="products",
        artifact="product-manual",
        entity="Armor Pro Panel",
        project="Manual Refresh",
    )
    assert result.path == "02-Projects/Active/manual-refresh/Products/armor-pro-panel/Documentation/"


def test_work_product_products_spec_sheet_workspace():
    result = MODULE.route_request(
        object_type="work-product",
        domain="products",
        artifact="spec-sheet",
        entity="Line Bar X",
    )
    assert result.path == "02-Projects/Workspaces/Products/line-bar-x/Spec-Sheets/"


def test_work_product_products_price_list_project():
    result = MODULE.route_request(
        object_type="work-product",
        domain="products",
        artifact="price-list",
        entity="Shelf Led",
        project="Pricing 2026",
    )
    assert result.path == "02-Projects/Active/pricing-2026/Products/shelf-led/Price-Lists/"


def test_work_product_operations_process_doc_workspace():
    result = MODULE.route_request(object_type="work-product", domain="operations", artifact="process-doc")
    assert result.path == "02-Projects/Workspaces/Operations/Process-Docs/"


def test_work_product_operations_checklist_workspace():
    result = MODULE.route_request(object_type="work-product", domain="operations", artifact="checklist")
    assert result.path == "02-Projects/Workspaces/Operations/Checklists/"


def test_work_product_operations_internal_report_project():
    result = MODULE.route_request(
        object_type="work-product",
        domain="operations",
        artifact="internal-report",
        project="Warehouse Audit",
    )
    assert result.path == "02-Projects/Active/warehouse-audit/Operations/Internal-Reports/"


def test_record_meeting_routes():
    result = MODULE.route_request(object_type="record", record_type="meeting")
    assert result.path == "03-Records/Meetings/"


def test_record_email_routes():
    result = MODULE.route_request(object_type="record", record_type="email")
    assert result.path == "03-Records/Emails/"


def test_record_conversation_routes():
    result = MODULE.route_request(object_type="record", record_type="conversation")
    assert result.path == "03-Records/Conversations/"


def test_record_feedback_routes():
    result = MODULE.route_request(object_type="record", record_type="feedback")
    assert result.path == "03-Records/Feedback/"


def test_record_published_routes():
    result = MODULE.route_request(object_type="record", record_type="published")
    assert result.path == "03-Records/Published/"


def test_record_journal_routes_with_year():
    result = MODULE.route_request(object_type="record", record_type="journal", year="2026")
    assert result.path == "03-Records/Journal/2026/"


def test_knowledge_company_routes():
    assert MODULE.route_request(object_type="knowledge", knowledge_type="company").path == "01-Knowledge/Company/"


def test_knowledge_brand_routes():
    assert MODULE.route_request(object_type="knowledge", knowledge_type="brand").path == "01-Knowledge/Brand/"


def test_knowledge_product_routes():
    assert MODULE.route_request(object_type="knowledge", knowledge_type="product").path == "01-Knowledge/Products/"


def test_knowledge_customer_routes():
    assert MODULE.route_request(object_type="knowledge", knowledge_type="customer").path == "01-Knowledge/Customers/"


def test_knowledge_rule_routes():
    assert MODULE.route_request(object_type="knowledge", knowledge_type="rule").path == "01-Knowledge/Rules/"


def test_knowledge_insight_routes():
    assert MODULE.route_request(object_type="knowledge", knowledge_type="insight").path == "01-Knowledge/Insights/"


def test_research_source_routes():
    assert MODULE.route_request(object_type="research", research_kind="source").path == "04-Research/Sources/"


def test_research_note_routes():
    assert MODULE.route_request(object_type="research", research_kind="note").path == "04-Research/Notes/"


def test_unresolved_explicit_routes():
    result = MODULE.route_request(object_type="unresolved")
    assert result.path == "90-Inbox/"
    assert result.reason == "explicit unresolved routing"


def test_deterministic_repeated_output():
    first = MODULE.route_request(
        object_type="work-product",
        domain="website",
        artifact="article",
        project="Armor Website",
    )
    second = MODULE.route_request(
        object_type="work-product",
        domain="website",
        artifact="article",
        project="Armor Website",
    )
    assert first == second


def test_path_traversal_rejected():
    with pytest.raises(ValueError, match="path traversal"):
        MODULE.route_request(
            object_type="work-product",
            domain="website",
            artifact="article",
            project="../escape",
        )


def test_absolute_path_rejected():
    with pytest.raises(ValueError, match="absolute path"):
        MODULE.route_request(
            object_type="work-product",
            domain="website",
            artifact="article",
            project="/tmp/escape",
        )


def test_shell_metacharacters_rejected():
    with pytest.raises(ValueError, match="forbidden"):
        MODULE.route_request(
            object_type="work-product",
            domain="products",
            artifact="product-manual",
            entity="bad;name",
        )


def test_unicode_project_name_normalizes():
    result = MODULE.route_request(
        object_type="work-product",
        domain="website",
        artifact="article",
        project="产品 发布",
    )
    assert result.path == "02-Projects/Active/产品-发布/Content/Articles/"


def test_unicode_entity_name_normalizes():
    result = MODULE.route_request(
        object_type="work-product",
        domain="products",
        artifact="product-manual",
        entity="货架 灯条",
    )
    assert result.path == "02-Projects/Workspaces/Products/货架-灯条/Documentation/"


def test_invalid_domain_artifact_combo_rejected():
    with pytest.raises(ValueError, match="not supported"):
        MODULE.route_request(object_type="work-product", domain="website", artifact="campaign")


def test_missing_entity_for_product_manual_rejected():
    with pytest.raises(ValueError, match="entity is required"):
        MODULE.route_request(object_type="work-product", domain="products", artifact="product-manual")


@pytest.mark.parametrize(
    ("args", "needle"),
    [
        (["--object", "unknown"], "invalid choice"),
        (["--object", "work-product"], "--domain is required"),
        (["--object", "work-product", "--domain", "website"], "--artifact is required"),
        (["--object", "record"], "--record-type is required"),
        (["--object", "record", "--record-type", "journal"], "--year is required"),
        (["--object", "knowledge"], "--knowledge-type is required"),
        (["--object", "research"], "--research-kind is required"),
        (["--object", "unresolved", "--domain", "website"], "no additional routing fields are allowed"),
        (["--object", "work-product", "--domain", "website", "--artifact", "campaign"], "not supported"),
        (["--object", "work-product", "--domain", "website", "--artifact", "article", "--project", "../bad"], "path traversal"),
    ],
)
def test_cli_rejections(args: list[str], needle: str):
    completed = run_cli(*args)
    assert completed.returncode == 2
    assert needle in completed.stderr


def test_cli_json_output():
    completed = run_cli(
        "--object",
        "work-product",
        "--domain",
        "website",
        "--artifact",
        "article",
        "--project",
        "armor-website",
        "--json",
    )
    assert completed.returncode == 0
    assert '"path": "02-Projects/Active/armor-website/Content/Articles/"' in completed.stdout
