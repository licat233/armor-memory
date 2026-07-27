---
type: "core"
memory_layer: "core"
status: "active"
authority: "ssot"
write_policy: "proposal_required"
created: "2026-07-27"
updated: "2026-07-27"
tags:
  - "routing"
  - "deterministic"
author_agent: "Codex"
confidence: "high"
---

# Routing Rules

## Rule 1: Work Product

When the task is to create, write, draft, edit, improve, design, prepare, or generate a deliverable:

`-> 02-Projects/`

If there is an active named project:

`-> 02-Projects/Active/<project>/`

If there is no named project:

`-> 02-Projects/Workspaces/<domain>/`

## Rule 2: Record

When the task is to save, record, preserve, archive, or document something that already happened or was received:

`-> 03-Records/`

## Rule 3: Knowledge

When the task explicitly asks to remember, organize, summarize into reusable knowledge, define a long-term rule, or maintain a knowledge page:

`-> 01-Knowledge/`

## Rule 4: Research

When the task is to investigate, research, compare external information, gather sources, or analyze an external topic:

`-> 04-Research/`

External source copies:

`-> 04-Research/Sources/`

Research notes and conclusions:

`-> 04-Research/Notes/`

## Rule 5: Inbox

Use `90-Inbox/` only when the task purpose cannot be determined.

Required metadata:

```yaml
routing_status: "unresolved"
routing_reason: "<specific reason>"
```

Do not use Inbox merely because something is unverified.

## Priority Order

1. Explicit active project
2. Explicit persistent workspace
3. Record of an event or received content
4. Explicit long-term knowledge request
5. External research request
6. Inbox only if classification is unresolved

