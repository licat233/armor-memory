# ARMOR Minimal Stable

This repository is the implementation and maintenance layer for ARMOR's shared memory architecture. It stores the router, tests, documentation, and migration tooling. It does not store live ARMOR business memory.

## Identity

```text
Repository:
licat233/armor-memory

Shared Skill:
/Users/licat/AI-Agent-Skills/armor-memory

Active Vault:
/Users/licat/armor-vault

Frozen Legacy Vault:
/Users/licat/Obsidian-V7.2-Legacy
```

The architecture name is `ARMOR Minimal Stable`.

Do not call this system `V8.0`.

## Current Status

- Status: Production / Stable
- Migration: Completed on 2026-07-28
- Active Vault: `/Users/licat/armor-vault`
- Legacy V7.2: Frozen and read-only
- Test baseline: `102 passed`

## Architecture Flow

```text
Codex / Claude Code / Hermes Agent
                ↓
Shared Skill: armor-memory
                ↓
Router
                ↓
ARMOR_VAULT_ROOT
                ↓
/Users/licat/armor-vault
```

- The Shared Skill defines memory behavior and routing discipline.
- The Router determines the destination path.
- `ARMOR_VAULT_ROOT` resolves the active Vault location.
- The Vault stores ARMOR business memory.
- This repository stores architecture, code, tests, and maintenance tools.
- The frozen V7.2 Vault is historical and read-only.

## Active Vault Structure

```text
armor-vault/
├── 00-System/
├── 01-Knowledge/
├── 02-Projects/
├── 03-Records/
├── 04-Research/
├── 90-Inbox/
└── 99-Archive/
```

- `00-System/`: system rules, start points, and operational guidance
- `01-Knowledge/`: canonical business knowledge and reusable facts
- `02-Projects/`: active projects and persistent workspaces
- `03-Records/`: published records, meetings, journals, and communications
- `04-Research/`: notes and source collections for ongoing investigation
- `90-Inbox/`: explicitly unresolved material only
- `99-Archive/`: inactive Minimal Stable material retained for reference

## Core Principles

- Minimal structure over lifecycle complexity.
- Object type determines location.
- Draft and Proposal are statuses, not permanent root directories.
- Projects and canonical Knowledge remain separate.
- Skill controls behavior; Vault stores business memory.
- Business memory must not contain unrelated personal machine administration.
- Bulk changes must be backed up, manifest-driven, and reversible.
- Do not recreate V7.2 lifecycle architecture.
- Do not call the system V8.0.

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

## Update Policy

ARMOR Minimal Stable does not perform automatic update discovery.

Updates are explicitly initiated by the human operator.
Agents do not check repository versions, Skill versions, CHANGELOG files,
or update status during normal memory tasks.

Update process:

1. The operator requests an update.
2. The Agent reads the specific update instructions.
3. Relevant files are backed up.
4. Approved changes are applied.
5. Tests and Agent verification are run.
6. The operator reviews the result.

Normal Agent sessions must not perform version checks.
Normal memory operations must not read update metadata.
No automatic update notification is required.
No background update process is used.
No Agent may silently self-update.

`VERSION` and `CHANGELOG.md` may exist as human-facing release records, but ordinary memory work must not depend on them.

## Development And Testing

Run tests from the repository root:

```bash
cd /Volumes/MacData/projects/AI-Agent-Memory-Architecture
python3 -m pytest minimal-stable/tests -v
```

Current accepted baseline: `102 passed`

Run the test suite after changes to routing, Vault path handling, Skill integration, or migration tooling.

The verified baseline should be updated only after a successful test run.

## Backup And Rollback

Final V7.2 archive:

`/Users/licat/ARMOR-Migration-Backups/armor-v7.2-final-20260728-212459.tar.gz`

SHA-256:

`b646b7c56575f86d583bb7e1c1fddf412bce3b269be70945b0575502b87f90b6`

Rollback guide:

`/Users/licat/ARMOR-Migration-Reports/final-acceptance-20260728-172412/ROLLBACK-V7.2-FREEZE.md`

Rollback must never overwrite `/Users/licat/armor-vault`.

## Legacy Status

`/Users/licat/Obsidian-V7.2-Legacy` remains frozen, read-only, and available only for historical verification or disaster recovery.

It must not be used as the active ARMOR business-memory source.

## Operational Rules

### Do

- Write new ARMOR memory only to `/Users/licat/armor-vault`.
- Use the shared Skill and Router.
- Keep Knowledge stable and reusable.
- Store active work in Projects.
- Store historical evidence in Records.
- Run tests after architectural changes.
- Back up files before bulk changes.

### Do Not

- Do not write to `/Users/licat/Obsidian-V7.2-Legacy`.
- Do not restore V7.2 Hooks, Skill, or Router behavior.
- Do not recreate `90-Drafts`, `93-Proposals`, or other V7.2 lifecycle roots.
- Do not add automatic update checks to normal Agent workflows.
- Do not silently overwrite existing Vault files.
- Do not mix personal machine maintenance into ARMOR business memory.
- Do not rename the shared Skill away from `armor-memory`.

## Repository Layout

```text
minimal-stable/
minimal-stable/00-System/
minimal-stable/scripts/
minimal-stable/tests/
shared/
shared/frontmatter/
shared/document-map/
```

`minimal-stable/scripts/`
Router and migration utilities.

`minimal-stable/tests/`
Automated verification for routing, migration safety, and Agent integration.

`shared/`
Shared standards and templates used by the architecture repository.

## Migration History

- 513 effective business files were migrated.
- The old Vault was backed up and frozen.
- Active V7.2 instructions and active path dependencies were reduced to zero.
- Codex, Claude Code, and Hermes Agent all passed post-freeze verification.
- Detailed reports are stored under `/Users/licat/ARMOR-Migration-Reports/`.

## Final Authority Statement

`/Users/licat/armor-vault` is the sole active ARMOR business-memory Vault.

This `README.md` is the authoritative repository-level status document for ARMOR Minimal Stable.
