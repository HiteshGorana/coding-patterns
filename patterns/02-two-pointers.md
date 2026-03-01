# Pattern 02: Two Pointers

## At a Glance

| Item | Summary |
|---|---|
| Use when | You can move indices with a monotonic rule to eliminate candidates |
| Main tradeoff | Often needs sorted input (or sorting) and careful pointer invariants |
| Typical runtime | `O(n)` scan (or `O(n log n)` if sorting is required first) |
| Main structures | indices/pointers: `left/right`, `slow/fast`, optional fixed outer index |
| Common prompts | pair sum in sorted array, palindrome, remove duplicates, 3Sum, max area |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 02 Top 10 Questions Playbook](./questions/02-two-pointers-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Common mode: opposite ends on sorted data

left                               right
  v                                   v
[  ... small values ... | ... large values ... ]

if current state is too small -> move left rightward
if current state is too large -> move right leftward
```

### Read-the-Question Trigger Cues

- Input is sorted, or sorting is allowed without breaking output requirements.
- Prompt asks for pair/triplet relation (`sum`, `difference`, `closest`, `palindrome`).
- Brute force would compare many pairs/subranges.
- You can prove one pointer move discards impossible answers safely.

### Intuition Anchor

- "Every pointer move should permanently eliminate a region I no longer need to check."

### 3-Second Pattern Check

- Can I define a rule for moving `left` or `right` based on current comparison?
- Does each move shrink the search space without missing a valid answer?
- Will each pointer move only forward (or only backward), giving linear passes?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| pair sum on sorted array | opposite-end pointers | `left/right -> current sum` | compare `sum` vs `target` |
| in-place dedupe/compaction | same-direction pointers | `slow -> write`, `fast -> read` | should `nums[fast]` be written? |
| palindrome/string mirror | opposite-end pointers | `left/right -> chars` | `s[left] == s[right]` |
| max-area style | opposite-end pointers | `left/right -> width & min height` | move shorter side |
| 3Sum/4Sum inner scan | fixed outer + inner pair | `i, left, right -> current sum` | compare to goal and skip duplicates |
| merge-like scans | two forward pointers | `i/j -> next smallest candidate` | choose and advance one pointer |

## Universal Invariant

Before coding, say this sentence out loud:

- "At every step, the region already moved past by my pointers cannot contain a better or missing valid answer under my movement rule."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`False`, `[]`, `0`, or `-1`).
2. Initialize pointers with one clear meaning comment.
3. Loop while pointer condition holds (`left < right` or `fast < n`).
4. Compute current state (`sum`, `area`, match/mismatch, distinctness, etc.).
5. Use state result (return/update answer).
6. Move pointer(s) using one explicit elimination rule.
7. Return the default if no hit happened.

Fill-in template:

```python
def solve(items):
    ans_default = ...
    left, right = 0, len(items) - 1  # or slow/fast

    while left < right:
        state = ...  # current pair/window state

        if state == ...:
            return ...  # or update running answer

        if should_move_left(state):
            left += 1
        else:
            right -= 1

    return ans_default
```

## Query/Update Order Rules

### A) Query, then update (most common)

Use for sorted pair comparison tasks (Two Sum II, closest pair).

```python
while left < right:
    state = evaluate(left, right)  # query current pair
    if hit(state):
        return answer
    move_one_pointer_by_rule(state)  # update pointer position
```

### B) Update, then query (window/state variants)

Use when the current element must be incorporated before validity check.

```python
while right < n:
    expand_window_with(nums[right])  # update
    right += 1
    while window_invalid():
        shrink_window_with(nums[left])
        left += 1
    use_current_window()  # query/update answer
```

### C) Two-pass (count then select)

Use when one pass prepares ordering/state and second pass runs two pointers.

```python
arr = sorted((x, i) for i, x in enumerate(nums))  # pass 1: prepare
left, right = 0, len(arr) - 1                     # pass 2: select
while left < right:
    s = arr[left][0] + arr[right][0]
    move_or_return_by_sum(s)
```

## Detailed Example (Two Sum)

**Input:** `numbers = [2, 7, 11, 15], target = 9` (sorted)

1. `left=0 (2)`, `right=3 (15)`, sum `17` > `9`, move `right` left.
2. `left=0 (2)`, `right=2 (11)`, sum `13` > `9`, move `right` left.
3. `left=0 (2)`, `right=1 (7)`, sum `9`, return indices.

Why it works: sorted order makes pointer movement safe, so each move discards impossible pairs.

## Reusable Python Templates

### 1) Membership (Contains Duplicate)

```python
def contains_duplicate_sorted(nums):
    if len(nums) < 2:
        return False

    nums.sort()
    left, right = 0, 1

    while right < len(nums):
        if nums[left] == nums[right]:
            return True
        left += 1
        right += 1

    return False
```

Example:

```python
contains_duplicate_sorted([1, 2, 3, 1])  # True
contains_duplicate_sorted([1, 2, 3, 4])  # False
```

### 2) Frequency Count (Anagram/Mode/Counts)

```python
def run_length_counts(nums):
    nums = sorted(nums)
    out = []
    left = 0

    while left < len(nums):
        right = left
        while right < len(nums) and nums[right] == nums[left]:
            right += 1
        out.append((nums[left], right - left))
        left = right

    return out
```

Example:

```python
run_length_counts([4, 4, 2])  # [(2, 1), (4, 2)]
run_length_counts([1, 1, 1, 2, 3, 3])  # [(1, 3), (2, 1), (3, 2)]
```

### 3) Value -> Index (Two Sum style)

```python
def two_sum_with_index_recovery(nums, target):
    arr = sorted((x, i) for i, x in enumerate(nums))
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left][0] + arr[right][0]
        if s == target:
            return [arr[left][1], arr[right][1]]
        if s < target:
            left += 1
        else:
            right -= 1

    return []
