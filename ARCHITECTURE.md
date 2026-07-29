# AI Agent Memory Architecture

This document is a historical architecture overview from the repository's pre-Minimal-Stable era.

For the current active system, start with [`README.md`](README.md), which now defines the public mainline for ARMOR Minimal Stable.

Historical release alignment captured in this file:

```text
AI Agent Memory Architecture v1.6.0
ARMOR Enterprise V7.2 Stable
```

## 1. What This Project Is

AI Agent Memory Architecture is a governed long-term memory architecture for AI agents using Markdown or Obsidian Vaults.

It is not:

- a vector database
- a prompt extension
- a runtime cache
- a loose folder of notes
- an Obsidian UI plugin system
- a replacement for human judgment

It is:

- a durable memory operating system
- a source-of-truth structure
- a permission and retrieval model
- a promotion workflow for turning raw input into governed memory
- a shared language for multiple trusted agents operating on the same Vault

The main rule:

```text
The Vault is long-term memory.
The agent runtime is only an executor.
Runtime memory is temporary infrastructure.
```

## 2. Why It Exists

AI agents often remember too much, remember the wrong things, or treat weak notes as facts.

This architecture prevents memory pollution by separating:

- current truth from historical evidence
- reviewed knowledge from raw capture
- authority from technical write capability
- user-approved memory from runtime convenience
- active files from archive files

The goal is not to preserve everything.

The goal is to preserve memory that is:

- useful
- source-backed
- reviewable
- retrievable
- authority-labeled
- honest about uncertainty

## 3. Active Architecture Branch

| Branch | Version | Use Case | Human Authority |
| --- | --- | --- | --- |
| ARMOR Enterprise | V7.2 Stable | Teams, companies, business operations, brand/product/customer/project knowledge | Human owner or reviewer approves high-authority changes |

PAMA Personal V5.3 Stable has been archived under `archive/personal/PAMA-Personal-v5.3-Stable/` and is no longer part of the active install or update path.

## 4. Universal Principles

These principles apply to the active ARMOR architecture.

| Principle | Meaning |
| --- | --- |
| SSOT | Every current truth should have one authoritative home. |
| Capture is not authority | Fast notes are allowed, but capture does not make them true. |
| Capability is not permission | A tool may be able to edit a file, but architecture decides whether it may. |
| Store lower when uncertain | Weak, inferred, or temporary material belongs in low-authority layers. |
| Conservative retrieval | Drafts, logs, records, proposals, and archives are excluded from default truth retrieval. |
| Runtime memory is not long-term memory | SQLite, embeddings, caches, session summaries, and indexes are infrastructure only. |
| Archive instead of erase | Preserve historical context while removing stale active files from current truth paths. |

## 5. Governance Pattern

| Layer Type | ARMOR Example | Role |
| --- | --- | --- |
| Core governance | `00-Core/` | Architecture, permission, retrieval, routing, runtime policy |
| Current truth | `01-Facts/`, `02-Rules/` | Stable facts, rules, and approved standards |
| Validated learning | `03-Insights/` | Lessons, decisions, reviews, patterns |
| Research and uncertainty | `04-Research/` | External knowledge, hypotheses, assumptions |
| Active work | `05-Projects/` | Current execution and project workspaces |
| Evidence | `06-Records/` | Raw source material, not automatic truth |
| Operations | `70-Schemas/`, `80-Indexes/`, `81-Dashboards/` | Validation, navigation, audits |
| Low-authority capture | `90-Drafts/`, `91-Inbox/`, `92-Logs/`, `93-Proposals/` | Fast capture, proposals, logs, pending review |
| Archive | `99-Archive/` | Deprecated, expired, superseded, or historical memory |

## 6. ARMOR Enterprise At A Glance

ARMOR is the enterprise branch.

It is designed for business-critical memory:

- brand facts
- product specifications
- company facts
- customer profiles
- SOPs
- content standards
- project workspaces
- meeting records
- research
- proposals and review queues

### ARMOR Vault Structure

```text
Vault/
├── 00-Core/                  # Constitution, protocols, policies
├── 01-Facts/                 # Confirmed current truth
├── 02-Rules/                 # SOPs and reusable execution standards
├── 03-Insights/              # Validated cases, learnings, patterns, postmortems
├── 04-Research/              # Raw and reviewed external knowledge
│   ├── 00-Inbox/
│   └── 01-Reviewed/
├── 05-Projects/              # Active project workspaces
├── 06-Records/               # Raw evidence
├── 70-Schemas/               # Schemas and templates
├── 80-Indexes/               # Navigation indexes
├── 81-Dashboards/            # Health and debt dashboards
├── 90-Drafts/                # Unapproved working drafts
├── 91-Inbox/                 # Unclassified incoming content
├── 92-Logs/                  # Agent execution logs
├── 93-Proposals/             # Pending authority-changing changes
├── 94-Review-Queues/         # Scheduled reviews
└── 99-Archive/               # Historical or deprecated material
```

