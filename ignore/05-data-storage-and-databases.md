# 5) Data Storage & Databases

## Basics
Storage design decides how data is structured, accessed, and scaled.

Core components:
- Relational DB concepts (indexes, joins, transactions)
- NoSQL types: key-value, document, wide-column, graph
- CAP theorem + consistency models (strong/eventual/causal)
- Replication (sync/async), sharding/partitioning
- Read replicas, write scaling
- OLTP vs OLAP
- Data modeling (normalization vs denormalization)
- Migrations and zero-downtime schema changes

## How It Works
Choose storage based on access patterns, consistency needs, and growth profile.

```text
Workload -> Data Model -> DB Type -> Scaling Strategy
```

Cause-effect idea:
- Missing index -> table scans -> latency spikes.
- Poor shard key -> hot partition -> write bottleneck.

## Simple Example
Orders platform:
- OLTP relational DB for checkout transactions.
- Read replicas for analytics-heavy dashboards.
- Async pipeline to OLAP warehouse for reporting.

Analogy: Normalization is organizing a library catalog; denormalization is putting popular books on a quick-access shelf.

## Why and What-If Questions
- Why eventual consistency sometimes acceptable?
  - Some read paths tolerate brief staleness for better availability.
- What if a schema change blocks writes?
  - Use online migrations: add new column, dual-write, backfill, switch reads.
- What if replication lag grows?
  - Route critical reads to primary or use read-after-write strategies.

## Practical Applications
- Multi-tenant SaaS data layout.
- Global read scaling with replicas.
- Safe schema evolution in always-on systems.

## Compare With Related Ideas
- OLTP vs OLAP: transactional correctness vs large-scale analytical scans.
- Sync vs async replication: stronger freshness vs lower write latency.

## Retention Tips
- For each use case, write `read pattern`, `write pattern`, `consistency need` first.
- Learn one failure story for indexing, sharding, and migration each.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
