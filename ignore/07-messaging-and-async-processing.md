# 7) Messaging & Async Processing

## Basics
Messaging decouples producers and consumers so work can happen asynchronously and resiliently.

Core components:
- Message queues vs streams (e.g., RabbitMQ/SQS vs Kafka)
- Pub/Sub patterns
- Ordering guarantees, partitions
- Delivery semantics: at-most-once / at-least-once / exactly-once (practically)
- Dead-letter queues (DLQ)
- Backpressure and consumer groups
- Task scheduling, cron, delayed jobs

## How It Works
- Producer publishes event/message.
- Broker stores and routes it.
- Consumer group processes messages.
- Failed messages move to DLQ or retry path.

```text
Producer -> Broker -> Consumer Group -> DB/API
               |
              DLQ
```

Cause-effect idea:
- Slow consumers without backpressure -> queue growth -> delayed processing.
- Ignoring DLQ -> silent data loss.

## Simple Example
Order pipeline:
- `order_created` event published.
- Inventory, payment, and notification consumers process independently.
- Failed notification goes to DLQ for reprocessing.

Analogy: Broker is a post office. Producers drop letters; consumers pick up at their own pace.

## Why and What-If Questions
- Why use streams instead of queues?
  - Streams keep ordered logs and support replay.
- What if exactly-once is required?
  - In practice, combine at-least-once delivery with idempotent consumers.
- What if partitioning breaks ordering?
  - Ordering is usually guaranteed only within a partition/key.

## Practical Applications
- Event-driven microservices.
- Background job processing.
- Time-delayed workflows (email reminders, retries).

## Compare With Related Ideas
- Queue vs stream: work distribution vs durable event history.
- Cron vs event scheduling: fixed clock-based triggers vs state-driven execution.

## Retention Tips
- Think in terms of `produce, persist, process, retry`.
- Always define idempotency and DLQ handling before launch.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
