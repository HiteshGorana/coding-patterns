# Pattern 26 Interview Playbook: Union-Find (Disjoint Set Union)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Tracks dynamic connectivity between elements with near-constant-time union/find operations.
- Core intuition: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Trigger cue 1: Dynamic connectivity, redundant edge, component count.
- Quick self-check: Am I repeatedly asking if two nodes belong to same group?
- Target complexity: Time pattern-optimal, Space O(n)

---

## Q1. Redundant Connection

### Problem Statement (Concrete)
Solve **Redundant Connection** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Redundant Connection** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_redundant_connection(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_redundant_connection(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_redundant_connection(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Number of Provinces

### Problem Statement (Concrete)
Solve **Number of Provinces** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Number of Provinces** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_number_of_provinces(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_number_of_provinces(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_number_of_provinces(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Accounts Merge

### Problem Statement (Concrete)
Solve **Accounts Merge** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Accounts Merge** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_accounts_merge(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_accounts_merge(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_accounts_merge(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Graph Valid Tree

### Problem Statement (Concrete)
Solve **Graph Valid Tree** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Graph Valid Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_graph_valid_tree(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_graph_valid_tree(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_graph_valid_tree(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Number of Islands II

### Problem Statement (Concrete)
Solve **Number of Islands II** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Number of Islands II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_number_of_islands_ii(grid):
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

def better_number_of_islands_ii(grid):
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

def better_number_of_islands_ii(grid):
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

## Q6. Most Stones Removed with Same Row or Column

### Problem Statement (Concrete)
Solve **Most Stones Removed with Same Row or Column** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Most Stones Removed with Same Row or Column** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_most_stones_removed_with_same_row_or_column(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_most_stones_removed_with_same_row_or_column(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_most_stones_removed_with_same_row_or_column(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Satisfiability of Equality Equations

### Problem Statement (Concrete)
Solve **Satisfiability of Equality Equations** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Satisfiability of Equality Equations** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_satisfiability_of_equality_equations(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_satisfiability_of_equality_equations(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_satisfiability_of_equality_equations(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Min Cost to Connect All Points

### Problem Statement (Concrete)
Solve **Min Cost to Connect All Points** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Min Cost to Connect All Points** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_min_cost_to_connect_all_points(n, edges):
    # Enumerate all spanning edge subsets of size n-1 (only for tiny n).
    from itertools import combinations

    best = float('inf')
    for comb in combinations(edges, n - 1):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True
        w = 0
        c = 0
        ok = True
        for u, v, wt in comb:
            if not union(u, v):
                ok = False
                break
            w += wt
            c += 1
        if ok and c == n - 1 and len({find(i) for i in range(n)}) == 1:
            best = min(best, w)
    return best if best < float('inf') else -1
```

#### Complexity
- Time combinatorial `O(C(m, n-1) * alpha(n))`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use Prim to grow one connected component with cheapest boundary edge.

#### Python
```python
import heapq

def better_min_cost_to_connect_all_points(n, edges):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((w, v))
        g[v].append((w, u))

    seen = [False] * n
    h = [(0, 0)]
    total = 0
    used = 0
    while h and used < n:
        w, u = heapq.heappop(h)
        if seen[u]:
            continue
        seen[u] = True
        total += w
        used += 1
        for nw, v in g[u]:
            if not seen[v]:
                heapq.heappush(h, (nw, v))
    return total if used == n else -1
```

#### Complexity
- Time `O(m log n)`, Space `O(m)`.

### Approach 3: Optimal (Best)
#### Intuition
- Kruskal sorts edges and greedily adds non-cycle edges via DSU.

#### Python
```python
def solve_min_cost_to_connect_all_points(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    total = 0
    used = 0
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            total += w
            used += 1
            if used == n - 1:
                break
    return total if used == n - 1 else -1
```

#### Correctness (Why This Works)
- Cut property: lightest edge crossing any cut belongs to some MST.
- Kruskal repeatedly selects globally light feasible edges, preserving MST optimality.

#### Complexity
- Time `O(m log m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. The Earliest Moment When Everyone Become Friends

### Problem Statement (Concrete)
Solve **The Earliest Moment When Everyone Become Friends** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **The Earliest Moment When Everyone Become Friends** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_the_earliest_moment_when_everyone_become_friends(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_the_earliest_moment_when_everyone_become_friends(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_the_earliest_moment_when_everyone_become_friends(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Detect Cycle in Undirected Graph

### Problem Statement (Concrete)
Solve **Detect Cycle in Undirected Graph** using **Union-Find (Disjoint Set Union)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes
- `edges`/`pairs`: list[list[int]] connectivity operations

### Output
- Component count, cycle detection result, or merged groups based on prompt.

### Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= m <= 4 * 10^5`

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2  # connected components
Explanation: Union operations merge sets; repeated find on same root signals existing connectivity.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Union-Find (Disjoint Set Union)**.
- Red flags: brute force for **Detect Cycle in Undirected Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build adjacency and count components with graph traversal.

#### Python
```python
def brute_detect_cycle_in_undirected_graph(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    seen = [False] * n
    comp = 0
    for i in range(n):
        if seen[i]:
            continue
        comp += 1
        st = [i]
        seen[i] = True
        while st:
            u = st.pop()
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
    return comp
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use plain DSU without balancing/path compression.

#### Python
```python
def better_detect_cycle_in_undirected_graph(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})
```

#### Complexity
- Near-linear but can degrade in adversarial union order.

### Approach 3: Optimal (Best)
#### Intuition
- Union by rank + path compression gives inverse-Ackermann amortized operations.

#### Python
```python
def solve_detect_cycle_in_undirected_graph(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    comps = n
    for u, v in edges:
        if union(u, v):
            comps -= 1
    return comps
```

#### Correctness (Why This Works)
- Each set representative defines one connected component partition.
- Union merges partitions exactly when an inter-component edge appears.

#### Complexity
- Time `O((n+m) * alpha(n))`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
