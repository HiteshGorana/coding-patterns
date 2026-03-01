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

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
