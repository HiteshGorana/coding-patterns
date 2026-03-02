# 14) Data & Analytics Pipelines

## Basics
Pipelines move, transform, and validate data for analytics and decision-making.

Core components:
- ETL vs ELT
- Batch vs streaming pipelines
- Data lake vs warehouse
- Event schemas and evolution
- Exactly-once challenges in pipelines
- Data quality checks

## How It Works
- Ingest data from sources.
- Transform and enrich it.
- Load to storage for analytics consumption.
- Validate quality and freshness continuously.

```text
Sources -> Ingest -> Transform -> Store -> BI/ML
```

Cause-effect idea:
- Schema drift without governance -> broken downstream reports.
- Missing quality checks -> incorrect business decisions.

## Simple Example
Order analytics:
- Stream `order_events` for near real-time dashboards.
- Nightly batch job reconciles totals.
- Quality checks verify row count and null thresholds.

Analogy: Pipeline is a water treatment plant: collect, clean, test, then distribute.

## Why and What-If Questions
- Why ELT in modern stacks?
  - Warehouses can scale transformations efficiently after load.
- What if events are duplicated?
  - Deduplicate by event ID and watermark windows.
- What if late data arrives?
  - Use reprocessing windows and correction jobs.

## Practical Applications
- Executive KPI dashboards.
- Fraud detection streams.
- Product experiment analytics.

## Compare With Related Ideas
- Batch vs streaming: lower cost/high latency vs continuous/low latency.
- Data lake vs warehouse: flexible raw storage vs modeled analytical performance.

## Retention Tips
- For every dataset, track `freshness`, `completeness`, `accuracy`.
- Build one lineage diagram per pipeline.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
