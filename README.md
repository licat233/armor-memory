# ARMOR Minimal Stable

This repository is the implementation and maintenance layer for ARMOR's shared memory architecture. It stores the active router, tests, architecture documentation, Agent integration, and read-only knowledge-quality tooling. It does not store live ARMOR business memory.

## Identity

```text
Repository:
licat233/armor-memory

Shared Skill:
/Users/licat/AI-Agent-Skills/armor-memory

Active Vault:
/Users/licat/armor-vault
```

The architecture name is `ARMOR Minimal Stable`.

Do not invent a numeric successor name for this architecture unless an explicit architecture decision establishes one.

## Current Status

- Status: Production / Stable
- Active Vault: `/Users/licat/armor-vault`
- The current repository tree contains active Minimal Stable material only.
- Superseded architecture material is intentionally excluded from the working tree; Git history is the historical record.
- Knowledge-quality focused validation on 2026-09-05: `12 passed`
- Lifecycle-neutral routing is now the current architecture; the one-time live Vault path migration remains operational until executed locally.

## Architecture Flow

```text
Codex / Claude Code / Hermes Agent
                ↓
Shared Skill: armor-memory
                ↓
Router / explicit knowledge-quality tools
                ↓
ARMOR_VAULT_ROOT
                ↓
/Users/licat/armor-vault
```

- The Shared Skill defines memory behavior and routing discipline.
- The Router determines destination paths.
- Knowledge-quality checks are explicit, read-only diagnostics.
- `ARMOR_VAULT_ROOT` resolves the active Vault location.
- The Vault stores ARMOR business memory.
- This repository stores architecture, code, tests, and maintenance tools.

## Active Vault Structure

```text
armor-vault/
├── 00-System/
├── 01-Knowledge/
├── 02-Projects/
│   ├── Projects/
│   └── Workspaces/
├── 03-Records/
├── 04-Research/
├── 90-Inbox/
└── 99-Archive/
```

- `00-System/`: system rules, start points, and operational guidance
- `01-Knowledge/`: canonical business knowledge and reusable facts
- `02-Projects/Projects/`: stable home for named project work; no Active -> Completed move lifecycle
- `02-Projects/Workspaces/`: stable home for persistent domain/entity work and channel-content sources
- `03-Records/`: evidence of events, publications, meetings, journals, and communications
- `04-Research/`: notes and source collections for ongoing investigation
- `90-Inbox/`: explicitly unresolved material only
- `99-Archive/`: inactive material retained only when preserving history/reference is useful

## Core Principles

- Minimal structure over lifecycle complexity.
- Object type determines location.
- Directory location represents operational purpose, not lifecycle state.
- Draft and Proposal are statuses, not permanent root directories.
- Projects and canonical Knowledge remain separate.
- Skill controls behavior; Vault stores business memory.
- The Vault remains the sole durable knowledge source of truth.
- Derived tools must not become a second authoritative store.
- Human attention is reserved for material judgment, authority, ambiguity, and risk; routine metadata, routing, status updates, and deterministic file maintenance should be performed by the Agent.
- Do not require repeated human approval when the current instruction already authorizes the exact change.
- Do not create recurring human-maintained lifecycle queues or folder-move chores when stable routing or metadata can represent the same outcome.
- Business memory must not contain unrelated personal machine administration.
- Bulk changes must be bounded, checked for conflicts, and reversible when practical.
- Obsolete architecture copies are not retained in the current repository tree.
- Git history is used for explicit historical investigation instead of keeping deprecated instructions beside active rules.

## Human-Cost Policy

ARMOR Minimal Stable should minimize recurring human operating cost as document volume and team size grow.

Human involvement is justified when the system needs a real business decision, unresolved authority judgment, identity/scope clarification, or approval not already granted. Humans should not be assigned routine work such as choosing deterministic destinations, manually synchronizing status fields, repeatedly confirming an already-approved change, moving files between lifecycle folders, or cleaning Inbox items after the missing classification has already been supplied.

Prefer a one-time Agent-executed migration over a permanent human-maintained process when a directory or workflow design creates lifecycle housekeeping.

## Lifecycle-Neutral Routing

Current stable routing rules include:

```text
Named project work
-> 02-Projects/Projects/<project>/

Website article source
-> 02-Projects/Workspaces/Website/Articles/

Official social-copy source
-> 02-Projects/Workspaces/Marketing/Social-Media/

Actual publication evidence / requested snapshot
-> 03-Records/Published/
```

Website articles and official social copy each have one stable editable-source location. Draft, review, publication, update, or retirement status does not require moving the source file.

`03-Records/Published/` is an evidence layer. Do not route a newly written article or social post there merely because it is intended to be published.

## One-Time Live Vault Migration

The old named-project root was:

```text
02-Projects/Active/
```

The current root is:

```text
02-Projects/Projects/
```

The temporary migration helper is:

```bash
python3 minimal-stable/scripts/migrate-lifecycle-neutral.py --vault /Users/licat/armor-vault
```

That command is dry-run only. Apply only after reviewing the plan:

```bash
python3 minimal-stable/scripts/migrate-lifecycle-neutral.py \
  --vault /Users/licat/armor-vault \
  --apply
```

The helper fails before moving projects when destination name collisions exist. It does not bulk-migrate `03-Records/Published/` because legacy routing mixed true publication evidence with content merely created for publication; guessing would risk rewriting historical meaning.

