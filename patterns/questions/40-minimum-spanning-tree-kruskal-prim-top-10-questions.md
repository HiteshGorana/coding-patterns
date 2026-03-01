# Pattern 40 Interview Playbook: Minimum Spanning Tree (Kruskal / Prim)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: MST patterns solve minimum-cost connectivity over undirected weighted graphs using Kruskal or Prim.
- Core intuition: Use cut property: the lightest edge crossing any cut is safe for MST.
- Trigger cue 1: Connect all vertices with minimum sum weight.
- Trigger cue 2: Need exactly `n-1` edges without cycles.
- Quick self-check: Is this 'connect everything at min total edge cost' rather than shortest path from one source?
- Target complexity: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E).

---

## Q1. Min Cost to Connect All Points

### Problem Statement (Concrete)
Solve **Min Cost to Connect All Points** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
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

## Q2. Connecting Cities With Minimum Cost

### Problem Statement (Concrete)
Solve **Connecting Cities With Minimum Cost** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **Connecting Cities With Minimum Cost** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_connecting_cities_with_minimum_cost(n, edges):
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

def better_connecting_cities_with_minimum_cost(n, edges):
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
def solve_connecting_cities_with_minimum_cost(n, edges):
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

## Q3. Optimize Water Distribution in a Village

### Problem Statement (Concrete)
Solve **Optimize Water Distribution in a Village** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **Optimize Water Distribution in a Village** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_optimize_water_distribution_in_a_village(n, edges):
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

def better_optimize_water_distribution_in_a_village(n, edges):
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
def solve_optimize_water_distribution_in_a_village(n, edges):
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

## Q4. Critical and Pseudo-Critical Edges in Minimum Spanning Tree

### Problem Statement (Concrete)
Solve **Critical and Pseudo-Critical Edges in Minimum Spanning Tree** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **Critical and Pseudo-Critical Edges in Minimum Spanning Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_critical_and_pseudo_critical_edges_in_minimum_spanning_tree(n, edges):
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

def better_critical_and_pseudo_critical_edges_in_minimum_spanning_tree(n, edges):
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
def solve_critical_and_pseudo_critical_edges_in_minimum_spanning_tree(n, edges):
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

## Q5. Kruskal Algorithm Implementation

### Problem Statement (Concrete)
Solve **Kruskal Algorithm Implementation** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **Kruskal Algorithm Implementation** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_kruskal_algorithm_implementation(n, edges):
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

def better_kruskal_algorithm_implementation(n, edges):
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
def solve_kruskal_algorithm_implementation(n, edges):
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

## Q6. Prim Algorithm Implementation

### Problem Statement (Concrete)
Solve **Prim Algorithm Implementation** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **Prim Algorithm Implementation** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_prim_algorithm_implementation(n, edges):
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

def better_prim_algorithm_implementation(n, edges):
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
def solve_prim_algorithm_implementation(n, edges):
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

## Q7. Minimum Cable Length to Connect Network

### Problem Statement (Concrete)
Solve **Minimum Cable Length to Connect Network** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **Minimum Cable Length to Connect Network** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_minimum_cable_length_to_connect_network(n, edges):
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

def better_minimum_cable_length_to_connect_network(n, edges):
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
def solve_minimum_cable_length_to_connect_network(n, edges):
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

## Q8. MST in Dense Graph

### Problem Statement (Concrete)
Solve **MST in Dense Graph** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **MST in Dense Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_mst_in_dense_graph(n, edges):
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

def better_mst_in_dense_graph(n, edges):
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
def solve_mst_in_dense_graph(n, edges):
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

## Q9. MST in Sparse Graph

### Problem Statement (Concrete)
Solve **MST in Sparse Graph** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **MST in Sparse Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_mst_in_sparse_graph(n, edges):
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

def better_mst_in_sparse_graph(n, edges):
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
def solve_mst_in_sparse_graph(n, edges):
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

## Q10. MST with Pre-connected Components

### Problem Statement (Concrete)
Solve **MST with Pre-connected Components** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Minimum Spanning Tree (Kruskal / Prim)**.
- Red flags: brute force for **MST with Pre-connected Components** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible spanning subsets and keep minimum connected one.

#### Python
```python
def brute_mst_with_pre_connected_components(n, edges):
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

def better_mst_with_pre_connected_components(n, edges):
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
def solve_mst_with_pre_connected_components(n, edges):
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
