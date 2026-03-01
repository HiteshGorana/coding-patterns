# 19) Testing Strategy (for Distributed Systems)

## Basics
Testing distributed systems requires multiple layers to catch correctness and behavior issues under load/failure.

Core components:
- Unit, integration, contract tests
- Load testing, stress testing
- Chaos testing concepts
- Replay/testing with production-like data (safely)

## How It Works
- Unit tests validate local logic.
- Integration/contract tests validate service interactions.
- Load/stress tests validate capacity limits.
- Chaos tests validate resilience assumptions.

```text
Unit -> Integration -> Contract -> Load/Stress -> Chaos -> Confidence
```

Cause-effect idea:
- Only unit tests -> integration bugs escape.
- No load tests -> surprise bottlenecks in production.

## Simple Example
Order service:
- Contract tests ensure payment API compatibility.
- Load tests validate 10k RPS target.
- Chaos test drops one dependency to verify fallback.

Analogy: Testing layers are like building inspections from material quality to earthquake simulation.

## Why and What-If Questions
- Why contract tests between teams?
  - Catch breaking API/schema changes early.
- What if production data is sensitive?
  - Anonymize/mask before replay in lower environments.
- What if chaos tests fail often?
  - Start with controlled blast radius and improve hardening iteratively.

## Practical Applications
- Release gating in CI/CD.
- Capacity readiness before major launches.
- Reliability drills for critical services.

## Compare With Related Ideas
- Load vs stress testing: expected peak validation vs beyond-limit behavior.
- Integration vs end-to-end tests: component interactions vs full user journey.

## Retention Tips
- Maintain a test matrix by risk area (correctness, scale, failure).
- Turn incident postmortems into new automated tests.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
