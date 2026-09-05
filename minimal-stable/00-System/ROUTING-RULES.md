---
type: "system"
status: "active"
authority: "canonical"
created: "2026-07-27"
updated: "2026-09-05"
---

# Routing Rules

The router is a deterministic path mapper. It does not read natural language and it does not guess intent from keywords.

## Interface

Use structured arguments only:

```bash
python3 scripts/armor-route.py \
  --object work-product \
  --domain website \
  --artifact article \
  --project armor-website
```

## Closed Enums

- `object`: `work-product`, `record`, `knowledge`, `research`, `unresolved`
- `domain`: `website`, `content`, `marketing`, `products`, `operations`
- `artifact`: `article`, `landing-page`, `case-study`, `blog-post`, `report`, `campaign`, `email-sequence`, `social-copy`, `product-manual`, `spec-sheet`, `price-list`, `process-doc`, `checklist`, `internal-report`
- `record-type`: `meeting`, `email`, `conversation`, `journal`, `feedback`, `published`
- `knowledge-type`: `company`, `brand`, `product`, `customer`, `rule`, `insight`
- `research-kind`: `source`, `note`

Unknown values fail immediately through `argparse choices=`.

## Lifecycle-Neutral Rule

Directory location represents operational purpose, not lifecycle state.

- Named project work uses `02-Projects/Projects/<project>/`; project completion does not require moving the project tree.
- Stable channel content uses one content home regardless of draft/review/published status.
- `03-Records/Published/` is for evidence of an actual publication event or an explicitly requested snapshot, not for newly created content merely intended for publication.

## Deterministic Rules

### Work Product

- `work-product + website + article + project`
  `-> 02-Projects/Workspaces/Website/Articles/`
- `work-product + website + article`
  `-> 02-Projects/Workspaces/Website/Articles/`
- `work-product + marketing + social-copy + project`
  `-> 02-Projects/Workspaces/Marketing/Social-Media/`
- `work-product + marketing + social-copy`
  `-> 02-Projects/Workspaces/Marketing/Social-Media/`
- `work-product + products + product-manual + entity`
  `-> 02-Projects/Workspaces/Products/<entity>/Documentation/`
- `work-product + products + product-manual + entity + project`
  `-> 02-Projects/Projects/<project>/Products/<entity>/Documentation/`
- other supported work-products with `--project`
  `-> 02-Projects/Projects/<project>/<domain-specific-tail>/`

Article and official social content each have one lifecycle-neutral destination. A supplied project value is still validated but does not change those two channel-content destinations.

### Record

- `record + journal + year`
  `-> 03-Records/Journal/<year>/`
- `record + meeting`
  `-> 03-Records/Meetings/`
- `record + published`
  `-> 03-Records/Published/`

`record + published` means publication evidence/snapshot. It does not mean editable source content.

### Knowledge

- `knowledge + product`
  `-> 01-Knowledge/Products/`

### Research

- `research + source`
  `-> 04-Research/Sources/`
- `research + note`
  `-> 04-Research/Notes/`

### Unresolved

- `unresolved`
  `-> 90-Inbox/`

## Argument Failures

- Missing required arguments must fail.
- Invalid enum values must fail.
- Unsupported domain and artifact combinations must fail.
- `90-Inbox/` is valid only when `--object unresolved` is explicitly provided.

## Name Safety

Project and entity names use deterministic slug normalization:

```yaml
NFKC normalize
trim whitespace
lowercase
replace spaces and underscores with hyphens
collapse repeated hyphens
```

Rejected names include absolute paths, path traversal, slash separators, and shell metacharacters.
