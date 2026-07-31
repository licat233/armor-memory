# Authority Guide

- `working`: the default state for project documents, research notes, and new knowledge pages
- `verified`: checked against a relevant source or reviewer
- `canonical`: explicitly approved or designated as the authoritative version
- `evidence`: record material documenting what happened or what was received

Rules:

- project documents default to `working`
- research notes default to `working`
- records may use `evidence`
- knowledge defaults to `working` unless verified
- `canonical` requires explicit user approval or an explicitly designated authoritative source
- canonical content must not be silently overwritten

## Authority during retrieval

- Read the file's explicit `authority` field. Do not infer authority from other
  metadata.
- `status: active` means the file is in current use; it is not an authority
  level.
- `revision`, `source_quality`, `write_policy`, `type`, and folder location are
  supporting metadata, not substitutes for `authority`.
- A knowledge file without explicit `authority` remains `working`.
- Rank claims only as explicit `canonical` > explicit `verified` > `working`.
- When equal or unclear authority sources conflict, expose the conflict and
  ask for a decision.
- Do not describe a set of claims as verified unless every material claim has
  explicit verified/canonical authority or was checked in the current task.

Before changing canonical content:

1. Read current content.
2. Identify the exact change.
3. Obtain explicit approval.
4. Update the file.
5. Add a short changelog entry.

Do not add Proposal files or Review Queues to the default workflow.
