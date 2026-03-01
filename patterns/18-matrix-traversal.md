# Pattern 18: Matrix Traversal (Grid BFS/DFS)

## Diagram + Intuition

### Pattern Diagram
```text
grid => graph
cell -> neighbors (4/8 dirs)
visit once
```

### Read-the-Question Trigger Cues
- Islands/regions/flood fill/shortest steps in unweighted grid.

### Intuition Anchor
- "Treat grid as implicit graph."

### 3-Second Pattern Check
- Is this a connectivity or shortest-unweighted path problem on cells?

## What This Pattern Solves
Navigates 2D grids for connectivity, shortest steps (unweighted), and region counting.

## Recognition Signals
- Input is matrix/grid with movement rules.
- Need count islands/components, fill regions, or shortest path in steps.
- Cell state depends on neighbors (up/down/left/right, sometimes diagonals).

## Core Intuition
Treat grid as implicit graph:
- each cell is a node
- valid moves are edges

Use:
- DFS for traversal/component marking
- BFS for shortest path in unweighted grids

## Step-by-Step Method
1. Loop through all cells.
2. On unvisited target cell, start DFS/BFS.
3. Mark visited immediately when enqueued/entered.
4. Explore neighbors with boundary checks.
5. Aggregate result per traversal (count, size, distance).

## Detailed Example (Number of Islands)
1. Scan matrix for `'1'`.
2. Every unvisited `'1'` starts DFS and marks connected land.
3. Increment island count once per DFS launch.
4. Final count equals number of connected land components.

## Complexity
- Time: `O(R * C)` each cell processed constant times
- Space: `O(R * C)` worst-case recursion/queue/visited

## Python Template (BFS)
```python
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

## Common Pitfalls
- Marking visited too late (causes duplicates in queue/stack).
- Boundary checks in wrong order leading to index errors.
- Using DFS recursion on huge grids without considering recursion limit.
- Mixing weighted path logic (should use Dijkstra, not plain BFS).

## Variations
- Number of Islands
- Rotting Oranges
- Flood Fill
- Shortest Path in Binary Matrix

## Interview Tips
- State graph conversion explicitly: "Grid cells are graph nodes."
- Clarify neighbor model (4-direction vs 8-direction).
- Mention in-place marking to reduce extra memory if allowed.

## Practice Problems
- Number of Islands
- Rotting Oranges
- Surrounded Regions
- Shortest Path in Binary Matrix
