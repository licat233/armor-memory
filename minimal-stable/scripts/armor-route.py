#!/usr/bin/env python3
"""Deterministic router for ARMOR Minimal Stable."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass


WORKSPACES = {
    "website": "Website",
    "content": "Content",
    "marketing": "Marketing",
    "products": "Products",
    "operations": "Operations",
}

RECORD_FOLDERS = {
    "meeting": "Meetings",
    "email": "Emails",
    "conversation": "Conversations",
    "journal": "Journal",
    "feedback": "Feedback",
    "published": "Published",
}

KNOWLEDGE_FOLDERS = {
    "company": "Company",
    "brand": "Brand",
    "product": "Products",
    "products": "Products",
    "customer": "Customers",
    "customers": "Customers",
    "rule": "Rules",
    "rules": "Rules",
    "insight": "Insights",
    "insights": "Insights",
}


@dataclass
class RouteResult:
    path: str
    category: str
    reason: str

    def as_dict(self) -> dict[str, str]:
        return {
            "path": self.path,
            "category": self.category,
            "reason": self.reason,
        }


def normalize(value: str | None) -> str:
    return (value or "").strip().lower()


def slug_to_title(value: str) -> str:
    parts = [part for part in value.replace("_", "-").split("-") if part]
    if not parts:
        return "General"
    return "".join(part[:1].upper() + part[1:] for part in parts)


def route_task(
    task: str,
    *,
    project: str | None = None,
    workspace: str | None = None,
    record_type: str | None = None,
    knowledge_type: str | None = None,
    research_kind: str | None = None,
) -> RouteResult:
    task_text = normalize(task)
    project_name = (project or "").strip()
    workspace_key = normalize(workspace)
    record_key = normalize(record_type)
    knowledge_key = normalize(knowledge_type)
    research_key = normalize(research_kind)

    if project_name:
        return RouteResult(
            path=f"02-Projects/Active/{project_name}/",
            category="project",
            reason="explicit active project",
        )

    if workspace_key in WORKSPACES:
        return RouteResult(
            path=f"02-Projects/Workspaces/{WORKSPACES[workspace_key]}/",
            category="project",
            reason="explicit persistent workspace",
        )

    if record_key in RECORD_FOLDERS:
        return RouteResult(
            path=f"03-Records/{RECORD_FOLDERS[record_key]}/",
            category="record",
            reason="explicit record type",
        )

    if knowledge_key in KNOWLEDGE_FOLDERS:
        return RouteResult(
            path=f"01-Knowledge/{KNOWLEDGE_FOLDERS[knowledge_key]}/",
            category="knowledge",
            reason="explicit long-term knowledge request",
        )

    if research_key == "source":
        return RouteResult(
            path="04-Research/Sources/",
            category="research",
            reason="explicit research source copy",
        )

    if research_key in {"note", "notes", "analysis"}:
        return RouteResult(
            path="04-Research/Notes/",
            category="research",
            reason="explicit research notes",
        )

    if any(word in task_text for word in ["create", "write", "draft", "edit", "improve", "design", "prepare", "generate"]):
        guessed = guess_workspace(task_text)
        return RouteResult(
            path=f"02-Projects/Workspaces/{guessed}/",
            category="project",
            reason="work product",
        )

    if any(word in task_text for word in ["save", "record", "preserve", "archive", "document"]):
        guessed = guess_record_folder(task_text)
        return RouteResult(
            path=f"03-Records/{guessed}/",
            category="record",
            reason="record of event or received content",
        )

    if any(word in task_text for word in ["remember", "organize", "summarize", "maintain", "define"]):
        guessed = guess_knowledge_folder(task_text)
        return RouteResult(
            path=f"01-Knowledge/{guessed}/",
            category="knowledge",
            reason="long-term reusable knowledge",
        )

    if any(word in task_text for word in ["investigate", "research", "compare", "gather sources", "analyze"]):
        folder = "Sources" if "source" in task_text else "Notes"
        return RouteResult(
            path=f"04-Research/{folder}/",
            category="research",
            reason="external research request",
        )

    return RouteResult(
        path="90-Inbox/",
        category="inbox",
        reason="routing unresolved",
    )


def guess_workspace(task_text: str) -> str:
    if "website" in task_text or "article" in task_text:
        return "Website"
    if "marketing" in task_text or "campaign" in task_text:
        return "Marketing"
    if "product" in task_text or "manual" in task_text:
        return "Products"
    if "operation" in task_text or "ops" in task_text:
        return "Operations"
    if "content" in task_text:
        return "Content"
    return "Content"


def guess_record_folder(task_text: str) -> str:
    if "meeting" in task_text or "transcript" in task_text:
        return "Meetings"
    if "email" in task_text:
        return "Emails"
    if "conversation" in task_text or "chat" in task_text:
        return "Conversations"
    if "journal" in task_text:
        return "Journal"
    if "feedback" in task_text:
        return "Feedback"
    if "published" in task_text or "snapshot" in task_text:
        return "Published"
    return "Conversations"


def guess_knowledge_folder(task_text: str) -> str:
    if "brand" in task_text:
        return "Brand"
    if "product" in task_text:
        return "Products"
    if "customer" in task_text:
        return "Customers"
    if "rule" in task_text:
        return "Rules"
    if "insight" in task_text or "lesson" in task_text:
        return "Insights"
    if "company" in task_text:
        return "Company"
    return "Insights"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Route a task in ARMOR Minimal Stable.")
    parser.add_argument("task", help="Task description")
    parser.add_argument("--project", help="Active project name")
    parser.add_argument("--workspace", help="Persistent workspace name")
    parser.add_argument("--record-type", help="Record subtype")
    parser.add_argument("--knowledge-type", help="Knowledge subtype")
    parser.add_argument("--research-kind", help="Research subtype")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    result = route_task(
        args.task,
        project=args.project,
        workspace=args.workspace,
        record_type=args.record_type,
        knowledge_type=args.knowledge_type,
        research_kind=args.research_kind,
    )

    if args.json:
        print(json.dumps(result.as_dict(), ensure_ascii=True, indent=2))
    else:
        print(result.path)
        print(result.category)
        print(result.reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