```

Example:

```python
two_sum_with_index_recovery([2, 7, 11, 15], 9)  # [0, 1]
two_sum_with_index_recovery([3, 2, 4], 6)  # [1, 2]
```

### 4) Prefix Sum + Hash Map (Subarray Sum Equals K)

```python
def count_subarrays_sum_k_nonnegative(nums, k):
    # Works for non-negative arrays; two pointers rely on monotonic window sum.
    left = 0
    window_sum = 0
    ans = 0

    for right, x in enumerate(nums):
        window_sum += x
        while left <= right and window_sum > k:
            window_sum -= nums[left]
            left += 1

        if window_sum == k:
            ans += 1
            temp = left
            # Count extra starts caused by leading zeros.
            while temp < right and nums[temp] == 0:
                ans += 1
                temp += 1

    return ans
```

Example:

```python
count_subarrays_sum_k_nonnegative([1, 1, 1], 2)  # 2
count_subarrays_sum_k_nonnegative([0, 0, 0], 0)  # 6
```

## Complexity

Let:

- `n` = number of input elements.
- `k` = number of answers produced (relevant for output-heavy variants).

Per-operation cost:

- Pointer compare/move/update: `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| opposite-end scan on sorted input | `O(n)` | `O(1)` |
| sort + opposite-end scan | `O(n log n)` | `O(1)` to `O(n)` (language sort dependent) |
| slow/fast compaction | `O(n)` | `O(1)` |
| palindrome two-pointer scan | `O(n)` | `O(1)` |
| fixed outer + inner two pointers (3Sum) | `O(n^2)` | `O(1)` extra (excluding output) |

Interview note:

- State scan complexity and whether sorting is included.
- Mention output-sensitive behavior when answer size is large.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: boolean, indices, count, length, or list.
- No-solution behavior is explicit and correct (`[]`, `-1`, `False`, or `0`).
- If original indices are required, do not lose them by sorting without recovery.
- If 1-based indexing is required, convert before returning.

### Data-Rule Checks

- Sorted-input assumption is valid or created safely.
- Pointer movement rule is monotonic and justified (always progresses).
- Duplicate-handling policy is intentional (especially for 3Sum/4Sum).
- For strings, case and punctuation rules match prompt semantics.
- In compaction problems, write pointer updates do not overwrite unread data incorrectly.

### Input Boundary Checks

- Empty input and single-element input are handled safely.
- Two-element boundary is correct (exactly one possible pair).
- All-equal input is handled (for example `[2, 2, 2, 2]`).
- Negative numbers and zero are handled where relevant.
- Large `n` does not trigger accidental nested-loop behavior.

