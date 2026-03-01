# Pattern 09: Greedy

## Diagram + Intuition

### Pattern Diagram
```text
repeat:
  take best local safe choice
```

### Read-the-Question Trigger Cues
- Min/max optimization with local decision opportunities.
- Can prove local choice never hurts global optimum.

### Intuition Anchor
- "Commit early only if I can justify safety."

### 3-Second Pattern Check
- Can I give a short exchange/invariant argument?

## What This Pattern Solves
Greedy algorithms make the best local decision at each step, aiming for global optimality.

## Recognition Signals
- Problem asks for minimum/maximum count, cost, or feasibility.
- Choices are irreversible but can be justified by exchange argument.
- DP exists but may be overkill if greedy property holds.

## Core Intuition
If a local choice never hurts an optimal final solution, commit early and move on.  
Greedy works only when problem structure supports it (matroid-like/exchange properties).

## Step-by-Step Method
1. Define candidate local decision rule.
2. Prove or justify why local choice is safe.
3. Iterate once, maintaining minimal state.
4. Return constructed objective value.

## Detailed Example (Jump Game)
Goal: can you reach last index?
1. Track farthest reachable index `reach`.
2. Iterate through array; if current index exceeds `reach`, fail.
3. Update `reach = max(reach, i + nums[i])`.
4. If loop finishes, success.

This greedy invariant is enough; no backtracking needed.

## Complexity
- Time: often `O(n)` (after optional sort)
- Space: usually `O(1)`

## Python Template
```python
def can_jump(nums):
    reach = 0
    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)
    return True
```

## Common Pitfalls
- Using greedy without proof when counterexamples exist.
- Confusing "locally largest value" with "best structural choice."
- Not sorting when greedy order depends on sorted criteria.
- Missing tie-breaking rules that preserve optimality.

## Variations
- Interval scheduling (pick earliest finishing interval).
- Gas Station (cumulative deficit reset logic).
- Minimum arrows for balloons.
- Partition labels / task assignment variants.

## Interview Tips
- Present quick counterexample check to validate greedy rule.
- Explain invariant in one sentence before code.
- If proof is hard, mention fallback DP approach and complexity tradeoff.

## Practice Problems
- Jump Game
- Gas Station
- Non-overlapping Intervals
- Partition Labels
