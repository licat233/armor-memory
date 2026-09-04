---
type: "system"
status: "active"
created: "2026-07-27"
updated: "2026-09-05"
---

# ARMOR Minimal Stable Architecture

ARMOR Minimal Stable is a deterministic routing model for shared LLM workflows.

Its purpose is not to classify free-form language. Its purpose is to map structured routing inputs to stable paths.

## Design Rules

1. The router accepts only closed enums.
2. Unknown enum values fail immediately through `argparse choices=`.
3. Missing required fields fail immediately.
4. `90-Inbox/` is reachable only through explicit `--object unresolved`.
5. Routing is based on operational purpose, not truth status.

## Feature Admission Gate

Minimal Stable must not grow by accumulating every capability that is technically possible or available in other knowledge systems.

A proposed feature is admitted only when its expected operational benefit is clearly greater than the complexity, failure risk, data-integrity risk, and long-term maintenance burden it introduces.

Before adding a feature, service, database, index, automation, schema, workflow, dependency, or background process, answer these questions:

1. **Concrete need** — What recurring ARMOR problem does this solve? A speculative future use case is not enough by itself.
2. **Benefit** — What becomes materially more reliable, faster, safer, easier, or more capable after the change?
3. **Simpler alternative** — Can the same outcome be achieved by an existing component, a smaller rule change, a script, or a derived artifact?
4. **Failure modes** — What new ways can the system fail, become inconsistent, expose data, or silently produce incorrect knowledge?
5. **Maintenance cost** — What must now be installed, upgraded, monitored, backed up, repaired, migrated, or understood by future maintainers?
6. **Truth integrity** — Does the feature create a second authoritative store or duplicate facts that already belong in the Vault?
7. **Reversibility** — Can the feature be removed, rebuilt, or replaced without losing or corrupting canonical ARMOR knowledge?
8. **Net value** — Is the benefit clearly greater than the combined risk and maintenance cost?

If the answer to the final question is not clearly yes, the default decision is:

```text
Not now
```

`Not now` is a valid architecture outcome, not a missing feature.

### Source-of-Truth Boundary

The ARMOR Vault is the durable knowledge source of truth.

Optional infrastructure such as:

- search indexes
- embeddings
- vector stores
- caches
- generated registries
- relationship graphs
- derived databases

must remain derived and rebuildable from the Vault unless a future explicit architecture decision establishes a different boundary.

Do not allow an optional subsystem to silently become a second source of truth. If two persistent systems must independently store authoritative facts, the proposal must first justify the synchronization model, conflict policy, backup and recovery behavior, and additional maintenance cost.

### Infrastructure Budget

New persistent infrastructure carries a higher admission threshold than a file, rule, or script change.

Introducing a new database, service, daemon, server, background job, network dependency, runtime, or external platform requires an architecture note that states:

- the concrete ARMOR need;
- why the current system is insufficient;
- simpler alternatives considered;
- operational dependencies;
- failure and data-integrity risks;
- backup and recovery requirements;
- rollback or removal path;
- expected ongoing maintenance;
- the final benefit-versus-cost judgment.

A feature must not be added merely because a mature external project includes it. External projects are references from which ARMOR may adopt the smallest useful pattern.

### Preferred Decision Order

When solving a new knowledge-system requirement, prefer this order:

1. Reuse the current ARMOR Vault structure or rules.
2. Extend an existing ARMOR component with a small, testable change.
3. Add a rebuildable local script, generated file, or derived index.
4. Integrate a lightweight external component only when the previous options are insufficient.
5. Add a persistent service or new data store only when its benefit clearly justifies its operational cost.

Correctness, recoverability, and long-term knowledge integrity take priority over feature count.

## Knowledge Quality Capability

The first post-routing capability added to Minimal Stable is intentionally narrow: read-only knowledge-quality diagnostics.

The implementation is one standard-library Python tool:

```text
scripts/armor-knowledge.py
```

It exposes two commands:

```text
check
  -> scan 01-Knowledge only
  -> report authority/provenance/duplicate-title diagnostics
  -> never modify the Vault

diff
  -> compare a current Markdown file with a candidate file
  -> show a unified diff
  -> never approve or apply the change
```

### Why This Capability Is Admitted

Benefit:

- makes missing or invalid authority visible;
- makes weak provenance on verified/canonical pages visible;
- identifies possible duplicate knowledge pages before they become harder to manage;
- gives humans a concrete diff before material canonical edits;
- creates a machine-readable JSON diagnostic without creating another database.