### Pattern-Specific Checks

- Opposite-end mode: every loop iteration moves at least one pointer.
- Sum comparison mode: move left for smaller sum, right for larger sum.
- 3Sum mode: skip duplicates after recording a triplet.
- Slow/fast mode: return correct logical length, not physical list length.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| empty input | `[]` | returns defined default without crash |
| direct hit pair | `numbers=[2,7,11,15], target=9` | returns correct pair indices |
| no valid pair | `numbers=[1,2,3], target=100` | returns no-solution default |
| duplicate-heavy 3Sum | `[-2,0,0,2,2]` | returns unique triplets only |
| punctuation/case palindrome | `"A man, a plan, a canal: Panama"` | returns `True` |

## Common Pitfalls

- Applying opposite-end logic on unsorted data without sorting.
- Moving the wrong pointer for sum comparisons and skipping valid answers.
- Forgetting strict progress, causing infinite loops.
- Missing duplicate-skips in 3Sum/4Sum and returning repeated results.
- Sorting when prompt requires original position/index semantics.

## When Not Ideal

- If no monotonic movement rule exists, pointer elimination may be invalid.
- If relation depends on global history, hash map/prefix techniques are often better.
- If random access is expensive (linked list), opposite-end pointers are awkward.

## Variations

- Opposite ends on sorted arrays: Two Sum II, closest pair, pair difference.
- Slow/fast compaction: remove duplicates, move zeros, stable filtering.
- String mirror checks: valid palindrome and near-palindrome variants.
- Outer fixed + inner pointers: 3Sum, 3Sum Closest, 4Sum.
- Geometry-style elimination: Container With Most Water.

## Interview Tips

- Use this 20-second opener:
  "Brute force is usually `O(n^2)` because we try many pairs. I will use two pointers so each move eliminates impossible candidates, giving linear scan after sorting if needed."
- Say pointer roles before coding:
  "`left/right` track candidate pair boundaries" or "`slow` writes, `fast` reads."
- Say the loop invariant explicitly:
  "Everything outside pointer bounds is already ruled out by the movement rule."
- Call out movement rule out loud:
  "If sum is small, move `left`; if large, move `right`."
- While coding, narrate only decision points:
  evaluate state -> compare -> pointer move.
- Before finishing, run 2 quick tests verbally:
  one normal case and one edge case (empty/single/no-solution/duplicates).
- Close with complexity in one line:
  "Time is linear scan (plus optional sort), space is `O(1)` extra for pointer state."

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why two pointers instead of brute force? | Brute force checks many pairs (`O(n^2)`); two pointers discard candidates each move and scan in linear time on sorted data. |
| Why is moving this pointer safe? | Sorted order plus comparison tells us all skipped candidates cannot satisfy/improve the objective. |
| Do we need sorting first? | Only if input is not already sorted and sorting does not violate output/index constraints. |
| How do you avoid duplicate answers? | After a hit, move pointers and skip equal neighboring values. |
| What is the space tradeoff? | Pointer state is constant-space; sorting may add implementation-dependent memory. |
| Can this fail in worst case? | Runtime guarantees depend on valid monotonic movement; if that invariant fails, pattern is not appropriate. |
| How would this work on streaming input? | Opposite-end mode needs random access/full view; streaming often needs different patterns (window/hash/heap). |
| What if original indices are required? | Keep `(value, index)` pairs before sorting or choose a non-sorting approach. |
| Which edge case breaks this most often? | Wrong pointer movement rule, no strict progress, or duplicate-skip mistakes. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Container With Most Water (Max Area)

Problem:

- Given `height`, choose two lines that form a container with the maximum water area.

What interviewer is testing:

- Can you move from pair brute force to linear elimination?
- Can you justify why moving the shorter side is safe?
- Can you maintain max-area updates without off-by-one mistakes?

#### What to Say in First 30 Seconds

Use this script:

"Brute force checks all line pairs, which is `O(n^2)`.  
I will use opposite-end pointers and compute area each step as `min(h[left], h[right]) * (right - left)`.  
Then I move the pointer at the shorter line, because width always shrinks and only a taller shorter-side can improve area.  
This gives `O(n)` time with `O(1)` extra space."

