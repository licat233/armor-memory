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

