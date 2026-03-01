# Pattern 11: Monotonic Queue / Deque

## Diagram + Intuition

### Pattern Diagram
```text
window moves -> expire front
insert new -> pop worse from back
front = best in current window
```

### Read-the-Question Trigger Cues
- Sliding window max/min in strict O(n).

### Intuition Anchor
- "Deque stores only candidates that can still win."

### 3-Second Pattern Check
- Do I need best value per moving window with index expiry?

## What This Pattern Solves
Maintains min/max over a sliding window in linear time.

## Recognition Signals
- Need max/min for every contiguous window of size `k`.
- Naive solution with heap may need lazy deletion and extra overhead.
- Need strict `O(n)` for large constraints.

## Core Intuition
Use deque of indices in monotonic value order:
- decreasing deque for window maximum
- increasing deque for window minimum

Front always holds best candidate for current window.

## Step-by-Step Method
1. Iterate `right` from `0..n-1`.
2. Remove deque front indices that are out of current window (`<= right-k`).
3. Pop from back while monotonic condition is violated by new value.
4. Push current index.
5. Once window reaches size `k`, read answer from deque front.

## Detailed Example (Sliding Window Maximum)
`nums = [1,3,-1,-3,5,3,6,7], k = 3`
1. Build deque for first window with decreasing values.
2. For each slide, discard expired index, then enforce decreasing order.
3. Front index always points to current max.
4. Output becomes `[3,3,5,5,6,7]`.

## Complexity
- Time: `O(n)` amortized
- Space: `O(k)` to `O(n)` worst-case index storage

## Python Template
```python
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()  # indices, values decreasing
    ans = []

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= x:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans
```

## Common Pitfalls
- Storing values instead of indices (cannot expire by position).
- Forgetting to evict out-of-window indices first.
- Using wrong comparator with duplicates (`<` vs `<=`) causing stale entries.
- Mixing min and max monotonic direction.

## Variations
- Sliding window minimum
- Constrained subsequence sum (deque over DP)
- Shortest subarray with sum at least K (monotonic prefix deque)

## Interview Tips
- Emphasize difference from stack: queue supports both insertion and expiration.
- Mention each index is pushed/popped at most once.
- Show one small manual window evolution to prove correctness.

## Practice Problems
- Sliding Window Maximum
- Constrained Subsequence Sum
- Shortest Subarray with Sum at Least K
