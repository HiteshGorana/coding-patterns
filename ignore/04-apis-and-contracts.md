# 4) APIs & Contracts

## Basics
APIs and contracts define how systems talk without breaking each other.

Core components:
- API design (REST principles, versioning)
- Idempotency, retries, pagination
- Authentication vs authorization
- API gateways
- Backward compatibility
- Schema evolution (Protobuf/Avro/JSON)

## How It Works
- Design stable resources and operations.
- Version when breaking behavior is unavoidable.
- Add idempotency for safe retries.
- Enforce authn/authz at gateway and service layers.

```text
Client -> API Gateway -> Service
  |         |              |
 authn    policy         schema
```

Cause-effect idea:
- Weak contracts -> client breakage after deploy.
- No idempotency -> duplicate side effects during retries.

## Simple Example
Payment API:
- `POST /payments` with `Idempotency-Key`.
- If network times out, retry with same key returns same result.
- Pagination on transaction history with cursor tokens.

Analogy: API contract is like a legal contract. Both parties must agree on format and obligations.

## Why and What-If Questions
- Why prefer backward-compatible schema changes?
  - To avoid coordinated upgrades across many clients.
- What if clients are on old versions?
  - Keep deprecated fields for a transition period and monitor usage.
- What if authn passes but authz fails?
  - Identity is known but permissions are insufficient; return `403`.

## Practical Applications
- Public APIs for partners.
- Internal platform APIs shared across teams.
- Safe rollouts with multi-version clients.

## Compare With Related Ideas
- Authentication vs authorization: who you are vs what you can do.
- Offset vs cursor pagination: offset is simple, cursor is better for large mutable datasets.

## Retention Tips
- Use the checklist `SIRVA`: Schema, Idempotency, Retries, Versioning, Authorization.
- Document one good and one bad API change from past work.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
