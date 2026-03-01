# Pattern 41: Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)

## Diagram + Intuition

### Pattern Diagram
```text
Bellman-Ford: relax all edges V-1 times
extra pass improvement -> negative cycle
Floyd: k as intermediate for all-pairs
```

### Read-the-Question Trigger Cues
- Graph has negative edges.
- Need detect negative cycle.
- Need all-pairs shortest paths with moderate `n`.

### Intuition Anchor
- "Dijkstra breaks on negative weights, so switch to relaxation-based algorithms."

### 3-Second Pattern Check
- Are negative edges/cycles possible or explicitly mentioned?

## What This Pattern Solves
Bellman-Ford and Floyd-Warshall handle shortest paths when negative weights exist and can detect/report negative cycles.

## Recognition Signals
- Need shortest path with possible negative costs.
- Currency arbitrage/cycle-profit style prompts.
- All-pairs shortest path matrix requirement.

## Core Intuition
Repeated edge relaxation converges shortest distances if no negative cycle is reachable.

## Step-by-Step Method
1. Initialize distances (`0` at source, INF elsewhere).
2. Relax all edges `V-1` rounds.
3. Run one extra round to detect negative cycle improvements.
4. For all-pairs, use Floyd-Warshall triple loop with intermediates.

## Detailed Example
In arbitrage, transforming exchange rates to negative logs allows negative-cycle detection via Bellman-Ford.

## Complexity
- Time: Bellman-Ford `O(V*E)`, Floyd-Warshall `O(V^3)`.
- Space: Bellman-Ford `O(V)`, Floyd-Warshall `O(V^2)`.

## Python Template
```python
def bellman_ford(n, edges, src):  # edges: (u, v, w)
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    has_neg_cycle = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_neg_cycle = True
            break

    return dist, has_neg_cycle
```

## Common Pitfalls
- Using Dijkstra with negative edges.
- Ignoring unreachable nodes during relaxations.
- Not distinguishing reachable vs global negative cycles.

## Variations
- Bellman-Ford single-source
- Floyd-Warshall all-pairs
- Arbitrage detection
- K-stop constrained relaxations

## Interview Tips
- Mention when each algorithm is chosen (`V*E` vs `V^3`).
- Explain negative-cycle check with extra relaxation pass.

## Practice Problems
- Cheapest Flights Within K Stops
- Arbitrage Detection
- Bellman-Ford implementation
- Floyd-Warshall implementation
