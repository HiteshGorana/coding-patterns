# 9) Scalability Techniques

## Basics
Scalability is about maintaining performance and reliability as load grows.

Core components:
- Horizontal vs vertical scaling
- Stateless services and session management
- Partitioning strategies (by user, by time, by geography)
- Read/write separation
- Bulkheads, isolation, multi-tenancy
- Autoscaling fundamentals

## How It Works
- Identify bottleneck resource (CPU, memory, I/O, lock contention).
- Scale the constrained component.
- Isolate workloads to prevent cascading impact.

```text
Growth -> Bottleneck -> Scale/Partition/Isolate -> Stable SLA
```

Cause-effect idea:
- Stateful app instances -> sticky-session complexity -> poor elasticity.
- Single large tenant sharing pool -> noisy-neighbor failures.

## Simple Example
Social feed service:
- Stateless API pods behind LB.
- Session stored in Redis/JWT.
- Reads served from replicas and cache.
- Autoscaling on p95 latency + CPU.

Analogy: Horizontal scaling adds checkout counters; vertical scaling makes one counter faster.

## Why and What-If Questions
- Why not only vertical scaling?
  - Hardware limits and failure blast radius become problems.
- What if partition key is bad?
  - Uneven load causes hot shards; repartition strategy needed.
- What if autoscaling is too reactive?
  - Add predictive scaling and cooldown tuning.

## Practical Applications
- SaaS onboarding growth.
- Seasonal traffic spikes.
- Tenant isolation for enterprise plans.

## Compare With Related Ideas
- Stateless sessions vs sticky sessions: easier scaling vs simpler local state.
- Bulkheads vs circuit breakers: isolate capacity vs stop failing dependencies.

## Retention Tips
- Use `BPSI`: Bottleneck, Partition, Statelessness, Isolation.
- Plot throughput vs latency curves whenever load changes.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
