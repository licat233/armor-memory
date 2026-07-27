---
type: "core"
memory_layer: "core"
status: "active"
authority: "ssot"
write_policy: "proposal_required"
created: "2026-07-27"
updated: "2026-07-27"
tags:
  - "authority"
  - "routing"
author_agent: "Codex"
confidence: "high"
---

# Authority Rules

ARMOR Minimal Stable separates operational location from truth status.

- `01-Knowledge/` stores reusable knowledge.
- `02-Projects/` stores work products and deliverables.
- `03-Records/` stores evidence of events, decisions, communications, publications, and received input.
- `04-Research/` stores external source material and research notes.
- `90-Inbox/` is for unresolved routing only.
- `99-Archive/` is for superseded or historical content.

Draft is a status, not a top-level destination.

The base architecture intentionally avoids global drafts, lifecycle queues, freshness tiers, and promotion pipelines.