### ARMOR Permission Classes

| Class | Includes | Direct Write | Correct Behavior |
| --- | --- | --- | --- |
| A | `00-Core/`, `01-Facts/`, `02-Rules/` | No by default | Create proposal or ask for explicit human approval |
| B | `03-Insights/`, reviewed research, active projects | Conditional | Create or append when scoped; propose authority-changing edits |
| C | Drafts, inbox, logs, proposals, review queues | Yes | Direct low-authority writes allowed |
| R | Records and raw evidence | Append only | Preserve evidence; do not rewrite into current truth |

### ARMOR Required Core Documents

An ARMOR Vault should expose these active Core entry points:

```text
00-Core/Core-Document-Index.md
00-Core/Installed-Memory-Architecture.md
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
```

If an installed Vault still has active files such as `Hermes-V71-Adaptation-Guide.md`, `Hermes-Operating-Protocol.md`, `Profile-Skills-Architecture.md`, or `80-Indexes/V7-1-Index.md`, treat them as likely superseded active files and follow `AGENT_UPDATE.md`.

## 7. Runtime Model

Supported runtime examples:

- Hermes
- Claude Code
- Codex
- Opencode
- Cline
- OpenHands
- custom agents
- MCP-backed agents

The runtime may:

- read files
- search files
- draft
- patch allowed files
- append records
- create proposals
- write logs
- build indexes
- run validation checks

The runtime may not:

- treat its own memory database as authority
- silently edit high-authority files
- convert raw evidence into facts without review
- use another agent's working notes as current truth
- treat proposals as approved truth
- bypass human approval for high-risk changes

## 9. Default Retrieval Rules

For ARMOR, current-truth retrieval may use:

```text
00-Core/
01-Facts/
02-Rules/
03-Insights/
04-Research/01-Reviewed/
05-Projects/ relevant active project only
```

Exclude by default:

```text
90-Drafts/
91-Inbox/
92-Logs/
93-Proposals/
94-Review-Queues/
99-Archive/
04-Research/00-Inbox/
06-Records/ unless evidence mode is requested
```

## 10. Write Routing

When the user asks to remember something:

```text
Prompt Intake Router
  -> Memory Write Router
  -> classify memory candidate
  -> search for existing SSOT
  -> write low-authority material directly or create proposal
```

When the user reports an error or wrong behavior:

```text
Prompt Intake Router
  -> Root-Cause Fix Protocol
  -> locate source layer
  -> fix source or create proposal
  -> do not patch with runtime memory
```

When the user asks for discussion, analysis, or opinion:

```text
Do not write memory unless explicitly asked.
If uncertain, ask one concise clarification question.
```

## 11. Promotion Pipeline

Memory should move upward only when evidence and review justify it.

```text
Conversation / raw input
        |
        v
Low-authority capture
Drafts / inbox / records / working memory / research inbox
        |
        v
Classification + evidence check + SSOT search
        |
        v
Review or proposal when authority changes
        |
        v
Authoritative memory
Facts / rules / truth / reviewed research / validated insights
```

## 12. Multi-Agent Shared Vault Rules

When multiple agents share one Vault, each agent must use its own namespace for low-authority writes.

ARMOR examples:

```text
91-Inbox/Codex/
91-Inbox/Hermes/
91-Inbox/Claude-Code/

92-Logs/Codex/
92-Logs/Hermes/
92-Logs/Claude-Code/

93-Proposals/Codex/
93-Proposals/Hermes/
93-Proposals/Claude-Code/
```

Rules:

- Each agent may write logs in its own namespace.
- Agents may read other agents' logs for coordination, but logs are not authority.
- One agent's proposal is not current truth until approved.
- Conflicts between agents should become proposals or conflict notes.
- Authority files must not be directly edited just because an agent has file access.

## 13. Frontmatter Governance

All managed Markdown memory files should follow `FRONTMATTER_STANDARD.md`.

The standard separates:

```text
Universal Core fields
Conditional Governance fields
Domain Profile fields
Tool or Skill Extension fields
```

Canonical concepts must remain distinct:

```text
memory_layer      = where memory belongs
permission_class  = ARMOR write class A/B/C/R
authority         = truth or knowledge authority
confidence        = epistemic confidence
write_policy      = modification policy
```

Installed registries:

```text
ARMOR: 70-Schemas/Frontmatter-Registry.md
```

New files use canonical fields immediately. Existing files migrate lazily when meaningfully updated. Logs, records, and archives are not mass-rewritten merely to remove legacy field names.

## 14. Document Map

Every installed Vault should expose:

```text
Static Vault Map
Dynamic Document Registry
```

The static map explains:

- architecture entry points
- top-level layers
- authority boundaries
- agent reading order
- task-to-document routing
- retrieval defaults and exclusions

The dynamic `.base` registry uses canonical frontmatter to show:

- current authority
- files needing review
- expiring documents
- proposals and conflicts
- documents grouped by memory layer
- historical files

