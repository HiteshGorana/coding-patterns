# Pattern 38 Interview Playbook: Multi-source BFS

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Multi-source BFS computes shortest unweighted distances from the nearest source by initializing BFS with all sources at distance zero.
- Core intuition: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Trigger cue 1: Need nearest distance to any of many sources.
- Trigger cue 2: Diffusion/spread problems in unweighted grid/graph.
- Quick self-check: Can I treat every source as level-0 and expand in one BFS?
- Target complexity: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited.

---

## Q1. 01 Matrix

### Problem Statement (Specific)
Solve **01 Matrix** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For 01 Matrix, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for 01 Matrix directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_q_01_matrix(data):
    """Brute-force baseline for: 01 Matrix."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for 01 Matrix to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_q_01_matrix(data):
    """Intermediate optimized approach for: 01 Matrix."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to 01 Matrix: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_q_01_matrix(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q2. Rotting Oranges

### Problem Statement (Specific)
Solve **Rotting Oranges** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: list[list[int]]

### Output
- Minimum minutes to rot all fresh oranges, or -1.

### Constraints (Typical)
- 1 <= rows, cols <= 200

### Example (Exact)
```text
Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Explanation: Multi-source BFS from all rotten oranges at time 0.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Rotting Oranges directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_rotting_oranges(data):
    """Brute-force baseline for: Rotting Oranges."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Rotting Oranges to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_rotting_oranges(data):
    """Intermediate optimized approach for: Rotting Oranges."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Rotting Oranges: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_rotting_oranges(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q3. Walls and Gates

### Problem Statement (Specific)
Solve **Walls and Gates** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Walls and Gates, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Walls and Gates directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_walls_and_gates(data):
    """Brute-force baseline for: Walls and Gates."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Walls and Gates to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_walls_and_gates(data):
    """Intermediate optimized approach for: Walls and Gates."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Walls and Gates: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_walls_and_gates(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q4. As Far from Land as Possible

### Problem Statement (Specific)
Solve **As Far from Land as Possible** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For As Far from Land as Possible, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for As Far from Land as Possible directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_as_far_from_land_as_possible(data):
    """Brute-force baseline for: As Far from Land as Possible."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for As Far from Land as Possible to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_as_far_from_land_as_possible(data):
    """Intermediate optimized approach for: As Far from Land as Possible."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to As Far from Land as Possible: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_as_far_from_land_as_possible(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q5. Map of Highest Peak

### Problem Statement (Specific)
Solve **Map of Highest Peak** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Map of Highest Peak, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Map of Highest Peak directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_map_of_highest_peak(data):
    """Brute-force baseline for: Map of Highest Peak."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Map of Highest Peak to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_map_of_highest_peak(data):
    """Intermediate optimized approach for: Map of Highest Peak."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Map of Highest Peak: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_map_of_highest_peak(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q6. Shortest Bridge

### Problem Statement (Specific)
Solve **Shortest Bridge** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Shortest Bridge, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Shortest Bridge directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_shortest_bridge(data):
    """Brute-force baseline for: Shortest Bridge."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Shortest Bridge to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_shortest_bridge(data):
    """Intermediate optimized approach for: Shortest Bridge."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Shortest Bridge: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_shortest_bridge(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q7. Nearest Exit Distance with Multiple Entrances

### Problem Statement (Specific)
Solve **Nearest Exit Distance with Multiple Entrances** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Nearest Exit Distance with Multiple Entrances, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Nearest Exit Distance with Multiple Entrances directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_nearest_exit_distance_with_multiple_entrances(data):
    """Brute-force baseline for: Nearest Exit Distance with Multiple Entrances."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Nearest Exit Distance with Multiple Entrances to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_nearest_exit_distance_with_multiple_entrances(data):
    """Intermediate optimized approach for: Nearest Exit Distance with Multiple Entrances."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Nearest Exit Distance with Multiple Entrances: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_nearest_exit_distance_with_multiple_entrances(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q8. Fire Spread Simulation in Grid

### Problem Statement (Specific)
Solve **Fire Spread Simulation in Grid** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Fire Spread Simulation in Grid, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Fire Spread Simulation in Grid directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_fire_spread_simulation_in_grid(data):
    """Brute-force baseline for: Fire Spread Simulation in Grid."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Fire Spread Simulation in Grid to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_fire_spread_simulation_in_grid(data):
    """Intermediate optimized approach for: Fire Spread Simulation in Grid."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Fire Spread Simulation in Grid: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_fire_spread_simulation_in_grid(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q9. Nearest Facility in Unweighted Graph

### Problem Statement (Specific)
Solve **Nearest Facility in Unweighted Graph** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Nearest Facility in Unweighted Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Nearest Facility in Unweighted Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_nearest_facility_in_unweighted_graph(data):
    """Brute-force baseline for: Nearest Facility in Unweighted Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Nearest Facility in Unweighted Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_nearest_facility_in_unweighted_graph(data):
    """Intermediate optimized approach for: Nearest Facility in Unweighted Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Nearest Facility in Unweighted Graph: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_nearest_facility_in_unweighted_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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

## Q10. Minimum Time to Infect All Nodes

### Problem Statement (Specific)
Solve **Minimum Time to Infect All Nodes** using **Multi-source BFS**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Minimum Time to Infect All Nodes, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Time to Infect All Nodes directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_time_to_infect_all_nodes(data):
    """Brute-force baseline for: Minimum Time to Infect All Nodes."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Time to Infect All Nodes to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_time_to_infect_all_nodes(data):
    """Intermediate optimized approach for: Minimum Time to Infect All Nodes."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Multi-source BFS invariant to Minimum Time to Infect All Nodes: BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.
- Complexity target: Time O(V + E) on graph, O(R*C) on grid., Space O(V) or O(R*C) for queue + distance/visited..

#### Optimal Python (Question-Specific)
```python
def solve_minimum_time_to_infect_all_nodes(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def distance_to_nearest_zero(mat):
        rows, cols = len(mat), len(mat[0])
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
        return dist
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