#### Solution A: Brute Force

Idea:

- Try every pair `(i, j)` with `i < j` and take max area.

```python
def max_area_bruteforce(height):
    n = len(height)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, min(height[i], height[j]) * (j - i))
    return ans
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Sort by Height + Farthest Index Tracking

Idea:

- Process bars by descending height.
- Keep min/max index among processed bars (all have height >= current).
- For current bar, best partner is the farthest processed index.

```python
def max_area_sort_based(height):
    pairs = sorted(((h, i) for i, h in enumerate(height)), reverse=True)
    ans = 0
    min_idx = float("inf")
    max_idx = float("-inf")

    for h, i in pairs:
        if min_idx != float("inf"):
            far = max(abs(i - min_idx), abs(max_idx - i))
            ans = max(ans, h * far)
        min_idx = min(min_idx, i)
        max_idx = max(max_idx, i)

    return ans
```

Complexity:

- Time `O(n log n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "It is correct, but sorting adds `n log n`; two pointers achieves linear time and simpler state."

#### Solution C: Two Pointers (Optimal for this prompt)

Idea:

- Start at both ends.
- Compute area, update answer, move the shorter-height pointer inward.

```python
def max_area_optimal(height):
    left, right = 0, len(height) - 1
    ans = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        ans = max(ans, h * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans
```

Complexity:

- Time `O(n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "Current area uses min height and pointer distance."
2. "Moving the taller side cannot help while shorter side stays limiting."
3. "So I move only the shorter side to search for a potentially taller minimum."
4. "I will test with `[1,8,6,2,5,4,8,3,7]` and `[1,1]`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why move the shorter pointer? | The shorter height limits area; moving the taller side only decreases width without raising the limiting height. |
| Could moving both pointers be faster? | It can skip optimal pairs; move one pointer by a justified elimination rule. |
| What if heights are equal? | Moving either one is safe; many implementations move `right` (or `left`) consistently. |

### 2) Valid Palindrome (Ignore Non-Alphanumeric)

Problem:

- Given string `s`, return whether it is a palindrome after ignoring non-alphanumeric characters and case.

What interviewer is testing:

- Can you implement mirrored pointer logic with skip rules?
- Can you normalize comparisons without building unnecessary structures?
- Can you reason about linear scan and constant auxiliary space?

#### What to Say in First 30 Seconds

Use this script:

"A direct brute-force version can clean the string then compare with reverse.  
To optimize space, I can run two pointers from both ends.  
I skip non-alphanumeric characters on each side and compare lowercase characters.  
Every step moves inward, so runtime is `O(n)` with `O(1)` extra space."

#### Solution A: Brute Force

Idea:

- Build normalized string and compare it with its reverse.

```python
def is_palindrome_bruteforce(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
```

Complexity:

- Time `O(n)`, Space `O(n)`.

#### Solution B: Stack + Half Compare

Idea:

- Normalize once, push first half to stack, compare with second half.

```python
def is_palindrome_stack(s):
    arr = [ch.lower() for ch in s if ch.isalnum()]
    n = len(arr)
    st = []

    for i in range(n // 2):
        st.append(arr[i])

    start = (n + 1) // 2
    for i in range(start, n):
        if not st or st.pop() != arr[i]:
            return False

    return not st
```

Complexity:

- Time `O(n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "It is linear time, but extra memory is avoidable with direct two pointers."

#### Solution C: Two Pointers (Optimal for this prompt)

Idea:

- Move inward from both ends while skipping non-alphanumeric chars.
- Compare lowercased characters at valid positions.

```python
def is_palindrome_optimal(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

Complexity:

- Time `O(n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "Only alphanumeric chars participate in comparison."
2. "I normalize on the fly with `.lower()` instead of building a second string."
3. "Each pointer only moves inward, so total pointer moves are linear."
4. "I will test with `\"A man, a plan, a canal: Panama\"` and `\"race a car\"`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why skip characters in loops instead of preprocessing? | It keeps auxiliary space `O(1)` and still remains linear time. |
| Is this case-sensitive? | No, comparisons use lowercase normalization. |
| What edge cases matter most? | Empty string, punctuation-only strings, and mixed case with symbols. |
