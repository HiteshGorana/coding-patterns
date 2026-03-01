# Pattern 26: Union-Find (Disjoint Set Union)

## Diagram + Intuition

### Pattern Diagram
```text
find(x) -> root
union(a,b) -> merge roots
```

### Read-the-Question Trigger Cues
- Dynamic connectivity, redundant edge, component count.

### Intuition Anchor
- "Represent each component by a root id."

### 3-Second Pattern Check
- Am I repeatedly asking if two nodes belong to same group?

## What This Pattern Solves
Tracks dynamic connectivity between elements with near-constant-time union/find operations.

## Recognition Signals
- Need to answer "are these nodes connected?" repeatedly.
- Edges added over time.
- Need cycle detection in undirected graph.
- Need count of connected components/provinces.

## Core Intuition
Represent each component as a tree with representative root.
- `find(x)` returns component root
- `union(a, b)` merges components if roots differ

Optimizations:
- path compression in `find`
- union by rank/size

## Step-by-Step Method
1. Initialize each node as its own parent.
2. For each edge:
   - find roots
   - if same root and edge should not connect same component -> cycle/redundant
   - else union roots
3. Maintain component count if needed.

## Complexity
- Amortized almost constant: `O(alpha(n))` per operation
- Space: `O(n)`

## Python Template
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
```

## Common Pitfalls
- Forgetting path compression or union by size/rank (can degrade performance).
- Using DSU directly for directed graph cycle detection (not generally valid).
- Off-by-one index conversion between 1-based and 0-based node labels.

## Variations
- Redundant Connection
- Number of Provinces
- Accounts Merge
- Kruskal's MST algorithm

## Interview Tips
- Say DSU excels at "connectivity under unions."
- Mention amortized complexity with inverse Ackermann.
- Keep API clean: `find`, `union`, optional `connected`.

## Practice Problems
- Redundant Connection
- Number of Provinces
- Accounts Merge
- Graph Valid Tree
