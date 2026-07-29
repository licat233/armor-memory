# Agent Update Guide

This guide is a historical update workflow for the earlier AI Agent Memory Architecture / ARMOR Enterprise line.

For the current active public system, start with [`README.md`](README.md) and the `minimal-stable/` workflow documents.

It is intentionally different from `AGENT_INSTALL.md`.

Installation answers:

```text
How do I create the architecture?
```

Update answers:

```text
How do I align an existing Vault with the latest architecture without leaving stale active files behind?
```

Historical target captured in this document:

```text
AI Agent Memory Architecture v1.6.0
ARMOR Enterprise V7.2 Stable
```

## Core Principle

Do not overwrite history to make search results look clean.

Instead:

- update active authority files
- add missing current files
- archive superseded active files
- mark superseded proposals
- leave logs, records, decisions, and archive files as historical evidence unless the user explicitly asks to rewrite them

Runtime memory, embeddings, indexes, local databases, and session summaries are not long-term memory. They may be rebuilt after the Vault is aligned.

## Update Prompt

Users can give this prompt to an AI agent:

```text
Please read and execute AGENT_UPDATE.md from this repository:
https://github.com/licat233/AI-Agent-Memory-Architecture

Help me update my existing AI Agent Memory Architecture Vault.
Target architecture: AI Agent Memory Architecture v1.6.0.
Default branch: ARMOR Enterprise V7.2 Stable.
Target Vault path: <paste your Vault or Markdown directory path here>

Do not install any Obsidian UI plugin.
Do not use runtime memory as long-term memory.
Preserve user content and history.
Archive superseded active files instead of deleting them.
Update active Core, Indexes, runtime adaptation guides, routers, and governance files.
Mark obsolete pending proposals as superseded when they point to retired files.
Do not rewrite logs, records, decisions, or archive files unless they are being used as current truth.
Write an update log and run the validation checklist.
```

## Required First Reads

Before changing files, read:

```text
README.md
AGENT_INSTALL.md
AGENT_UPDATE.md
FRONTMATTER_STANDARD.md
shared/frontmatter/Frontmatter-Registry-Template.md
DOCUMENT_MAP_STANDARD.md
shared/document-map/
TEMPLATE_AUTOMATION_GUIDE.md
shared/templates/
```

For ARMOR updates, also read:

```text
enterprise/README.md
enterprise/V7_2_Stable.md
enterprise/V7_1_5_Governance_Patch.md
enterprise/agent_runtime_adaptation_guide.md
enterprise/multi_agent_shared_vault_governance.md
enterprise/Prompt_Intake_Router.md
enterprise/Memory_Write_Router.md
enterprise/Root_Cause_Fix_Protocol.md
enterprise/Runtime_Memory_Policy.md
```

PAMA Personal V5.3 Stable is archived under `archive/personal/PAMA-Personal-v5.3-Stable/` and is not part of the active update path.

## Update Workflow

### 1. Identify Installed State

Inspect the target Vault for:

```text
00-Core/
80-Indexes/
81-Dashboards/
90-Drafts/
91-Inbox/
92-Logs/
93-Proposals/
99-Archive/
```

Then read any installed version markers:

```text
00-Core/Installed-Memory-Architecture.md
00-Core/Core-Document-Index.md
00-Core/Frontmatter-Standard.md
70-Schemas/Frontmatter-Registry.md
00-Core/Document-Map-Standard.md
80-Indexes/Vault-Document-Map.md
80-Indexes/Document-Registry.base
00-Core/Template-Automation-Guide.md
00-Core/Core-Memory.md
80-Indexes/README.md
```

If no version marker exists, infer the version from Core filenames, index filenames, and changelogs.

### 2. Create a Cleanup Archive

Before moving or replacing active files, create:

```text
99-Archive/Updates/YYYY-MM-DD-v<target-version>-update/
```

Inside it, create:

```text
snapshot-before-update/
deprecated-active-files/
```

Copy active files that will be touched into `snapshot-before-update/`.

Move superseded active files into `deprecated-active-files/`.

Do not move logs, raw records, decisions, or existing archive files unless the user explicitly asks.

### 3. Sync Current Core Files

For ARMOR, active Core should include:

```text
00-Core/ARMOR-V7.2-Stable.md
00-Core/Governance-Patch-V715.md
00-Core/Agent-Runtime-Adaptation-Guide.md
00-Core/Multi-Agent-Shared-Vault-Governance.md
00-Core/Prompt-Intake-Router.md
00-Core/Memory-Write-Router.md
00-Core/Root-Cause-Fix-Protocol.md
00-Core/Runtime-Memory-Policy.md
00-Core/Permission-Policy.md
00-Core/Retrieval-Rules.md
00-Core/Source-of-Truth-Map.md
00-Core/Installed-Memory-Architecture.md
00-Core/Core-Document-Index.md
```

