# Pattern 03: Sliding Window (Fixed Size)

## At a Glance

| Item | Summary |
|---|---|
| Use when | You must evaluate every contiguous segment of exact length `k` |
| Main tradeoff | Small extra state for each slide to avoid recomputing full window |
| Typical runtime | `O(n)` |
| Main structures | `left/right` pointers + rolling sum/count/frequency |
| Common prompts | max/min/avg sum of size `k`, anagram windows, distinct count per window |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 03 Top 10 Questions Playbook](./questions/03-sliding-window-fixed-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Build first exact window of size k.

left                              right
  v                                 v
[ a b c d e f g ]
    [window size = k]

Slide by 1 each step:
  add incoming at right + 1
  remove outgoing at left
  left += 1, right += 1
```

### Read-the-Question Trigger Cues

- Prompt explicitly gives fixed length `k`.
- Need answer over every contiguous block of exactly `k` elements/chars.
- Brute force would recalculate each block independently (`O(n*k)`).

### Intuition Anchor

- "Adjacent windows overlap by `k - 1` items, so I should reuse prior work."

### 3-Second Pattern Check

- Do I only care about windows of exact size `k`?
- Can I update window state using `+incoming` and `-outgoing`?
- Can each element enter and leave the window once?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| max/min/sum of size `k` | rolling numeric state | `window -> running_sum` | compare/update best |
| max average size `k` | rolling numeric state | `window -> running_sum` | `running_sum / k` |
| anagram/permutation windows | frequency arrays/maps | `char -> count delta` | is all delta zero? |
| distinct count per window | frequency map + counter | `value -> frequency` | current distinct count |
| fixed threshold windows | rolling state + count | `window -> metric` | metric meets threshold? |
| fixed binary feature count | rolling count | `window -> feature_count` | maximize count in size `k` |

## Universal Invariant

Before coding, say this sentence out loud:

- "When I evaluate answer at index `right`, my state represents exactly the current window `[right-k+1, right]` (or equivalent `left..right` with length `k`)."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`0`, `[]`, `False`, or `-1`).
2. Handle invalid size early (`k <= 0` or `k > n`, based on prompt contract).
3. Initialize rolling state (`window_sum`, `freq`, `distinct`, etc.).
4. Expand `right` one step and add incoming element to state.
5. If window length exceeds `k`, remove `nums[left]` from state and move `left`.
6. When window length equals `k`, query/update answer.
7. Return final answer after full scan.

Fill-in template:

```python
def solve(items, k):
    ans_default = ...
    if k <= 0 or k > len(items):
        return ans_default

    left = 0
    state = ...  # running sum / freq / distinct / etc.

    for right, x in enumerate(items):
        add_to_state(x)

        if right - left + 1 > k:
            remove_from_state(items[left])
            left += 1

        if right - left + 1 == k:
            use_state_to_update_answer()

    return final_answer_or_default()
```

## Query/Update Order Rules

### A) Add incoming, remove outgoing, then query (most common)

Use for rolling sums/counts where answer is based on the exact current window.

```python
for right, x in enumerate(nums):
    add(x)
    if window_too_large():
        remove(nums[left])
        left += 1
    if window_is_exactly_k():
        update_answer()
```

### B) Query after forming first full window, then slide by one

Use for imperative style where you seed first window explicitly.

```python
window_sum = sum(nums[:k])
best = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]
    best = max(best, window_sum)
```

### C) Two-pass (prepare target state, then scan windows)

Use when validity depends on a precomputed target (for example, anagram frequency).

```python
need = build_freq(pattern)  # pass 1: target
window = {}
for right, ch in enumerate(text):  # pass 2: rolling match
    add(window, ch)
    if right >= k:
        remove(window, text[right - k])
    if right + 1 >= k and window_matches_need(window, need):
        record_hit(right - k + 1)
