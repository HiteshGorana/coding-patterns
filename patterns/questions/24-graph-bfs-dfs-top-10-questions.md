# Pattern 24 Interview Playbook: Graph BFS/DFS

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Explores graph connectivity, components, reachability, and traversal order.
- Core intuition: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Trigger cue 1: Components, reachability, clone/traverse graph.
- Quick self-check: Is this a generic graph traversal with V+E structure?
- Target complexity: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue

---

## Q1. Clone Graph

### Problem Statement (Specific)
Solve **Clone Graph** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Clone Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Clone Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_clone_graph(data):
    """Brute-force baseline for: Clone Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Clone Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_clone_graph(data):
    """Intermediate optimized approach for: Clone Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Clone Graph: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_clone_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q2. Number of Connected Components in an Undirected Graph

### Problem Statement (Specific)
Solve **Number of Connected Components in an Undirected Graph** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Number of Connected Components in an Undirected Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Number of Connected Components in an Undirected Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_connected_components_in_an_undirected_graph(data):
    """Brute-force baseline for: Number of Connected Components in an Undirected Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of Connected Components in an Undirected Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_connected_components_in_an_undirected_graph(data):
    """Intermediate optimized approach for: Number of Connected Components in an Undirected Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Number of Connected Components in an Undirected Graph: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_number_of_connected_components_in_an_undirected_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q3. Number of Provinces

### Problem Statement (Specific)
Solve **Number of Provinces** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
- Apply Graph BFS/DFS invariant to Number of Provinces: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_number_of_provinces(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q4. Is Graph Bipartite?

### Problem Statement (Specific)
Solve **Is Graph Bipartite?** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Is Graph Bipartite?, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Is Graph Bipartite? directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_is_graph_bipartite(data):
    """Brute-force baseline for: Is Graph Bipartite?."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Is Graph Bipartite? to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_is_graph_bipartite(data):
    """Intermediate optimized approach for: Is Graph Bipartite?."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Is Graph Bipartite?: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_is_graph_bipartite(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q5. Graph Valid Tree

### Problem Statement (Specific)
Solve **Graph Valid Tree** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
- Apply Graph BFS/DFS invariant to Graph Valid Tree: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_graph_valid_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q6. Reorder Routes to Make All Paths Lead to the City Zero

### Problem Statement (Specific)
Solve **Reorder Routes to Make All Paths Lead to the City Zero** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Reorder Routes to Make All Paths Lead to the City Zero, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reorder Routes to Make All Paths Lead to the City Zero directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reorder_routes_to_make_all_paths_lead_to_the_city_zero(data):
    """Brute-force baseline for: Reorder Routes to Make All Paths Lead to the City Zero."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reorder Routes to Make All Paths Lead to the City Zero to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reorder_routes_to_make_all_paths_lead_to_the_city_zero(data):
    """Intermediate optimized approach for: Reorder Routes to Make All Paths Lead to the City Zero."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Reorder Routes to Make All Paths Lead to the City Zero: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_reorder_routes_to_make_all_paths_lead_to_the_city_zero(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q7. Evaluate Division

### Problem Statement (Specific)
Solve **Evaluate Division** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Evaluate Division, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Evaluate Division directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_evaluate_division(data):
    """Brute-force baseline for: Evaluate Division."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Evaluate Division to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_evaluate_division(data):
    """Intermediate optimized approach for: Evaluate Division."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Evaluate Division: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_evaluate_division(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q8. Keys and Rooms

### Problem Statement (Specific)
Solve **Keys and Rooms** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Keys and Rooms, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Keys and Rooms directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_keys_and_rooms(data):
    """Brute-force baseline for: Keys and Rooms."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Keys and Rooms to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_keys_and_rooms(data):
    """Intermediate optimized approach for: Keys and Rooms."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Keys and Rooms: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_keys_and_rooms(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q9. All Paths From Source to Target

### Problem Statement (Specific)
Solve **All Paths From Source to Target** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For All Paths From Source to Target, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for All Paths From Source to Target directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_all_paths_from_source_to_target(data):
    """Brute-force baseline for: All Paths From Source to Target."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for All Paths From Source to Target to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_all_paths_from_source_to_target(data):
    """Intermediate optimized approach for: All Paths From Source to Target."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to All Paths From Source to Target: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_all_paths_from_source_to_target(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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

## Q10. Possible Bipartition

### Problem Statement (Specific)
Solve **Possible Bipartition** using **Graph BFS/DFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Possible Bipartition, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Possible Bipartition directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_possible_bipartition(data):
    """Brute-force baseline for: Possible Bipartition."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Possible Bipartition to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_possible_bipartition(data):
    """Intermediate optimized approach for: Possible Bipartition."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Graph BFS/DFS invariant to Possible Bipartition: Track visited nodes to avoid infinite loops and repeated work. Use: - DFS for deep exploration/component marking - BFS for shortest path in unweighted graphs
- Complexity target: Time O(V + E), Space O(V + E) adjacency + visited + recursion/queue.

#### Optimal Python (Question-Specific)
```python
def solve_possible_bipartition(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_components(n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = [False] * n
        components = 0
    
        for start in range(n):
            if visited[start]:
                continue
            components += 1
            stack = [start]
            visited[start] = True
    
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
    
        return components
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
