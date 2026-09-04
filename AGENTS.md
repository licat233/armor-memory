# AGENTS

## ARMOR Minimal Stable

When creating or storing a persistent ARMOR Vault document:

1. Read `.agent/skills/armor-memory/SKILL.md`.
2. Classify the task using the shared classification protocol.
3. Do not choose or construct a destination path manually.
4. Call `.agent/skills/armor-memory/scripts/route.sh`.
5. Use exactly the returned destination path.
6. Draft and unverified are statuses, not storage destinations.
7. Ordinary writes are route -> write -> stop.
8. Do not create new router enum values during ordinary work.

## Active Architecture Precedence

For current ARMOR Minimal Stable work, active rules are defined by:

1. `README.md`
2. `minimal-stable/ARCHITECTURE.md`
3. `minimal-stable/00-System/`
4. `.agent/skills/armor-memory/SKILL.md` and its current references

Root-level documents that explicitly describe ARMOR Enterprise V7.2 or the pre-Minimal-Stable architecture are historical references only. In particular, do not import legacy V7.2 frontmatter, authority, lifecycle, review-queue, or promotion rules into Minimal Stable unless a current Minimal Stable document explicitly adopts them.

When active and historical documents disagree, the active Minimal Stable documents above take precedence.

## Architecture Change Gate

When designing, reviewing, or implementing an upgrade to `armor-memory`, preserve the Minimal Stable philosophy.

Before adding any feature, service, database, index, automation, schema, workflow, dependency, or background process, evaluate all of the following:

1. What concrete recurring problem does it solve?
2. What measurable or operational benefit does it provide?
3. Can the same result be achieved with an existing component or a simpler change?
4. What new failure modes, data-integrity risks, security risks, synchronization problems, and maintenance work does it introduce?
5. Does it create another source of truth or duplicate knowledge already stored in the Vault?
6. Can it be removed or rebuilt without losing canonical ARMOR knowledge?
7. Is the expected benefit clearly greater than the combined complexity, risk, and long-term maintenance cost?

If the answer to item 7 is not clearly yes, do not add the feature by default. `Not now` is an acceptable architecture decision.

Additional rules:

- Do not add features merely because another mature project has them or because they are technically possible.
- Prefer the smallest change that preserves correctness, recoverability, and long-term knowledge integrity.
- The ARMOR Vault remains the durable source of truth. Search indexes, embeddings, vector stores, caches, graphs, databases, and generated registries must remain derived and rebuildable unless an explicit architecture decision says otherwise.
- New infrastructure must not silently become a second authoritative knowledge store.
- Prefer extending existing ARMOR components over introducing a new subsystem.
- Any architecture proposal that adds persistent infrastructure must state its benefit, operational cost, failure modes, rollback path, and why the existing system is insufficient.
