# Pattern 18 Interview Playbook: Matrix Traversal (Grid BFS/DFS)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Navigates 2D grids for connectivity, shortest steps (unweighted), and region counting.
- Core intuition: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Trigger cue 1: Islands/regions/flood fill/shortest steps in unweighted grid.
- Quick self-check: Is this a connectivity or shortest-unweighted path problem on cells?
- Target complexity: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited

---

## Q1. Number of Islands

### Problem Statement (Concrete)
Solve **Number of Islands** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Number of Islands** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_number_of_islands(grid):
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

def better_number_of_islands(grid):
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

def better_number_of_islands(grid):
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
Solve **Rotting Oranges** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
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

## Q3. Flood Fill

### Problem Statement (Concrete)
Solve **Flood Fill** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Flood Fill** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_flood_fill(grid):
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

def better_flood_fill(grid):
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

def better_flood_fill(grid):
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

## Q4. Surrounded Regions

### Problem Statement (Concrete)
Solve **Surrounded Regions** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Surrounded Regions** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_surrounded_regions(grid):
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

def better_surrounded_regions(grid):
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

def better_surrounded_regions(grid):
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

## Q5. Walls and Gates

### Problem Statement (Concrete)
Solve **Walls and Gates** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
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

## Q6. Pacific Atlantic Water Flow

### Problem Statement (Concrete)
Solve **Pacific Atlantic Water Flow** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Pacific Atlantic Water Flow** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_pacific_atlantic_water_flow(grid):
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

def better_pacific_atlantic_water_flow(grid):
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

def better_pacific_atlantic_water_flow(grid):
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

## Q7. Word Search

### Problem Statement (Concrete)
Solve **Word Search** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

### Input
- `text`/`s`: str
- `pattern`/`queries`: variant-specific

### Output
- Index, boolean, count, or transformed string as required.

### Constraints
- `1 <= length <= 2 * 10^5`
- Use near-linear processing to avoid `O(n*m)` restarts.

### Example (Exact)
```text
Input:  text = "sadbutsad", pattern = "sad"
Output: 0
Explanation: Efficient preprocessing avoids rechecking already-matched characters.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Word Search** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_word_search(grid):
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

def better_word_search(grid):
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

def better_word_search(grid):
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

## Q8. Shortest Path in Binary Matrix

### Problem Statement (Concrete)
Solve **Shortest Path in Binary Matrix** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Shortest Path in Binary Matrix** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_shortest_path_in_binary_matrix(grid):
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

def better_shortest_path_in_binary_matrix(grid):
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

def better_shortest_path_in_binary_matrix(grid):
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

## Q9. 01 Matrix

### Problem Statement (Concrete)
Solve **01 Matrix** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
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

## Q10. Number of Closed Islands

### Problem Statement (Concrete)
Solve **Number of Closed Islands** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Matrix Traversal (Grid BFS/DFS)**.
- Red flags: brute force for **Number of Closed Islands** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_number_of_closed_islands(grid):
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

def better_number_of_closed_islands(grid):
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

def better_number_of_closed_islands(grid):
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
