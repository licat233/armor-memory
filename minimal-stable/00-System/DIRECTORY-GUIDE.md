---
type: "system"
status: "active"
authority: "canonical"
created: "2026-07-27"
updated: "2026-09-05"
---

# Directory Guide

```text
minimal-stable/
├── ARCHITECTURE.md
├── 00-System/
├── 01-Knowledge/
├── 02-Projects/
├── 03-Records/
├── 04-Research/
├── 90-Inbox/
├── 99-Archive/
├── scripts/
└── tests/
```

Recommended substructure:

```text
01-Knowledge/
├── Company/
├── Brand/
├── Products/
├── Customers/
├── Rules/
└── Insights/

02-Projects/
├── Projects/
└── Workspaces/

03-Records/
├── Meetings/
├── Emails/
├── Conversations/
├── Journal/
├── Feedback/
└── Published/

04-Research/
├── Sources/
└── Notes/
```

## Lifecycle Cost Rule

Directory location represents operational purpose, not lifecycle status.

`02-Projects/Projects/` is the stable home for named project work. A project remains there when it starts, pauses, completes, or is revisited. Do not create `Active/` and `Completed/` lifecycle roots that require humans or Agents to move project trees as status changes.

`02-Projects/Workspaces/` is the stable home for persistent domain/entity work that is not scoped to one named project. Website articles and official social copy use lifecycle-neutral channel-content homes under Workspaces.

`03-Records/Published/` stores evidence of publication events or explicitly requested published snapshots. Editable article/social source content does not move there merely because it becomes published.

Status metadata is optional and should be Agent-maintained when useful. Humans should not be assigned routine status, move, or archive chores merely to keep the directory tree cosmetically synchronized with lifecycle state.
