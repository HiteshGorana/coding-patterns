# Pattern 31: Interval DP / Partition DP

## Diagram + Intuition

### Pattern Diagram
```text
dp[l][r]
try split k in [l..r-1]
combine left + right + merge cost
```

### Read-the-Question Trigger Cues
- Best way to parenthesize/split intervals.

### Intuition Anchor
- "Answer for range comes from best split point."

### 3-Second Pattern Check
- Is problem about partitioning a contiguous segment?

## What This Pattern Solves
Problems where optimal answer for range `[l, r]` depends on splitting at intermediate pivot `k`.

## Recognition Signals
- Need best cost/score for parenthesization, interval bursting/cutting, palindrome partitioning.
- Subproblems are contiguous ranges.
- Order of operations affects total result.

## Core Intuition
Define DP over intervals:
- `dp[l][r]` = answer for subarray/range `l..r`

Try all partition points:
`dp[l][r] = best over k of combine(dp[l][k], dp[k+1][r], cost(l,k,r))`

## Step-by-Step Method
1. Define interval state and combine formula.
2. Choose iteration by increasing interval length.
3. For each `[l, r]`, try all split points `k`.
4. Keep best/min result.

## Detailed Example (Matrix Chain Multiplication style)
Cost to multiply matrices `l..r`:
1. Try split at every `k`.
2. Total = left cost + right cost + merge cost at split.
3. Minimum across all `k` gives `dp[l][r]`.

## Complexity
- Typical: `O(n^3)` time, `O(n^2)` space
- Some variants can optimize with monotonic/convex properties

## Python Template
```python
def interval_dp(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for l in range(0, n - length + 1):
            r = l + length - 1
            best = float("inf")
            for k in range(l, r):
                best = min(best, dp[l][k] + dp[k + 1][r])  # + merge cost
            dp[l][r] = best

    return dp[0][n - 1]
```

## Common Pitfalls
- Wrong fill order; shorter intervals must be computed first.
- Missing merge-cost term in transition.
- Incorrect base for length-1 intervals.
- Large constants causing TLE even with correct `O(n^3)`.

## Variations
- Burst Balloons
- Minimum Cost to Cut a Stick
- Palindrome Partitioning II
- Matrix Chain Multiplication

## Interview Tips
- Start by writing recurrence before touching code.
- Draw one small interval split tree to verify formula.
- Mention potential optimizations only if constraints demand.

## Practice Problems
- Burst Balloons
- Minimum Cost to Cut a Stick
- Matrix Chain Multiplication
- Palindrome Partitioning II
