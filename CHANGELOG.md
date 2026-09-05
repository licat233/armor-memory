# Changelog

This file records changes to the current ARMOR Minimal Stable architecture.

Superseded architecture generations are intentionally omitted from the working tree to reduce instruction ambiguity. Git history remains the historical record.

## 2026-09-05

### Added

- Added the Architecture Change Gate: new capabilities must demonstrate that operational benefit is greater than complexity, failure risk, data-integrity risk, and long-term maintenance cost.
- Added read-only knowledge-quality tooling for authority, provenance, duplicate-title diagnostics, and candidate diff preview.
- Added LLM knowledge-engineering guardrails covering deterministic validation, evidence preservation, conservative identity merging, low-entropy model handles, source trust boundaries, and ingestion separation.
- Added explicit Knowledge Compilation, Conflict Closure, and Topic Convergence workflows so resolved facts and mature topics converge instead of repeatedly consuming human attention.
- Added the Human-Cost Gate: recurring human steps must justify the material judgment or risk reduction they provide.
- Added a temporary dry-run-first lifecycle-neutral migration tool for `02-Projects/Active/ -> 02-Projects/Projects/`, with collision preflight and focused tests.

### Changed

- Clarified that the ARMOR Vault is the sole durable knowledge source of truth.
- Clarified that derived indexes, caches, embeddings, graphs, and databases must remain rebuildable unless an explicit architecture decision establishes otherwise.
- Changed canonical approval handling so an explicit current user instruction can already constitute approval for the exact requested change; duplicate confirmation is not required.
- Changed named-project routing from lifecycle-named `02-Projects/Active/<project>/` to stable `02-Projects/Projects/<project>/`.
- Changed website article routing to the lifecycle-neutral source home `02-Projects/Workspaces/Website/Articles/`.
- Changed official social-copy routing to `02-Projects/Workspaces/Marketing/Social-Media/`.
- Clarified that `03-Records/Published/` is evidence of actual publication or an explicitly requested published snapshot, not the default destination for newly created content.
- Clarified that project completion, publication, and routine status changes do not require humans to move files.
- Simplified repository documentation so active Minimal Stable sources are the only architecture instructions present on the default branch.

### Removed

- Removed `02-Projects/Completed/` from the recommended architecture.
- Removed the design assumption that humans should maintain lifecycle folders or manually synchronize routine status metadata.
- Removed superseded architecture documentation, archived architecture copies, older migration-only tooling, obsolete templates, and their tests from the default branch.
- Removed compatibility guidance whose only purpose was to distinguish current rules from retired architecture rules.

### Migration Note

The live Vault still requires the bounded project-root migration from `02-Projects/Active/` to `02-Projects/Projects/`. The temporary migration helper intentionally does not bulk-move legacy `03-Records/Published/` content because the previous router mixed true publication evidence with content merely created for publication; guessing would risk rewriting historical meaning.

After the live project-root migration is completed and verified, the temporary migration script and its focused test should be deleted from the active tree.

### Rationale

Minimal Stable is optimized for low recurring human cost. Humans should make real business, authority, identity, scope, and risk decisions; they should not become file administrators. Lifecycle-neutral paths remove recurring move/status chores, while evidence and canonical knowledge remain explicit and auditable.
