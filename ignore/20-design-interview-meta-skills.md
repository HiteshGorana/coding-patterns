# 20) Design Interview "Meta" Skills

## Basics
Meta skills are the communication and structuring habits that turn technical knowledge into a strong interview performance.

Core components:
- Clarify requirements quickly
- Draw the high-level architecture first
- Identify bottlenecks early
- Discuss tradeoffs explicitly
- Define data model + APIs
- Consider failure modes + monitoring
- Provide an incremental rollout plan

## How It Works
- Start by framing the problem and constraints.
- Present a clear baseline architecture.
- Dive into critical components and bottlenecks.
- Close with reliability, observability, and rollout strategy.

```text
Clarify -> High-level -> Deep dive -> Tradeoffs -> Failure/Monitoring -> Rollout
```

Cause-effect idea:
- Jumping into details too early -> misaligned solution.
- Avoiding tradeoffs -> shallow design signal.

## Simple Example
Design ride-sharing dispatch system:
- Clarify latency and geography constraints.
- Draw ingest, matching, and location update services.
- Identify hotspot: geo-query and surge events.
- Propose phased rollout by city.

Analogy: Interview design is like telling a map-guided story; interviewer should always know where you are and why.

## Why and What-If Questions
- Why start high-level first?
  - Establish shared mental model before optimization details.
- What if requirements are ambiguous?
  - State assumptions explicitly and continue.
- What if interviewer challenges your tradeoff?
  - Re-evaluate with their constraints and adapt.

## Practical Applications
- Better technical communication in architecture reviews.
- Faster design alignment across teams.
- Stronger decision documentation in real projects.

## Compare With Related Ideas
- Interview design vs production design: same principles, less implementation detail.
- Correct answer vs reasoned answer: interviews favor clear tradeoff reasoning.

## Retention Tips
- Practice a repeatable 30-40 minute structure.
- Keep a personal checklist: requirements, API/data model, scale, failures, rollout.

## Interviewer Ask Checklist (Must Remember)
- Clarify scope: users, features, constraints, and out-of-scope items.
- Quantify load: QPS/RPS, read-write ratio, storage growth, peak traffic.
- Set targets: latency, availability, consistency, durability, and budget.
- Draw high-level architecture before component-level deep dive.
- Define API contracts and core data model early.
- Explain scaling plan: caching, sharding/partitioning, replicas, async processing.
- Call out tradeoffs explicitly with reasoned choices.
- Handle failures: retries, timeouts, idempotency, circuit breakers, fallbacks.
- Cover observability: metrics, logs, traces, alerting, SLO/SLI.
- Mention security basics: authentication, authorization, encryption, rate limiting.
- Close with phased rollout: MVP first, then 10x growth improvements.

## Tips and Tricks to Impress the Interviewer
- Lead with structure: say your plan upfront (requirements -> design -> tradeoffs -> scaling -> failures).
- Think aloud clearly; narrate why each decision is being made.
- Use rough back-of-the-envelope math to justify architecture choices.
- Name realistic defaults first, then mention alternatives if constraints change.
- Proactively discuss one likely bottleneck and how you would detect/fix it.
- Speak in tradeoffs, not absolutes ("this improves latency but increases cost").
- Keep diagrams simple and layered so the interviewer can follow quickly.
- Summarize every 5-7 minutes to show control of the conversation.
- Ask for feedback checkpoints ("Should I go deeper on storage or caching next?").
- End with a crisp recap: final design, key risks, and next scaling step.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
