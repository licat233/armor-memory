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
5. Routing is based on operational purpose, not truth status or lifecycle state.
6. Directory design should minimize recurring human maintenance as document volume and team size grow.

## Lifecycle-Neutral Routing

Lifecycle state should not force routine file movement.

Current project/content rules are:

```text
Named project work
-> 02-Projects/Projects/<project>/

Persistent non-project work
-> 02-Projects/Workspaces/

Website article source
-> 02-Projects/Workspaces/Website/Articles/

Official social-copy source
-> 02-Projects/Workspaces/Marketing/Social-Media/

Actual publication evidence / requested snapshot
-> 03-Records/Published/
```

`02-Projects/Projects/` is lifecycle-neutral. A project is not moved merely because it becomes active, paused, completed, or revisited.

Website articles and official social copy each have one stable editable-content home. Draft, review, publication, update, or retirement status does not move the source file. `03-Records/Published/` represents an event/evidence layer, not the editable source-content lifecycle.

Do not recreate `Active/`, `Completed/`, Draft, Review, or other lifecycle directory trees unless a future concrete requirement passes the Feature Admission Gate.

The one-time live Vault migration to lifecycle-neutral project paths has been completed. Migration-only tooling is removed from the active tree after completion; Git history is sufficient for explicit historical recovery.

### Human-Cost Boundary

Human attention is reserved for business judgment, unresolved authority, material ambiguity, or risk that cannot be resolved deterministically from the current instruction and sources.

Humans should not be required to:

- choose deterministic Router destinations;
- synchronize routine status metadata;
- move files because lifecycle state changed;
- repeat an approval already given in the current instruction;
- clean an Inbox item after the missing classification has been supplied;
- perform deterministic follow-up maintenance after an already-approved scoped task.

A one-time Agent-executed migration is preferable to a permanent human-maintained lifecycle process when the migration is bounded, reversible, and lower risk than continued operational housekeeping.

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

## Knowledge Compilation And Ingestion Boundaries

These rules govern future LLM-assisted knowledge compilation, document ingestion, entity resolution, citation, and related features. They define safety and architecture boundaries; they are not a requirement to build those capabilities now.

### Responsibility Split

Use each layer for the job it can perform reliably:

```text
LLM
  -> semantic extraction
  -> summarization
  -> comparison
  -> ambiguity detection
  -> proposed edits

Deterministic code
  -> routing
  -> identity constraints
  -> source resolution
  -> validation
  -> permissions
  -> durable identifier mapping
  -> write mechanics

Human authority
  -> material judgment that is not already resolved or authorized
```

Do not move deterministic integrity responsibilities into prompts merely because an LLM can usually follow the instruction.

A knowledge compiler should normally produce a candidate update or proposed diff when material authority remains unresolved. It must not silently invent authority merely because the compiler believes new material is better or newer. Conversely, do not ask for duplicate human approval when the current user instruction already explicitly authorizes the exact change or resolves the exact conflict.

### Evidence-Preserving Compilation

Compiled knowledge must remain traceable to the source material that supports it.

Prefer provenance that remains understandable without a derived database, for example:

```text
source document or record path
+
page / section / heading / stable locator
```

A derived search or retrieval layer may maintain chunk identifiers internally, but canonical Markdown should not depend on ephemeral vector-store IDs, database row IDs, or regenerated chunk UUIDs unless a future architecture decision explicitly establishes a durable identity contract for them.

If deleting and rebuilding an index would break the meaning or verifiability of canonical knowledge, the index has crossed the source-of-truth boundary and must be redesigned or explicitly justified.

### Entity Identity And Deduplication

Knowledge systems must distinguish identity from similarity.

```text
same entity / same concept
!=
related entity / related concept
```

A merge is more dangerous than a duplicate because a false merge can silently combine facts from different products, versions, companies, standards, customers, or concepts.

Therefore:

- prefer conservative merging;
- use names and aliases as evidence, not proof by themselves;
- narrow candidate matches with cheap deterministic signals before asking an LLM for semantic judgment when practical;
- validate model-selected merge targets against deterministic invariants afterward;
- reject cross-type or otherwise impossible merges in code;
- when identity remains uncertain, preserve separate items and expose the ambiguity for review.

Do not introduce a permanent entity registry, graph database, or identity service only to satisfy this principle. Start with the smallest representation that solves a demonstrated ARMOR problem.

