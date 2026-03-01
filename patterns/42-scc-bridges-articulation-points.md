# Pattern 42: SCC / Bridges / Articulation Points

## Diagram + Intuition

### Pattern Diagram
```text
DFS timestamps + low-link
low[child] > tin[parent] => bridge
low[child] >= tin[parent] => articulation
SCC via stack order
```

### Read-the-Question Trigger Cues
- Need critical edges/nodes whose removal disconnects graph.
- Need strongly connected components in directed graph.

### Intuition Anchor
- "Low-link values summarize whether a DFS subtree can reconnect to an ancestor."

### 3-Second Pattern Check
- Does question ask for critical links/cut vertices/strongly connected blocks?

## What This Pattern Solves
This pattern extracts advanced graph structure: SCCs in directed graphs, bridges and articulation points in undirected graphs.

## Recognition Signals
- Network reliability / single-point failures.
- Compress graph into components.
- Need linear-time DFS-based decomposition.

## Core Intuition
Track entry times and low-link values during DFS; structural inequalities identify critical graph elements.

## Step-by-Step Method
1. Run DFS with discovery time array.
2. Maintain low-link values from back edges and child subtrees.
3. Apply bridge/articulation conditions per edge/node.
4. For SCC, use Tarjan/Kosaraju to build components.

## Detailed Example
In Critical Connections, edges with `low[v] > tin[u]` are bridges because subtree `v` cannot reach above `u`.

## Complexity
- Time: Usually `O(V + E)`.
- Space: `O(V + E)` plus recursion/stack.

## Python Template
```python
def critical_connections(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    tin = [-1] * n
    low = [0] * n
    timer = 0
    bridges = []

    def dfs(u, p):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v in g[u]:
            if v == p:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append([u, v])

    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)

    return bridges
```

## Common Pitfalls
- Applying bridge logic to directed graph without adjustment.
- Skipping disconnected components.
- Wrong parent/back-edge handling in DFS.

## Variations
- Critical Connections
- Articulation points
- SCC condensation graph
- 2-SAT component checks

## Interview Tips
- Write bridge condition explicitly in interview.
- Name arrays clearly (`tin`, `low`) to avoid mistakes.

## Practice Problems
- Critical Connections in a Network
- Articulation Points in Graph
- Strongly Connected Components
- Min Days to Disconnect Island
