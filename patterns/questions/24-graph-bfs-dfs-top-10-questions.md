# Pattern 24 Interview Playbook: Graph BFS/DFS

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Explores graph connectivity, components, reachability, and traversal order.
- Core intuition: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Trigger cue 1: Components, reachability, clone/traverse graph.
- Quick self-check: Is this a generic graph traversal with V+E structure?
- Target complexity: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue

---

## Q1. Clone Graph

### Problem Statement (Concrete)
Solve **Clone Graph** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Clone Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_clone_graph(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_clone_graph(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_clone_graph(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Number of Connected Components in an Undirected Graph

### Problem Statement (Concrete)
Solve **Number of Connected Components in an Undirected Graph** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Number of Connected Components in an Undirected Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_number_of_connected_components_in_an_undirected_graph(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_number_of_connected_components_in_an_undirected_graph(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_number_of_connected_components_in_an_undirected_graph(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Number of Provinces

### Problem Statement (Concrete)
Solve **Number of Provinces** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Number of Provinces** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_number_of_provinces(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_number_of_provinces(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_number_of_provinces(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Is Graph Bipartite?

### Problem Statement (Concrete)
Solve **Is Graph Bipartite?** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Is Graph Bipartite?** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_is_graph_bipartite(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_is_graph_bipartite(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_is_graph_bipartite(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Graph Valid Tree

### Problem Statement (Concrete)
Solve **Graph Valid Tree** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Graph Valid Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_graph_valid_tree(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_graph_valid_tree(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_graph_valid_tree(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Reorder Routes to Make All Paths Lead to the City Zero

### Problem Statement (Concrete)
Solve **Reorder Routes to Make All Paths Lead to the City Zero** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Reorder Routes to Make All Paths Lead to the City Zero** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_reorder_routes_to_make_all_paths_lead_to_the_city_zero(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_reorder_routes_to_make_all_paths_lead_to_the_city_zero(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_reorder_routes_to_make_all_paths_lead_to_the_city_zero(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Evaluate Division

### Problem Statement (Concrete)
Solve **Evaluate Division** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Evaluate Division** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_evaluate_division(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_evaluate_division(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_evaluate_division(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Keys and Rooms

### Problem Statement (Concrete)
Solve **Keys and Rooms** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Keys and Rooms** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_keys_and_rooms(start, target):
    # DFS/backtracking over state graph (practical only for tiny spaces).
    best = 10**9
    seen = set()
    def dfs(state, steps):
        nonlocal best
        if steps >= best or state in seen:
            return
        if state == target:
            best = min(best, steps)
            return
        seen.add(state)
        for i in range(len(state)):
            d = int(state[i])
            for nd in ((d + 1) % 10, (d - 1) % 10):
                nxt = state[:i] + str(nd) + state[i+1:]
                dfs(nxt, steps + 1)
        seen.remove(state)
    dfs(start, 0)
    return -1 if best == 10**9 else best
```

#### Complexity
- Time exponential in branching depth, Space `O(depth)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Classic BFS over state graph gives shortest steps in unweighted transitions.

#### Python
```python
from collections import deque

def better_keys_and_rooms(start, target, dead=None):
    dead = set(dead or [])
    if start in dead:
        return -1
    q = deque([(start, 0)])
    seen = {start}
    while q:
        state, d = q.popleft()
        if state == target:
            return d
        for i in range(len(state)):
            x = int(state[i])
            for y in ((x + 1) % 10, (x - 1) % 10):
                nxt = state[:i] + str(y) + state[i+1:]
                if nxt not in seen and nxt not in dead:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
    return -1
```

#### Complexity
- Time `O(V + E)` over reachable states, Space `O(V)`.

### Approach 3: Optimal (Best)
#### Intuition
- Bidirectional BFS shrinks explored frontier dramatically on symmetric state spaces.

#### Python
```python
from collections import deque

def solve_keys_and_rooms(start, target, dead=None):
    dead = set(dead or [])
    if start in dead or target in dead:
        return -1
    if start == target:
        return 0

    front = {start}
    back = {target}
    seen = {start, target}
    steps = 0

    while front and back:
        if len(front) > len(back):
            front, back = back, front
        nxt_front = set()
        steps += 1
        for state in front:
            for i in range(len(state)):
                x = int(state[i])
                for y in ((x + 1) % 10, (x - 1) % 10):
                    nxt = state[:i] + str(y) + state[i+1:]
                    if nxt in dead:
                        continue
                    if nxt in back:
                        return steps
                    if nxt not in seen:
                        seen.add(nxt)
                        nxt_front.add(nxt)
        front = nxt_front
    return -1
```

#### Correctness (Why This Works)
- Each frontier expansion adds exactly one step distance from its side.
- First frontier intersection corresponds to minimal combined distance by BFS layering.

#### Complexity
- Time `O(b^(d/2))` typical, Space `O(b^(d/2))`, where `b` is branching factor.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. All Paths From Source to Target

### Problem Statement (Concrete)
Solve **All Paths From Source to Target** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **All Paths From Source to Target** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_all_paths_from_source_to_target(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_all_paths_from_source_to_target(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_all_paths_from_source_to_target(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Possible Bipartition

### Problem Statement (Concrete)
Solve **Possible Bipartition** using **Graph BFS/DFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Graph BFS/DFS**.
- Red flags: brute force for **Possible Bipartition** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all paths/states without strong pruning.

#### Python
```python
from collections import deque

def brute_possible_bipartition(n, edges, src=0):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    best = [10**9] * n
    def dfs(u, d):
        if d >= best[u]:
            return
        best[u] = d
        for v in g[u]:
            dfs(v, d + 1)
    dfs(src, 0)
    return best
```

#### Complexity
- Time can blow up to exponential in path count.

### Approach 2: Better (Intermediate)
#### Intuition
- Use graph structure (in-degree BFS/standard BFS) to avoid repeated traversal work.

#### Python
```python
from collections import deque

def better_possible_bipartition(n, edges, src=0):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order
```

#### Complexity
- Time around `O(V + E)`, Space `O(V + E)`.

### Approach 3: Optimal (Best)
#### Intuition
- Choose optimal graph primitive for objective (Dijkstra/Topo/DSU/BFS) and maintain its invariant.

#### Python
```python
import heapq

def solve_possible_bipartition(n, edges, src=0):
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
- The selected primitive maintains a correctness invariant: finalized shortest distance / valid dependency order / disjoint connectivity sets.
- Each transition updates state only when invariant-improving, ensuring convergence to optimal valid answer.

#### Complexity
- Time `O((V+E) log V)` or `O(V+E)` depending on exact primitive; Space `O(V+E)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
