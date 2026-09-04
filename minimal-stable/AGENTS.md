# ARMOR Minimal Stable Development Rules

This directory implements deterministic document routing.

- Do not add natural-language keyword inference.
- Do not call an LLM from the router.
- Do not scan the Vault from the router.
- Do not add implicit Inbox fallbacks.
- Do not silently accept unknown values.
- Every new enum or route requires documentation and tests.
- Run: `python3 -m pytest minimal-stable/tests -v`
- Do not modify V7.2 while working in this directory.

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
