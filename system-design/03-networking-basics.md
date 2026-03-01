# 3) Networking Basics

## Basics
Networking basics explain how clients and services communicate reliably and securely.

Core components:
- HTTP/HTTPS, REST, gRPC, WebSockets
- TCP vs UDP, TLS basics
- DNS, CDN, caching headers
- Load balancing (L4 vs L7)
- NAT, VPC basics, subnets, security groups
- Rate limiting and throttling strategies

## How It Works
1. DNS resolves domain to IP.
2. Client opens transport connection (usually TCP).
3. TLS secures the channel for HTTPS.
4. Requests route through load balancers and gateways.
5. Caching layers and rate limiters protect origins.

```text
Client -> DNS -> CDN/LB -> App -> DB
         |          |
       cache      throttle
```

Cause-effect idea:
- Missing caching headers -> repeated origin hits -> higher latency and cost.
- No rate limit -> abuse spikes -> noisy-neighbor failures.

## Simple Example
Mobile app API calls:
- HTTPS for security.
- L7 load balancer routes by path.
- CDN caches static images.
- Rate limits per API key.

Analogy: DNS is the phonebook, load balancer is traffic police, TLS is a locked envelope.

## Why and What-If Questions
- Why gRPC over REST?
  - Better for low-latency internal RPC and strong schema contracts.
- What if you need real-time updates?
  - Use WebSockets or streaming protocols.
- What if UDP drops packets?
  - App must handle loss; use TCP if reliable ordered delivery is required.

## Practical Applications
- API traffic shaping.
- Multi-tier network isolation in cloud.
- Global content delivery with CDN edge caches.

## Compare With Related Ideas
- L4 vs L7 LB: L4 routes by IP/port; L7 routes by HTTP metadata.
- Rate limiting vs throttling: limiting enforces hard caps; throttling slows throughput.

## Retention Tips
- Keep a request lifecycle sketch in memory: `resolve -> connect -> secure -> route -> respond`.
- Practice by tracing one real request using logs and headers.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