Cost and risk:

- one Python script, one thin Agent wrapper, and focused tests;
- Python standard library only;
- no persistent derived state;
- no daemon, scheduler, service, database, embedding model, or network dependency;
- diagnostics can produce false positives, so uncertain findings remain warnings.

Net decision:

```text
Admit
```

The benefit is materially greater than the operational cost, and removal of the tool would not affect the Vault or canonical knowledge.

### Diagnostic Severity Boundary

Hard errors are reserved for conditions that are clearly invalid under current Minimal Stable rules, such as an unsupported explicit authority value or a file that cannot be read.

Advisory warnings include:

- missing authority, because retrieval already falls back to `working`;
- `evidence` authority found inside Knowledge;
- verified/canonical pages without an explicit provenance marker;
- duplicate titles;
- multiple canonical pages with the same normalized title.

A title collision is not proof that two pages represent the same entity. The tool must not infer deletion, merging, demotion, or promotion from a warning.

### Explicit-Only Operation

Knowledge-quality checks are not part of ordinary reads or writes.

They run only when explicitly requested for audit, diagnosis, review, or knowledge maintenance. This avoids turning a simple memory operation into a hidden full-Vault maintenance workflow.

### Deferred Capabilities

The following remain `Not now` until a concrete ARMOR problem demonstrates that the existing approach is insufficient:

- semantic duplicate detection using embeddings;
- natural-language fact conflict detection;
- automatic canonical rewriting or merging;
- automatic authority promotion/demotion;
- vector database or semantic-search service;
- knowledge graph / GraphRAG;
- persistent health database or dashboard backend;
- scheduled or background Vault scanning;
- full document-ingestion platform;
- MCP server solely for knowledge-quality tooling.

These capabilities may be revisited individually through the Feature Admission Gate. They are not bundled into a future version by default.

## Required Deliverables

This implementation includes:

- `00-System/START-HERE.md`
- `00-System/ROUTING-RULES.md`
- `00-System/AUTHORITY-RULES.md`
- `00-System/DIRECTORY-GUIDE.md`
- `00-System/ROUTING-TESTS.md`
- `scripts/armor-route.py`
- `scripts/armor-knowledge.py`
- `tests/test_armor_route.py`
- `tests/test_armor_knowledge.py`

## Router Interface

```bash
python3 scripts/armor-route.py \
  --object work-product \
  --domain website \
  --artifact article \
  --project armor-website
```

Supported enums:

- `object`: `work-product`, `record`, `knowledge`, `research`, `unresolved`
- `domain`: `website`, `content`, `marketing`, `products`, `operations`
- `artifact`: `article`, `landing-page`, `case-study`, `blog-post`, `report`, `campaign`, `email-sequence`, `social-copy`, `product-manual`, `spec-sheet`, `price-list`, `process-doc`, `checklist`, `internal-report`
- `record-type`: `meeting`, `email`, `conversation`, `journal`, `feedback`, `published`
- `knowledge-type`: `company`, `brand`, `product`, `customer`, `rule`, `insight`
- `research-kind`: `source`, `note`

## Name Normalization

Project and entity names are normalized with this exact procedure:

1. Apply Unicode `NFKC` normalization.
2. Trim leading and trailing whitespace.
3. Convert to lowercase.
4. Replace spaces and underscores with `-`.
5. Collapse repeated hyphens into a single hyphen.
6. Reject empty results.

Rejected inputs:

- absolute paths
- names containing `/` or `\`
- names containing `..`
- shell metacharacters such as `;`, `&`, `|`, `<`, `>`, `$`, `` ` ``, `!`

## Deterministic Examples

- `work-product + website + article + project`
  `-> 03-Records/Published/Articles/`
- `work-product + website + article`
  `-> 03-Records/Published/Articles/`
- `work-product + marketing + social-copy + project`
  `-> 03-Records/Published/Social-Media/`
- `work-product + marketing + social-copy`
  `-> 03-Records/Published/Social-Media/`
- `work-product + products + product-manual + entity`
  `-> 02-Projects/Workspaces/Products/<entity>/Documentation/`
- `record + journal + year`
  `-> 03-Records/Journal/<year>/`
- `knowledge + product`
  `-> 01-Knowledge/Products/`
- `research + source`
  `-> 04-Research/Sources/`
- `unresolved`
  `-> 90-Inbox/`
