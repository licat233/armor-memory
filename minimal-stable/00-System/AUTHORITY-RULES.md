---
type: "system"
status: "active"
authority: "canonical"
created: "2026-07-27"
updated: "2026-09-05"
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

A knowledge file without an explicit `authority` field is treated as `working`. Location inside `01-Knowledge/` does not by itself promote authority.

## Knowledge Quality Diagnostics

`armor-knowledge check` is a read-only diagnostic for `01-Knowledge/`.

It may report:

- missing authority as a warning;
- unsupported authority values as an error;
- `evidence` authority in Knowledge as a classification warning;
- verified or canonical knowledge without an explicit provenance marker as a warning;
- duplicate titles and possible canonical title collisions as warnings.

Warnings are investigation prompts, not automatic correction instructions. A duplicate title does not prove that two pages represent the same entity or that either page should be deleted.

The diagnostic must not:

- edit frontmatter;
- promote or demote authority;
- merge or delete pages;
- rewrite canonical knowledge;
- create a separate knowledge database or source of truth.

## Canonical Update Procedure

1. Read the current canonical document.
2. Identify the exact proposed change and the relevant source or reviewer basis.
3. Present the material change to the human before writing. When current and candidate files exist, use `armor-knowledge diff` to show the change.
4. Obtain explicit approval for the authority-changing or material canonical edit.
5. Update the document in its purpose-based location.
6. Verify the change against the relevant source or reviewer.
7. Keep the updated file as the current canonical version in its local metadata or document note.
8. Add a short changelog note describing what changed and why.

The diff helper is diagnostic only. It does not approve or apply changes.

## Short Changelog Requirement

Canonical or verified documents should include a short human-readable changelog section when changes materially alter meaning, routing guidance, or reusable knowledge.

Recommended format:

```text
Changelog
- 2026-07-27: Clarified deterministic routing for product manuals.
```

The base architecture intentionally avoids global drafts, lifecycle queues, freshness tiers, and promotion pipelines.