Do not add PAMA Core equivalents during normal updates. They belong to the archived personal branch.

Preserve Vault-local policies that are still valid, but update their references to current active files.

Sync the canonical frontmatter files:

| Branch | Source | Destination |
| --- | --- | --- |
| ARMOR | `FRONTMATTER_STANDARD.md` | `00-Core/Frontmatter-Standard.md` |
| ARMOR | `shared/frontmatter/Frontmatter-Registry-Template.md` | `70-Schemas/Frontmatter-Registry.md` |

If a Registry already exists, preserve its approved domain and tool fields. Merge canonical changes through a proposal or explicit human approval instead of replacing organization-specific entries.

Sync the Document Map files:

| Branch | Source | Destination |
| --- | --- | --- |
| ARMOR | `DOCUMENT_MAP_STANDARD.md` | `00-Core/Document-Map-Standard.md` |
| ARMOR | `shared/document-map/ARMOR-Vault-Document-Map-Template.md` | `80-Indexes/Vault-Document-Map.md` |
| ARMOR | `shared/document-map/Document-Registry.base` | `80-Indexes/Document-Registry.base` |

Preserve Vault-local domain routing in an existing static map. Correct retired entry points and architecture versions without replacing valid organization-specific sections.

Sync the agent runtime bootstrap rule:

```text
AGENT_VAULT_BOOTSTRAP_RULE.md
→ each agent's durable startup instructions, system prompt, profile rule file, project instruction file, or equivalent runtime configuration
```

The update is not complete if agents can access the Vault but do not know to open the installed Vault Map before broad search.

Sync the Template Automation Guide:

```text
TEMPLATE_AUTOMATION_GUIDE.md
→ 00-Core/Template-Automation-Guide.md
```

Identify the active template profile before replacing templates:

```text
Plain Markdown
Obsidian Core Templates
Templater
```

Preserve one active syntax profile. Do not mix unresolved `{{date}}` and `<% tp.* %>` expressions.

When Templater is active:

- preserve reviewed organization-specific templates
- update canonical frontmatter fields
- keep system commands disabled unless explicitly approved
- keep user scripts and startup templates empty unless reviewed
- verify folder mappings point to existing templates

### 4. Sync Active Indexes

Active indexes should point to the current architecture.

For ARMOR v1.6.0 / V7.2, prefer:

```text
80-Indexes/Vault-Document-Map.md
80-Indexes/Document-Registry.base
80-Indexes/README.md
```

Archive old active indexes such as:

```text
80-Indexes/V7-1-Index.md
80-Indexes/V7-2-draft-index.md
```

Do not leave old version indexes in active `80-Indexes/` unless they are clearly marked `status: historical` and excluded from default retrieval.

### 5. Sync Optional Project Execution Templates

For ARMOR, copy the optional project execution templates if they are missing:

```text
70-Schemas/Project-Execution/Project-Execution-Workflow.md
70-Schemas/Project-Execution/Agent-Project-Execution-Prompt.md
70-Schemas/Project-Execution/task_plan.md
70-Schemas/Project-Execution/findings.md
70-Schemas/Project-Execution/progress.md
70-Schemas/Project-Execution/closeout.md
```

These files are low-authority execution templates only. They must not be treated as Core policy, Facts, Rules, or a replacement for the ARMOR routers.

Do not copy archived PAMA personal execution templates during normal updates.

### 6. Clean Active References

Search only active truth and navigation layers first:

```text
00-Core/
01-Facts/
02-Rules/
03-Insights/
04-Research/01-Reviewed/
05-Projects/
80-Indexes/
81-Dashboards/
```

Look for retired filenames, retired tools, and old version labels.

Examples:

```text
Claudian
Hermes-V71-Adaptation-Guide
Hermes-Operating-Protocol
Profile-Skills-Architecture
V7.1 Stable
AI Agent Memory Architecture v1.1.0
PAMA Personal V5.2
memory_class
created_at
target_layer
review_required
default_truth_retrieval
authority: high
authority: medium
authority: low
```

Classify each hit:

| Hit Location | Default Action |
| --- | --- |
| Active Core current rule | Update or replace |
| Active Index | Update or archive |
| Active Fact or Rule | Update only if it claims current truth |
| Active Project | Update if it controls ongoing work |
| Pending Proposal targeting retired files | Mark superseded or retarget |
| Log | Preserve |
| Raw Record | Preserve |
| Decision Record | Preserve, optionally add a superseded note |
| Archive | Preserve |

### 7. Mark Superseded Proposals

If a pending proposal references retired active files, do not silently execute it.

Either:

- update its target to current files if the proposal is still valid
- mark it `status: superseded` if the migration has already been completed or the target architecture changed

