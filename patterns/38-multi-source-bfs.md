# Pattern 38: Multi-source BFS

## Diagram + Intuition

### Pattern Diagram
```text
enqueue all sources at distance 0
BFS wave expands simultaneously
```

### Read-the-Question Trigger Cues
- Need nearest distance to any of many sources.
- Diffusion/spread problems in unweighted grid/graph.

### Intuition Anchor
- "Start BFS from all valid origins at once to get globally shortest expansion levels."

### 3-Second Pattern Check
- Can I treat every source as level-0 and expand in one BFS?

## What This Pattern Solves
Multi-source BFS computes shortest unweighted distances from the nearest source by initializing BFS with all sources at distance zero.

## Recognition Signals
- Question asks nearest hospital/land/gate/zero/source.
- Spread in minutes/steps from many initial points.
- Uniform edge cost (unweighted).

## Core Intuition
BFS from all sources in parallel preserves shortest-distance layering and avoids running BFS repeatedly per source.

## Step-by-Step Method
1. Push all source nodes into queue initially.
2. Initialize distance for sources as 0.
3. Run standard BFS; assign first-visit distance for each node.
4. Stop when queue empties or all targets reached.

## Detailed Example
In 01 Matrix, enqueue all `0` cells first, then assign each `1` cell its shortest distance to a `0`.

## Complexity
- Time: `O(V + E)` on graph, `O(R*C)` on grid.
- Space: `O(V)` or `O(R*C)` for queue + distance/visited.

## Python Template
```python
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

## Common Pitfalls
- Running BFS from each source separately (too slow).
- Not initializing all sources before BFS loop starts.
- Using Dijkstra when all edges are unit weight.

## Variations
- 01 Matrix
- Walls and Gates
- Rotting Oranges
- As Far from Land as Possible

## Interview Tips
- State that first time visited in BFS gives shortest distance.
- Clarify level-by-level interpretation for time-based spread.

## Practice Problems
- 01 Matrix
- Rotting Oranges
- Walls and Gates
- As Far from Land as Possible
