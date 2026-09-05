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
- `tests/` — routing, Agent integration, and knowledge-quality tests

Current routing principles:

- named project work lives under `02-Projects/Projects/<project>/` without Active/Completed lifecycle moves;
- website article source content lives under `02-Projects/Workspaces/Website/Articles/`;
- official social source content lives under `02-Projects/Workspaces/Marketing/Social-Media/`;
- `03-Records/Published/` stores actual publication evidence or explicitly requested snapshots.

Knowledge-quality maintenance is explicit-only. It does not run automatically after ordinary Vault reads or writes and does not modify canonical knowledge.

The one-time lifecycle-neutral Vault migration has been completed. Migration-only tooling is intentionally absent from the active tree; use Git history only if historical recovery is explicitly required.

Superseded architecture material is not retained in the current tree. Use Git history only when an explicit historical investigation is required.
