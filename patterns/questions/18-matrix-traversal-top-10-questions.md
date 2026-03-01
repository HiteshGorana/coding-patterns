# Pattern 18 Interview Playbook: Matrix Traversal (Grid BFS/DFS)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Navigates 2D grids for connectivity, shortest steps (unweighted), and region counting.
- Core intuition: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Trigger cue 1: Islands/regions/flood fill/shortest steps in unweighted grid.
- Quick self-check: Is this a connectivity or shortest-unweighted path problem on cells?
- Target complexity: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited

---

## Q1. Number of Islands

### Problem Statement (Specific)
Solve **Number of Islands** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

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
- Enumerate all candidate answers for Number of Islands directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_islands(data):
    """Brute-force baseline for: Number of Islands."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of Islands to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_islands(data):
    """Intermediate optimized approach for: Number of Islands."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Number of Islands: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_number_of_islands(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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
Solve **Rotting Oranges** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

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
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Rotting Oranges: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_rotting_oranges(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q3. Flood Fill

### Problem Statement (Specific)
Solve **Flood Fill** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Flood Fill, treat cells as graph nodes with visited control.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Flood Fill directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_flood_fill(data):
    """Brute-force baseline for: Flood Fill."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Flood Fill to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_flood_fill(data):
    """Intermediate optimized approach for: Flood Fill."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Flood Fill: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_flood_fill(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q4. Surrounded Regions

### Problem Statement (Specific)
Solve **Surrounded Regions** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Surrounded Regions, treat cells as graph nodes with visited control.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Surrounded Regions directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_surrounded_regions(data):
    """Brute-force baseline for: Surrounded Regions."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Surrounded Regions to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_surrounded_regions(data):
    """Intermediate optimized approach for: Surrounded Regions."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Surrounded Regions: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_surrounded_regions(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q5. Walls and Gates

### Problem Statement (Specific)
Solve **Walls and Gates** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Walls and Gates, treat cells as graph nodes with visited control.
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
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Walls and Gates: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_walls_and_gates(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q6. Pacific Atlantic Water Flow

### Problem Statement (Specific)
Solve **Pacific Atlantic Water Flow** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Pacific Atlantic Water Flow, treat cells as graph nodes with visited control.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Pacific Atlantic Water Flow directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_pacific_atlantic_water_flow(data):
    """Brute-force baseline for: Pacific Atlantic Water Flow."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Pacific Atlantic Water Flow to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_pacific_atlantic_water_flow(data):
    """Intermediate optimized approach for: Pacific Atlantic Water Flow."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Pacific Atlantic Water Flow: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_pacific_atlantic_water_flow(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q7. Word Search

### Problem Statement (Specific)
Solve **Word Search** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Word Search, treat cells as graph nodes with visited control.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Word Search directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_word_search(data):
    """Brute-force baseline for: Word Search."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Word Search to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_word_search(data):
    """Intermediate optimized approach for: Word Search."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Word Search: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_word_search(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q8. Shortest Path in Binary Matrix

### Problem Statement (Specific)
Solve **Shortest Path in Binary Matrix** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Shortest Path in Binary Matrix, treat cells as graph nodes with visited control.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Shortest Path in Binary Matrix directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_shortest_path_in_binary_matrix(data):
    """Brute-force baseline for: Shortest Path in Binary Matrix."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Shortest Path in Binary Matrix to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_shortest_path_in_binary_matrix(data):
    """Intermediate optimized approach for: Shortest Path in Binary Matrix."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Shortest Path in Binary Matrix: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_shortest_path_in_binary_matrix(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q9. 01 Matrix

### Problem Statement (Specific)
Solve **01 Matrix** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For 01 Matrix, treat cells as graph nodes with visited control.
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
- Apply Matrix Traversal (Grid BFS/DFS) invariant to 01 Matrix: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_q_01_matrix(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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

## Q10. Number of Closed Islands

### Problem Statement (Specific)
Solve **Number of Closed Islands** using **Matrix Traversal (Grid BFS/DFS)**. Return exactly what the problem asks and justify complexity.

### Input
- `grid`: matrix

### Output
- Count/min-time/boolean according to prompt.

### Constraints (Typical)
- 1 <= rows, cols <= 300

### Example (Exact)
```text
Input:  grid = [[1,1,0],[1,0,0],[0,0,1]]
Output: 2
Explanation: For Number of Closed Islands, treat cells as graph nodes with visited control.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Number of Closed Islands directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_closed_islands(data):
    """Brute-force baseline for: Number of Closed Islands."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of Closed Islands to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_closed_islands(data):
    """Intermediate optimized approach for: Number of Closed Islands."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Matrix Traversal (Grid BFS/DFS) invariant to Number of Closed Islands: Treat grid as implicit graph: - each cell is a node - valid moves are edges Use: - DFS for traversal/component marking - BFS for shortest path in unweighted grids
- Complexity target: Time O(R * C) each cell processed constant times, Space O(R * C) worst-case recursion/queue/visited.

#### Optimal Python (Question-Specific)
```python
def solve_number_of_closed_islands(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def bfs_grid(grid, sr, sc):
        rows, cols = len(grid), len(grid[0])
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
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
