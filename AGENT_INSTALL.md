# Agent Installation Guide

> Historical install guide for the earlier AI Agent Memory Architecture / ARMOR Enterprise line.
>
> For the current active public system, start with [`README.md`](README.md) and the `minimal-stable/` tree instead of treating this file as the default install path.
>
> This is an architecture installation, not a software package installation. Do not install Obsidian UI plugins. Do not treat runtime memory, embeddings, SQLite, or indexes as the durable memory source.

---

## 1. Default Behavior

Install ARMOR Enterprise AI Workspace by default.

The user only needs to provide a target Vault or Markdown directory path.

Do not ask the user to choose between `enterprise`, `personal`, or `both` unless they explicitly request a non-default installation.

If the target path is provided, proceed with enterprise installation.

If the target path is missing, ask one question:

```text
What target Vault or Markdown directory should I install ARMOR into?
```

---

## 2. Install Goal

Create a governed enterprise memory Vault for AI agents.

The installed Vault must preserve these principles:

- The Vault is the durable source of truth.
- Runtime memory is temporary and low-authority.
- Uncertain information is stored lower.
- Authoritative memory requires evidence, review, and correct routing.
- High-authority changes require proposal or explicit human approval.
- Drafts, inboxes, logs, raw records, proposals, and archives are excluded from default truth retrieval.

---

## 3. Safe Install Rules

Before writing:

1. Resolve the target path.
2. If the path does not exist, create it.
3. If the path exists, inspect it briefly.
4. Create missing directories only.
5. Copy missing core documents only.
6. Never overwrite existing files silently.
7. If a target file already exists, preserve it and write a timestamped candidate under `93-Proposals/` or `90-Drafts/`.

The user's request to install is enough permission to create missing directories and missing architecture files inside the target path.

Ask for confirmation only when an existing file would be overwritten, renamed, deleted, or structurally changed.

---

## 4. Source Repository Assumptions

The installer should be run from a local checkout of this repository or from a location where these files are available:

```text
README.md
FRONTMATTER_STANDARD.md
shared/frontmatter/Frontmatter-Registry-Template.md
DOCUMENT_MAP_STANDARD.md
shared/document-map/
TEMPLATE_AUTOMATION_GUIDE.md
shared/templates/
enterprise/
archive/personal/ (historical only)
```

If the repository is not available locally, ask the user to provide the path or clone:

```text
https://github.com/licat233/AI-Agent-Memory-Architecture.git
```

Do not download or install additional tools unless the user explicitly approves.

---

## 5. Default Enterprise Installation: ARMOR

### 5.1 Create Top-Level Directories

Create these directories inside the target Vault if missing:

```text
00-Core/
01-Facts/
02-Rules/
03-Insights/
04-Research/
04-Research/00-Inbox/
04-Research/01-Reviewed/
05-Projects/
06-Records/
70-Schemas/
80-Indexes/
81-Dashboards/
90-Drafts/
91-Inbox/
92-Logs/
93-Proposals/
94-Review-Queues/
99-Archive/
```

Do not rename, merge, or invent top-level layers without explicit user approval.

### 5.2 Copy Core ARMOR Documents

Copy these repository files into the target Vault if missing:

| Source | Destination |
| --- | --- |
| `enterprise/V7_2_Stable.md` | `00-Core/ARMOR-V7.2-Stable.md` |
| `enterprise/V7_1_5_Governance_Patch.md` | `00-Core/ARMOR-Governance-Patch-V7.1.5.md` |
| `enterprise/Prompt_Intake_Router.md` | `00-Core/Prompt-Intake-Router.md` |
| `enterprise/Memory_Write_Router.md` | `00-Core/Memory-Write-Router.md` |
| `enterprise/Root_Cause_Fix_Protocol.md` | `00-Core/Root-Cause-Fix-Protocol.md` |
| `enterprise/Runtime_Memory_Policy.md` | `00-Core/Runtime-Memory-Policy.md` |
| `enterprise/agent_runtime_adaptation_guide.md` | `00-Core/Agent-Runtime-Adaptation-Guide.md` |
| `enterprise/multi_agent_shared_vault_governance.md` | `00-Core/Multi-Agent-Shared-Vault-Governance.md` |
| `FRONTMATTER_STANDARD.md` | `00-Core/Frontmatter-Standard.md` |
| `shared/frontmatter/Frontmatter-Registry-Template.md` | `70-Schemas/Frontmatter-Registry.md` |
| `DOCUMENT_MAP_STANDARD.md` | `00-Core/Document-Map-Standard.md` |
| `shared/document-map/ARMOR-Vault-Document-Map-Template.md` | `80-Indexes/Vault-Document-Map.md` |
| `shared/document-map/Document-Registry.base` | `80-Indexes/Document-Registry.base` |
| `TEMPLATE_AUTOMATION_GUIDE.md` | `00-Core/Template-Automation-Guide.md` |

