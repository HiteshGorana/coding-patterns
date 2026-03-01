# Dynamic Programming (Interview-Ready Guide)

Using `[TOPIC] = Dynamic Programming`.

## 0) Scope (Checklist)
- [x] When to use DP (overlap + optimal substructure)
- [x] Memoization vs tabulation
- [x] 1D DP
- [x] 2D DP
- [x] Knapsack patterns
- [x] LIS (`O(n log n)` idea)
- [x] DP on strings (LCS/edit distance/palindrome)
- [x] DP on trees
- [x] Bitmask DP (small n)

## 1) Foundations
DP solves optimization/counting problems by reusing subproblem results.

Core terms:
- State, transition, base case
- Memoization (top-down), tabulation (bottom-up)
- Choice dimension, dependency order

Mental model:
- Define "smallest subproblem that captures future needs."

## 2) How it works
Cause-effect:
1. Choose state variables.
2. Define recurrence from smaller states.
3. Set base cases.
4. Compute in dependency-safe order.

Tiny trace (climbing stairs):
- `dp[0]=1`, `dp[1]=1`
- `dp[2]=dp[1]+dp[0]=2`
- `dp[3]=dp[2]+dp[1]=3`
- `dp[4]=dp[3]+dp[2]=5`

## 3) Patterns (Interview Templates)
1. Linear 1D DP (`dp[i]` from previous few states)
2. Grid/string 2D DP (`dp[i][j]`)
3. Pick/skip knapsack style
4. Interval DP
5. Tree DP (postorder combine child states)
6. Bitmask DP (`dp[mask][last]`)

Invariants:
- `dp[state]` has one precise meaning.
- Transition only uses valid already-solved states.
- Initialize impossible states carefully (`inf`, `-inf`, or 0).

Signals:
- "Max/min/count ways"
- Overlapping recursive recomputation
- "Choose or skip each element"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: House Robber
- State: max profit up to index `i`.
- Transition: `max(dp[i-1], dp[i-2]+nums[i])`.

2. Medium: Coin Change
- State: min coins to make amount `a`.
- Transition from `a-coin`.

3. Medium: Longest Increasing Subsequence
- `O(n^2)` DP or `O(n log n)` tails binary-search method.

4. Hard: Edit Distance
- 2D DP with insert/delete/replace transitions.

5. Hard: Traveling Salesman style (bitmask DP)
- State by visited set and last node.

## 5) Why & What-if
Edge cases:
- Zero length inputs
- Impossible targets
- Large state space causing memory issues

Pitfalls:
- Wrong state definition
- Double counting due to transition order
- Missing base initialization

Why it works:
- Bellman principle: optimal solution built from optimal subsolutions.

Variations:
- Space optimize 2D to 1D when only previous row needed.
- Use memoization when state graph sparse.

## 6) Complexity and Tradeoffs
- Time: roughly `#states * #transitions`
- Space: `#states` (or optimized rolling arrays)

Tradeoffs:
- DP can be memory-heavy.
- Greedy may be faster if greedy-choice property exists.

## 7) Real-world uses
- Resource allocation and planning
- Sequence alignment in bioinformatics
- Text/autocorrect edit distance
- Routing and dynamic optimization

## 8) Comparisons
- DP vs recursion:
  - DP avoids repeated work.
- DP vs greedy:
  - DP exhaustive over states, greedy local decisions.
- Memoization vs tabulation:
  - Memoization simpler for sparse states.
  - Tabulation avoids recursion overhead.

## 9) Retention
Cheat sheet:
- Ask: state? transition? base? order?
- If recursion repeats states, think DP.
- Count ways vs min cost requires different initialization.

Recall hooks:
- "State meaning first, code second."
- "DP = cache the recursion tree."

Practice (10):
1. Easy: Climbing Stairs
2. Easy: Min Cost Climbing Stairs
3. Medium: House Robber
4. Medium: Coin Change
5. Medium: Longest Increasing Subsequence
6. Medium: Longest Common Subsequence
7. Medium: Partition Equal Subset Sum
8. Hard: Edit Distance
9. Hard: Burst Balloons
10. Hard: Shortest Path Visiting All Nodes (bitmask DP)
