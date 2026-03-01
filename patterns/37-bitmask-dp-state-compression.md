# Pattern 37: Bitmask DP / State Compression DP

## Diagram + Intuition

### Pattern Diagram
```text
dp[mask][u] = best with visited set=mask ending at u
transition by adding one bit at a time
```

### Read-the-Question Trigger Cues
- State is naturally a subset of items/nodes.
- Need exact optimization over visited/unvisited sets.

### Intuition Anchor
- "Encode set membership in bits so transitions become constant-time mask operations."

### 3-Second Pattern Check
- Is `n` small enough that `2^n` states are feasible?

## What This Pattern Solves
Bitmask DP solves problems where state includes which elements have been chosen/visited and `n` is small enough for subset-state enumeration.

## Recognition Signals
- Need shortest/cheapest way visiting subset of nodes.
- Assignment and matching with one-to-one constraints.
- TSP-like transitions on subsets.

## Core Intuition
Represent subsets as integers and define DP over masks; each transition sets or clears a bit to move between states.

## Step-by-Step Method
1. Define DP meaning (`dp[mask][i]`, `dp[mask]`, etc.).
2. Initialize base states.
3. Iterate masks in increasing or valid dependency order.
4. Transition by picking next element not yet in mask.
5. Extract final answer from full-mask states.

## Detailed Example
In TSP, `dp[mask][u]` stores minimum path cost that visits nodes in `mask` and ends at `u`.

## Complexity
- Time: Commonly `O(n^2 * 2^n)` or `O(n * 2^n)` depending transition.
- Space: `O(n * 2^n)`.

## Python Template
```python
def tsp_min_cycle(dist):
    n = len(dist)
    INF = 10**15
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                nxt = mask | (1 << v)
                dp[nxt][v] = min(dp[nxt][v], dp[mask][u] + dist[u][v])

    full = (1 << n) - 1
    ans = min(dp[full][u] + dist[u][0] for u in range(n))
    return ans
```

## Common Pitfalls
- Mask off-by-one mistakes.
- Too-large `n` causing memory/time blow-up.
- Wrong iteration order when dependencies are unmet.

## Variations
- Traveling Salesman
- Assignment DP
- Subset covering
- Bitmask BFS hybrid states

## Interview Tips
- Say complexity upfront: `2^n` only works for small `n`.
- Use bit operations explicitly in explanation (`mask | (1<<v)`).

## Practice Problems
- Shortest Path Visiting All Nodes
- Assignment Problem
- Smallest Sufficient Team
- Maximum Compatibility Score Sum