After the live Vault migration is completed and verified, remove this temporary migration helper and its focused test from the active tree.

## Routing

Shared entry points:

```text
Skill:
/Users/licat/AI-Agent-Skills/armor-memory/SKILL.md

Router wrapper:
/Users/licat/AI-Agent-Skills/armor-memory/scripts/route.sh
```

The Router should be used before a persistent write when the destination is not already explicit.

Journal destinations resolve under:

```text
/Users/licat/armor-vault/03-Records/Journal/<year>/
```

The Router determines the destination path only. It does not silently create business content.

## Knowledge Quality

ARMOR Minimal Stable includes a deliberately small read-only knowledge-quality layer.

Agent entry point:

```bash
bash /Users/licat/AI-Agent-Skills/armor-memory/scripts/knowledge.sh check
```

Repository entry point:

```bash
python3 minimal-stable/scripts/armor-knowledge.py check
```

The `check` command scans only `01-Knowledge/` and reports authority, provenance, and possible duplicate-title issues. It does not edit, merge, delete, promote, or demote knowledge.

For a material canonical change, a current file and candidate file can be compared with:

```bash
python3 minimal-stable/scripts/armor-knowledge.py diff current.md candidate.md
```

The diff is diagnostic only. It does not create authority by itself. A current explicit user instruction or an explicitly designated authoritative source may already provide sufficient authority for the exact requested update; do not request duplicate confirmation.

Knowledge-quality maintenance is explicit-only. Ordinary reads and writes remain lightweight and do not trigger hidden full-Vault scans.

## Update Policy

ARMOR Minimal Stable does not perform automatic update discovery.

Updates are explicitly initiated by the human operator. Agents do not check repository versions, Skill versions, CHANGELOG files, or update status during normal memory tasks.

Update process:

1. The operator requests an update.
2. The Agent reads the active architecture instructions.
3. Relevant files are backed up when a change is destructive or broad.
4. Approved changes are applied.
5. Relevant tests and Agent verification are run.
6. The operator reviews the result.

Normal Agent sessions must not perform version checks. No background update process is used. No Agent may silently self-update.

## Development And Testing

Run tests from the repository root:

```bash
python3 -m pytest minimal-stable/tests -v
```

Current test areas are:

- deterministic routing
- Agent integration
- read-only knowledge quality
- temporary lifecycle-neutral migration safety

Focused suites:

```bash
python3 -m pytest minimal-stable/tests/test_armor_knowledge.py -q
python3 -m pytest minimal-stable/tests/test_lifecycle_neutral_migration.py -q
```

Knowledge-quality validation recorded earlier on 2026-09-05: `12 passed`.

Do not record a new full-suite baseline until the complete current suite has actually run in a real repository checkout or CI.

## Operational Rules

### Do

- Write new ARMOR memory only to `/Users/licat/armor-vault`.
- Use the shared Skill and Router.
- Keep Knowledge stable and reusable.
- Keep named project work in `02-Projects/Projects/<project>/` without lifecycle moves.
- Keep article/social source content in their lifecycle-neutral Workspaces homes.
- Store publication snapshots and historical evidence in Records.
- Let the Agent perform deterministic routing, already-authorized metadata updates, scoped conflict closure, and resolved-Inbox re-routing.
- Run knowledge-quality checks only when explicitly requested.
- Run relevant tests after architectural changes.
- Check for collisions before broad filesystem migrations.

### Do Not

- Do not recreate `Active/`, `Completed/`, or other lifecycle project roots.
- Do not route newly created article/social source content directly to `03-Records/Published/`.
- Do not require humans to maintain status fields or move files solely because lifecycle state changed.
- Do not ask for duplicate approval already contained in the current instruction.
- Do not add automatic update checks to normal Agent workflows.
- Do not silently overwrite existing Vault files without sufficient authority.
- Do not treat diagnostic warnings as permission to modify canonical knowledge.
- Do not mix personal machine maintenance into ARMOR business memory.
- Do not rename the shared Skill away from `armor-memory` until a separate naming decision is explicitly made.
- Do not keep obsolete architecture copies in the current tree merely for reference; use Git history when historical material is explicitly needed.

## Repository Layout

```text
.agent/
minimal-stable/
minimal-stable/00-System/
minimal-stable/scripts/
minimal-stable/tests/
AGENTS.md
CLAUDE.md
HERMES.md
README.md
CHANGELOG.md
```

`minimal-stable/scripts/`
Router, read-only knowledge-quality tooling, and temporary bounded migration tooling while an active migration is still pending.

`minimal-stable/tests/`
Automated verification for routing, Agent integration, knowledge-quality behavior, and active migration safety.

## History Policy

The current branch is an operational architecture tree, not an archive of every previous architecture generation.

Superseded architecture documents, completed migration-only tooling, old templates, and archived architecture copies are intentionally removed from the current tree once they are no longer operationally required. Git history remains available for explicit historical investigation or recovery.

This reduces instruction ambiguity and prevents old rules from being mistaken for current policy by humans or Agents.

## Final Authority Statement

`/Users/licat/armor-vault` is the sole active ARMOR business-memory Vault.

This `README.md` is the authoritative repository-level status document for ARMOR Minimal Stable.
