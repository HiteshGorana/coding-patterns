# 11) Observability

## Basics
Observability is the ability to understand system behavior from external signals.

Core components:
- Logging (structured logs, correlation IDs)
- Metrics (SLIs/SLOs/SLAs)
- Tracing (distributed tracing)
- Alerting (symptoms vs causes)
- Dashboards and runbooks

## How It Works
- Logs explain events.
- Metrics show trends and health.
- Traces reveal request paths and bottlenecks.
- Alerts detect abnormal behavior tied to SLO impact.

```text
Request -> Logs + Metrics + Traces -> Alert -> Runbook -> Resolution
```

Cause-effect idea:
- Missing correlation IDs -> hard root-cause analysis across services.
- Alerting on causes only -> noisy and low actionability.

## Simple Example
User checkout latency spike:
- Metric shows p95 increased.
- Trace identifies slow payment dependency.
- Logs reveal timeout exceptions.
- Runbook guides rollback and dependency failover.

Analogy: Observability is like car diagnostics: dashboard lights (metrics), event history (logs), and component-level scan (traces).

## Why and What-If Questions
- Why prioritize SLI/SLO-based alerts?
  - They align alerts with user impact.
- What if dashboards look good but users report issues?
  - Missing telemetry or wrong aggregation dimensions.
- What if log volume explodes?
  - Sample logs and improve structured fields.

## Practical Applications
- Faster incident triage.
- Error budget management.
- Capacity planning from trend metrics.

## Compare With Related Ideas
- Monitoring vs observability: monitoring checks known issues; observability helps diagnose unknown issues.
- Symptoms vs causes alerts: user-impact alerts are usually better paging signals.

## Retention Tips
- For each service, define top 4 golden signals: latency, traffic, errors, saturation.
- Keep runbooks short and linked directly from alerts.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
