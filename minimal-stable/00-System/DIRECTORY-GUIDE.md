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
├── Active/
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

`02-Projects/Completed/` is not part of the recommended structure. Project completion must not create a recurring human obligation to move an entire project tree merely to express that its lifecycle changed.

`02-Projects/Active/` remains the current Router path for named projects for compatibility with the deployed Minimal Stable layout. Its name must not be interpreted as requiring a later move to `Completed/`.

If the `Active/` naming itself becomes operationally confusing, replacing it with a lifecycle-neutral project root should be handled as a one-time migration with the Router and live Vault changed together. Do not create parallel old/new project roots during normal operation.

Status metadata is optional and should be Agent-maintained when useful. Humans should not be assigned routine status, move, or archive chores merely to keep the directory tree cosmetically synchronized with lifecycle state.
