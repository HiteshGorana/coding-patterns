# 8) Consistency, Concurrency, Coordination

## Basics
This area covers correctness when many distributed actors read/write shared state.

Core components:
- Distributed locks (when to avoid them)
- Leader election
- Consensus basics (Raft/Paxos high-level)
- Idempotency keys
- Race conditions, optimistic/pessimistic locking
- Conflict resolution strategies (last-write-wins, vector clocks concept)

## How It Works
- Use coordination only where necessary.
- Prefer designs that avoid global locks.
- Apply conflict resolution and idempotency to handle retries and concurrent updates.

```text
Concurrent Writers -> Conflict Risk -> Locking/Versioning -> Resolved State
```

Cause-effect idea:
- Coarse distributed locks -> low throughput and deadlock risk.
- No concurrency control -> lost updates and inconsistent state.

## Simple Example
Seat booking:
- Optimistic lock with version field.
- If two users reserve same seat, one update fails and retries with fresh state.

Analogy: Two people editing the same document; version checks prevent overwriting each other's changes.

## Why and What-If Questions
- Why avoid distributed locks when possible?
  - They add latency, complexity, and failure modes.
- What if leader fails?
  - Election picks a new leader; clients may see temporary unavailability.
- What if duplicate requests arrive?
  - Idempotency keys prevent duplicate side effects.

## Practical Applications
- Inventory reservation correctness.
- Primary election for metadata services.
- Conflict handling in multi-region writes.

## Compare With Related Ideas
- Optimistic vs pessimistic locking: retry-on-conflict vs lock-before-write.
- Last-write-wins vs vector clocks: simple timestamp resolution vs causality-aware merging.

## Retention Tips
- Ask first: `Can I redesign to avoid coordination?`
- Practice by modeling one race condition and its fix each week.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
