# 10) Reliability & Resilience

## Basics
Reliability keeps systems correct over time; resilience keeps systems useful during failures.

Core components:
- Timeouts, retries, exponential backoff + jitter
- Circuit breakers, fallbacks
- Graceful degradation
- Health checks (liveness/readiness)
- Disaster recovery (RPO/RTO)
- Multi-AZ vs multi-region
- Failover strategies

## How It Works
- Detect failures quickly.
- Contain blast radius.
- Recover automatically when safe.
- Plan disaster recovery targets in advance.

```text
Failure -> Detect -> Isolate -> Recover -> Learn
```

Cause-effect idea:
- No timeout -> thread exhaustion -> cascading outages.
- Aggressive retries without jitter -> retry storms.

## Simple Example
Checkout service depends on recommendations API:
- Timeout recommendation call at 100 ms.
- On failure, fallback to static best-sellers.
- Circuit breaker opens after repeated failures.

Analogy: Airplane systems have redundancy; when one part fails, backup keeps core function available.

## Why and What-If Questions
- Why add jitter to retries?
  - To avoid synchronized retry spikes.
- What if entire region fails?
  - Multi-region failover with DNS or traffic manager.
- What if readiness checks are wrong?
  - LB sends traffic to unhealthy pods, causing user-facing errors.

## Practical Applications
- High-availability payment systems.
- Incident response playbooks.
- Region-level disaster drills.

## Compare With Related Ideas
- Liveness vs readiness: process alive vs able to serve traffic.
- Multi-AZ vs multi-region: lower latency and simpler ops vs stronger disaster isolation.

## Retention Tips
- Remember `TRCG`: Timeout, Retry, Circuit breaker, Graceful degradation.
- During design reviews, always ask: `How does this fail, and how do we recover?`

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
