# Pattern 28: Dynamic Programming (1D)

## Diagram + Intuition

### Pattern Diagram
```text
dp[i] depends on earlier states
fill left -> right
```

### Read-the-Question Trigger Cues
- Max/min/count ways over linear index.
- Overlapping subproblems in recursion.

### Intuition Anchor
- "State at i summarizes all best history needed."

### 3-Second Pattern Check
- Can I define `dp[i]` with a small recurrence?

## What This Pattern Solves
Optimizes sequential decisions where state depends on previous positions.

## Recognition Signals
- "maximum/minimum/number of ways" with overlapping subproblems.
- Recursive brute force repeats same states.
- State can be indexed by one dimension (index/time/length).

## Core Intuition
Define `dp[i]` as best/count answer up to position `i` (or from `i` onward).  
Transition uses a few previous states:
`dp[i] = combine(dp[i-1], dp[i-2], ...)`

## Step-by-Step Method
1. Choose state meaning precisely.
2. Write recurrence relation.
3. Set base cases.
4. Fill DP table in dependency order.
5. Optional: optimize to rolling variables.

## Detailed Example (House Robber)
`dp[i]` = max money from first `i+1` houses.
Recurrence:
- skip current: `dp[i-1]`
- rob current: `nums[i] + dp[i-2]`
Take max of the two.

## Complexity
- Time: usually `O(n)`
- Space: `O(n)` or `O(1)` optimized

## Python Template
```python
def house_robber(nums):
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]
    for x in nums:
        curr = max(prev1, prev2 + x)
        prev2, prev1 = prev1, curr
    return prev1
```

## Common Pitfalls
- Ambiguous state definition leads to wrong recurrence.
- Incorrect base cases for small `n`.
- Computing states in wrong order.
- Missing modulo operations in counting problems.

## Variations
- Climbing Stairs
- Min Cost Climbing Stairs
- Decode Ways
- Longest Increasing Subsequence (1D + optimization options)

## Interview Tips
- Start from top-down recursion to derive recurrence, then optimize bottom-up.
- Say state definition out loud before writing transitions.
- Mention rolling-array optimization when only few previous states are needed.

## Practice Problems
- House Robber
- Climbing Stairs
- Decode Ways
- Coin Change
