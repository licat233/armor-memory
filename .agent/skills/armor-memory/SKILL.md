---
name: armor-memory
description: >
  Retrieve or route documents using ARMOR Minimal Stable. Use when an
  Agent reads, searches, creates, stores, records, researches, or updates
  content in the ARMOR Vault.
---

# ARMOR Memory

## Use this Skill when

Use this Skill when a task reads, searches, creates, stores, modifies, records, researches, or classifies content in the ARMOR Vault.

Do not use it for:

- ordinary source-code edits
- temporary chat answers
- terminal output
- calculations
- disposable scratch files
- files outside the ARMOR Vault

## Retrieval workflow

1. If an exact file or domain `index.md` is known, read it directly.
2. Otherwise choose one relevant top-level area: current business facts and rules -> `01-Knowledge/`; active work -> `02-Projects/`; event or publication evidence -> `03-Records/`; external sources or analysis -> `04-Research/`.
3. Search only that area first.
4. Exclude Records, Inbox, and Archive unless the task requires evidence, unresolved material, audit, or history.
5. Expand to the full ARMOR Vault only after the scoped search fails, and state why; this does not mean switching to Web search.
6. Treat search results as candidates; determine authority from `00-System/AUTHORITY-RULES.md` and the underlying files.

## Retrieval authority rules

When a task depends on whether a claim is current or authoritative, read
`references/AUTHORITY-GUIDE.md`.

- Use only an explicit `authority` field to assign an authority level.
- `status: active` is a lifecycle state. It does not mean `verified` or
  `canonical`.
- `revision`, `source_quality`, `write_policy`, document type, and location in
  `01-Knowledge/` do not promote a file to `verified` or `canonical`.
- If a knowledge file has no explicit authority, treat it as `working` and
  qualify claims from it accordingly.
- Prefer explicit `canonical` over explicit `verified`, and explicit
  `verified` over `working`.
- If sources of equal or unclear authority conflict, report the conflict and
  request a decision. Do not silently choose one.
- Never say "all facts verified" unless each relied-on claim comes from an
  explicitly verified or canonical source, or was verified in the current
  task.

## Write workflow

1. Classify the task using `references/CLASSIFICATION-PROTOCOL.md`.
2. Select only supported router values.
3. Call `scripts/route.sh`.
4. Use exactly the path returned by the router.
5. Write or update the document.
6. Stop.

官网文章仍按 `work-product + website + article` 分类；Router 会直接返回唯一文章目录 `03-Records/Published/Articles/`。

官方社媒内容按 `work-product + marketing + social-copy` 分类；Router 始终返回唯一目录 `03-Records/Published/Social-Media/`，无论是否提供 `--project`。官方社媒内容只有一个目的地，没有 Workspace 到 Published 的移动/复制生命周期。临时或内部探索内容归入 Workspaces 下的其他分类。

## Mandatory rules

- Full-Vault search is a fallback, not the first retrieval action.
- Do not treat Records, Research, Inbox, or Archive as current truth without qualification.
- Never construct a destination path manually.
- Never add a new router value during ordinary work.
- Never route unverified content to Inbox merely because it is unverified.
- Inbox is allowed only through explicit `object=unresolved`.
- Draft is a status, not a destination.
- Do not run extra memory-maintenance operations after an ordinary write.

## Canonical knowledge

Load `references/AUTHORITY-GUIDE.md` when changing canonical knowledge or when
retrieval requires an authority judgment.
