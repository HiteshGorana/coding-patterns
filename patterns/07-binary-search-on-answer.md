# Pattern 07: Binary Search on Answer

## Diagram + Intuition

### Pattern Diagram
```text
answer range [low..high]
check(mid) -> feasible?
true: move left  false: move right
```

### Read-the-Question Trigger Cues
- "minimum feasible", "maximum feasible"
- Rate/capacity/time threshold problems.

### Intuition Anchor
- "I cannot build answer directly, but I can verify a guess."

### 3-Second Pattern Check
- If `x` works, do all larger/smaller values also work?

## What This Pattern Solves
Use this when answer is a numeric value and feasibility is monotonic:
- if value `x` works, all larger/smaller values also work (depending on problem)

## Recognition Signals
- Need minimum/maximum feasible rate, capacity, time, distance.
- Direct search over arrangements is expensive.
- A `can(mid)` check can verify feasibility in linear/near-linear time.

## Core Intuition
Search not over array indices, but over the answer range `[low, high]`.  
At each midpoint, run predicate `can(mid)`:
- If feasible, try better side.
- If infeasible, move opposite side.

## Step-by-Step Method
1. Define monotonic predicate `can(x)`.
2. Set search bounds covering all possible answers.
3. Binary search bounds until converged.
4. Return boundary representing min or max feasible value.

## Detailed Example (Koko Eating Bananas)
Goal: minimum eating speed `k` to finish within `h` hours.
1. `can(k)` computes total hours needed at speed `k`.
2. If hours `<= h`, speed is feasible; try smaller speed.
3. Else increase speed.
4. Final left boundary is minimum feasible speed.

## Complexity
- Let `R = high - low + 1`, check cost `C`.
- Time: `O(C * log R)`
- Space: depends on check, often `O(1)`.

## Python Template
```python
def min_feasible(low, high, can):
    # Finds smallest x in [low, high] such that can(x) is True.
    while low < high:
        mid = low + (high - low) // 2
        if can(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

## Common Pitfalls
- Predicate not truly monotonic.
- Bounds not covering full answer space.
- Using wrong midpoint update for max-feasible variant.
- Integer division/rounding mistakes in feasibility calculations.

## Variations
- Minimize max load (ship capacity, split array largest sum).
- Maximize minimum distance (aggressive cows style).
- Search over real numbers with epsilon for precision.
- Binary search with greedy feasibility checks.

## Interview Tips
- State monotonicity proof briefly before coding.
- Write `can(x)` first; it clarifies everything.
- Clarify whether returning first true, last true, or exact crossing.

## Practice Problems
- Koko Eating Bananas
- Capacity To Ship Packages Within D Days
- Split Array Largest Sum
- Minimized Maximum of Products Distributed to Any Store
