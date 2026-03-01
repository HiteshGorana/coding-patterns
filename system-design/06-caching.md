# 6) Caching

## Basics
Caching stores frequently used data in faster layers to reduce latency and load.

Core components:
- Client-side vs server-side vs CDN caching
- Cache-aside, write-through, write-back
- TTLs, invalidation strategies
- Hot keys, cache stampede, cache penetration
- Consistent hashing
- Distributed cache (Redis/Memcached patterns)

## How It Works
1. Request arrives.
2. Check nearest cache layer.
3. On miss, fetch from source and populate cache.
4. Invalidate or expire entries based on policy.

```text
Client -> CDN -> App Cache -> DB
          hit?      hit?
```

Cause-effect idea:
- Long TTL on dynamic data -> stale reads.
- No stampede protection -> many misses trigger DB meltdown.

## Simple Example
Product page:
- CDN caches images.
- Redis caches product details for 60 seconds.
- Use request coalescing to prevent concurrent miss storms.

Analogy: Cache is like keeping frequently used tools on your desk instead of always walking to the storage room.

## Why and What-If Questions
- Why not cache everything?
  - Memory is finite and stale risk increases.
- What if one key becomes extremely hot?
  - Replicate key, shard reads, or use local near-cache.
- What if invalidation is hard?
  - Prefer short TTL + event-driven invalidation for critical entities.

## Practical Applications
- Read-heavy API acceleration.
- Cost reduction by lowering database query volume.
- Global low-latency asset delivery with CDN.

## Compare With Related Ideas
- Cache-aside vs write-through: app-managed lazy loading vs immediate cache updates on writes.
- Redis vs Memcached: richer data structures/persistence vs simpler volatile cache.

## Retention Tips
- Remember the hard rule: `There are only two hard things: cache invalidation and naming`.
- Track cache hit ratio and p95 latency together, not in isolation.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
