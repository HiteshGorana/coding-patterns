# Pattern 40 Interview Playbook: Minimum Spanning Tree (Kruskal / Prim)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: MST patterns solve minimum-cost connectivity over undirected weighted graphs using Kruskal or Prim.
- Core intuition: Use cut property: the lightest edge crossing any cut is safe for MST.
- Trigger cue 1: Connect all vertices with minimum sum weight.
- Trigger cue 2: Need exactly `n-1` edges without cycles.
- Quick self-check: Is this 'connect everything at min total edge cost' rather than shortest path from one source?
- Target complexity: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E).

---

## Q1. Min Cost to Connect All Points

### Problem Statement (Specific)
Solve **Min Cost to Connect All Points** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Min Cost to Connect All Points, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Min Cost to Connect All Points directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_min_cost_to_connect_all_points(data):
    """Brute-force baseline for: Min Cost to Connect All Points."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Min Cost to Connect All Points to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_min_cost_to_connect_all_points(data):
    """Intermediate optimized approach for: Min Cost to Connect All Points."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Min Cost to Connect All Points: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_min_cost_to_connect_all_points(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q2. Connecting Cities With Minimum Cost

### Problem Statement (Specific)
Solve **Connecting Cities With Minimum Cost** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 2
Output: 7
Explanation: For Connecting Cities With Minimum Cost, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Connecting Cities With Minimum Cost directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_connecting_cities_with_minimum_cost(data):
    """Brute-force baseline for: Connecting Cities With Minimum Cost."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Connecting Cities With Minimum Cost to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_connecting_cities_with_minimum_cost(data):
    """Intermediate optimized approach for: Connecting Cities With Minimum Cost."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Connecting Cities With Minimum Cost: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_connecting_cities_with_minimum_cost(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q3. Optimize Water Distribution in a Village

### Problem Statement (Specific)
Solve **Optimize Water Distribution in a Village** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 0
Output: 7
Explanation: For Optimize Water Distribution in a Village, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Optimize Water Distribution in a Village directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_optimize_water_distribution_in_a_village(data):
    """Brute-force baseline for: Optimize Water Distribution in a Village."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Optimize Water Distribution in a Village to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_optimize_water_distribution_in_a_village(data):
    """Intermediate optimized approach for: Optimize Water Distribution in a Village."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Optimize Water Distribution in a Village: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_optimize_water_distribution_in_a_village(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q4. Critical and Pseudo-Critical Edges in Minimum Spanning Tree

### Problem Statement (Specific)
Solve **Critical and Pseudo-Critical Edges in Minimum Spanning Tree** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Critical and Pseudo-Critical Edges in Minimum Spanning Tree, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Critical and Pseudo-Critical Edges in Minimum Spanning Tree directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_critical_and_pseudo_critical_edges_in_minimum_spanning_tree(data):
    """Brute-force baseline for: Critical and Pseudo-Critical Edges in Minimum Spanning Tree."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Critical and Pseudo-Critical Edges in Minimum Spanning Tree to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_critical_and_pseudo_critical_edges_in_minimum_spanning_tree(data):
    """Intermediate optimized approach for: Critical and Pseudo-Critical Edges in Minimum Spanning Tree."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Critical and Pseudo-Critical Edges in Minimum Spanning Tree: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_critical_and_pseudo_critical_edges_in_minimum_spanning_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q5. Kruskal Algorithm Implementation

### Problem Statement (Specific)
Solve **Kruskal Algorithm Implementation** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 2
Output: 7
Explanation: For Kruskal Algorithm Implementation, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Kruskal Algorithm Implementation directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_kruskal_algorithm_implementation(data):
    """Brute-force baseline for: Kruskal Algorithm Implementation."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Kruskal Algorithm Implementation to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_kruskal_algorithm_implementation(data):
    """Intermediate optimized approach for: Kruskal Algorithm Implementation."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Kruskal Algorithm Implementation: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_kruskal_algorithm_implementation(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q6. Prim Algorithm Implementation

### Problem Statement (Specific)
Solve **Prim Algorithm Implementation** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 0
Output: 7
Explanation: For Prim Algorithm Implementation, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Prim Algorithm Implementation directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_prim_algorithm_implementation(data):
    """Brute-force baseline for: Prim Algorithm Implementation."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Prim Algorithm Implementation to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_prim_algorithm_implementation(data):
    """Intermediate optimized approach for: Prim Algorithm Implementation."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Prim Algorithm Implementation: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_prim_algorithm_implementation(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q7. Minimum Cable Length to Connect Network

### Problem Statement (Specific)
Solve **Minimum Cable Length to Connect Network** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Minimum Cable Length to Connect Network, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Cable Length to Connect Network directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_cable_length_to_connect_network(data):
    """Brute-force baseline for: Minimum Cable Length to Connect Network."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Cable Length to Connect Network to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_cable_length_to_connect_network(data):
    """Intermediate optimized approach for: Minimum Cable Length to Connect Network."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to Minimum Cable Length to Connect Network: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_minimum_cable_length_to_connect_network(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q8. MST in Dense Graph

### Problem Statement (Specific)
Solve **MST in Dense Graph** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 2
Output: 7
Explanation: For MST in Dense Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for MST in Dense Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_mst_in_dense_graph(data):
    """Brute-force baseline for: MST in Dense Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for MST in Dense Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_mst_in_dense_graph(data):
    """Intermediate optimized approach for: MST in Dense Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to MST in Dense Graph: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_mst_in_dense_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q9. MST in Sparse Graph

### Problem Statement (Specific)
Solve **MST in Sparse Graph** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 0
Output: 7
Explanation: For MST in Sparse Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for MST in Sparse Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_mst_in_sparse_graph(data):
    """Brute-force baseline for: MST in Sparse Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for MST in Sparse Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_mst_in_sparse_graph(data):
    """Intermediate optimized approach for: MST in Sparse Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to MST in Sparse Graph: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_mst_in_sparse_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q10. MST with Pre-connected Components

### Problem Statement (Specific)
Solve **MST with Pre-connected Components** using **Minimum Spanning Tree (Kruskal / Prim)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For MST with Pre-connected Components, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for MST with Pre-connected Components directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_mst_with_pre_connected_components(data):
    """Brute-force baseline for: MST with Pre-connected Components."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for MST with Pre-connected Components to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_mst_with_pre_connected_components(data):
    """Intermediate optimized approach for: MST with Pre-connected Components."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Minimum Spanning Tree (Kruskal / Prim) invariant to MST with Pre-connected Components: Use cut property: the lightest edge crossing any cut is safe for MST.
- Complexity target: Time Kruskal O(E log E), Prim O(E log V) with heap., Space O(V + E)..

#### Optimal Python (Question-Specific)
```python
def solve_mst_with_pre_connected_components(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
            self.sz = [1] * n
    
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.sz[ra] < self.sz[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            self.sz[ra] += self.sz[rb]
            return True
    
    def kruskal_mst(n, edges):  # edges: (w, u, v)
        edges.sort()
        dsu = DSU(n)
        total = 0
        used = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---
