# Pattern 04: Sliding Window (Variable Size)

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need longest/shortest/count of contiguous segments under a dynamic constraint |
| Main tradeoff | Requires strict validity invariant and careful shrink conditions |
| Typical runtime | `O(n)` for monotonic two-pointer movement |
| Main structures | `left/right` pointers + rolling state (`sum`, `freq`, `distinct`, violations) |
| Common prompts | longest unique substring, at most/exactly K distinct, min length with sum >= target |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 04 Top 10 Questions Playbook](./questions/04-sliding-window-variable-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Core flow:

right expands -> add incoming -> check invariant
while invariant broken:
  remove outgoing at left
  left += 1

when invariant holds:
  update answer (max/min/count depending on prompt)
```

### Read-the-Question Trigger Cues

- "Longest/shortest subarray/substring with condition."
- "At most K distinct", "without repeating characters", "sum >= target", "replace at most K chars."
- Window size is not fixed; validity depends on current content.

### Intuition Anchor

- "Expand to explore candidates, shrink to repair constraint."

### 3-Second Pattern Check

- Can I express validity as a condition on window state?
- If window is invalid, can moving `left` only forward restore validity?
- Does each element enter/exit at most once?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| longest unique substring | freq map or last-seen map | `char -> count/index` | duplicate present? |
| at most `k` distinct | freq map + distinct counter | `value -> frequency` | `distinct <= k` |
| min length with sum >= target (positive nums) | running sum | `window -> sum` | shrink while `sum >= target` |
| replacement budget constraints | freq map + max frequency | `char -> count` | `window_len - max_freq <= k` |
| count subarrays with at most `k` property | freq map + combinatorics | state of current window | add `right - left + 1` |
| exactly `k` counts | two at-most passes | helper result | `atMost(k) - atMost(k-1)` |

## Universal Invariant

Before coding, say this sentence out loud:

- "After my inner shrink loop, window `[left, right]` is valid under the problem constraint, and all earlier `left` values that were removed are intentionally excluded."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`0`, `-1`, `[]`, or `""`).
2. Initialize `left = 0` and rolling state with one clear meaning comment.
3. Expand `right` across input and apply incoming update.
4. While window violates constraint (or can still be tightened), rollback outgoing at `left` and move `left`.
5. Once window is valid, update answer using current window.
6. Keep movement monotonic: only `left += 1`, `right += 1`.
7. Return final answer.

Fill-in template:

```python
def solve(items, k):
    ans = ...
    left = 0
    state = ...  # sum/freq/distinct/violations

    for right, x in enumerate(items):
        add_to_state(x)

        while window_invalid(state, k):
            remove_from_state(items[left])
            left += 1

        use_valid_window(left, right, state)  # update max/min/count

    return ans
```

## Query/Update Order Rules

### A) Expand, then shrink until valid, then query (most common)

Use for longest-valid-window style prompts.

```python
for right, x in enumerate(nums):
    add(x)                     # update
    while invalid():
        remove(nums[left])     # repair
        left += 1
    update_answer(left, right) # query
```

### B) Expand, then query while condition holds, then shrink (min-window style)

Use when you seek smallest valid window.

```python
for right, x in enumerate(nums):
    add(x)
    while valid():
        update_min_answer(left, right)
        remove(nums[left])
        left += 1
```

### C) Two-pass (atMost conversion)

Use for exact count variants where direct exact-window maintenance is hard.

```python
def exactly_k(nums, k):
    return at_most_k(nums, k) - at_most_k(nums, k - 1)
```

## Detailed Example (Longest Substring Without Repeating Characters)

**Input:** `s = "abcabcbb"`

1. Expand to `"abc"`: valid, best length = `3`.
2. Next char is `"a"` (duplicate), shrink left until duplicate removed.
3. Continue expand/shrink; valid window maintained after each repair.
4. Maximum valid length remains `3`.

Why it works: right pointer explores candidates, left pointer only moves forward to restore validity, so total pointer movement is linear.

## Reusable Python Templates

### 1) Membership (Longest Unique Substring with Set)

```python
def longest_unique_set(s):
    seen = set()
    left = 0
    best = 0

    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1

        seen.add(ch)
        best = max(best, right - left + 1)

    return best
```

Example:

```python
longest_unique_set("abcabcbb")  # 3
longest_unique_set("bbbbb")  # 1
```

### 2) Frequency Count (At Most K Distinct)

```python
def longest_at_most_k_distinct(s, k):
    if k <= 0:
        return 0

    left = 0
    freq = {}
    distinct = 0
    best = 0

    for right, ch in enumerate(s):
        if freq.get(ch, 0) == 0:
            distinct += 1
        freq[ch] = freq.get(ch, 0) + 1

        while distinct > k:
            out = s[left]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]
                distinct -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

Example:

```python
longest_at_most_k_distinct("eceba", 2)  # 3
longest_at_most_k_distinct("aa", 1)  # 2
```

### 3) Value -> Index (Last Seen Jump Optimization)

```python
def longest_unique_last_seen(s):
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best
```

Example:

