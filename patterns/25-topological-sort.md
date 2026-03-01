# Pattern 25: Topological Sort

## Diagram + Intuition

### Pattern Diagram
```text
DAG + indegree
queue indegree-0 nodes
pop -> reduce neighbors indegree
```

### Read-the-Question Trigger Cues
- Prerequisites/dependency ordering.

### Intuition Anchor
- "Do tasks only when prerequisites are cleared."

### 3-Second Pattern Check
- Is graph directed and dependency-based?

## What This Pattern Solves
Produces valid ordering of tasks in a directed acyclic graph (DAG) respecting dependencies.

## Recognition Signals
- "Prerequisite", "dependency", "build order", "schedule courses".
- Directed edges with precedence constraints.
- Need to detect cycles that make ordering impossible.

## Core Intuition
Nodes with in-degree `0` have no unmet prerequisites and can be processed now.  
Removing them may unlock new in-degree `0` nodes.

## Kahn's Algorithm (BFS Topological Sort)
1. Build adjacency list and in-degree array.
2. Enqueue all nodes with in-degree `0`.
3. Pop node, append to order.
4. Decrease in-degree of neighbors.
5. Enqueue neighbors that reach in-degree `0`.
6. If processed node count < total nodes, cycle exists.

## Complexity
- Time: `O(V + E)`
- Space: `O(V + E)`

## Python Template
```python
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

## Common Pitfalls
- Reversing edge direction unintentionally.
- Forgetting to detect cycle when output length is short.
- Assuming topological order is unique.
- Using topo sort on graph that may not be DAG without cycle handling.

## Variations
- Course Schedule I/II
- Alien Dictionary
- Sequence reconstruction constraints
- Parallel course scheduling (levels/semesters)

## Interview Tips
- Mention both Kahn BFS and DFS postorder approaches.
- Clarify edge direction: `u -> v` means `u` before `v`.
- For cycle detection only, count processed nodes.

## Practice Problems
- Course Schedule
- Course Schedule II
- Alien Dictionary
- Parallel Courses
