# Classification Protocol

This protocol converts natural-language document tasks into structured router arguments.

The protocol chooses router values. The router produces the final path.

## Object Classification

Use exactly one object type:

- `work-product`
- `record`
- `knowledge`
- `research`
- `unresolved`

### `work-product`

Use when the user asks to create, write, draft, edit, improve, design, prepare, produce, or generate a business document or deliverable.

Examples:

- website article
- product manual
- marketing copy
- campaign plan
- report
- checklist
- landing page copy

### `record`

Use when preserving something that already happened or was received.

Examples:

- meeting record
- email
- conversation
- journal
- feedback
- published-content snapshot

A proposal written after a meeting is a `work-product`. The meeting transcript itself is a `record`.

### `knowledge`

Use only when the user explicitly asks to remember something long term, maintain reusable knowledge, define a reusable rule, update product knowledge, update brand knowledge, or preserve an insight for future reuse.

Do not classify an ordinary article or report as knowledge merely because it contains facts.

### `research`

Use when investigating external information.

Examples:

- competitor research
- market research
- external technical investigation
- saved external source
- research notes

### `unresolved`

Use only when the task cannot be classified after considering:

- the user request
- active project context
- current working directory
- existing Agent conversation context

Unverified content is not automatically unresolved.

## Project Priority

If an explicit active project exists and the object is a `work-product`, include `--project`.

Do not send records, knowledge, or research into a project unless the router explicitly supports it.

## Entity Usage

Use `--entity` only when required by the router.

Current required product examples:

- `product-manual`
- `spec-sheet`
- `price-list`

Do not invent a generic entity argument for unsupported combinations.

## Closed Values

Inspect supported values from:

```bash
python3 minimal-stable/scripts/armor-route.py --help
```

Agents must not invent:

- object types
- domains
- artifacts
- record types
- knowledge types
- research kinds

If a legitimate task cannot be represented, stop and report:

```text
Router vocabulary gap
```

Do not silently choose the nearest value.

## Structured Classification Shape

Before calling the router, resolve a structure like:

```json
{
  "object": "work-product",
  "domain": "website",
  "artifact": "article",
  "project": "armor-website",
  "entity": null,
  "record_type": null,
  "knowledge_type": null,
  "research_kind": null,
  "year": null
}
```

Agents do not need to show this structure unless debugging or evaluation is requested.

