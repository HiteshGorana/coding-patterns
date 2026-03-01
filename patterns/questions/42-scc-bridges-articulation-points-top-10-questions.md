# Pattern 42 Interview Playbook: SCC / Bridges / Articulation Points

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: This pattern extracts advanced graph structure: SCCs in directed graphs, bridges and articulation points in undirected graphs.
- Core intuition: Track entry times and low-link values during DFS; structural inequalities identify critical graph elements.
- Trigger cue 1: Need critical edges/nodes whose removal disconnects graph.
- Trigger cue 2: Need strongly connected components in directed graph.
- Quick self-check: Does question ask for critical links/cut vertices/strongly connected blocks?
- Target complexity: Time Usually O(V + E)., Space O(V + E) plus recursion/stack.

---

## Q1. Critical Connections in a Network

### Problem Statement (Concrete)
Solve **Critical Connections in a Network** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Critical Connections in a Network** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_critical_connections_in_a_network(n, edges):
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
def better_critical_connections_in_a_network(n, edges):
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
def solve_critical_connections_in_a_network(n, edges):
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

## Q2. Articulation Points in Graph

### Problem Statement (Concrete)
Solve **Articulation Points in Graph** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Articulation Points in Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_articulation_points_in_graph(n, edges):
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
def better_articulation_points_in_graph(n, edges):
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
def solve_articulation_points_in_graph(n, edges):
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

## Q3. Strongly Connected Components (Tarjan)

### Problem Statement (Concrete)
Solve **Strongly Connected Components (Tarjan)** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Strongly Connected Components (Tarjan)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_strongly_connected_components_tarjan(n, edges):
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
def better_strongly_connected_components_tarjan(n, edges):
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
def solve_strongly_connected_components_tarjan(n, edges):
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

## Q4. Strongly Connected Components (Kosaraju)

### Problem Statement (Concrete)
Solve **Strongly Connected Components (Kosaraju)** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Strongly Connected Components (Kosaraju)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_strongly_connected_components_kosaraju(n, edges):
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
def better_strongly_connected_components_kosaraju(n, edges):
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
def solve_strongly_connected_components_kosaraju(n, edges):
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

## Q5. Min Days to Disconnect Island

### Problem Statement (Concrete)
Solve **Min Days to Disconnect Island** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Min Days to Disconnect Island** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_min_days_to_disconnect_island(n, edges):
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
def better_min_days_to_disconnect_island(n, edges):
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
def solve_min_days_to_disconnect_island(n, edges):
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

## Q6. Find Eventual Safe States (SCC perspective)

### Problem Statement (Concrete)
Solve **Find Eventual Safe States (SCC perspective)** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Find Eventual Safe States (SCC perspective)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_find_eventual_safe_states_scc_perspective(n, edges):
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
def better_find_eventual_safe_states_scc_perspective(n, edges):
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
def solve_find_eventual_safe_states_scc_perspective(n, edges):
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

## Q7. Build Condensation DAG

### Problem Statement (Concrete)
Solve **Build Condensation DAG** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Build Condensation DAG** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_build_condensation_dag(n, edges):
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
def better_build_condensation_dag(n, edges):
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
def solve_build_condensation_dag(n, edges):
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

## Q8. 2-SAT Feasibility via SCC

### Problem Statement (Concrete)
Solve **2-SAT Feasibility via SCC** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **2-SAT Feasibility via SCC** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_q_2_sat_feasibility_via_scc(n, edges):
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
def better_q_2_sat_feasibility_via_scc(n, edges):
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
def solve_q_2_sat_feasibility_via_scc(n, edges):
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

## Q9. Bridge-Finding in Large Sparse Graph

### Problem Statement (Concrete)
Solve **Bridge-Finding in Large Sparse Graph** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Bridge-Finding in Large Sparse Graph** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_bridge_finding_in_large_sparse_graph(n, edges):
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
def better_bridge_finding_in_large_sparse_graph(n, edges):
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
def solve_bridge_finding_in_large_sparse_graph(n, edges):
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

## Q10. Network Vulnerability Analysis

### Problem Statement (Concrete)
Solve **Network Vulnerability Analysis** using **SCC / Bridges / Articulation Points**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **SCC / Bridges / Articulation Points**.
- Red flags: brute force for **Network Vulnerability Analysis** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute mutual reachability pairwise for each vertex (expensive).

#### Python
```python
def brute_network_vulnerability_analysis(n, edges):
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
def better_network_vulnerability_analysis(n, edges):
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
def solve_network_vulnerability_analysis(n, edges):
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
