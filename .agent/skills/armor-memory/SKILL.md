---
name: armor-memory
description: >
  Classify and route persistent documents using ARMOR Minimal Stable.
  Use when an Agent creates, stores, records, researches, or updates
  a persistent document in the ARMOR Vault.
---

# ARMOR Memory Routing

## Use this Skill when

Use this Skill when a task creates, stores, modifies, records, researches, or classifies a persistent document in the ARMOR Vault.

Do not use it for:

- ordinary source-code edits
- temporary chat answers
- terminal output
- calculations
- disposable scratch files
- files outside the ARMOR Vault

## Workflow

1. Classify the task using `references/CLASSIFICATION-PROTOCOL.md`.
2. Select only supported router values.
3. Call `scripts/route.sh`.
4. Use exactly the path returned by the router.
5. Write or update the document.
6. Stop.

## Mandatory rules

- Never construct a destination path manually.
- Never add a new router value during ordinary work.
- Never route unverified content to Inbox merely because it is unverified.
- Inbox is allowed only through explicit `object=unresolved`.
- Draft is a status, not a destination.
- Do not run extra memory-maintenance operations after an ordinary write.

## Canonical knowledge

Load `references/AUTHORITY-GUIDE.md` only when changing canonical knowledge.