If a destination file already exists, do not overwrite it. Preserve the file and create a candidate copy under:

```text
93-Proposals/Install-Candidates/
```

### 5.3 Create Starter Core Files

If missing, create these small placeholder files:

```text
00-Core/Source-of-Truth-Map.md
00-Core/Permission-Policy.md
00-Core/Retrieval-Rules.md
00-Core/Lifecycle-Policy.md
00-Core/Installed-Memory-Architecture.md
```

Each placeholder should state that it must follow ARMOR V7.2 and the governance patch.

### 5.4 Copy Optional Project Execution Templates

Copy these repository templates into the target Vault if missing:

| Source | Destination |
| --- | --- |
| `enterprise/Project_Execution_Workflow.md` | `70-Schemas/Project-Execution/Project-Execution-Workflow.md` |
| `enterprise/Agent_Project_Execution_Prompt.md` | `70-Schemas/Project-Execution/Agent-Project-Execution-Prompt.md` |
| `enterprise/templates/project_execution/task_plan.md` | `70-Schemas/Project-Execution/task_plan.md` |
| `enterprise/templates/project_execution/findings.md` | `70-Schemas/Project-Execution/findings.md` |
| `enterprise/templates/project_execution/progress.md` | `70-Schemas/Project-Execution/progress.md` |
| `enterprise/templates/project_execution/closeout.md` | `70-Schemas/Project-Execution/closeout.md` |

These templates are optional execution aids for complex project work. They do not create a new authority layer and must not bypass the Memory Write Router, Root-Cause Fix Protocol, or permission model.

Recommended use inside a Vault:

```text
05-Projects/<project-name>/Execution/YYYY-MM-DD-<task-slug>/
  task_plan.md
  findings.md
  progress.md
  closeout.md
```

Execution files are low-authority working materials. Candidate long-term memory found during execution must be routed through the normal ARMOR workflow before it can become current truth.

### 5.5 Install Note-Type Templates

Install Plain Markdown templates by default:

```text
shared/templates/armor/plain/
→ 70-Schemas/Templates/
```

Plain templates have no plugin dependency and are usable by AI agents and scripts.

If the user explicitly chooses Obsidian's official Templates core plugin, copy:

```text
shared/templates/armor/obsidian-core/
→ 70-Schemas/Templates/
```

If the user explicitly chooses Templater and it is already installed or the user approves installation, copy:

```text
shared/templates/armor/templater/
→ 70-Schemas/Templates/
```

Then configure:

```text
Template folder location: 70-Schemas/Templates
Trigger Templater on new file creation: enabled
Folder Templates: enabled
System Commands: disabled
User Scripts: disabled by default
Startup Templates: empty
```

Use `shared/templates/templater/armor-folder-templates.json` as the recommended Folder Templates mapping.

Do not mix Plain, Core Templates, and Templater syntax in the same active template files.

---

## 6. Runtime Integration

After installing files, explain this to the user and the operating agent:

```text
The Vault is long-term memory.
The agent runtime provides capability.
Runtime memory, SQLite, embeddings, and indexes are temporary infrastructure.
They are not authoritative memory.
```

Any trusted runtime can operate the Vault if it has file read/search/write/patch capability and follows ARMOR governance.

Examples:

- Hermes
- Claude Code
- Codex
- Opencode
- Cline
- OpenHands
- custom agents
- MCP-backed agents

The runtime should:

