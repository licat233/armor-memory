# Changelog

This file records changes to the current ARMOR Minimal Stable architecture.

Superseded architecture generations are intentionally omitted from the working tree to reduce instruction ambiguity. Git history remains the historical record.

## 2026-09-05

### Added

- Added the Architecture Change Gate: new capabilities must demonstrate that operational benefit is greater than complexity, failure risk, data-integrity risk, and long-term maintenance cost.
- Added read-only knowledge-quality tooling for authority, provenance, duplicate-title diagnostics, and candidate diff preview.
- Added LLM knowledge-engineering guardrails covering deterministic validation, evidence preservation, conservative identity merging, low-entropy model handles, source trust boundaries, and ingestion separation.

### Changed

- Clarified that the ARMOR Vault is the sole durable knowledge source of truth.
- Clarified that derived indexes, caches, embeddings, graphs, and databases must remain rebuildable unless an explicit architecture decision establishes otherwise.
- Clarified that material canonical changes require the existing authority and human-approval boundary.
- Simplified repository documentation so active Minimal Stable sources are the only architecture instructions present on the default branch.

### Removed

- Removed superseded architecture documentation, archived architecture copies, migration-only tooling, obsolete templates, and their tests from the default branch.
- Removed compatibility guidance whose only purpose was to distinguish current rules from retired architecture rules.

### Rationale

The default branch is an operational architecture tree, not a permanent in-tree archive. Keeping retired rules beside active rules creates avoidable retrieval and instruction-pollution risk for humans and Agents. Historical recovery remains available through Git history without increasing current maintenance or ambiguity.