Recommended note:

```text
Superseded on YYYY-MM-DD by AI Agent Memory Architecture vX.Y.Z / <branch version>.
Retained as historical migration context only. Do not execute old target paths.
Current active entry points are: <list current files>.
```

### 8. Preserve Historical Evidence

Do not rewrite these just because they mention old tools or versions:

```text
06-Records/
92-Logs/
99-Archive/
historical decisions
completed proposals
```

Old terms in these locations are evidence of what happened at the time.

Only add a superseded note when a historical file is likely to be mistaken for current instructions.

### 9. Write an Update Log

For ARMOR shared Vaults, use the agent namespace:

```text
92-Logs/{Agent-Name}/YYYY-MM-DD-architecture-update.md
```

For archived PAMA shared Vaults, use the configured historical PAMA agent log or review namespace only when explicitly performing archival maintenance.

The update log should include:

- source repository and target version
- files added
- files replaced
- files archived
- proposals marked superseded
- validation results
- remaining known historical references

### 10. Validate

Run these checks:

```text
1. Required current Core files exist.
2. Active indexes point to the current architecture.
3. Retired active filenames are absent from active truth layers, except in explicit "archived/superseded" notes.
4. Runtime memory is not described as long-term memory.
5. Logs, records, and archives were not rewritten to erase history.
6. Agent namespaces exist when the Vault is shared by multiple agents.
7. Pending proposals do not target retired active files.
8. Optional project execution templates exist or were intentionally skipped.
9. Update log exists.
10. Frontmatter Standard and branch Registry exist.
11. New templates use canonical field names.
12. Static Vault Map links point to current entry files.
13. Dynamic Document Registry parses as valid YAML.
14. Active templates use one syntax profile.
15. Rendered templates produce valid canonical frontmatter.
```

## Version-Specific Cleanup Notes

### v1.6.0 / ARMOR Enterprise V7.2 Stable

Current active replacements:

| Old Active File or Concept | Current Replacement | Action |
| --- | --- | --- |
| `00-Core/Hermes-V71-Adaptation-Guide.md` | `00-Core/Agent-Runtime-Adaptation-Guide.md` | Archive old active file |
| `00-Core/Hermes-Operating-Protocol.md` | Generic routers + runtime adaptation + multi-agent governance | Archive old active file |
| `00-Core/Profile-Skills-Architecture.md` | Runtime-local Hermes documentation, not ARMOR Core | Archive or move outside active Core |
| `80-Indexes/V7-1-Index.md` or old architecture index | `80-Indexes/Vault-Document-Map.md` | Archive or supersede old active index |
| Claudian or Obsidian UI executor plugin support | Direct trusted runtime file access | Archive old execution guides |
| `AI Agent Memory Architecture v1.1.0` through `v1.5.0` as current version | `AI Agent Memory Architecture v1.6.0` | Update active version markers |
| `PAMA Personal` active install path | Archived PAMA branch | Move active PAMA material out of the current install path |
| Branch-specific or runtime-specific frontmatter rules | `00-Core/Frontmatter-Standard.md` + installed Registry | Preserve approved domain fields, migrate canonical fields lazily |
| `memory_class` | `permission_class` or `memory_layer` | Inspect meaning before migration |
| `created_at` | `created` | Migrate on meaningful update |
| `target_layer` | `memory_layer` | Normalize directory layer value |
| `review_required` | `write_policy` or `review_date` | Convert based on intent |
| `default_truth_retrieval` | `retrieval_scope` | Normalize retrieval behavior |
| `authority: high/medium/low` | Canonical authority vocabulary | Resolve from evidence and review state |
| No stable Vault navigation entry | Static Vault Map + dynamic Document Registry | Install branch-specific map files |
| Mixed template syntaxes | One selected Plain/Core/Templater profile | Preserve one active profile |
| Templater installed but auto-trigger disabled | Safe Templater settings | Enable only after mappings and templates validate |
| Legacy template frontmatter | Canonical `FRONTMATTER_STANDARD.md` fields | Update templates; migrate existing notes lazily |

Expected active ARMOR entry points:

```text
00-Core/Core-Document-Index.md
00-Core/Installed-Memory-Architecture.md
00-Core/Agent-Runtime-Adaptation-Guide.md
00-Core/Multi-Agent-Shared-Vault-Governance.md
80-Indexes/Vault-Document-Map.md
80-Indexes/Document-Registry.base
```

Retain historical mentions in:

```text
06-Records/
92-Logs/
99-Archive/
completed or superseded proposals
```

## Final Rule

An update is complete only when the active Vault points to the latest architecture and stale active files cannot be mistaken for current truth.

Clean active truth.

Preserve history.

Archive instead of erase.
