# Pattern 02: Two Pointers

## Diagram + Intuition

### Pattern Diagram
```text
sorted array
L ---------------- R
 move L or R based on condition
```

### Read-the-Question Trigger Cues
- Sorted array/string.
- Need pair/triplet relation (`sum`, `diff`, palindrome).

### Intuition Anchor
- "Each pointer move should eliminate impossible answers."

### 3-Second Pattern Check
- If I move one pointer, can I prove I never miss optimum?

## What This Pattern Solves
Two pointers is ideal for problems on arrays/strings where two positions move with rules.  
It removes nested loops by coordinating pointer movement based on conditions.

## Recognition Signals
- Input is sorted, or can be sorted without breaking problem constraints.
- Need pair/triplet relationships (`sum`, `difference`, `palindrome` checks).
- Ask for in-place operations with limited extra memory.
- Brute force compares many pairs (`O(n^2)`).

## Core Intuition
Each pointer movement should eliminate impossible candidates.  
When pointers move with monotonic logic, every element is processed a limited number of times.

## Common Pointer Modes
- Opposite ends: `left = 0`, `right = n-1`
- Same direction (fast/slow): compaction/filtering
- Multiple pointers (3Sum outer index + inner two pointers)

## Step-by-Step Method (Opposite Ends)
1. Initialize pointers at boundaries.
2. Evaluate current pair.
3. If condition satisfied, record answer.
4. Move one pointer based on sorted-order logic:
   - sum too small -> `left += 1`
   - sum too large -> `right -= 1`
5. Continue until pointers cross.

## Detailed Example (Two Sum II - Sorted)
For `numbers = [2, 7, 11, 15], target = 9`:
1. `left=0 (2)`, `right=3 (15)`, sum 17 too large -> `right--`.
2. `left=0 (2)`, `right=2 (11)`, sum 13 too large -> `right--`.
3. `left=0 (2)`, `right=1 (7)`, sum 9 -> return indices.

## Complexity
- Time: usually `O(n)` after sorting
- Space: `O(1)` extra (excluding optional sort cost)

## Python Template
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        if s < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]
```

## Common Pitfalls
- Applying opposite-end logic on unsorted data without sorting.
- Forgetting duplicate handling for unique-triplet outputs (e.g., 3Sum).
- Pointer moves that do not strictly progress can cause infinite loops.
- Sorting when original order/index preservation is required.

## Variations
- Remove duplicates in-place (slow writes, fast reads).
- Palindrome check ignoring punctuation.
- Container With Most Water (move shorter height pointer).
- 3Sum / 4Sum hybrid with sorting + fixed outer index.

## Interview Tips
- Explain invariant: "Everything outside pointers is already ruled out."
- Show why pointer movement is safe using sorted property.
- Mention whether sorting changes expected output semantics.

## Practice Problems
- Two Sum II
- 3Sum
- Container With Most Water
- Valid Palindrome
- Remove Duplicates from Sorted Array
