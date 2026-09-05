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

`status` metadata is optional operational metadata. It must not become a recurring human-maintenance obligation. If a status change is useful and is directly implied by the task the Agent is already performing, the Agent should update it in the same operation rather than asking the human to maintain it manually.

When several materials discuss the same mature topic, an explicit canonical Knowledge page is the default current-reference entry point. Project documents, Records, Research, and other supporting material do not become peer current-truth authorities merely because they discuss the same subject.

## Human Involvement Boundary

Human attention is reserved for material judgment, not file administration.

A human decision is required when:

- competing authoritative claims cannot be resolved from an already designated source;
- identity, scope, meaning, or business intent remains materially ambiguous;
- a canonical change lacks sufficient authority in the current instruction or source basis;
- the action would make a material business decision that the Agent was not already authorized to make.

Human action is not required merely to:

- choose a deterministic destination already defined by the Router;
- change routine status metadata;
- move a file because a lifecycle label changed;
- repeat approval already stated in the current instruction;
- close a conflict after the human has already resolved it;
- re-route a previously unresolved item after the user supplies the missing classification information;
- perform mechanical cleanup that follows deterministically from an approved scoped task.

The system should prefer one human decision that becomes durable over repeated future escalations of the same settled question.

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
3. Determine whether authority is already sufficient. The user's current instruction counts as approval when it explicitly approves the exact change, resolves the conflict, or designates the conclusion as the current reference. An explicitly designated authoritative source may also provide sufficient authority for an unambiguous requested update.
4. Ask the human only if a material judgment remains unresolved. Do not request duplicate confirmation.
5. Update the document in its purpose-based location.
6. Verify the change against the relevant source or reviewer basis.
7. Keep the updated file as the current canonical version in its local metadata or document note.
8. Add a short changelog note describing what changed and why.
9. If the update resolves a knowledge conflict, complete the scoped conflict-closure steps in the same task instead of leaving follow-up cleanup to the human.

The diff helper is diagnostic only. It does not approve or apply changes by itself.

## Conflict Resolution And Closure

A conflict is not closed merely because a human answered the Agent in the current conversation.

When the human explicitly resolves competing claims, that decision should be converted into durable current Knowledge so the same settled question is not repeatedly escalated.

After an explicit resolution:

1. Apply the approved conclusion to the intended current Knowledge target.
2. Preserve the source/reviewer basis for the resolution.
3. Search the relevant `01-Knowledge/` scope for other current Knowledge that still presents the rejected claim as current truth.
4. Reconcile those competing current claims when identity and scope are clear.
5. If reconciliation is unsafe or ambiguous, report that conflict closure is incomplete instead of silently choosing or merging.
6. Do not rewrite `03-Records/`, `04-Research/`, historical published material, or other evidence merely to make past documents match the new current conclusion.

A later Agent should rely on the closed current Knowledge unless materially new evidence reopens the issue.

This rule is intended to make human judgment durable, not to authorize automatic canonical rewriting without sufficient authority.

## Topic Convergence

Multiple source or working documents may legitimately coexist. Knowledge should nevertheless converge when a topic has matured enough that humans or Agents need a clear default answer to "what does ARMOR currently know, believe, or follow?"

Topic convergence follows these rules:

- prefer an existing canonical Knowledge entry as the default current-reference page;
- create or update Knowledge only when the topic is reusable, repeatedly queried, operationally important, supported by multiple materials, or has produced recurring ambiguity/conflict;
- compile ARMOR's current conclusion rather than a transcript-style summary of every source's opinion;
- preserve unresolved questions as unresolved instead of inventing consensus;
- supporting Project, Record, and Research documents remain evidence/history and should not compete with the canonical entry as default current truth;
- do not create new lifecycle roots, review queues, or parallel "final" directories merely to represent convergence.

The purpose of convergence is to reduce repeated interpretation and repeated human reading, not to produce more documents for their own sake.

## Short Changelog Requirement

Canonical or verified documents should include a short human-readable changelog section when changes materially alter meaning, routing guidance, or reusable knowledge.

Recommended format:

```text
Changelog
- 2026-07-27: Clarified deterministic routing for product manuals.
```

The base architecture intentionally avoids global drafts, lifecycle queues, freshness tiers, and promotion pipelines.