Recommended locations:

```text
ARMOR:
  80-Indexes/Vault-Document-Map.md
  80-Indexes/Document-Registry.base
```

The map is navigation, not authority. Agents must open the underlying authority files before answering or writing.

See `DOCUMENT_MAP_STANDARD.md`.

## 15. Template Profiles

Templates are creation aids, not authority sources.

The project ships three mutually exclusive syntax profiles:

| Profile | Best For | Runtime Requirement |
| --- | --- | --- |
| Plain Markdown | AI agents and portable Markdown workspaces | None |
| Obsidian Core Templates | Manual insertion in Obsidian | Official Templates core plugin |
| Templater | Folder-based automatic templates | Optional reviewed community plugin |

Install one active profile per template folder. Do not mix unresolved Plain, `{{date}}`, and `<% tp.* %>` variables.

Templater must keep system commands disabled by default. Automatic file creation still follows the Frontmatter Standard, routers, permission classes, and human approval requirements.

See `TEMPLATE_AUTOMATION_GUIDE.md`.

## 16. Installation Mental Model

Use `AGENT_INSTALL.md` when the target Vault does not yet have the architecture.

Installation means:

- create missing top-level folders
- copy current Core documents
- create or verify schemas and templates
- create agent namespaces if shared
- write an installation log
- validate required files and retrieval exclusions

Default install branch:

```text
ARMOR Enterprise V7.2 Stable
```

PAMA is archived and should not be installed from the active path.

## 17. Update Mental Model

Use `AGENT_UPDATE.md` when the Vault already exists.

Update means:

- identify installed version
- create archive snapshot
- sync current Core and Indexes
- archive superseded active files
- retarget or mark obsolete pending proposals
- preserve logs, records, decisions, and archives
- write an update log
- validate that stale active files cannot be mistaken for current truth

Do not rewrite history to make search results clean.

Clean active truth.

Preserve historical evidence.

## 18. Common Retired Active Files

For v1.6.0 / ARMOR V7.2, these old active files or concepts should not remain active:

| Retired Active File or Concept | Current Replacement | Action |
| --- | --- | --- |
| `00-Core/Hermes-V71-Adaptation-Guide.md` | `00-Core/Agent-Runtime-Adaptation-Guide.md` | Archive old active file |
| `00-Core/Hermes-Operating-Protocol.md` | Routers + runtime adaptation + multi-agent governance | Archive old active file |
| `00-Core/Profile-Skills-Architecture.md` | Runtime-local Hermes documentation | Archive or move outside active Core |
| `80-Indexes/V7-1-Index.md` or another old architecture index | `80-Indexes/Vault-Document-Map.md` | Archive or supersede old active index |
| Claudian or Obsidian UI executor plugin support | Direct trusted runtime file access | Archive old execution guides |
| Runtime memory as long-term memory | Vault as durable memory | Update active policy |
| Multiple conflicting frontmatter standards | `FRONTMATTER_STANDARD.md` + installed Registry | Preserve domain extensions, migrate canonical fields lazily |
| No stable Vault navigation entry | `DOCUMENT_MAP_STANDARD.md` + static map + dynamic registry | Install branch-specific map files |
| Mixed template syntaxes or legacy template frontmatter | `TEMPLATE_AUTOMATION_GUIDE.md` + one selected profile | Preserve one active profile and normalize templates |
| PAMA active install path | `archive/personal/PAMA-Personal-v5.3-Stable/` | Keep as historical archive only |

Historical mentions in `06-Records/`, `92-Logs/`, `99-Archive/`, or superseded proposals are acceptable when clearly historical.

## 19. Which File Should An Agent Read Next?

Use this routing table after reading this document.

| Task | Next File |
| --- | --- |
| First-time install | `AGENT_INSTALL.md` |
| Existing Vault update | `AGENT_UPDATE.md` |
| Frontmatter fields or migration | `FRONTMATTER_STANDARD.md` |
| Vault navigation or document discovery | `DOCUMENT_MAP_STANDARD.md` |
| Template installation or automation | `TEMPLATE_AUTOMATION_GUIDE.md` |
| Enterprise architecture details | `enterprise/V7_2_Stable.md` |
| Runtime integration | `enterprise/agent_runtime_adaptation_guide.md` |
| Shared ARMOR Vault | `enterprise/multi_agent_shared_vault_governance.md` |
| User says "remember" | Memory Write Router for the selected branch |
| User reports wrong behavior | Root-Cause Fix Protocol for the selected branch |
| Ambiguous or risky command | Prompt Intake Router for the selected branch |
| Runtime memory question | Runtime Memory Policy for the selected branch |

## 20. Final Operating Summary

If you remember nothing else, remember this:

```text
Vault = durable memory and audit layer.
Runtime = executor and temporary state.
Low-authority capture is allowed.
Authority requires source, routing, review, and permission.
Logs, records, drafts, proposals, and archives are not current truth by default.
When upgrading, archive retired active files instead of deleting history.
```
