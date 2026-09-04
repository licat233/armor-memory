# ARMOR Minimal Stable

ARMOR Minimal Stable is the active ARMOR shared-memory architecture.

The live business-memory Vault is outside this repository and is resolved through `ARMOR_VAULT_ROOT`. The frozen V7.2 material in this repository is historical only and must not be restored as the active architecture.

Start with:

- `00-System/START-HERE.md`
- `00-System/ROUTING-RULES.md`
- `00-System/AUTHORITY-RULES.md`
- `ARCHITECTURE.md`

Core implementation:

- `scripts/armor-route.py` — deterministic destination routing
- `scripts/armor-knowledge.py` — read-only knowledge quality checks and diff preview
- `tests/` — routing, migration-safety, Agent integration, and knowledge-quality tests

Knowledge-quality maintenance is explicit-only. It does not run automatically after ordinary Vault reads or writes and does not modify canonical knowledge.
