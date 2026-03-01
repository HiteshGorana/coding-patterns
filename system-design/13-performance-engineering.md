# 13) Performance Engineering

## Basics
Performance engineering systematically improves latency, throughput, and efficiency.

Core components:
- Profiling and bottleneck analysis
- Latency budgeting (p50/p95/p99)
- N+1 query issues
- Index tuning and query plans (high-level)
- Connection pooling
- Compression (gzip/brotli), payload optimization

## How It Works
- Define performance targets and budgets.
- Measure baseline with real traffic patterns.
- Find top bottlenecks and optimize highest-impact path first.
- Re-measure after each change.

```text
Target -> Measure -> Profile -> Optimize -> Validate
```

Cause-effect idea:
- Optimize without profiling -> wasted engineering effort.
- Ignoring tail latency -> good averages, poor user experience.

## Simple Example
Search API p99 too high:
- Profile reveals DB query N+1.
- Add join/preload and index.
- Enable compression for large responses.
- p99 drops from 900 ms to 220 ms.

Analogy: Performance work is triage in an emergency room: treat biggest risk first.

## Why and What-If Questions
- Why watch p99, not only p50?
  - Tail users often drive complaints and SLA misses.
- What if connection pool is too small?
  - Queuing delays and timeouts increase.
- What if compression increases CPU too much?
  - Use thresholds and tune level by payload size.

## Practical Applications
- API latency reduction projects.
- Cost reduction via efficient compute and query paths.
- Capacity planning with realistic performance envelopes.

## Compare With Related Ideas
- Profiling vs benchmarking: where time is spent vs overall throughput under load.
- Gzip vs brotli: broad compatibility vs often better compression ratio.

## Retention Tips
- Keep a `Top 5 Latency Contributors` dashboard.
- Use a repeating loop: `measure -> change -> measure`.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