```python
longest_unique_last_seen("abcabcbb")  # 3
longest_unique_last_seen("pwwkew")  # 3
```

### 4) At Most Conversion (Exactly K Distinct Subarrays)

```python
def subarrays_with_k_distinct(nums, k):
    def at_most(t):
        if t < 0:
            return 0
        left = 0
        freq = {}
        distinct = 0
        total = 0

        for right, x in enumerate(nums):
            if freq.get(x, 0) == 0:
                distinct += 1
            freq[x] = freq.get(x, 0) + 1

            while distinct > t:
                y = nums[left]
                freq[y] -= 1
                if freq[y] == 0:
                    del freq[y]
                    distinct -= 1
                left += 1

            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)
```

Example:

```python
subarrays_with_k_distinct([1, 2, 1, 2, 3], 2)  # 7
subarrays_with_k_distinct([1, 2, 1, 3, 4], 3)  # 3
```

## Complexity

Let:

- `n` = number of input elements.
- `u` = number of distinct elements tracked in window state.

Per-operation cost:

- Pointer move/update/rollback: `O(1)`.
- Hash map frequency updates: average `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| longest/shortest valid window with monotonic shrink | `O(n)` | `O(u)` |
| sum-based variable window (positive numbers) | `O(n)` | `O(1)` |
| at most `k` distinct count | `O(n)` | `O(u)` |
| exactly `k` via atMost difference | `O(n)` | `O(u)` |
| last-seen index optimization | `O(n)` | `O(u)` |

Interview note:

- Emphasize that each pointer moves forward at most `n` times.
- Mention limits: monotonic sum logic usually needs non-negative values.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: length, count, indices, string, or list.
- No-solution behavior is explicit and correct (`0`, `-1`, `[]`, or `""`).
- If prompt asks minimum length, ensure "not found" return is correct.
- If indices/window bounds are required, verify inclusive/exclusive conventions.

### Data-Rule Checks

- Validity condition is explicit and tested in exactly one place.
- Shrink loop uses `while`, not `if`, when multiple removals may be needed.
- State rollback mirrors add logic exactly (count decrement/delete, sum rollback).
- For distinct count, zero-frequency keys are removed consistently.
- For last-seen maps, outdated indices (`< left`) are ignored correctly.

### Input Boundary Checks

- Empty input and single-element input are handled safely.
- `k = 0` and `k < 0` behavior is explicit where relevant.
- All-equal and all-unique inputs are both handled correctly.
- Large input does not accidentally trigger nested rescans.
- For sum constraints, confirm assumptions about negative values.

### Pattern-Specific Checks

- Window is valid after each shrink phase.
- Answer update timing matches objective:
  longest -> after window valid, shortest -> inside valid loop.
- At-most counting adds `right - left + 1` after repair.
- Exactly-`k` counting uses `atMost(k) - atMost(k - 1)` when applicable.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| empty input | `s=""` | returns defined default without crash |
| duplicate repair | `s="abba"` | longest unique length is `2` |
| at most distinct | `s="eceba", k=2` | longest valid length is `3` |
| min-size sum (positive) | `nums=[2,3,1,2,4,3], target=7` | minimum length is `2` |
| exactly-k distinct count | `[1,2,1,2,3], k=2` | count is `7` |

## Common Pitfalls

- Shrinking once with `if` instead of repeatedly with `while`.
- Updating answer before restoring window validity.
- Forgetting to rollback outgoing state (sum/count/distinct) correctly.
- Applying sum-based variable window on arrays with negative numbers without proof.
- Confusing "at most K" and "exactly K" counting logic.

## When Not Ideal

- If window size is fixed, fixed-size sliding window is simpler.
- If values can be negative and condition is sum-based monotonicity, this pattern may fail.
- If prompt is non-contiguous subset/combination, use backtracking/DP/greedy instead.
- If many offline range queries are needed, prefix sums/segment trees may be better.

## Variations

- Longest Substring Without Repeating Characters.
- Minimum Window Substring.
- Longest Repeating Character Replacement.
- Minimum Size Subarray Sum.
- Subarrays with At Most/Exactly K Distinct.
- Fruit Into Baskets.

## Interview Tips

- Use this 20-second opener:
  "I will use a variable sliding window with two pointers. I expand right to include candidates, and when constraint breaks I shrink left until window is valid again."
- Say the invariant out loud:
  "After the shrink loop, my window is valid."
- Clarify objective timing:
  longest update after repair, shortest update while valid.
- For exact counts, call out conversion:
  `exactly(K) = atMost(K) - atMost(K-1)`.
- Mention complexity reasoning:
  each pointer advances monotonically, so total movement is linear.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why variable window here? | Constraint depends on current content, so fixed size is not known in advance. |
| Why is this `O(n)`? | Each index is added once by `right` and removed at most once by `left`. |
| Why `while` shrink, not `if`? | One removal may not restore validity; we must repair fully before using window. |
| When do you update answer? | After repair for longest-valid, or during valid phase for shortest-valid. |
| Does this work with negative numbers for sum constraints? | Not always; monotonic sum-shrink logic usually assumes non-negative values. |
| How to do exactly `k` distinct count? | Compute `atMost(k) - atMost(k-1)`. |
| What is your state contract? | Explicitly define map/counters so add and remove are symmetric. |
| Most common bug? | Mismatch between incoming update and outgoing rollback causing stale state. |
| Can memory be reduced? | Some variants are `O(1)` (sum only); frequency-based variants need `O(u)`. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Longest Substring Without Repeating Characters

Problem:

- Given string `s`, return the length of the longest substring without repeated characters.

What interviewer is testing:

- Can you maintain validity invariant (`no duplicates`)?
- Can you shrink correctly on conflicts?
- Can you explain linear pointer movement clearly?

#### What to Say in First 30 Seconds

Use this script:

"Brute force checks all substrings, which is quadratic or worse.  
I will use a variable window with character frequency.  
I expand right, and while a character count exceeds `1`, I move left and decrement counts.  
After repair, window is valid and I update best length. This is `O(n)` time."

#### Solution A: Brute Force

Idea:

- Enumerate every start/end and test uniqueness with a set.

```python
def longest_unique_bruteforce(s):
    n = len(s)
    best = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)

    return best
