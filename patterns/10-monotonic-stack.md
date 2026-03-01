# Pattern 10: Monotonic Stack

## Diagram + Intuition

### Pattern Diagram
```text
stack keeps monotonic values
new value breaks order -> pop and resolve
```

### Read-the-Question Trigger Cues
- "next greater/smaller", nearest boundary, histogram area.

### Intuition Anchor
- "Unresolved elements wait on a stack until a breaker appears."

### 3-Second Pattern Check
- Does each element need nearest bigger/smaller on one side?

## What This Pattern Solves
Monotonic stacks answer "next greater/smaller" and boundary-span questions in linear time.

## Recognition Signals
- Need nearest greater/smaller element to left/right.
- Need contribution ranges (e.g., histogram rectangles, subarray minimums).
- Brute force checks neighbors for each index.

## Core Intuition
Maintain stack of indices with monotonic values:
- increasing stack for next smaller queries
- decreasing stack for next greater queries

When current element breaks monotonicity, pop until restored.  
Each index is pushed and popped at most once.

## Step-by-Step Method
1. Decide monotonic direction from query type.
2. Iterate indices.
3. While stack violates monotonic condition, pop and resolve answer for popped index.
4. Push current index.
5. Handle leftovers if needed (no next greater/smaller).

## Detailed Example (Daily Temperatures)
Need days until warmer temperature:
1. Keep decreasing stack of temperature indices.
2. For current day, pop all colder previous days.
3. For each popped index `j`, answer is `i - j`.
4. Push current day index.

## Complexity
- Time: `O(n)` (amortized)
- Space: `O(n)`

## Python Template
```python
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []  # indices, values in decreasing order

    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            j = stack.pop()
            ans[j] = i
        stack.append(i)

    return ans
```

## Common Pitfalls
- Storing values instead of indices when distance is needed.
- Choosing wrong strictness (`<` vs `<=`) with duplicates.
- Forgetting sentinel pass for histogram-style problems.
- Using stack on unsuited problems where window structure is required.

## Variations
- Largest Rectangle in Histogram
- Trapping Rain Water (stack version)
- Next Greater Element I/II
- Sum of Subarray Minimums

## Interview Tips
- Explicitly say what monotonic property the stack maintains.
- Mention amortized proof: each index enters/leaves once.
- Clarify duplicate handling rule because it affects boundaries.

## Practice Problems
- Daily Temperatures
- Next Greater Element I
- Largest Rectangle in Histogram
- Sum of Subarray Minimums
