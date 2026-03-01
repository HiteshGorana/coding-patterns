# Pattern 24: Graph BFS/DFS

## Diagram + Intuition

### Pattern Diagram
```text
for each unvisited node:
  traverse component via BFS/DFS
```

### Read-the-Question Trigger Cues
- Components, reachability, clone/traverse graph.

### Intuition Anchor
- "Visited set prevents cycles and repeated work."

### 3-Second Pattern Check
- Is this a generic graph traversal with V+E structure?

## What This Pattern Solves
Explores graph connectivity, components, reachability, and traversal order.

## Recognition Signals
- Nodes/edges representation (explicit or implicit).
- Need connected components, path existence, cloning, bipartite checks.
- Data may contain cycles, unlike trees.

## Core Intuition
Track visited nodes to avoid infinite loops and repeated work.

Use:
- DFS for deep exploration/component marking
- BFS for shortest path in unweighted graphs

## Step-by-Step Method
1. Build adjacency list if needed.
2. Initialize visited set.
3. Traverse each unvisited node to cover disconnected components.
4. During traversal, process neighbors and mark visited early.

## Detailed Example (Count Connected Components)
1. Iterate through all nodes.
2. Each unvisited node starts DFS/BFS and marks one full component.
3. Increment component count once per traversal start.

## Complexity
- Time: `O(V + E)`
- Space: `O(V + E)` adjacency + visited + recursion/queue

## Python Template (DFS Iterative)
```python
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

## Common Pitfalls
- Marking visited after popping, causing duplicates.
- Assuming graph is connected.
- Forgetting directionality in directed graphs.
- Recursion depth issues on large graphs.

## Variations
- Clone Graph
- Number of Connected Components
- Is Graph Bipartite?
- Pacific Atlantic Water Flow (implicit graph)

## Interview Tips
- Start by clarifying directed vs undirected and weighted vs unweighted.
- Mention adjacency list as default sparse-graph representation.
- Explain traversal choice based on required output (distance vs connectivity).

## Practice Problems
- Number of Connected Components in an Undirected Graph
- Clone Graph
- Is Graph Bipartite?
- Number of Provinces
