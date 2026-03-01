# Pattern 27: Shortest Path (Dijkstra / 0-1 BFS)

## Diagram + Intuition

### Pattern Diagram
```text
min-heap of (dist,node)
pop closest unresolved node -> relax edges
```

### Read-the-Question Trigger Cues
- Weighted shortest path with non-negative weights.
- Only 0/1 weights -> deque-based 0-1 BFS.

### Intuition Anchor
- "Expand cheapest frontier first."

### 3-Second Pattern Check
- Is distance cost weighted (not just step count)?

## What This Pattern Solves
Finds minimum path cost in weighted graphs.

## Recognition Signals
- Graph edges have non-negative weights -> Dijkstra.
- Edge weights only 0 or 1 -> 0-1 BFS is faster/simpler.
- Need shortest distance from source to all nodes or one destination.

## Core Intuition (Dijkstra)
Always expand currently known closest unfinalized node using min-heap.  
Once a node is popped with minimum distance, its shortest distance is finalized (non-negative edges).

## Dijkstra Steps
1. Build adjacency list `(neighbor, weight)`.
2. Initialize distances to infinity except source `0`.
3. Push `(0, source)` to min-heap.
4. Pop node; skip stale entries where popped distance > `dist[node]`.
5. Relax outgoing edges and push improved distances.

## 0-1 BFS Intuition
Use deque:
- weight 0 edge -> push front
- weight 1 edge -> push back
This mimics Dijkstra with `O(V + E)` complexity for 0/1 weights.

## Complexity
- Dijkstra with heap: `O((V + E) log V)`
- 0-1 BFS: `O(V + E)`

## Python Template (Dijkstra)
```python
import heapq

def dijkstra(n, graph, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist
```

## Common Pitfalls
- Using Dijkstra with negative weights (invalid).
- Not skipping stale heap entries, causing extra work.
- Overflow risks in languages with fixed integer types.
- Confusing BFS shortest path (unweighted) with weighted shortest path.

## Variations
- Network Delay Time
- Cheapest Flights Within K Stops (modified state-space shortest path)
- Path with Minimum Effort (Dijkstra on grid)
- Minimum Cost to Make at Least One Valid Path in a Grid (0-1 BFS)

## Interview Tips
- Explicitly state edge-weight assumptions.
- Mention Bellman-Ford if negative weights exist.
- If constraints are 0/1 weights, propose 0-1 BFS for linear complexity.

## Practice Problems
- Network Delay Time
- Path with Minimum Effort
- Minimum Cost to Make at Least One Valid Path in a Grid
- Dijkstra implementation exercises