```

## Detailed Example (Max Sum Subarray of Size K)

**Input:** `nums = [2, 1, 5, 1, 3, 2], k = 3`

1. Build first full window `[2, 1, 5]`, sum = `8`, best = `8`.
2. Slide: add `1`, remove `2` -> sum = `7`, best = `8`.
3. Slide: add `3`, remove `1` -> sum = `9`, best = `9`.
4. Slide: add `2`, remove `5` -> sum = `6`, best = `9`.
5. Return `9`.

Why it works: every size-`k` window is visited once, and each slide updates in `O(1)`.

## Reusable Python Templates

### 1) Membership (Window Contains Duplicate)

```python
def has_duplicate_in_any_window(nums, k):
    if k <= 1:
        return False

    left = 0
    freq = {}

    for right, x in enumerate(nums):
        freq[x] = freq.get(x, 0) + 1

        if right - left + 1 > k:
            y = nums[left]
            freq[y] -= 1
            if freq[y] == 0:
                del freq[y]
            left += 1

        if right - left + 1 == k and len(freq) < k:
            return True

    return False
```

Example:

```python
has_duplicate_in_any_window([1, 2, 3, 1], 3)  # False
has_duplicate_in_any_window([1, 2, 2, 3], 3)  # True
```

### 2) Frequency Count (Distinct in Every Window)

```python
def distinct_count_per_window(nums, k):
    if k <= 0 or k > len(nums):
        return []

    left = 0
    freq = {}
    out = []

    for right, x in enumerate(nums):
        freq[x] = freq.get(x, 0) + 1

        if right - left + 1 > k:
            y = nums[left]
            freq[y] -= 1
            if freq[y] == 0:
                del freq[y]
            left += 1

        if right - left + 1 == k:
            out.append(len(freq))

    return out
```

Example:

```python
distinct_count_per_window([1, 2, 1, 3, 4, 2, 3], 4)  # [3, 4, 4, 3]
distinct_count_per_window([4, 4, 4], 2)  # [1, 1]
```

### 3) Value -> Index (Max Sum of Size K)

```python
def max_sum_k(nums, k):
    if k <= 0 or k > len(nums):
        return 0

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

Example:

```python
max_sum_k([2, 1, 5, 1, 3, 2], 3)  # 9
max_sum_k([1, -1, 5, -2, 3], 2)  # 4
```

### 4) Frequency Map + Sliding Window (Anagram Hits)

```python
def find_anagrams(s, p):
    k = len(p)
    if k > len(s):
        return []

    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    out = []

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1

        if right >= k:
            left_ch = s[right - k]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]

        if right + 1 >= k and window == need:
            out.append(right - k + 1)

    return out
```

Example:

```python
find_anagrams("cbaebabacd", "abc")  # [0, 6]
find_anagrams("abab", "ab")  # [0, 1, 2]
```

## Complexity

Let:

- `n` = number of input elements.
- `k` = fixed window length.
- `u` = unique items in a window (`u <= k`).

Per-operation cost:

