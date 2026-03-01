# Pattern 04: Sliding Window (Variable Size)

## Diagram + Intuition

### Pattern Diagram
```text
expand right -> window invalid?
  yes: shrink left until valid
  no: update answer
```

### Read-the-Question Trigger Cues
- "Longest/shortest substring/subarray with constraint"
- "At most K distinct", "without repeating", "sum >= target"

### Intuition Anchor
- "Grow to explore, shrink to repair."

### 3-Second Pattern Check
- Can a valid window be maintained with two moving boundaries?

## What This Pattern Solves
Variable sliding window finds longest/shortest contiguous segment satisfying a condition.

## Recognition Signals
- Phrases like "longest substring with at most K...", "smallest subarray with sum >= target".
- Constraint depends on window content, not fixed length.
- Need optimization over all valid contiguous segments.

## Core Intuition
Use two pointers:
- expand right to include new elements
- shrink left while window is invalid (or while it can be improved)

Each index enters and exits window at most once, giving linear time.

## Step-by-Step Method
1. Initialize `left = 0` and state (counts/sum/distinct).
2. For each `right`, update state with current element.
3. While constraint is violated (or can still be tightened), move `left` and rollback state.
4. After window becomes valid, update answer (max/min length).

## Detailed Example (Longest Substring Without Repeating Characters)
For `"abcabcbb"`:
1. Expand until duplicate appears.
2. Shrink left until duplicate removed.
3. Track max length of valid unique-character window.
4. Best length found is `3` (`"abc"`).

## Complexity
- Time: `O(n)`
- Space: `O(alphabet)` or `O(n)` depending domain

## Python Template
```python
def longest_unique(s):
    left = 0
    freq = {}
    best = 0

    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1

        while freq[ch] > 1:
            left_ch = s[left]
            freq[left_ch] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

## Common Pitfalls
- Shrinking only once instead of while invalid.
- Forgetting to delete or decrement frequency correctly.
- Confusing "at most K" with "exactly K" (update answer at different times).
- Not updating best answer after window becomes valid.

## Variations
- Minimum window substring
- Longest repeating character replacement
- Subarrays with at most/exactly K distinct
- Minimum size subarray sum

## Interview Tips
- State invariant clearly: "Window [left, right] is always valid after inner loop."
- Explain why total pointer movement is `O(n)`.
- If "exactly K" is asked, mention conversion: `exactly(K) = atMost(K) - atMost(K-1)` for counts.

## Practice Problems
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Repeating Character Replacement
- Subarray Product Less Than K
