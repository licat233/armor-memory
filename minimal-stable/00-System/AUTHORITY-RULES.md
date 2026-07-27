---
type: "system"
status: "active"
authority: "canonical"
created: "2026-07-27"
updated: "2026-07-27"
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

## Status Meanings

- `working`: in progress, editable, not yet relied on as a stable reference
- `verified`: checked against the relevant source or review step
- `canonical`: the current reference version for that document or knowledge page
- `evidence`: a record that documents what happened or what was received

## Canonical Update Procedure

1. Edit the document in its purpose-based location.
2. Verify the change against the relevant source or reviewer.
3. Mark the updated file as the current canonical version in its local metadata or document note.
4. Add a short changelog note describing what changed and why.

## Short Changelog Requirement

Canonical or verified documents should include a short human-readable changelog section when changes materially alter meaning, routing guidance, or reusable knowledge.

Recommended format:

```text
Changelog
- 2026-07-27: Clarified deterministic routing for product manuals.
```

The base architecture intentionally avoids global drafts, lifecycle queues, freshness tiers, and promotion pipelines.