- Add/remove/query rolling numeric state: `O(1)`.
- Add/remove/query hash frequency: average `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| rolling sum / max sum size `k` | `O(n)` | `O(1)` |
| max average size `k` | `O(n)` | `O(1)` |
| fixed-window frequency map | `O(n)` average | `O(u)` |
| fixed-window anagram check (map equality) | `O(n)` with fixed alphabet, up to `O(n*u)` otherwise | `O(u)` |
| fixed small alphabet (array frequency) | `O(n)` | `O(1)` |

Interview note:

- State that every element is added once and removed once.
- Mention average hash complexity caveat if using maps/sets.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: number, boolean, count, index list, or array.
- `k` boundary behavior is explicit (`k <= 0`, `k > n`, `k == n`).
- Output format is correct (start indices, not substrings, when required).
- If prompt asks maximum value and all numbers are negative, default handling is correct.

### Data-Rule Checks

- Window state always matches exact current window content.
- Incoming update and outgoing rollback are symmetric.
- Frequency map deletes zero-count keys if distinct count matters.
- For strings, case and charset assumptions match prompt.
- Equality check strategy for maps/arrays is consistent with constraints.

### Input Boundary Checks

- Empty input and single-element input are handled safely.
- `k = 1` behavior is correct.
- `k = n` produces exactly one evaluated window.
- Repeated elements are handled without count drift.
- Large `n` does not trigger accidental `O(n*k)` recomputation.

### Pattern-Specific Checks

- Answer is updated only when window length is exactly `k`.
- Outgoing element is removed before/after update in correct order for your invariant.
- No stale values remain in window state after left pointer moves.
- For anagram problems, compare frequencies only after full window forms.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| `k > n` | `nums=[1,2], k=3` | returns prompt-defined default |
| single full window | `nums=[2,5,1], k=3` | evaluates exactly once |
| duplicate-heavy window | `nums=[1,1,1,1], k=2` | state remains consistent |
| negative values | `nums=[-2,-1,-3], k=2` | max sum logic still works |
| anagram hits overlap | `s="abab", p="ab"` | returns `[0,1,2]` |

## Common Pitfalls

- Off-by-one errors in window length checks.
- Updating answer before removing overflow element (or vice versa) inconsistently.
- Recomputing each window from scratch and losing linear complexity.
- Forgetting to decrement/delete outgoing frequency.
- Applying fixed-window logic when window size should vary.

## When Not Ideal

- If window size is not fixed and depends on validity, use variable sliding window.
- If prompt asks non-contiguous subsets, this pattern does not apply.
- If each query is independent offline, prefix sums/segment trees may be cleaner.

## Variations

- Maximum average subarray of size `k`.
- Find all anagrams/permutations in string windows.
- Distinct element count in every window.
- Maximum vowels in substring length `k`.
- Sliding window maximum (often combined with deque).

## Interview Tips

- Use this 20-second opener:
  "Because `k` is fixed, I can maintain one rolling window and update by adding the new element and removing the outgoing one, so total work is linear."
- State window invariant before coding:
  "At each step, state represents exactly the current size-`k` window."
- Say update order explicitly:
  "I add incoming, evict outgoing if needed, then read answer when length is `k`."
- Mention complexity reason:
  "Each index enters and exits once, so time is `O(n)`."
- Before finishing, run two quick tests:
  one normal case and one edge case (`k > n`, all negatives, or repeated chars).

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why sliding window here? | Every answer depends on contiguous blocks of fixed size `k`; adjacent blocks overlap, so reuse avoids `O(n*k)`. |
| Why is this `O(n)`? | Each element is added once and removed once; no nested re-scan per window. |
| What is your invariant? | State matches exactly one current size-`k` window at all times. |
| When do you update answer? | Only when window length is exactly `k`. |
| What if `k > n`? | Return prompt-defined default early. |
| What breaks most often? | Off-by-one on window length and forgetting outgoing rollback. |
| How do you handle duplicates? | Use frequency map and decrement/delete on eviction. |
| Does this work with negative numbers? | Yes for fixed-size windows; unlike variable sum windows, no monotonicity is required. |
| Can we reduce space? | For numeric rolling sum, space is `O(1)`; frequency variants need `O(u)`. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Maximum Sum Subarray of Size K

Problem:

- Given `nums` and integer `k`, return the maximum sum among all contiguous subarrays of length `k`.

What interviewer is testing:

- Can you identify fixed-size overlap and avoid recomputation?
- Can you maintain invariant and window length correctly?
- Can you handle boundaries (`k > n`, negatives)?

#### What to Say in First 30 Seconds

Use this script:

"Brute force would compute each length-`k` sum separately in `O(n*k)`.  
Because windows overlap, I will maintain a rolling sum.  
At each step I add the incoming value, remove the outgoing value when size exceeds `k`, and update best when size is exactly `k`.  
This gives `O(n)` time and `O(1)` extra space."

#### Solution A: Brute Force

Idea:

- Try every start index and sum next `k` values.

```python
def max_sum_bruteforce(nums, k):
    if k <= 0 or k > len(nums):
        return 0

    best = float("-inf")
    for start in range(0, len(nums) - k + 1):
        s = 0
        for j in range(start, start + k):
            s += nums[j]
        best = max(best, s)
    return best
