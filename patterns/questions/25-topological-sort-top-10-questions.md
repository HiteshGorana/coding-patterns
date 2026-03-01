# Pattern 25 Interview Playbook: Topological Sort

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Produces valid ordering of tasks in a directed acyclic graph (DAG) respecting dependencies.
- Core intuition: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Trigger cue 1: Prerequisites/dependency ordering.
- Quick self-check: Is graph directed and dependency-based?
- Target complexity: Time O(V + E), Space O(V + E)

---

## Q1. Course Schedule

### Problem Statement (Specific)
Solve **Course Schedule** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

### Input
- `numCourses`: int
- `prerequisites`: list[list[int]]

### Output
- Boolean indicating whether all courses can be finished.

### Constraints (Typical)
- 1 <= numCourses <= 2e5

### Example (Exact)
```text
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Cycle detection in directed prerequisite graph.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Course Schedule directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_course_schedule(data):
    """Brute-force baseline for: Course Schedule."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Course Schedule to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_course_schedule(data):
    """Intermediate optimized approach for: Course Schedule."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Course Schedule: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
from collections import deque

def solve_course_schedule(num_courses, prerequisites):
    g = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        g[b].append(a)
        indeg[a] += 1
    q = deque([i for i in range(num_courses) if indeg[i] == 0])
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == num_courses
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

## Q2. Course Schedule II

### Problem Statement (Specific)
Solve **Course Schedule II** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

### Input
- `numCourses`: int
- `prerequisites`: list[list[int]]

### Output
- Valid topological order of courses, or empty list.

### Constraints (Typical)
- 1 <= numCourses <= 2e5

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] (one valid answer)
Explanation: Kahn BFS emits nodes when in-degree becomes 0.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Course Schedule II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_course_schedule_ii(data):
    """Brute-force baseline for: Course Schedule II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Course Schedule II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_course_schedule_ii(data):
    """Intermediate optimized approach for: Course Schedule II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Course Schedule II: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
from collections import deque

def solve_course_schedule_ii(num_courses, prerequisites):
    g = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        g[b].append(a)
        indeg[a] += 1
    q = deque([i for i in range(num_courses) if indeg[i] == 0])
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == num_courses
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

## Q3. Alien Dictionary

### Problem Statement (Specific)
Solve **Alien Dictionary** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Alien Dictionary, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Alien Dictionary directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_alien_dictionary(data):
    """Brute-force baseline for: Alien Dictionary."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Alien Dictionary to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_alien_dictionary(data):
    """Intermediate optimized approach for: Alien Dictionary."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Alien Dictionary: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_alien_dictionary(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q4. Parallel Courses

### Problem Statement (Specific)
Solve **Parallel Courses** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Parallel Courses, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Parallel Courses directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_parallel_courses(data):
    """Brute-force baseline for: Parallel Courses."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Parallel Courses to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_parallel_courses(data):
    """Intermediate optimized approach for: Parallel Courses."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Parallel Courses: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_parallel_courses(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q5. Sequence Reconstruction

### Problem Statement (Specific)
Solve **Sequence Reconstruction** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sequence Reconstruction, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sequence Reconstruction directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sequence_reconstruction(data):
    """Brute-force baseline for: Sequence Reconstruction."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sequence Reconstruction to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sequence_reconstruction(data):
    """Intermediate optimized approach for: Sequence Reconstruction."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Sequence Reconstruction: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_sequence_reconstruction(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q6. Find All Possible Recipes from Given Supplies

### Problem Statement (Specific)
Solve **Find All Possible Recipes from Given Supplies** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find All Possible Recipes from Given Supplies, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find All Possible Recipes from Given Supplies directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_all_possible_recipes_from_given_supplies(data):
    """Brute-force baseline for: Find All Possible Recipes from Given Supplies."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find All Possible Recipes from Given Supplies to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_all_possible_recipes_from_given_supplies(data):
    """Intermediate optimized approach for: Find All Possible Recipes from Given Supplies."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Find All Possible Recipes from Given Supplies: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_find_all_possible_recipes_from_given_supplies(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q7. Sort Items by Groups Respecting Dependencies

### Problem Statement (Specific)
Solve **Sort Items by Groups Respecting Dependencies** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sort Items by Groups Respecting Dependencies, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sort Items by Groups Respecting Dependencies directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sort_items_by_groups_respecting_dependencies(data):
    """Brute-force baseline for: Sort Items by Groups Respecting Dependencies."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sort Items by Groups Respecting Dependencies to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sort_items_by_groups_respecting_dependencies(data):
    """Intermediate optimized approach for: Sort Items by Groups Respecting Dependencies."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Sort Items by Groups Respecting Dependencies: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_sort_items_by_groups_respecting_dependencies(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q8. Build a Matrix With Conditions

### Problem Statement (Specific)
Solve **Build a Matrix With Conditions** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Build a Matrix With Conditions, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Build a Matrix With Conditions directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_build_a_matrix_with_conditions(data):
    """Brute-force baseline for: Build a Matrix With Conditions."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Build a Matrix With Conditions to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_build_a_matrix_with_conditions(data):
    """Intermediate optimized approach for: Build a Matrix With Conditions."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Build a Matrix With Conditions: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_build_a_matrix_with_conditions(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q9. Loud and Rich

### Problem Statement (Specific)
Solve **Loud and Rich** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Loud and Rich, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Loud and Rich directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_loud_and_rich(data):
    """Brute-force baseline for: Loud and Rich."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Loud and Rich to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_loud_and_rich(data):
    """Intermediate optimized approach for: Loud and Rich."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Loud and Rich: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_loud_and_rich(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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

## Q10. Eventual Safe States

### Problem Statement (Specific)
Solve **Eventual Safe States** using **Topological Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Eventual Safe States, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Eventual Safe States directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_eventual_safe_states(data):
    """Brute-force baseline for: Eventual Safe States."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Eventual Safe States to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_eventual_safe_states(data):
    """Intermediate optimized approach for: Eventual Safe States."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Topological Sort invariant to Eventual Safe States: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Complexity target: Time O(V + E), Space O(V + E).

#### Optimal Python (Question-Specific)
```python
def solve_eventual_safe_states(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def topo_sort(n, edges):
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
    
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
    
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []
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
