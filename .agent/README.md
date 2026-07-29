# Shared Agent Layer

This repository provides one shared ARMOR Minimal Stable integration layer for Hermes Agent, Claude Code, and Codex.

Layout:

- `skills/armor-memory/`: shared routing skill
- `evaluation/`: manual cross-Agent evaluation cases and expected classifications

## Hermes Setup

Expose the shared Skill directory to Hermes using the project-level or external Skill mechanism supported by the local Hermes installation.

Portable path example:

```text
<repo-root>/.agent/skills
```

Suggested setup flow:

1. Register or expose `<repo-root>/.agent/skills`.
2. Confirm Hermes can load `armor-memory`.
3. Use the shared Skill for persistent ARMOR Vault document operations.

Do not hard-code machine-specific home paths in the repository.

## Wrapper Script

`skills/armor-memory/scripts/route.sh` is the shared wrapper around `minimal-stable/scripts/armor-route.py`.

If your environment requires it, ensure the wrapper is executable:

```bash
chmod +x .agent/skills/armor-memory/scripts/route.sh
```

