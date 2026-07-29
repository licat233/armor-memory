# ARMOR Minimal Stable for Hermes Agent

When a task creates or stores a persistent ARMOR Vault document:

1. Load `.agent/skills/armor-memory/SKILL.md`.
2. Classify the task using the shared protocol.
3. Do not construct a destination path.
4. Call `.agent/skills/armor-memory/scripts/route.sh`.
5. Use exactly the returned path.
6. Ordinary writes are route -> write -> stop.

Do not copy the ARMOR Vault into Hermes runtime memory.

Hermes runtime memory is for short user preferences and active-session context.
ARMOR Minimal Stable is the persistent document system.