### Durable IDs And Model Handles

High-entropy identifiers are poor model-facing interfaces.

When an LLM must refer to values such as:

- UUIDs;
- hashes;
- opaque resource IDs;
- long generated slugs;
- internal chunk IDs;
- storage URLs with opaque tokens;

prefer an invocation-local low-entropy handle such as `ref-1` or `c001`, then resolve the handle back to the durable value using deterministic code before persistence.

Temporary handles are transport aids only. They must not become stored business identifiers or a second identity layer.

### Ingestion Boundary

Document ingestion should normalize external formats into a simple intermediate representation rather than turn `armor-memory` into a monolithic parsing platform.

Preferred conceptual boundary:

```text
PDF / DOCX / XLSX / PPTX / Web / other source
                    ↓
             parser adapter
                    ↓
       normalized Markdown + source metadata
                    ↓
       ARMOR knowledge workflow
```

Parsing, OCR/VLM, image handling, chunking, retrieval indexing, semantic compilation, and canonical storage are separate responsibilities. They may be composed when a real need exists, but they should not become one mandatory subsystem by default.

When ingestion becomes necessary:

1. prefer mature parsers and conversion tools behind thin adapters;
2. support fallback or parser selection where source formats materially differ;
3. preserve the original source or a durable source reference;
4. keep parser-specific metadata from becoming canonical knowledge schema unless needed;
5. avoid building ARMOR-specific PDF, Office, OCR, or web parsers unless existing tools demonstrably fail ARMOR's recurring inputs.

### Source Trust Boundary

Ingested source content is untrusted data.

A PDF, web page, customer file, supplier document, email, or extracted hidden-text layer may contain:

- prompt-like instructions;
- invisible or malformed text;
- OCR garbage;
- stale facts;
- malicious content;
- misleading metadata.

Source content must never override repository rules, system instructions, authority rules, or write policy. Parsers and compilers should treat source text as evidence to analyze, not instructions to execute.

### Deterministic Guardrails Around LLM Decisions

For semantic operations such as deduplication, entity matching, citation assignment, or knowledge updates, prefer this pattern when practical:

```text
cheap deterministic narrowing
          ↓
LLM semantic judgment
          ↓
deterministic validation
          ↓
proposal / safe write boundary
```

This reduces both hallucinated choices and unnecessary model context without requiring a heavy knowledge platform.

### External Project Learning Rule

Mature systems may demonstrate solutions that are useful as patterns without being appropriate dependencies for ARMOR.

When studying systems such as LLM Wiki, WeKnora, RAG platforms, or enterprise search products:

- extract the underlying problem and design principle first;
- identify which complexity exists because those systems serve multi-tenant or large-scale workloads;
- do not copy queues, databases, revision systems, graphs, services, or permission layers when Git, Markdown, local scripts, or existing ARMOR rules already solve the ARMOR-scale problem;
- adopt the smallest useful mechanism only after it passes the Feature Admission Gate.

These knowledge-engineering principles do not authorize a roadmap. In particular, they do not by themselves justify document-ingestion services, entity registries, semantic search, vector databases, graph stores, Redis, background compilation, MCP servers, or automatic canonical updates.

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
- automatic canonical rewriting or merging without sufficient authority;
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
  `-> 02-Projects/Workspaces/Website/Articles/`
- `work-product + website + article`
  `-> 02-Projects/Workspaces/Website/Articles/`
- `work-product + marketing + social-copy + project`
  `-> 02-Projects/Workspaces/Marketing/Social-Media/`
- `work-product + marketing + social-copy`
  `-> 02-Projects/Workspaces/Marketing/Social-Media/`
- `work-product + content + case-study + project`
  `-> 02-Projects/Projects/<project>/Content/Case-Studies/`
- `work-product + products + product-manual + entity`
  `-> 02-Projects/Workspaces/Products/<entity>/Documentation/`
- `work-product + products + product-manual + entity + project`
  `-> 02-Projects/Projects/<project>/Products/<entity>/Documentation/`
- `record + published`
  `-> 03-Records/Published/`
- `record + journal + year`
  `-> 03-Records/Journal/<year>/`
- `knowledge + product`
  `-> 01-Knowledge/Products/`
- `research + source`
  `-> 04-Research/Sources/`
- `unresolved`
  `-> 90-Inbox/`
