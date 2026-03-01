# Pattern 29: Dynamic Programming (2D)

## Diagram + Intuition

### Pattern Diagram
```text
dp[i][j] table
cell uses top/left/diag (or variants)
```

### Read-the-Question Trigger Cues
- Two-dimensional state: strings, grids, pair indices.

### Intuition Anchor
- "Each cell is a smaller subproblem answer."

### 3-Second Pattern Check
- Do I naturally need two coordinates for state?

## What This Pattern Solves
Handles problems where state depends on two indices/dimensions (strings, grids, pair ranges).

## Recognition Signals
- Two varying parameters (`i, j`) define subproblem.
- Typical in string alignment and grid path counting.
- Recursive solutions revisit same `(i, j)` states.

## Core Intuition
Define a table where each cell stores answer for subproblem `(i, j)`.  
Transition combines neighboring states according to problem rules.

## Step-by-Step Method
1. Define state `dp[i][j]`.
2. Determine transition from prior states.
3. Initialize base row/column.
4. Fill table in dependency-respecting order.
5. Return target cell.

## Detailed Example (Longest Common Subsequence)
`dp[i][j]` = LCS length for prefixes `text1[:i]`, `text2[:j]`.
- if chars match: `dp[i][j] = 1 + dp[i-1][j-1]`
- else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

## Complexity
- Time: often `O(n*m)`
- Space: `O(n*m)`; sometimes reducible to `O(min(n,m))`

## Python Template
```python
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
```

## Common Pitfalls
- Off-by-one indexing between strings and DP table.
- Wrong fill order causing dependency on uncomputed cells.
- Forgetting base initialization for empty prefixes.
- Memory blow-up for large inputs without optimization.

## Variations
- Edit Distance
- Unique Paths / Minimum Path Sum
- Distinct Subsequences
- Longest Palindromic Subsequence

## Interview Tips
- Draw tiny `3x3` example table before coding.
- Explain each dimension's meaning clearly.
- Mention rolling array optimization if only previous row/column needed.

## Practice Problems
- Longest Common Subsequence
- Edit Distance
- Unique Paths
- Distinct Subsequences
