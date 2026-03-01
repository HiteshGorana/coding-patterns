# Pattern 16: Cyclic Sort

## Diagram + Intuition

### Pattern Diagram
```text
value x belongs to index x (or x-1)
swap until each value is in its home slot
```

### Read-the-Question Trigger Cues
- Array values in bounded range `0..n` or `1..n`.
- Missing/duplicate/corrupt numbers.

### Intuition Anchor
- "Use value as address."

### 3-Second Pattern Check
- Is there a natural correct index for each value?

## What This Pattern Solves
Cyclic sort places numbers into their correct indices when values are from a known range.

## Recognition Signals
- Array values are in range `1..n` or `0..n`.
- Need missing/duplicate/corrupt numbers.
- Want linear time with constant extra space.

## Core Intuition
If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value.

Unlike comparison sort, this uses value-index mapping directly.

## Step-by-Step Method
1. Set `i = 0`.
2. Compute correct index for `nums[i]`.
3. If current value is in range and not already in correct spot, swap.
4. Else increment `i`.
5. After placement phase, scan for mismatch to identify missing/duplicate.

## Detailed Example (Missing Number 0..n)
`nums = [3,0,1]`
1. Place each value at its index when valid.
2. After placement, array becomes `[0,1,3]`.
3. First index mismatch is `2`, so missing number is `2`.

## Complexity
- Time: `O(n)` (each swap places at least one element correctly)
- Space: `O(1)`

## Python Template
```python
def find_missing(nums):
    i = 0
    n = len(nums)
    while i < n:
        x = nums[i]
        if 0 <= x < n and nums[i] != nums[x]:
            nums[i], nums[x] = nums[x], nums[i]
        else:
            i += 1

    for i, x in enumerate(nums):
        if i != x:
            return i
    return n
```

## Common Pitfalls
- Infinite swap loops when duplicate handling condition is wrong.
- Applying pattern when range assumptions are false.
- Off-by-one between `1..n` and `0..n` variants.
- Modifying input when mutation is not allowed by prompt.

## Variations
- Find All Numbers Disappeared in an Array
- Find the Duplicate Number (note: Floyd also possible)
- Set Mismatch
- First Missing Positive (uses indexed placement with constraints)

## Interview Tips
- State required assumptions explicitly before selecting cyclic sort.
- Explain why total swaps are linear, not quadratic.
- Mention fallback hash set method if constraints do not allow in-place mutation.

## Practice Problems
- Missing Number
- Find All Numbers Disappeared in an Array
- Set Mismatch
- First Missing Positive
