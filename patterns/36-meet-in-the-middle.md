# Pattern 36: Meet in the Middle

## Diagram + Intuition

### Pattern Diagram
```text
left half -> all subset sums
right half -> all subset sums
sort one side + binary search combine
```

### Read-the-Question Trigger Cues
- Constraints suggest brute force `2^n` is too large but `n` is only around `30..45`.
- Subset/partition/sum objective where combining two halves is natural.

### Intuition Anchor
- "Split once, solve both halves exactly, then combine efficiently."

### 3-Second Pattern Check
- Can I reduce `2^n` to roughly `2^(n/2)` per side?

## What This Pattern Solves
Meet in the Middle solves subset-style problems where full exponential search is too large, but splitting the input in half makes exhaustive enumeration feasible.

## Recognition Signals
- `n` is too big for full bitmask brute force but small enough for half-enumeration.
- Need best pair of subset properties across a split.
- Question has subset sum, closest sum, or balanced partition objective.

## Core Intuition
Generate all possibilities for each half, then combine with sorting/binary search/hash lookups to recover global optimum.

## Step-by-Step Method
1. Split array into left and right halves.
2. Enumerate all subset sums (or signatures) for each half.
3. Sort one side for binary search or use map for exact complements.
4. For each value in one side, pick best matching candidate from the other side.
5. Track global optimum and return.

## Detailed Example
For `nums=[5,-7,3,5], goal=6`, left sums and right sums are enumerated separately, then paired to minimize absolute difference.

## Complexity
- Time: Typically `O(2^(n/2) * n)` generation + combine cost (`O(2^(n/2) log 2^(n/2))`).
- Space: `O(2^(n/2))`.

## Python Template
```python
import bisect

def max_subset_sum_leq(nums, limit):
    n = len(nums)
    mid = n // 2
    left, right = nums[:mid], nums[mid:]

    left_sums = [0]
    for x in left:
        left_sums += [s + x for s in left_sums]

    right_sums = [0]
    for x in right:
        right_sums += [s + x for s in right_sums]
    right_sums.sort()

    best = float('-inf')
    for s in left_sums:
        if s > limit:
            continue
        idx = bisect.bisect_right(right_sums, limit - s) - 1
        if idx >= 0:
            best = max(best, s + right_sums[idx])

    return best
```

## Common Pitfalls
- Forgetting to include empty subset (`0`).
- Using full `2^n` enumeration accidentally.
- Not handling duplicates/negative sums correctly during combine.

## Variations
- Closest Subsequence Sum
- Partition with minimum difference
- Meet-in-the-middle knapsack
- Count subsets hitting a target

## Interview Tips
- Explicitly mention complexity drop from `2^n` to `2^(n/2)`.
- Choose combine strategy based on exact-match vs nearest-match objective.

## Practice Problems
- Closest Subsequence Sum
- Partition Array Into Two Arrays to Minimize Sum Difference
- Subset Sum (n around 40)
- Meet-in-the-Middle Knapsack
