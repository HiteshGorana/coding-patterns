# 18) Deployment & Operations

## Basics
Deployment and operations practices move code safely from commit to production.

Core components:
- CI/CD basics
- Blue/green, canary deployments
- Rollbacks and feature flags
- Containerization (Docker basics)
- Orchestration (Kubernetes concepts)
- Infrastructure as Code (Terraform concept)
- Configuration management

## How It Works
- CI validates code quality and tests.
- CD deploys incrementally with safety checks.
- Runtime platform orchestrates workloads and scaling.
- IaC/versioned config keeps environments reproducible.

```text
Commit -> CI -> Artifact -> Deploy Strategy -> Monitor -> Rollback/Promote
```

Cause-effect idea:
- Manual environment drift -> hard-to-debug production differences.
- No rollback path -> prolonged incidents.

## Simple Example
Canary rollout:
- Deploy v2 to 5% traffic.
- Compare error rate and latency against v1.
- Increase gradually to 100% if healthy.

Analogy: Canary deployment is sampling a new recipe with a small group before serving everyone.

## Why and What-If Questions
- Why feature flags with canaries?
  - Separate code deployment from feature release.
- What if canary metrics degrade?
  - Auto-rollback and open incident.
- What if Terraform state is corrupted?
  - Remote state backups and lock protection are critical.

## Practical Applications
- Safe frequent releases.
- Multi-environment consistency.
- Reduced MTTR via fast rollback.

## Compare With Related Ideas
- Blue/green vs canary: instant environment switch vs gradual risk exposure.
- Containerization vs orchestration: package app dependencies vs manage fleet lifecycle.

## Retention Tips
- Track DORA-style metrics: deploy frequency, change failure rate, MTTR.
- Keep rollback runbook tested, not just documented.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
