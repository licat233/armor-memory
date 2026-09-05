# ARMOR Minimal Stable Development Rules

This directory implements deterministic document routing plus a deliberately small, read-only knowledge-quality capability.

Routing rules:

- Do not add natural-language keyword inference.
- Do not call an LLM from the router.
- Do not scan the Vault from the router.
- Do not add implicit Inbox fallbacks.
- Do not silently accept unknown values.
- Every new enum or route requires documentation and tests.

Knowledge-quality rules:

- `armor-knowledge check` is diagnostic and read-only.
- Do not add automatic fixes, merges, deletions, authority promotion, or canonical rewriting to the quality tool.
- Do not run quality scans automatically after ordinary reads or writes.
- Keep uncertain duplicate/provenance findings advisory rather than turning heuristics into hard errors.
- Prefer Python standard-library implementation while the current capability can be expressed reliably without a dependency.
- Current authority values are `working`, `verified`, `canonical`, and `evidence`; knowledge without an explicit authority is treated as `working` during retrieval.
- Do not import deprecated authority vocabularies or retired lifecycle rules into current diagnostics.

Testing:

- Run: `python3 -m pytest minimal-stable/tests -v`
- Focused knowledge-quality suite: `python3 -m pytest minimal-stable/tests/test_armor_knowledge.py -q`
- Current tests cover routing, Agent integration, and knowledge quality.

## Minimal Stable Feature Rules

- Do not add a feature only because it is technically interesting, fashionable, or present in another knowledge platform.
- Every proposed feature must solve a concrete ARMOR problem and show that its expected benefit is greater than its added complexity, failure risk, data risk, and maintenance cost.
- Prefer an existing component, a smaller rule change, or a derived artifact before introducing a new subsystem.
- New databases, vector stores, graph stores, caches, indexes, services, daemons, background jobs, and external dependencies require explicit justification.
- Derived systems must be rebuildable from the ARMOR Vault and must not become an independent source of truth.
- Do not duplicate canonical knowledge across multiple authoritative stores.
- Prefer reversible changes. A failed or removed optional subsystem must not damage or strand canonical knowledge.
- For architecture changes, document the concrete need, simpler alternatives considered, new failure modes, maintenance burden, rollback path, and final benefit-versus-cost decision.
- If the benefit is uncertain or merely speculative, default to `Not now`.

## Repository Hygiene

- Keep this directory focused on current Minimal Stable implementation and tests.
- Do not retain migration-only scripts or tests after the migration they serve is permanently complete and no active dependency remains.
- Do not keep superseded architecture copies beside current rules solely for reference; use Git history when historical inspection is explicitly required.
