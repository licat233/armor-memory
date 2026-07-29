---
type: "system"
status: "active"
authority: "reference"
created: "2026-07-27"
updated: "2026-07-27"
---

# Routing Tests

Structured routing cases only. The router does not accept natural-language task text.

| # | Structured input | Expected destination |
| --- | --- | --- |
| 1 | `work-product + website + article` | `03-Records/Published/Articles/` |
| 2 | `work-product + website + article + project=armor-website` | `03-Records/Published/Articles/` |
| 3 | `work-product + website + landing-page` | `02-Projects/Workspaces/Website/Landing-Pages/` |
| 4 | `work-product + website + case-study` | `02-Projects/Workspaces/Website/Case-Studies/` |
| 5 | `work-product + content + blog-post` | `02-Projects/Workspaces/Content/Blog-Posts/` |
| 6 | `work-product + content + report` | `02-Projects/Workspaces/Content/Reports/` |
| 7 | `work-product + content + case-study + project=q4-content` | `02-Projects/Active/q4-content/Content/Case-Studies/` |
| 8 | `work-product + marketing + campaign` | `02-Projects/Workspaces/Marketing/Campaigns/` |
| 9 | `work-product + marketing + email-sequence + project=launch-2026` | `02-Projects/Active/launch-2026/Marketing/Email-Sequences/` |
| 10 | `work-product + marketing + social-copy` | `02-Projects/Workspaces/Marketing/Social-Copy/` |
| 11 | `work-product + products + product-manual + entity=armor-pro-panel` | `02-Projects/Workspaces/Products/armor-pro-panel/Documentation/` |
| 12 | `work-product + products + product-manual + entity=armor-pro-panel + project=manual-refresh` | `02-Projects/Active/manual-refresh/Products/armor-pro-panel/Documentation/` |
| 13 | `work-product + products + spec-sheet + entity=line-bar-x` | `02-Projects/Workspaces/Products/line-bar-x/Spec-Sheets/` |
| 14 | `work-product + products + price-list + entity=shelf-led + project=pricing-2026` | `02-Projects/Active/pricing-2026/Products/shelf-led/Price-Lists/` |
| 15 | `work-product + operations + process-doc` | `02-Projects/Workspaces/Operations/Process-Docs/` |
| 16 | `work-product + operations + checklist` | `02-Projects/Workspaces/Operations/Checklists/` |
| 17 | `work-product + operations + internal-report + project=warehouse-audit` | `02-Projects/Active/warehouse-audit/Operations/Internal-Reports/` |
| 18 | `record + meeting` | `03-Records/Meetings/` |
| 19 | `record + email` | `03-Records/Emails/` |
| 20 | `record + conversation` | `03-Records/Conversations/` |
| 21 | `record + feedback` | `03-Records/Feedback/` |
| 22 | `record + published` | `03-Records/Published/` |
| 23 | `record + journal + year=2026` | `03-Records/Journal/2026/` |
| 24 | `knowledge + company` | `01-Knowledge/Company/` |
| 25 | `knowledge + brand` | `01-Knowledge/Brand/` |
| 26 | `knowledge + product` | `01-Knowledge/Products/` |
| 27 | `knowledge + customer` | `01-Knowledge/Customers/` |
| 28 | `knowledge + rule` | `01-Knowledge/Rules/` |
| 29 | `knowledge + insight` | `01-Knowledge/Insights/` |
| 30 | `research + source` | `04-Research/Sources/` |
| 31 | `research + note` | `04-Research/Notes/` |
| 32 | `unresolved` | `90-Inbox/` |
| 33 | repeated `work-product + website + article + project=armor-website` | same output every run |
| 34 | unknown enum value | fail |
| 35 | missing required argument | fail |
| 36 | invalid domain and artifact combination | fail |
| 37 | path traversal in project or entity | fail |
| 38 | Unicode project or entity name | normalize with deterministic slug rules |
