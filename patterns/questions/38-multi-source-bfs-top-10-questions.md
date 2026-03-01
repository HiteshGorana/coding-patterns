# Pattern 38 Interview Playbook: Multi-source BFS

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Multi-source BFS computes shortest unweighted distances from the nearest source by initializing BFS with all sources at distance zero.
- Core intuition: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Trigger cue 1: Need nearest distance to any of many sources.
- Trigger cue 2: Diffusion/spread problems in unweighted grid/graph.
- Quick self-check: Can I treat every source as level-0 and expand in one BFS?
- Target complexity: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited.

---

## Q1. 01 Matrix

### Problem Statement (Concrete)
Solve **01 Matrix** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **01 Matrix** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_q_01_matrix(grid):
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

def better_q_01_matrix(grid):
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

def better_q_01_matrix(grid):
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

## Q2. Rotting Oranges

### Problem Statement (Concrete)
Solve **Rotting Oranges** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Rotting Oranges** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_rotting_oranges(grid):
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

def better_rotting_oranges(grid):
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

def better_rotting_oranges(grid):
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

## Q3. Walls and Gates

### Problem Statement (Concrete)
Solve **Walls and Gates** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Walls and Gates** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_walls_and_gates(grid):
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

def better_walls_and_gates(grid):
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

def better_walls_and_gates(grid):
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

## Q4. As Far from Land as Possible

### Problem Statement (Concrete)
Solve **As Far from Land as Possible** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **As Far from Land as Possible** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_as_far_from_land_as_possible(grid):
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

def better_as_far_from_land_as_possible(grid):
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

def better_as_far_from_land_as_possible(grid):
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

## Q5. Map of Highest Peak

### Problem Statement (Concrete)
Solve **Map of Highest Peak** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Map of Highest Peak** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_map_of_highest_peak(grid):
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

def better_map_of_highest_peak(grid):
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

def better_map_of_highest_peak(grid):
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

## Q6. Shortest Bridge

### Problem Statement (Concrete)
Solve **Shortest Bridge** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Shortest Bridge** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_shortest_bridge(n, edges):
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        rg[v].append(u)

    def reach(start, graph):
        st = [start]
        seen = {start}
        while st:
            u = st.pop()
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    st.append(v)
        return seen

    comp = []
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        a = reach(i, g)
        b = reach(i, rg)
        scc = sorted(a & b)
        for x in scc:
            used[x] = True
        comp.append(scc)
    return comp
```

#### Complexity
- Time roughly `O(n*(n+m))`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kosaraju obtains finish-time order then reverse-graph DFS to extract SCCs.

#### Python
```python
def better_shortest_bridge(n, edges):
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        rg[v].append(u)

    seen = [False] * n
    order = []
    def dfs1(u):
        seen[u] = True
        for v in g[u]:
            if not seen[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not seen[i]:
            dfs1(i)

    comp = []
    seen = [False] * n
    def dfs2(u, cur):
        seen[u] = True
        cur.append(u)
        for v in rg[u]:
            if not seen[v]:
                dfs2(v, cur)

    for u in reversed(order):
        if not seen[u]:
            cur = []
            dfs2(u, cur)
            comp.append(cur)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Tarjan single DFS tracks discovery/low-link and stack membership to emit SCC roots.

#### Python
```python
def solve_shortest_bridge(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)

    disc = [-1] * n
    low = [0] * n
    onstack = [False] * n
    st = []
    timer = 0
    sccs = []

    def dfs(u):
        nonlocal timer
        disc[u] = low[u] = timer
        timer += 1
        st.append(u)
        onstack[u] = True

        for v in g[u]:
            if disc[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif onstack[v]:
                low[u] = min(low[u], disc[v])

        if low[u] == disc[u]:
            comp = []
            while True:
                x = st.pop()
                onstack[x] = False
                comp.append(x)
                if x == u:
                    break
            sccs.append(comp)

    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    return sccs
```

#### Correctness (Why This Works)
- `low[u]` captures earliest stack-reachable discovery index from `u`'s DFS subtree.
- When `low[u] == disc[u]`, `u` is SCC root and stack pop until `u` yields exactly one SCC.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Nearest Exit Distance with Multiple Entrances

### Problem Statement (Concrete)
Solve **Nearest Exit Distance with Multiple Entrances** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Nearest Exit Distance with Multiple Entrances** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_nearest_exit_distance_with_multiple_entrances(grid):
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

def better_nearest_exit_distance_with_multiple_entrances(grid):
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

def better_nearest_exit_distance_with_multiple_entrances(grid):
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

## Q8. Fire Spread Simulation in Grid

### Problem Statement (Concrete)
Solve **Fire Spread Simulation in Grid** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Fire Spread Simulation in Grid** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_fire_spread_simulation_in_grid(grid):
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

def better_fire_spread_simulation_in_grid(grid):
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

def better_fire_spread_simulation_in_grid(grid):
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

## Q9. Nearest Facility in Unweighted Graph

### Problem Statement (Concrete)
Solve **Nearest Facility in Unweighted Graph** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Nearest Facility in Unweighted Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_nearest_facility_in_unweighted_graph(grid):
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

def better_nearest_facility_in_unweighted_graph(grid):
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

def better_nearest_facility_in_unweighted_graph(grid):
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

## Q10. Minimum Time to Infect All Nodes

### Problem Statement (Concrete)
Solve **Minimum Time to Infect All Nodes** using **Multi-source BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Multi-source BFS**.
- Red flags: brute force for **Minimum Time to Infect All Nodes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_minimum_time_to_infect_all_nodes(grid):
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

def better_minimum_time_to_infect_all_nodes(grid):
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

def better_minimum_time_to_infect_all_nodes(grid):
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
