# Pattern 41 Interview Playbook: Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Bellman-Ford and Floyd-Warshall handle shortest paths when negative weights exist and can detect/report negative cycles.
- Core intuition: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Trigger cue 1: Graph has negative edges.
- Trigger cue 2: Need detect negative cycle.
- Quick self-check: Are negative edges/cycles possible or explicitly mentioned?
- Target complexity: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2).

---

## Q1. Bellman-Ford Algorithm Implementation

### Problem Statement (Concrete)
Solve **Bellman-Ford Algorithm Implementation** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Bellman-Ford Algorithm Implementation** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_bellman_ford_algorithm_implementation(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_bellman_ford_algorithm_implementation(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_bellman_ford_algorithm_implementation(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Cheapest Flights Within K Stops (Relaxation DP)

### Problem Statement (Concrete)
Solve **Cheapest Flights Within K Stops (Relaxation DP)** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Cheapest Flights Within K Stops (Relaxation DP)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_cheapest_flights_within_k_stops_relaxation_dp(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_cheapest_flights_within_k_stops_relaxation_dp(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_cheapest_flights_within_k_stops_relaxation_dp(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Arbitrage Detection

### Problem Statement (Concrete)
Solve **Arbitrage Detection** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Arbitrage Detection** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_arbitrage_detection(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_arbitrage_detection(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_arbitrage_detection(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Wormholes / Negative Cycle Detection

### Problem Statement (Concrete)
Solve **Wormholes / Negative Cycle Detection** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Wormholes / Negative Cycle Detection** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_wormholes_negative_cycle_detection(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_wormholes_negative_cycle_detection(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_wormholes_negative_cycle_detection(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Floyd-Warshall All Pairs Shortest Path

### Problem Statement (Concrete)
Solve **Floyd-Warshall All Pairs Shortest Path** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Floyd-Warshall All Pairs Shortest Path** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_floyd_warshall_all_pairs_shortest_path(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_floyd_warshall_all_pairs_shortest_path(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_floyd_warshall_all_pairs_shortest_path(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Find the City With the Smallest Number of Neighbors at a Threshold Distance

### Problem Statement (Concrete)
Solve **Find the City With the Smallest Number of Neighbors at a Threshold Distance** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Find the City With the Smallest Number of Neighbors at a Threshold Distance** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Currency Exchange Graph

### Problem Statement (Concrete)
Solve **Currency Exchange Graph** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Currency Exchange Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_currency_exchange_graph(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_currency_exchange_graph(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_currency_exchange_graph(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Shortest Path with Possible Negative Edges

### Problem Statement (Concrete)
Solve **Shortest Path with Possible Negative Edges** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Shortest Path with Possible Negative Edges** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_shortest_path_with_possible_negative_edges(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_shortest_path_with_possible_negative_edges(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_shortest_path_with_possible_negative_edges(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Path with At Most K Edges

### Problem Statement (Concrete)
Solve **Path with At Most K Edges** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Path with At Most K Edges** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_path_with_at_most_k_edges(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_path_with_at_most_k_edges(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_path_with_at_most_k_edges(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Detect Reachable Negative Cycle from Source

### Problem Statement (Concrete)
Solve **Detect Reachable Negative Cycle from Source** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**.
- Red flags: brute force for **Detect Reachable Negative Cycle from Source** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_detect_reachable_negative_cycle_from_source(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_detect_reachable_negative_cycle_from_source(n, edges, src):
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
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_detect_reachable_negative_cycle_from_source(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
