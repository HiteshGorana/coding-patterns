# Pattern 30: Knapsack DP

## Diagram + Intuition

### Pattern Diagram
```text
for each item:
  for capacity:
    skip vs take
```

### Read-the-Question Trigger Cues
- Pick/skip under capacity/target constraints.

### Intuition Anchor
- "Every item decision: include or exclude."

### 3-Second Pattern Check
- Is this subset decision under a budget-like limit?

## What This Pattern Solves
Optimization/counting problems with "pick or skip" decisions under capacity/target constraints.

## Recognition Signals
- Each item can be taken once (0/1) or multiple times (unbounded).
- Need max value, feasibility, or number of ways under limit.
- Brute force subsets are exponential.

## Core Intuition
DP state tracks best/possible outcome using first `i` items and capacity `c`.

0/1 knapsack transition:
- skip item `i`: `dp[c]`
- take item `i` if `w <= c`: `dp[c-w] + value`

Reverse capacity loop for 0/1 to avoid reusing same item multiple times.

## Step-by-Step Method (0/1 Value Maximization)
1. Initialize `dp[c] = 0`.
2. For each item `(w, v)`:
   - loop `c` from `capacity` down to `w`
   - update `dp[c] = max(dp[c], dp[c-w] + v)`
3. Answer at `dp[capacity]`.

## Complexity
- Time: `O(n * capacity)`
- Space: `O(capacity)` with 1D optimization

## Python Template
```python
def knapsack_01(weights, values, cap):
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]
```

## Common Pitfalls
- Wrong loop direction: forward loop in 0/1 causes duplicate item use.
- Confusing 0/1 vs unbounded knapsack transition.
- Capacity dimension too large for direct DP (need optimization/meet-in-middle).

## Variations
- Partition Equal Subset Sum (feasibility)
- Target Sum (count ways via transformed subset sum)
- Coin Change (unbounded)
- Last Stone Weight II

## Interview Tips
- Classify variant first: maximize, feasibility, or count.
- Mention loop direction rule explicitly.
- For boolean feasibility DP, use `dp[c] |= dp[c-w]`.

## Practice Problems
- 0/1 Knapsack
- Partition Equal Subset Sum
- Target Sum
- Coin Change
