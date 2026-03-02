# 17) Common System Components (Must-Know)

## Basics
These are reusable building blocks that appear in most modern architectures.

Core components:
- Load balancer
- Reverse proxy
- API gateway
- Service discovery
- Config service / feature flags
- Distributed cache
- Message broker
- Scheduler / workers
- Database + replicas
- Search engine
- CDN

## How It Works
Components combine to route traffic, enforce policies, process asynchronous work, and store/query data.

```text
Client -> CDN -> LB/Proxy -> API Gateway -> Services
                                     |      |   |
                                   Config  Cache Broker
                                            |
                                         DB/Search
```

Cause-effect idea:
- Missing service discovery -> brittle hardcoded endpoints.
- No feature flags -> risky all-at-once releases.

## Simple Example
Typical web app stack:
- CDN for static assets.
- LB and reverse proxy for ingress.
- Gateway for auth/rate limits.
- Services + cache + broker + DB replicas.

Analogy: These components are the organs of a system body; each has a specialized function but must coordinate.

## Why and What-If Questions
- Why both reverse proxy and API gateway?
  - Proxy handles ingress/routing basics; gateway handles API policies.
- What if scheduler queue backs up?
  - Scale workers and prioritize critical jobs.
- What if config service is unavailable?
  - Cache last known config and fail safely.

## Practical Applications
- Standard platform architecture templates.
- Faster onboarding for new teams.
- Consistent reliability and security controls.

## Compare With Related Ideas
- Load balancer vs reverse proxy: traffic distribution vs request handling and policy layers.
- Cache vs search engine: low-latency key/data retrieval vs relevance-based text retrieval.

## Retention Tips
- Draw this component map from memory once a week.
- For each component, memorize one failure mode and one mitigation.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
