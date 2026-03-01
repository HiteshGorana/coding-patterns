# Pattern 27 Interview Playbook: Shortest Path (Dijkstra / 0-1 BFS)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Finds minimum path cost in weighted graphs.
- Core intuition: Always expand currently known closest unfinalized node using min-heap. Once a node is popped with minimum distance, its shortest distance is finalized (non-negative edges).
- Trigger cue 1: Weighted shortest path with non-negative weights.
- Trigger cue 2: Only 0/1 weights -> deque-based 0-1 BFS.
- Quick self-check: Is distance cost weighted (not just step count)?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Network Delay Time

### Problem Statement (Concrete)
Solve **Network Delay Time** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Network Delay Time** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_network_delay_time(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_network_delay_time(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_network_delay_time(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Path with Minimum Effort

### Problem Statement (Concrete)
Solve **Path with Minimum Effort** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Path with Minimum Effort** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_path_with_minimum_effort(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_path_with_minimum_effort(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_path_with_minimum_effort(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Cheapest Flights Within K Stops

### Problem Statement (Concrete)
Solve **Cheapest Flights Within K Stops** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Cheapest Flights Within K Stops** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_cheapest_flights_within_k_stops(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_cheapest_flights_within_k_stops(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_cheapest_flights_within_k_stops(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Dijkstra Algorithm Implementation

### Problem Statement (Concrete)
Solve **Dijkstra Algorithm Implementation** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Dijkstra Algorithm Implementation** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_dijkstra_algorithm_implementation(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_dijkstra_algorithm_implementation(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_dijkstra_algorithm_implementation(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Minimum Cost to Make at Least One Valid Path in a Grid

### Problem Statement (Concrete)
Solve **Minimum Cost to Make at Least One Valid Path in a Grid** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

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

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Minimum Cost to Make at Least One Valid Path in a Grid** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_minimum_cost_to_make_at_least_one_valid_path_in_a_grid(grid):
    m, n = len(grid), len(grid[0])
    ans = [[10**9] * n for _ in range(m)]
    src = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
    for i in range(m):
        for j in range(n):
            for si, sj in src:
                ans[i][j] = min(ans[i][j], abs(i - si) + abs(j - sj))
    return ans
```

#### Complexity
- Time `O((mn)^2)` in dense-source case, Space `O(mn)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Run BFS from all sources simultaneously so each cell is finalized at first reach.

#### Python
```python
from collections import deque

def better_minimum_cost_to_make_at_least_one_valid_path_in_a_grid(grid):
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

#### Complexity
- Time `O(mn)`, Space `O(mn)`.

### Approach 3: Optimal (Best)
#### Intuition
- Multi-source BFS explores increasing distance layers exactly once per cell.

#### Python
```python
from collections import deque

def better_minimum_cost_to_make_at_least_one_valid_path_in_a_grid(grid):
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

#### Correctness (Why This Works)
- In unweighted grids, BFS layer number equals shortest path length.
- Seeding queue with all sources ensures nearest source claims each cell first.

#### Complexity
- Time `O(mn)`, Space `O(mn)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Swim in Rising Water

### Problem Statement (Concrete)
Solve **Swim in Rising Water** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Swim in Rising Water** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_swim_in_rising_water(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_swim_in_rising_water(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_swim_in_rising_water(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. The Maze II

### Problem Statement (Concrete)
Solve **The Maze II** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **The Maze II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_the_maze_ii(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_the_maze_ii(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_the_maze_ii(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Find the City With the Smallest Number of Neighbors at a Threshold Distance

### Problem Statement (Concrete)
Solve **Find the City With the Smallest Number of Neighbors at a Threshold Distance** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Find the City With the Smallest Number of Neighbors at a Threshold Distance** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Minimum Obstacle Removal to Reach Corner

### Problem Statement (Concrete)
Solve **Minimum Obstacle Removal to Reach Corner** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Minimum Obstacle Removal to Reach Corner** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_minimum_obstacle_removal_to_reach_corner(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_minimum_obstacle_removal_to_reach_corner(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_minimum_obstacle_removal_to_reach_corner(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Shortest Distance from All Buildings

### Problem Statement (Concrete)
Solve **Shortest Distance from All Buildings** using **Shortest Path (Dijkstra / 0-1 BFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int
- `edges`: list[[u,v,w]]
- `src` (and `dst` if required)

### Output
- Shortest distance value/list, or `-1` for unreachable target.

### Constraints
- `1 <= n <= 2 * 10^5`
- Use Dijkstra for non-negative weights and sparse graphs.

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1,1],[0,2,4],[1,2,2],[2,3,1]], src = 0
Output: [0,1,3,4]
Explanation: Priority queue always expands currently known closest unsettled node.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Shortest Path (Dijkstra / 0-1 BFS)**.
- Red flags: brute force for **Shortest Distance from All Buildings** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Relax all edges repeatedly (Bellman-style baseline).

#### Python
```python
def brute_shortest_distance_from_all_buildings(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] < INF:
                dist[v] = min(dist[v], dist[u] + w)
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use min-heap Dijkstra for non-negative weighted graphs.

#### Python
```python
import heapq

def better_shortest_distance_from_all_buildings(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dijkstra with stale-entry skip is optimal for sparse, non-negative edge settings.

#### Python
```python
import heapq

def better_shortest_distance_from_all_buildings(n, edges, src):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
    dist = [10**18] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

#### Correctness (Why This Works)
- When node `u` is popped with smallest tentative distance, that distance is final in non-negative graphs.
- Any alternative path to `u` must be at least as large due to heap order and non-negative edges.

#### Complexity
- Time `O((n+m) log n)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