```

Complexity:

- Time `O(n^2)`, Space `O(u)`.

#### Solution B: Last-Seen with Backward Recheck

Idea:

- Move right and keep last seen index, but with less clean pointer discipline.

```python
def longest_unique_mid(s):
    last = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last:
            left = max(left, last[ch] + 1)
        last[ch] = right
        best = max(best, right - left + 1)

    return best
```

Complexity:

- Time `O(n)`, Space `O(u)`.

Interviewer tradeoff answer:

- "This is already optimal; frequency-based shrink and last-seen jump are both valid linear approaches."

#### Solution C: Variable Window Frequency (Canonical)

Idea:

- Maintain freq map and shrink while duplicate exists.

```python
def longest_unique_optimal(s):
    left = 0
    freq = {}
    best = 0

    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1

        while freq[ch] > 1:
            out = s[left]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]
            left += 1

        best = max(best, right - left + 1)

    return best
```

Complexity:

- Time `O(n)`, Space `O(u)`.

What to say while solving with interviewer:

1. "Window invariant is all chars have count <= 1."
2. "If violated, shrink until restored."
3. "Update best after window becomes valid."
4. "I will test `abcabcbb`, `bbbbb`, and empty string."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why shrink loop required? | Multiple removals may be needed to eliminate duplicate. |
| Could set work instead of map? | Yes for this problem; map generalizes better to count-based constraints. |
| Why linear time? | `left` and `right` each move forward at most `n` steps. |

### 2) Minimum Size Subarray Sum (Positive Numbers)

Problem:

- Given positive integer array `nums` and target `target`, return minimal length of a contiguous subarray whose sum is at least `target`. Return `0` if none.

What interviewer is testing:

- Can you switch objective from longest to shortest correctly?
- Can you update answer inside the valid loop?
- Can you state the positivity assumption explicitly?

#### What to Say in First 30 Seconds

Use this script:

"Brute force checks all starts and ends in `O(n^2)`.  
Because all numbers are positive, expanding right only increases sum and shrinking left decreases it.  
So I use variable window: expand to reach `sum >= target`, then shrink as much as possible while still valid to minimize length.  
This gives `O(n)` time and `O(1)` space."

#### Solution A: Brute Force

Idea:

- Try each start index and extend until reaching target.

```python
def min_len_bruteforce(target, nums):
    n = len(nums)
    best = n + 1

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s >= target:
                best = min(best, j - i + 1)
                break

    return 0 if best == n + 1 else best
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Prefix Sum + Binary Search

Idea:

- Prefix sums are increasing (positive nums), so binary search next valid end.

```python
import bisect

def min_len_prefix_bs(target, nums):
    n = len(nums)
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)

    best = n + 1
    for i in range(n):
        want = prefix[i] + target
        j = bisect.bisect_left(prefix, want, i + 1)
        if j <= n:
            best = min(best, j - i)

    return 0 if best == n + 1 else best
```

Complexity:

- Time `O(n log n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "This is correct but slower and higher memory than direct variable window for positive arrays."

#### Solution C: Variable Window (Optimal)

Idea:

- Expand until valid, then shrink aggressively to get shortest valid window.

```python
def min_len_optimal(target, nums):
    left = 0
    window_sum = 0
    best = float("inf")

    for right, x in enumerate(nums):
        window_sum += x

        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else best
```

Complexity:

- Time `O(n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "I rely on positive numbers for monotonic sum behavior."
2. "When sum is valid, I shrink to minimize length before moving right again."
3. "Answer update happens inside the `while window_sum >= target` loop."
4. "I will test `[2,3,1,2,4,3], target=7`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why does positivity matter? | With negatives, shrinking may increase sum unpredictably; monotonic repair breaks. |
| Why update inside while loop? | We need shortest valid window ending at current `right`. |
| What if no valid window exists? | Return `0` per prompt contract. |
