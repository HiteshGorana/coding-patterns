# Pattern 40: Minimum Spanning Tree (Kruskal / Prim)

## Diagram + Intuition

### Pattern Diagram
```text
Kruskal: sort edges by weight -> union if no cycle
Prim: grow tree from seed with min outgoing edge
```

### Read-the-Question Trigger Cues
- Connect all vertices with minimum sum weight.
- Need exactly `n-1` edges without cycles.

### Intuition Anchor
- "MST picks cheapest safe edges that keep global connectivity optimal."

### 3-Second Pattern Check
- Is this 'connect everything at min total edge cost' rather than shortest path from one source?

## What This Pattern Solves
MST patterns solve minimum-cost connectivity over undirected weighted graphs using Kruskal or Prim.

## Recognition Signals
- Weighted undirected graph.
- Need spanning structure, not path between two nodes.
- Cycle-free with full connectivity.

## Core Intuition
Use cut property: the lightest edge crossing any cut is safe for MST.

## Step-by-Step Method
1. Kruskal: sort edges by weight.
2. Union endpoints if they are in different components.
3. Accumulate weight until `n-1` edges chosen.
4. Or Prim: expand frontier using min-heap edges.

## Detailed Example
For points/cities with costs, selecting cheapest non-cycling edges until all nodes connected yields MST.

## Complexity
- Time: Kruskal `O(E log E)`, Prim `O(E log V)` with heap.
- Space: `O(V + E)`.

## Python Template
```python
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True

def kruskal_mst(n, edges):  # edges: (w, u, v)
    edges.sort()
    dsu = DSU(n)
    total = 0
    used = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            total += w
            used += 1
            if used == n - 1:
                return total
    return -1
```

## Common Pitfalls
- Applying MST to directed graphs directly.
- Confusing MST with shortest path tree.
- Not handling disconnected graph (`-1`/impossible).

## Variations
- Kruskal MST
- Prim MST
- Critical edges in MST
- MST with Manhattan distances

## Interview Tips
- Say cut/cycle property briefly for correctness.
- Pick Kruskal when edges list is natural; Prim when adjacency is natural.

## Practice Problems
- Min Cost to Connect All Points
- Connecting Cities With Minimum Cost
- Optimize Water Distribution in a Village
- Critical and Pseudo-Critical Edges in MST
