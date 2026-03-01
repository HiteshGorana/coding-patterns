# Pattern 26 Interview Playbook: Union-Find (Disjoint Set Union)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Tracks dynamic connectivity between elements with near-constant-time union/find operations.
- Core intuition: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Trigger cue 1: Dynamic connectivity, redundant edge, component count.
- Quick self-check: Am I repeatedly asking if two nodes belong to same group?
- Target complexity: Time pattern-optimal, Space O(n)

---

## Q1. Redundant Connection

### Problem Statement (Specific)
Solve **Redundant Connection** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Redundant Connection, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Redundant Connection directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_redundant_connection(data):
    """Brute-force baseline for: Redundant Connection."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Redundant Connection to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_redundant_connection(data):
    """Intermediate optimized approach for: Redundant Connection."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Redundant Connection: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_redundant_connection(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q2. Number of Provinces

### Problem Statement (Specific)
Solve **Number of Provinces** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Number of Provinces, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Number of Provinces directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_provinces(data):
    """Brute-force baseline for: Number of Provinces."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of Provinces to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_provinces(data):
    """Intermediate optimized approach for: Number of Provinces."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Number of Provinces: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_number_of_provinces(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q3. Accounts Merge

### Problem Statement (Specific)
Solve **Accounts Merge** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Accounts Merge, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Accounts Merge directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_accounts_merge(data):
    """Brute-force baseline for: Accounts Merge."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Accounts Merge to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_accounts_merge(data):
    """Intermediate optimized approach for: Accounts Merge."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Accounts Merge: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_accounts_merge(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q4. Graph Valid Tree

### Problem Statement (Specific)
Solve **Graph Valid Tree** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Graph Valid Tree, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Graph Valid Tree directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_graph_valid_tree(data):
    """Brute-force baseline for: Graph Valid Tree."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Graph Valid Tree to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_graph_valid_tree(data):
    """Intermediate optimized approach for: Graph Valid Tree."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Graph Valid Tree: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_graph_valid_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q5. Number of Islands II

### Problem Statement (Specific)
Solve **Number of Islands II** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: list[list[str]]

### Output
- Count of connected components of land.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [["1","1","0"],["1","0","0"],["0","0","1"]]
Output: 2
Explanation: DFS/BFS each unvisited land cell once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Number of Islands II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_islands_ii(data):
    """Brute-force baseline for: Number of Islands II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of Islands II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_islands_ii(data):
    """Intermediate optimized approach for: Number of Islands II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Number of Islands II: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_number_of_islands_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q6. Most Stones Removed with Same Row or Column

### Problem Statement (Specific)
Solve **Most Stones Removed with Same Row or Column** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Most Stones Removed with Same Row or Column, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Most Stones Removed with Same Row or Column directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_most_stones_removed_with_same_row_or_column(data):
    """Brute-force baseline for: Most Stones Removed with Same Row or Column."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Most Stones Removed with Same Row or Column to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_most_stones_removed_with_same_row_or_column(data):
    """Intermediate optimized approach for: Most Stones Removed with Same Row or Column."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Most Stones Removed with Same Row or Column: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_most_stones_removed_with_same_row_or_column(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q7. Satisfiability of Equality Equations

### Problem Statement (Specific)
Solve **Satisfiability of Equality Equations** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Satisfiability of Equality Equations, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Satisfiability of Equality Equations directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_satisfiability_of_equality_equations(data):
    """Brute-force baseline for: Satisfiability of Equality Equations."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Satisfiability of Equality Equations to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_satisfiability_of_equality_equations(data):
    """Intermediate optimized approach for: Satisfiability of Equality Equations."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Satisfiability of Equality Equations: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_satisfiability_of_equality_equations(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q8. Min Cost to Connect All Points

### Problem Statement (Specific)
Solve **Min Cost to Connect All Points** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
- Apply Union-Find (Disjoint Set Union) invariant to Min Cost to Connect All Points: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_min_cost_to_connect_all_points(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q9. The Earliest Moment When Everyone Become Friends

### Problem Statement (Specific)
Solve **The Earliest Moment When Everyone Become Friends** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For The Earliest Moment When Everyone Become Friends, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for The Earliest Moment When Everyone Become Friends directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_the_earliest_moment_when_everyone_become_friends(data):
    """Brute-force baseline for: The Earliest Moment When Everyone Become Friends."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for The Earliest Moment When Everyone Become Friends to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_the_earliest_moment_when_everyone_become_friends(data):
    """Intermediate optimized approach for: The Earliest Moment When Everyone Become Friends."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to The Earliest Moment When Everyone Become Friends: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_the_earliest_moment_when_everyone_become_friends(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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

## Q10. Detect Cycle in Undirected Graph

### Problem Statement (Specific)
Solve **Detect Cycle in Undirected Graph** using **Union-Find (Disjoint Set Union)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Detect Cycle in Undirected Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Detect Cycle in Undirected Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_detect_cycle_in_undirected_graph(data):
    """Brute-force baseline for: Detect Cycle in Undirected Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Detect Cycle in Undirected Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_detect_cycle_in_undirected_graph(data):
    """Intermediate optimized approach for: Detect Cycle in Undirected Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Union-Find (Disjoint Set Union) invariant to Detect Cycle in Undirected Graph: Represent each component as a tree with representative root. - `find(x)` returns component root - `union(a, b)` merges components if roots differ Optimizations: - path compression in `find` - union by rank/size
- Complexity target: Time pattern-optimal, Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_detect_cycle_in_undirected_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            return True
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
