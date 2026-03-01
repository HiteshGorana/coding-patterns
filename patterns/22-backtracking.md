# Pattern 22: Backtracking

## Diagram + Intuition

### Pattern Diagram
```text
choose -> recurse -> unchoose
DFS over decision tree
```

### Read-the-Question Trigger Cues
- Need all combinations/permutations or constrained existence.

### Intuition Anchor
- "Build partial answer; undo when returning."

### 3-Second Pattern Check
- Is this an exponential choice tree where pruning helps?

## What This Pattern Solves
Explores combinatorial search spaces by building candidates incrementally and undoing choices.

## Recognition Signals
- Need all combinations/permutations/partitions.
- Need existence of solution with constraints (N-Queens, word search).
- Decision tree branching with pruning opportunities.

## Core Intuition
Model problem as DFS over decisions:
1. choose an option
2. recurse
3. unchoose (backtrack) to restore state

Backtracking differs from brute force by pruning invalid/pointless branches early.

## Step-by-Step Method
1. Define state and choice list at each recursion depth.
2. Define termination condition (solution complete).
3. Iterate choices:
   - check feasibility
   - apply choice
   - recurse
   - rollback state
4. Collect or return results.

## Detailed Example (Subsets)
For `[1,2,3]`, each index has include/exclude decision.
DFS tree explores all paths, producing `2^n` subsets.

## Complexity
- Usually exponential: `O(branch^depth)`
- Space: recursion depth + output size

## Python Template
```python
def backtrack(nums):
    ans = []
    path = []

    def dfs(i):
        if i == len(nums):
            ans.append(path[:])
            return

        # choice 1: skip
        dfs(i + 1)

        # choice 2: take
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

    dfs(0)
    return ans
```

## Common Pitfalls
- Forgetting rollback (`pop`, unmark visited) causing state leakage.
- Copy/reference errors when storing current path.
- Weak pruning leading to TLE.
- Duplicate outputs when input has repeated values and dedupe logic missing.

## Variations
- Permutations
- Combination Sum
- N-Queens
- Word Search

## Interview Tips
- State branching factor and depth to justify complexity.
- Discuss pruning rules before coding.
- Keep helper signature clean (`index`, `path`, `used`, etc.).

## Practice Problems
- Subsets
- Permutations
- Combination Sum
- N-Queens