```

Complexity:

- Time `O(n*k)`, Space `O(1)`.

#### Solution B: Prefix Sum Array

Idea:

- Build prefix sums and compute each window in `O(1)`.

```python
def max_sum_prefix(nums, k):
    if k <= 0 or k > len(nums):
        return 0

    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)

    best = float("-inf")
    for start in range(0, len(nums) - k + 1):
        s = prefix[start + k] - prefix[start]
        best = max(best, s)

    return best
```

Complexity:

- Time `O(n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Prefix sums give linear time but still use `O(n)` memory; rolling window keeps linear time with `O(1)` space."

#### Solution C: Sliding Window (Optimal)

Idea:

- Keep one rolling sum of current size-`k` window.

```python
def max_sum_optimal(nums, k):
    if k <= 0 or k > len(nums):
        return 0

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)

    return best
```

Complexity:

- Time `O(n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "My window is always exactly length `k`."
2. "Each slide adds one incoming and removes one outgoing."
3. "I evaluate best after every full window."
4. "I will test with `[2,1,5,1,3,2], k=3` and negative-heavy input."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why not nested loops? | Nested recomputes overlap work and is `O(n*k)`; rolling reuse is linear. |
| Why is window sum update valid? | Adjacent windows differ by exactly one outgoing and one incoming value. |
| What about all negatives? | Initialize best from first valid window, not from `0`. |

### 2) Find All Anagrams in a String

Problem:

- Given strings `s` and `p`, return start indices of substrings in `s` that are anagrams of `p`.

What interviewer is testing:

- Can you model fixed-size window with frequency state?
- Can you update counts symmetrically on slide?
- Can you avoid expensive per-window sorting?

#### What to Say in First 30 Seconds

Use this script:

"Window size is fixed to `len(p)`.  
Brute force sorting each window is expensive.  
I will keep rolling character frequencies for the current window and compare against target frequencies for `p`.  
Each step updates one incoming and one outgoing character, so scan is linear in `len(s)`."

#### Solution A: Brute Force (Sort Each Window)

Idea:

- For each window, sort and compare to sorted `p`.

```python
def find_anagrams_bruteforce(s, p):
    k = len(p)
    if k > len(s):
        return []

    target = sorted(p)
    out = []
    for i in range(len(s) - k + 1):
        if sorted(s[i:i + k]) == target:
            out.append(i)
    return out
```

Complexity:

- Time `O((n-k+1) * k log k)`, Space `O(k)`.

#### Solution B: Per-Window Frequency Rebuild

Idea:

- Rebuild frequency map for each window without sorting.

```python
def find_anagrams_rebuild_freq(s, p):
    k = len(p)
    if k > len(s):
        return []

    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1

    out = []
    for i in range(len(s) - k + 1):
        freq = {}
        for ch in s[i:i + k]:
            freq[ch] = freq.get(ch, 0) + 1
        if freq == need:
            out.append(i)
    return out
```

Complexity:

- Time `O((n-k+1) * k)`, Space `O(u)`.

Interviewer tradeoff answer:

- "Rebuilding map per window is better than sorting but still repeats work; rolling frequency removes that repetition."

#### Solution C: Fixed Sliding Window Frequency (Optimal)

Idea:

- Build target frequency once, maintain one rolling window frequency.

```python
def find_anagrams_optimal(s, p):
    k = len(p)
    if k > len(s):
        return []

    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    out = []

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1

        if right >= k:
            left_ch = s[right - k]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]

        if right + 1 >= k and window == need:
            out.append(right - k + 1)

    return out
```

Complexity:

- Time `O(n)` for fixed alphabet/optimized compare, or up to `O(n*u)` with generic map equality.
- Space `O(u)`.

What to say while solving with interviewer:

1. "Window length is fixed to pattern length `k`."
2. "I update counts for incoming/outgoing chars each step."
3. "I compare against target only when window is full."
4. "I will test overlapping hits like `s='abab', p='ab'`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why not sort each window? | Sorting each window is costly; rolling counts reuse prior window state. |
| Is map equality always `O(1)`? | Not in general; with fixed alphabet arrays it is constant-sized compare and practical linear total. |
| What bug appears most often? | Forgetting to remove/decrement outgoing char when window slides. |
