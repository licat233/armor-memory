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

## Write workflow

1. Classify the task using `references/CLASSIFICATION-PROTOCOL.md`.
2. Select only supported router values.
3. Call `scripts/route.sh`.
4. Use exactly the path returned by the router.
5. Write or update the document.
6. Stop.

官网文章仍按 `work-product + website + article` 分类；Router 会直接返回唯一文章目录 `03-Records/Published/Articles/`。

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

Load `references/AUTHORITY-GUIDE.md` only when changing canonical knowledge.
