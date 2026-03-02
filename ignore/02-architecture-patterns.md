# 2) Architecture Patterns

## Basics
Architecture patterns are reusable ways to organize services, modules, and dependencies.

Core components:
- Monolith vs microservices vs modular monolith
- Layered architecture, clean architecture, hexagonal
- Event-driven architecture
- CQRS (Command Query Responsibility Segregation)
- Sagas (distributed transactions)
- Service mesh basics
- SOA vs microservices (differences and when)

## How It Works
Pick an architecture by matching team size, domain complexity, and operational maturity.

```text
Business Domain + Team Constraints
            |
            v
   Architectural Pattern Choice
            |
            v
 Deployment, Data Boundaries, Operations
```

Cause-effect idea:
- Too many microservices too early -> operational overhead grows faster than feature velocity.
- Tight monolith coupling -> simple deploys today, slower scaling of teams tomorrow.

## Simple Example
E-commerce startup:
- Start with a modular monolith (catalog, cart, payment modules).
- Split only hot or independent modules into services later.
- Use events for order lifecycle updates.

Analogy: A monolith is one large building; microservices are many small buildings with roads and traffic rules between them.

## Why and What-If Questions
- Why use CQRS?
  - Separate read and write scaling when query patterns diverge.
- What if a saga step fails?
  - Trigger compensating actions for already-completed steps.
- What if service-to-service networking is complex?
  - Service mesh can standardize retries, mTLS, and observability.

## Practical Applications
- Scaling teams by domain ownership.
- Decoupling payment, inventory, and shipping lifecycles.
- Reducing cross-team deploy contention.

## Compare With Related Ideas
- SOA vs microservices: both are service-oriented; microservices push stronger autonomy, smaller scope, and independent deployability.
- Layered vs hexagonal: layered organizes by technical tiers; hexagonal organizes around domain and ports/adapters.

## Retention Tips
- Memorize `Pattern -> Best for -> Biggest cost`.
- Draw module boundaries before technology choices.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
