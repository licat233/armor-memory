# Routing Examples

## Website article without project

User request:

> 帮我写一篇 ARMOR 官网磁吸货架灯文章。

Classification:

```yaml
object: work-product
domain: website
artifact: article
project: null
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain website \
  --artifact article
```

Expected path:

```text
03-Records/Published/Articles/
```

## Website article with active project

User request:

> 为 ARMOR 官网重构项目写一篇磁吸货架灯文章。

Classification:

```yaml
object: work-product
domain: website
artifact: article
project: armor-website
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain website \
  --artifact article \
  --project armor-website
```

Expected path:

```text
03-Records/Published/Articles/
```

## Product manual

User request:

> 给磁吸货架灯产品写一份安装手册。

Classification:

```yaml
object: work-product
domain: products
artifact: product-manual
entity: magnetic-shelf-light
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain products \
  --artifact product-manual \
  --entity magnetic-shelf-light
```

Expected path:

```text
02-Projects/Workspaces/Products/magnetic-shelf-light/Documentation/
```

## Product spec sheet

User request:

> 整理这款线性灯条的规格表。

Classification:

```yaml
object: work-product
domain: products
artifact: spec-sheet
entity: linear-light-bar
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain products \
  --artifact spec-sheet \
  --entity linear-light-bar
```

Expected path:

```text
02-Projects/Workspaces/Products/linear-light-bar/Spec-Sheets/
```

## Marketing campaign

User request:

> 帮我准备一套秋季促销 campaign 方案。

Classification:

```yaml
object: work-product
domain: marketing
artifact: campaign
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain marketing \
  --artifact campaign
```

Expected path:

```text
02-Projects/Workspaces/Marketing/Campaigns/
```

## Social copy

User request:

> 写三条 LinkedIn 社媒文案。

Classification:

```yaml
object: work-product
domain: marketing
artifact: social-copy
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain marketing \
  --artifact social-copy
```

Expected path:

```text
02-Projects/Workspaces/Marketing/Social-Copy/
```

## Operations checklist

User request:

> 做一份展会出货检查清单。

Classification:

```yaml
object: work-product
domain: operations
artifact: checklist
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object work-product \
  --domain operations \
  --artifact checklist
```

Expected path:

```text
02-Projects/Workspaces/Operations/Checklists/
```

## Meeting record

User request:

> 保存今天的产品评审会议记录。

Classification:

```yaml
object: record
record_type: meeting
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object record \
  --record-type meeting
```

Expected path:

```text
03-Records/Meetings/
```

## Email record

User request:

> 归档客户刚发来的邮件。

Classification:

```yaml
object: record
record_type: email
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object record \
  --record-type email
```

Expected path:

```text
03-Records/Emails/
```

## Journal entry

User request:

> 记录今天的工作日志。

Classification:

```yaml
object: record
record_type: journal
year: "2026"
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object record \
  --record-type journal \
  --year 2026
```

Expected path:

```text
03-Records/Journal/2026/
```

## Product knowledge

User request:

> 把这条产品兼容性规则记成长期产品知识。

Classification:

```yaml
object: knowledge
knowledge_type: product
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object knowledge \
  --knowledge-type product
```

Expected path:

```text
01-Knowledge/Products/
```

## Brand knowledge

User request:

> 更新 ARMOR 的品牌定位知识页。

Classification:

```yaml
object: knowledge
knowledge_type: brand
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object knowledge \
  --knowledge-type brand
```

Expected path:

```text
01-Knowledge/Brand/
```

## Reusable rule

User request:

> 把这个写作规范保存成可复用规则。

Classification:

```yaml
object: knowledge
knowledge_type: rule
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object knowledge \
  --knowledge-type rule
```

Expected path:

```text
01-Knowledge/Rules/
```

## Competitor source

User request:

> 保存这篇竞争对手官网页面作为研究来源。

Classification:

```yaml
object: research
research_kind: source
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object research \
  --research-kind source
```

Expected path:

```text
04-Research/Sources/
```

## Competitor research note

User request:

> 整理一份竞争对手调研笔记。

Classification:

```yaml
object: research
research_kind: note
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object research \
  --research-kind note
```

Expected path:

```text
04-Research/Notes/
```

## Explicit unresolved input

User request:

> 先收下这段材料，我现在还不确定它属于哪一类。

Classification:

```yaml
object: unresolved
```

Command:

```bash
.agent/skills/armor-memory/scripts/route.sh \
  --object unresolved
```

Expected path:

```text
90-Inbox/
```
