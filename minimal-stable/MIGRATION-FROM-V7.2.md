# Migrate From V7.2

This workflow migrates an active ARMOR V7.2 Vault into ARMOR Minimal Stable without modifying or deleting the source Vault.

Current known source example on this machine:

```text
~/Obsidian
```

The scripts do not hard-code this path. Always pass explicit `--source`, `--target`, and `--report-dir` arguments.

## Goals

1. Inventory V7.2.
2. Produce deterministic migration proposals.
3. Copy approved content into Minimal Stable.
4. Validate file integrity and migration completeness.
5. Freeze V7.2 as read-only.
6. Remove Agent dependencies on V7.2.
7. Archive V7.2 safely.

## Default Mapping

```text
00-Core             -> archive only
01-Facts            -> 01-Knowledge
02-Rules            -> 01-Knowledge/Rules
03-Insights         -> 01-Knowledge/Insights
04-Research         -> 04-Research
05-Projects         -> 02-Projects
06-Records          -> 03-Records
70-Schemas          -> archive only
80-Indexes          -> do not migrate by default
81-Dashboards       -> do not migrate by default
90-Drafts           -> classify individually
91-Inbox            -> review individually
92-Logs             -> archive only
93-Proposals        -> review individually
94-Review-Queues    -> review individually
99-Archive          -> 99-Archive/V7.2
```

## Dry Run First

Dry-run is the default safe starting point and does not write to either Vault.

```bash
python3 minimal-stable/scripts/migrate-v72.py \
  --source <v7.2-vault> \
  --target <minimal-stable-vault> \
  --report-dir <report-directory> \
  --dry-run
```

Dry-run generates:

- `inventory.json`
- `proposed-moves.csv`
- `conflicts.csv`
- `unresolved.csv`
- `ignored.csv`
- `metadata-cleanup.csv`
- `link-audit.csv`
- `summary.md`

## Apply Copy

Formal migration requires `--apply`:

```bash
python3 minimal-stable/scripts/migrate-v72.py \
  --source <v7.2-vault> \
  --target <minimal-stable-vault> \
  --report-dir <report-directory> \
  --apply
```

Apply rules:

- copy files, do not move source files
- never overwrite an existing target
- calculate SHA-256 before and after copying
- stop on hash mismatch
- support safe resume through `copied-files.csv`
- do not rewrite Markdown content in the first pass
- do not auto-merge files
- preserve deterministic substructure where supported
- record provenance in reports, not by changing source content

## Complex Folders

These folders are not auto-assigned:

- `90-Drafts`
- `91-Inbox`
- `93-Proposals`
- `94-Review-Queues`

They remain in `unresolved.csv` until individually reviewed.

## Frontmatter And Links

The migration report identifies legacy metadata such as:

- `memory_layer`
- `permission_class`
- `write_policy`
- `retrieval_scope`
- `freshness_class`
- `proposal_type`
- `review_owner`
- `author_agent`
- `confidence`

The first pass does not remove those fields.

The migration report also audits Markdown for legacy V7.2 references such as `00-Core`, `01-Facts`, `02-Rules`, `03-Insights`, `05-Projects`, and `06-Records`.

## Validation Checklist

1. Review `summary.md`.
2. Review `conflicts.csv`.
3. Review `unresolved.csv`.
4. Confirm copied-file hashes in `copied-files.csv`.
5. Confirm legacy links listed in `link-audit.csv`.
6. Run dependency audit before freezing the old Vault.

## Freeze Procedure

After migration validation:

1. Rename the old Vault to a legacy read-only name.
2. Add a `DEPRECATED.md` file explaining that the Vault is frozen for verification only.
3. Remove Agent write references to the V7.2 Vault.
4. Keep the old Vault available for hash and content verification.
5. Confirm Hermes, Claude Code, and Codex point to Minimal Stable instead.

## Archive Procedure

After freeze:

```bash
tar -czf armor-v7.2-backup-YYYY-MM-DD.tar.gz <legacy-vault>
shasum -a 256 armor-v7.2-backup-YYYY-MM-DD.tar.gz
```

Do not delete the source as part of this workflow.

