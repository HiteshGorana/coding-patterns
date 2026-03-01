# Pattern 06: Binary Search (Index Space)

## Diagram + Intuition

### Pattern Diagram
```text
L ------- mid ------- R
keep half that can still contain target
```

### Read-the-Question Trigger Cues
- Sorted data.
- Need exact index, lower bound, upper bound.

### Intuition Anchor
- "Keep only the half that might still be correct."

### 3-Second Pattern Check
- Is the search condition monotonic across indices?

## What This Pattern Solves
Binary search finds positions or values in sorted/indexed structures in logarithmic time.

## Recognition Signals
- Input is sorted (or partially sorted with searchable property).
- Need first/last occurrence, insertion point, threshold index.
- Brute force linear scan is too slow for large `n`.

## Core Intuition
At each step, discard half the remaining search space based on midpoint comparison.

## Critical Invariants
- Search range usually `[left, right]` inclusive.
- Loop condition and pointer updates must guarantee progress.
- Decide whether searching for exact match, first true, or last true.

## Step-by-Step Method (Exact Match)
1. `left = 0`, `right = n - 1`.
2. Compute `mid = left + (right - left) // 2`.
3. If `arr[mid] == target`, return.
4. If `arr[mid] < target`, move `left = mid + 1`; else `right = mid - 1`.
5. Return not found if loop ends.

## Detailed Example (Search in Sorted Array)
`arr = [1, 3, 5, 7, 9], target = 7`
1. mid at index 2 (value 5), target greater -> move left to 3.
2. mid at index 3 (value 7), found.

## Complexity
- Time: `O(log n)`
- Space: `O(1)` iterative

## Python Template
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## Common Pitfalls
- Infinite loop from incorrect boundary updates.
- Off-by-one errors between inclusive and half-open intervals.
- Not handling duplicates when first/last position is required.
- Overflow concern in some languages using `(left + right) / 2`.

## Variations
- First/last occurrence via lower/upper bound.
- Search in rotated sorted array.
- Peak finding in mountain array.
- Binary search on discrete monotonic predicates.

## Interview Tips
- Declare variant upfront: exact, lower bound, upper bound.
- Explain invariant in one sentence before coding.
- Test mentally on small arrays of size `0`, `1`, and `2`.

## Practice Problems
- Binary Search
- Find First and Last Position of Element in Sorted Array
- Search in Rotated Sorted Array
- Find Peak Element
