# Pattern 44: Binary Lifting (LCA / Kth Ancestor)

## Diagram + Intuition

### Pattern Diagram
```text
up[v][j] = 2^j-th ancestor of v
raise nodes by binary decomposition of jump length
```

### Read-the-Question Trigger Cues
- Large number of ancestor/LCA queries.
- Static tree (preprocessing is allowed).

### Intuition Anchor
- "Precompute powers-of-two jumps so each query is answered in logarithmic time."

### 3-Second Pattern Check
- Will many online queries justify `O(n log n)` preprocessing?

## What This Pattern Solves
Binary lifting preprocesses ancestors at powers of two to answer kth-ancestor and LCA queries quickly.

## Recognition Signals
- `q` is large, tree is fixed.
- Need jump up by k steps repeatedly.
- Need LCA or distance queries quickly.

## Core Intuition
Store `up[node][j]` and depth; answer queries by jumping bits from high to low.

## Step-by-Step Method
1. Run DFS/BFS from root to fill depth and `up[node][0]`.
2. Build sparse ancestor table for all powers of two.
3. For kth ancestor, lift node according to set bits of `k`.
4. For LCA, align depths then lift both nodes together.

## Detailed Example
To jump 13 levels, decompose `13 = 8 + 4 + 1` and apply three table jumps.

## Complexity
- Time: Preprocess `O(n log n)`, query `O(log n)`.
- Space: `O(n log n)`.

## Python Template
```python
class BinaryLifting:
    def __init__(self, n, parent):  # parent[root] = -1
        self.LOG = (n).bit_length()
        self.up = [[-1] * self.LOG for _ in range(n)]
        self.depth = [0] * n

        for v in range(n):
            self.up[v][0] = parent[v]

        for j in range(1, self.LOG):
            for v in range(n):
                p = self.up[v][j - 1]
                self.up[v][j] = -1 if p == -1 else self.up[p][j - 1]

    def kth_ancestor(self, v, k):
        j = 0
        while k and v != -1:
            if k & 1:
                v = self.up[v][j]
            k >>= 1
            j += 1
        return v
```

## Common Pitfalls
- Wrong `LOG` size causing out-of-range jumps.
- Not aligning depths before LCA lift.
- Using on dynamic trees without rebuild strategy.

## Variations
- Kth ancestor
- LCA
- Distance queries
- Functional graph jumps

## Interview Tips
- Explain binary decomposition of jump length clearly.
- Mention preprocessing/query tradeoff.

## Practice Problems
- Kth Ancestor of a Tree Node
- LCA Queries
- Company Queries I
- Company Queries II