- point its long-term memory or workspace path to the installed Vault
- install the Agent Vault Bootstrap Rule from `AGENT_VAULT_BOOTSTRAP_RULE.md` into the runtime's durable startup instructions
- use `00-Core/Prompt-Intake-Router.md` before ambiguous, high-risk, fix, or remember requests
- use `00-Core/Memory-Write-Router.md` before storing permanent memory
- use `00-Core/Root-Cause-Fix-Protocol.md` when correcting errors
- use `00-Core/Runtime-Memory-Policy.md` to keep runtime memory temporary and low-authority
- use `00-Core/Multi-Agent-Shared-Vault-Governance.md` when multiple agents share the same Vault
- use `00-Core/Frontmatter-Standard.md` and the installed Frontmatter Registry before adding metadata fields
- read `80-Indexes/Vault-Document-Map.md` before broad Vault discovery
- use `80-Indexes/Document-Registry.base` or targeted search to locate candidate files

The bootstrap rule must tell the runtime where the installed Vault Map lives and that broad Vault-wide keyword search is not the default retrieval strategy.

For Codex, prefer a local reference plus a skill rather than writing durable facts into Codex runtime memory:

```text
~/.codex/memory/reference_armor_vault.md
~/.codex/skills/armor-enterprise-vault/SKILL.md
```

The reference should point to the installed Vault, and the skill should instruct Codex to read the ARMOR routers and policies before memory-related writes.

For multi-agent deployments, create starter namespaces when useful:

```text
91-Inbox/{agent-name}/
92-Logs/{agent-name}/
93-Proposals/{agent-name}/
93-Proposals/Conflicts/
```

---

## 7. Installation Log

Write an installation log after successful installation:

```text
92-Logs/YYYY-MM-DD-Memory-Architecture-Install.md
```

The log should include:

```yaml
architecture: ARMOR
project_version: v1.6.0
version: V7.2 Stable
installed_at: YYYY-MM-DD
source_repository: AI-Agent-Memory-Architecture
target_vault: /absolute/path
agent_runtime: unknown | Hermes | Claude Code | Codex | Opencode | Cline | OpenHands | other
files_created:
files_copied:
existing_files_preserved:
candidate_files_created:
open_questions:
```

If the runtime is unknown, write `unknown`. Do not block installation just to identify the runtime.

---

## 8. Validation Checklist

Before reporting completion, verify:

- The target Vault exists.
- Required ARMOR top-level directories exist.
- Core architecture documents were copied or preserved.
- The Frontmatter Standard and Frontmatter Registry were copied or preserved.
- The Document Map Standard, static Vault Map, and dynamic Document Registry were copied or preserved.
- The Template Automation Guide and one active template profile were copied or intentionally skipped.
- Optional project execution templates were copied or preserved.
- Existing user files were not overwritten silently.
- `93-Proposals/` exists.
- `06-Records/` exists.
- `90-Drafts/`, `91-Inbox/`, and `92-Logs/` exist.
- `00-Core/Memory-Write-Router.md` exists.
- Runtime memory was not configured as the durable source of truth.
- No Obsidian UI plugin was installed.
- The installation log exists.
- The user knows which path to point their AI agent at.
- Multi-agent deployments have a namespace and conflict policy.
- The static Vault Map points to current entry files.
- The dynamic Document Registry parses as valid YAML.

---

## 9. Advanced Options

Only use these if the user explicitly asks.

### Archived Personal / PAMA

PAMA Personal V5.3 Stable is archived under:

```text
archive/personal/PAMA-Personal-v5.3-Stable/
```

Do not install PAMA as part of the active default architecture. Use the archive only for historical reference or manual recovery.

If a user explicitly asks to revive PAMA, stop and explain that PAMA is archived. Create a proposal or release plan before restoring it into the active install path.

### Custom Runtime

If the user names a specific runtime, adapt only the final runtime instructions. Do not change the Vault structure unless the architecture requires it.

---

## 10. Completion Response

After installation, report:

1. Installed architecture: ARMOR Enterprise AI Workspace.
2. Target Vault path.
3. Core documents copied.
4. Document Map and Registry locations.
5. Existing files preserved or candidate files created.
6. Installation log path.
7. The next instruction the user's AI agent should follow.

Keep the response concise. Do not claim that memory has been promoted into truth unless the appropriate review or proposal process happened.

---

## 11. Final Rule

Installing the architecture only creates the governed memory system.

It does not make every future note authoritative.

The agent must continue to follow the routers, permission model, retrieval policy, runtime memory policy, and proposal workflow every time it reads or writes memory.
