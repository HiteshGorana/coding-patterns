# Pattern 43: Tree Rerooting DP

## Diagram + Intuition

### Pattern Diagram
```text
DFS1: compute subtree contribution
DFS2: reroot transfer parent->child to fill all answers
```

### Read-the-Question Trigger Cues
- Need answer for every node as root.
- Naive re-run DFS/BFS per root is too slow (`O(n^2)`).

### Intuition Anchor
- "Compute once for one root, then transfer answers along edges in O(1) per move."

### 3-Second Pattern Check
- Can answer at child be derived from parent answer by local adjustment?

## What This Pattern Solves
Tree rerooting DP computes values for all possible roots using two DFS passes and transfer formulas.

## Recognition Signals
- Per-node global metric in trees.
- Need all-root results efficiently.
- Subtree and outside-subtree contributions both matter.

## Core Intuition
First DFS computes subtree data; second DFS reroots by transferring contribution across each edge.

## Step-by-Step Method
1. Choose initial root (often 0).
2. DFS1: compute subtree size/value aggregates.
3. Compute answer for root from aggregates.
4. DFS2: reroot parent answer to each child using formula.
5. Store answer for every node.

## Detailed Example
In Sum of Distances in Tree, moving root from `u` to child `v` adjusts by `-subtree[v] + (n-subtree[v])`.

## Complexity
- Time: `O(n)`.
- Space: `O(n)`.

## Python Template
```python
def sum_of_distances_in_tree(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    size = [1] * n
    ans = [0] * n

    def dfs1(u, p, depth):
        ans[0] += depth
        for v in g[u]:
            if v == p:
                continue
            dfs1(v, u, depth + 1)
            size[u] += size[v]

    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            ans[v] = ans[u] - size[v] + (n - size[v])
            dfs2(v, u)

    dfs1(0, -1, 0)
    dfs2(0, -1)
    return ans
```

## Common Pitfalls
- Forgetting disconnected check (tree should have n-1 edges).
- Wrong reroot transfer formula signs.
- Mixing 1-index/0-index nodes.

## Variations
- Sum of distances for every node
- Max path metric per root
- Edge reversal counts per root
- Subtree/outside contribution blending

## Interview Tips
- Explain two-pass idea before coding.
- Derive transfer formula on a tiny 3-node example.

## Practice Problems
- Sum of Distances in Tree
- Tree Distances II
- Minimum Edge Reversals So Every Node Is Reachable
- Count Number of Possible Root Nodes
