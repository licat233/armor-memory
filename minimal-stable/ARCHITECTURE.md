---
type: "system"
status: "active"
created: "2026-07-27"
updated: "2026-07-27"
---

# ARMOR Minimal Stable Architecture

ARMOR Minimal Stable is a deterministic routing model for shared LLM workflows.

Its purpose is not to classify free-form language. Its purpose is to map structured routing inputs to stable paths.

## Design Rules

1. The router accepts only closed enums.
2. Unknown enum values fail immediately through `argparse choices=`.
3. Missing required fields fail immediately.
4. `90-Inbox/` is reachable only through explicit `--object unresolved`.
5. Routing is based on operational purpose, not truth status.

## Required Deliverables

This implementation includes:

- `00-System/START-HERE.md`
- `00-System/ROUTING-RULES.md`
- `00-System/AUTHORITY-RULES.md`
- `00-System/DIRECTORY-GUIDE.md`
- `00-System/ROUTING-TESTS.md`
- `scripts/armor-route.py`
- `tests/test_armor_route.py`

## Router Interface

```bash
python3 scripts/armor-route.py \
  --object work-product \
  --domain website \
  --artifact article \
  --project armor-website
```

Supported enums:

- `object`: `work-product`, `record`, `knowledge`, `research`, `unresolved`
- `domain`: `website`, `content`, `marketing`, `products`, `operations`
- `artifact`: `article`, `landing-page`, `case-study`, `blog-post`, `report`, `campaign`, `email-sequence`, `social-copy`, `product-manual`, `spec-sheet`, `price-list`, `process-doc`, `checklist`, `internal-report`
- `record-type`: `meeting`, `email`, `conversation`, `journal`, `feedback`, `published`
- `knowledge-type`: `company`, `brand`, `product`, `customer`, `rule`, `insight`
- `research-kind`: `source`, `note`

## Name Normalization

Project and entity names are normalized with this exact procedure:

1. Apply Unicode `NFKC` normalization.
2. Trim leading and trailing whitespace.
3. Convert to lowercase.
4. Replace spaces and underscores with `-`.
5. Collapse repeated hyphens into a single `-`.
6. Reject empty results.

Rejected inputs:

- absolute paths
- names containing `/` or `\`
- names containing `..`
- shell metacharacters such as `;`, `&`, `|`, `<`, `>`, `$`, `` ` ``, `!`

## Deterministic Examples

- `work-product + website + article + project`
  `-> 03-Records/Published/Articles/`
- `work-product + website + article`
  `-> 03-Records/Published/Articles/`
- `work-product + marketing + social-copy + project`
  `-> 03-Records/Published/Social-Media/`
- `work-product + marketing + social-copy`
  `-> 03-Records/Published/Social-Media/`
- `work-product + products + product-manual + entity`
  `-> 02-Projects/Workspaces/Products/<entity>/Documentation/`
- `record + journal + year`
  `-> 03-Records/Journal/<year>/`
- `knowledge + product`
  `-> 01-Knowledge/Products/`
- `research + source`
  `-> 04-Research/Sources/`
- `unresolved`
  `-> 90-Inbox/`
