# ARMOR Minimal Stable

ARMOR Minimal Stable is the active ARMOR shared-memory architecture.

The live business-memory Vault is outside this repository and is resolved through `ARMOR_VAULT_ROOT`.

Start with:

- `00-System/START-HERE.md`
- `00-System/ROUTING-RULES.md`
- `00-System/AUTHORITY-RULES.md`
- `ARCHITECTURE.md`

Core implementation:

- `scripts/armor-route.py` — deterministic lifecycle-neutral destination routing
- `scripts/armor-knowledge.py` — read-only knowledge-quality checks and diff preview
- `scripts/migrate-lifecycle-neutral.py` — temporary dry-run-first migration for `02-Projects/Active/ -> 02-Projects/Projects/`
- `tests/` — routing, Agent integration, knowledge-quality, and active migration-safety tests

Current routing principles:

- named project work lives under `02-Projects/Projects/<project>/` without Active/Completed lifecycle moves;
- website article source content lives under `02-Projects/Workspaces/Website/Articles/`;
- official social source content lives under `02-Projects/Workspaces/Marketing/Social-Media/`;
- `03-Records/Published/` stores actual publication evidence or explicitly requested snapshots.

Knowledge-quality maintenance is explicit-only. It does not run automatically after ordinary Vault reads or writes and does not modify canonical knowledge.

The lifecycle-neutral migration tool is temporary active tooling. Remove it and its focused test after the live Vault migration is complete and verified.

Superseded architecture material is not retained in the current tree. Use Git history only when an explicit historical investigation is required.
