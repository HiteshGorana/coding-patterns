# 1) Foundations

## Basics
System design foundations are the pre-build thinking steps that prevent expensive rework later.

Core components:
- Requirements gathering (functional vs non-functional)
- Assumptions, constraints, scope control
- Capacity estimation (QPS, peak traffic, storage, bandwidth)
- Latency vs throughput vs availability tradeoffs
- Cost estimation (cloud spend drivers)

## How It Works
1. Capture functional requirements (what the system must do).
2. Capture non-functional requirements (how well it must do it: latency, uptime, security, cost).
3. Record assumptions and constraints to bound the solution space.
4. Estimate capacity for day-1 and peak growth.
5. Evaluate tradeoffs and refine scope.

```text
Requirements -> Constraints -> Estimates -> Tradeoffs -> Architecture Draft
```

Cause-effect idea:
- Underestimated traffic -> overloaded services -> high latency and failures.
- Unclear scope -> architecture drift -> missed deadlines.

## Simple Example
Designing a URL shortener:
- Functional: create short URL, redirect fast.
- Non-functional: 99.99% availability, p95 redirect < 100 ms.
- Capacity: 20k writes/sec peak, 200k reads/sec peak.
- Cost: CDN + cache to reduce database read spend.

Analogy: This is like planning a road trip. Destination is functional requirements; fuel budget and travel time are non-functional requirements.

## Why and What-If Questions
- Why separate functional and non-functional requirements?
  - Because both can conflict: adding features may hurt latency or cost.
- What if assumptions are wrong?
  - Track them explicitly and review after each milestone.
- What if budget is strict?
  - Optimize for cost first, then iterate on performance hotspots.

## Practical Applications
- Interview problem framing in first 5 minutes.
- Production capacity planning before launches.
- Cloud cost forecasting and right-sizing.

## Compare With Related Ideas
- Requirements gathering vs backlog grooming: requirements define system intent; backlog grooming prioritizes implementation tasks.
- Capacity estimation vs load testing: estimation predicts; load testing validates.

## Retention Tips
- Use the checklist `RASCCT`: Requirements, Assumptions, Scope, Capacity, Cost, Tradeoffs.
- For any design, always write one table with `target metric`, `current estimate`, `risk`.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
