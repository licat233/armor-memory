# Uninstall V7.2

This document distinguishes four stages:

- `disable`
- `freeze`
- `archive`
- `permanent delete`

The workflow is intentionally conservative and reversible until the final optional delete step.

## Disable

Disable means agents stop writing to V7.2.

Checklist:

1. Run `minimal-stable/scripts/audit-v72-dependencies.py`.
2. Remove or update references to V7.2 directories in agent instruction files and wrappers.
3. Confirm all persistent document writes now use Minimal Stable.

## Freeze

Freeze means the V7.2 Vault remains available but becomes legacy read-only verification storage.

Checklist:

1. Rename the Vault to a legacy name such as `Obsidian-V7.2-Legacy`.
2. Add `DEPRECATED.md`.
3. Mark the directory read-only using the local filesystem workflow preferred on the machine.
4. Re-run the dependency audit and verify no active agent write references remain.

## Archive

Archive means packaging a frozen backup while still keeping restore capability.

```bash
tar -czf armor-v7.2-backup-YYYY-MM-DD.tar.gz <legacy-vault>
shasum -a 256 armor-v7.2-backup-YYYY-MM-DD.tar.gz
```

Checklist:

1. Store the archive in a safe backup location.
2. Save the SHA-256 checksum alongside the archive.
3. Keep the frozen Vault available until migration verification is complete.

## Permanent Delete

Permanent deletion is optional and must be the final step.

Do not automate it in this repository.

Required conditions:

1. migration validation completed successfully
2. no unresolved critical files remain
3. no active agent dependencies on V7.2 remain
4. backup archive verified by checksum
5. explicit user confirmation received

Only after all five conditions are met should a human choose whether to delete the legacy Vault.

