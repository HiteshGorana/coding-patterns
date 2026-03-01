# Pattern 03: Sliding Window (Fixed Size)

## Diagram + Intuition

### Pattern Diagram
```text
[ i ... i+k-1 ] -> slide right by 1
remove left, add right
```

### Read-the-Question Trigger Cues
- Window size `k` is fixed.
- Need max/min/sum/avg over every size-k segment.

### Intuition Anchor
- "Adjacent windows overlap; reuse prior work."

### 3-Second Pattern Check
- Can current window answer be updated with +incoming -outgoing?

## What This Pattern Solves
Fixed-size sliding window optimizes repeated computations over all subarrays/substrings of length `k`.

## Recognition Signals
- Problem explicitly gives a window size `k`.
- Need max/min/sum/average over every contiguous block of size `k`.
- Brute force recalculates each block from scratch (`O(n*k)`).

## Core Intuition
Adjacent windows overlap heavily.  
Instead of recomputing, update window result incrementally:
- add incoming element
- remove outgoing element

This turns `O(n*k)` into `O(n)`.

## Step-by-Step Method
1. Expand right pointer across the input.
2. Add current element to running state (`window_sum`, counts, etc.).
3. Once window length exceeds `k`, remove left element and move left.
4. When window length equals `k`, evaluate candidate answer.

## Detailed Example (Max Sum Subarray of Size K)
`nums = [2, 1, 5, 1, 3, 2], k = 3`
1. Build first window `[2,1,5]`, sum = 8.
2. Slide by 1: add `1`, remove `2`, sum = 7.
3. Slide: add `3`, remove `1`, sum = 9 (best).
4. Slide: add `2`, remove `5`, sum = 6.
Answer is `9`.

## Complexity
- Time: `O(n)`
- Space: `O(1)` or `O(alphabet)` if frequency table needed

## Python Template
```python
def max_sum_k(nums, k):
    left = 0
    window_sum = 0
    best = float("-inf")

    for right, x in enumerate(nums):
        window_sum += x

        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        if right - left + 1 == k:
            best = max(best, window_sum)

    return best
```

## Common Pitfalls
- Off-by-one errors in window length checks.
- Updating answer before removing overflow element.
- Forgetting constraints where `k > n`.
- Using fixed-window logic when constraint is variable (should use variable window).

## Variations
- Max average subarray of size `k`
- Find all anagrams in a string (fixed char-count window)
- Distinct elements in every window of size `k`
- Maximum vowels in substring of length `k`

## Interview Tips
- Say explicitly: "Every move changes window by exactly one outgoing and one incoming element."
- Show precise length formula: `right - left + 1`.
- Clarify whether negative numbers affect logic (they do not break fixed window mechanics).

## Practice Problems
- Maximum Average Subarray I
- Sliding Window Maximum (with deque optimization)
- Find All Anagrams in a String
- K Radius Subarray Averages
