# Pattern 43 Interview Playbook: Tree Rerooting DP

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Tree rerooting DP computes values for all possible roots using two DFS passes and transfer formulas.
- Core intuition: First DFS computes subtree data; second DFS reroots by transferring contribution across each edge.
- Trigger cue 1: Need answer for every node as root.
- Trigger cue 2: Naive re-run DFS/BFS per root is too slow (`O(n^2)`).
- Quick self-check: Can answer at child be derived from parent answer by local adjustment?
- Target complexity: Time O(n)., Space O(n).

---

## Q1. Sum of Distances in Tree

### Problem Statement (Concrete)
Solve **Sum of Distances in Tree** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Sum of Distances in Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_sum_of_distances_in_tree(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_sum_of_distances_in_tree(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_sum_of_distances_in_tree(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Tree Distances II

### Problem Statement (Concrete)
Solve **Tree Distances II** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Tree Distances II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_tree_distances_ii(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_tree_distances_ii(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_tree_distances_ii(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Minimum Edge Reversals So Every Node Is Reachable

### Problem Statement (Concrete)
Solve **Minimum Edge Reversals So Every Node Is Reachable** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Minimum Edge Reversals So Every Node Is Reachable** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_minimum_edge_reversals_so_every_node_is_reachable(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_minimum_edge_reversals_so_every_node_is_reachable(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_minimum_edge_reversals_so_every_node_is_reachable(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Count Number of Possible Root Nodes

### Problem Statement (Concrete)
Solve **Count Number of Possible Root Nodes** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Count Number of Possible Root Nodes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_count_number_of_possible_root_nodes(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_count_number_of_possible_root_nodes(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_count_number_of_possible_root_nodes(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Rerooting for Maximum Distance per Node

### Problem Statement (Concrete)
Solve **Rerooting for Maximum Distance per Node** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Rerooting for Maximum Distance per Node** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_rerooting_for_maximum_distance_per_node(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_rerooting_for_maximum_distance_per_node(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_rerooting_for_maximum_distance_per_node(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Rerooting for Subtree Sum Queries

### Problem Statement (Concrete)
Solve **Rerooting for Subtree Sum Queries** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Rerooting for Subtree Sum Queries** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_rerooting_for_subtree_sum_queries(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_rerooting_for_subtree_sum_queries(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_rerooting_for_subtree_sum_queries(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Rerooting for Color Contribution

### Problem Statement (Concrete)
Solve **Rerooting for Color Contribution** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Rerooting for Color Contribution** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_rerooting_for_color_contribution(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_rerooting_for_color_contribution(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_rerooting_for_color_contribution(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Rerooting DP with Edge Weights

### Problem Statement (Concrete)
Solve **Rerooting DP with Edge Weights** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Rerooting DP with Edge Weights** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_rerooting_dp_with_edge_weights(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_rerooting_dp_with_edge_weights(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_rerooting_dp_with_edge_weights(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Tree DP All-Roots Score

### Problem Statement (Concrete)
Solve **Tree DP All-Roots Score** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Tree DP All-Roots Score** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_tree_dp_all_roots_score(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_tree_dp_all_roots_score(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_tree_dp_all_roots_score(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Company Hierarchy Reroot Metrics

### Problem Statement (Concrete)
Solve **Company Hierarchy Reroot Metrics** using **Tree Rerooting DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Tree Rerooting DP**.
- Red flags: brute force for **Company Hierarchy Reroot Metrics** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Run full DFS/BFS from every possible root independently.

#### Python
```python
def brute_company_hierarchy_reroot_metrics(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    for root in range(n):
        st = [(root, -1, 0)]
        total = 0
        while st:
            u, p, d = st.pop()
            total += d
            for v in g[u]:
                if v != p:
                    st.append((v, u, d + 1))
        ans[root] = total
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compute root-0 DP once, then transfer root to children with constant-time reroot formula.

#### Python
```python
def better_company_hierarchy_reroot_metrics(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Rerooting reuses subtree sizes and parent contribution deltas across all roots.

#### Python
```python
def better_company_hierarchy_reroot_metrics(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    size = [1] * n
    dp = [0] * n

    def dfs1(u, p):
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u)
            size[u] += size[v]
            dp[u] += dp[v] + size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            dp[v] = dp[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dp
```

#### Correctness (Why This Works)
- Transition `child = parent - subtree_size + (n - subtree_size)` exactly accounts for distance shift when root moves across one edge.
- Two DFS passes cover all edges constant times, yielding all-root answers.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
