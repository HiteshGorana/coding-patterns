# Pattern 01: Hash Map / Set Lookup

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need fast lookup on values/states seen before |
| Main tradeoff | `O(n)` extra memory for faster runtime |
| Typical runtime | `O(n)` average |
| Main structures | `set` for membership, `map` for counts/indices/state |
| Common prompts | duplicate, frequency, first unique, pair sum, anagram |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 01 Top 10 Questions Playbook](./questions/01-hash-map-set-lookup-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Choose structure:
  set() for "seen?"
  map() for "how many/where/what state?"

for each element x at index i:
  1) query hash using the key you need
  2) use result (return/update answer)
  3) update hash with current element/state
```

### Read-the-Question Trigger Cues

- "contains duplicate", "count frequency", "first unique", "find pair", "seen before"
- Brute force would rescan earlier elements or compare many pairs.
- A left-to-right scan is possible if you remember prior state.

### Intuition Anchor

- "I need memory of what I have seen so far."

### 3-Second Pattern Check

- Can `value -> count/index/state` remove repeated scans?
- Can average `O(1)` lookup turn `O(n^2)` into `O(n)`?
- Do I only need information from earlier elements?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| duplicate/presence | `set` | `x` | `x in seen` |
| frequency/count | `map` | `x -> count` | `freq[x]` |
| pair/complement (Two Sum) | `map` | `x -> index` | `need in index_of` |
| first/last position | `map` | `x -> first_or_last_index` | use overwrite policy |
| subarray sum = `k` | `map` | `prefix_sum -> frequency` | `(prefix-k) in map` |
| grouping (anagrams) | `map` | `signature -> list` | append bucket |

## Universal Invariant

Before coding, say this sentence out loud:

- "At step `i`, my hash stores exactly the information I decided from already-processed elements (or from the current window, if this is sliding window)."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`False`, `[]`, `0`, or `-1`).
2. Create hash with one clear meaning comment.
3. Loop left to right.
4. Build the query key (`x`, `target - x`, `prefix - k`, signature, etc.).
5. Query hash and use result (return/update answer).
6. Update hash with current element/state.
7. Return the default if no hit happened.

Fill-in template:

```python
def solve(items):
    ans_default = ...
    table = {}  # key -> meaning

    for i, x in enumerate(items):
        key = ...  # what you need to query

        if key in table:
            return ...  # or update running answer

        # update after query (most common)
        table[...] = ...

    return ans_default
```

## Query/Update Order Rules

### A) Query, then update (most common)

Use for Two Sum and duplicate detection when self-reuse is illegal.

```python
for x in nums:
    if needed_info_in_hash(x):
        return answer
    update_hash(x)
```

### B) Update, then query (window/state variants)

Use when the current element must be included before validity check.

```python
for x in stream:
    update_hash(x)
    if now_valid_or_invalid():
        adjust_answer_or_window()
```

### C) Two-pass (count then select)

Use when selection depends on global counts (first unique character).

```python
for x in items:
    freq[x] = freq.get(x, 0) + 1
for i, x in enumerate(items):
    if freq[x] == 1:
        return i
```

## Detailed Example (Two Sum)

**Input:** `nums = [2, 7, 11, 15], target = 9`

1. `index_of = {}`
2. `x=2`, `need=7` not found, store `index_of[2] = 0`
3. `x=7`, `need=2` found at `0`
4. Return `[0, 1]`

Why it works: each step checks complements among prior elements only, so no index is reused.

## Reusable Python Templates

### 1) Membership (Contains Duplicate)

```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

Example:

```python
contains_duplicate([1, 2, 3, 1])  # True
contains_duplicate([1, 2, 3, 4])  # False
```

### 2) Frequency Count (Anagram/Mode/Counts)

```python
def build_freq(items):
    freq = {}
    for x in items:
        freq[x] = freq.get(x, 0) + 1
    return freq
```

Example:

```python
build_freq("aabca")  # {'a': 3, 'b': 1, 'c': 1}
build_freq([4, 4, 2])  # {4: 2, 2: 1}
```

### 3) Value -> Index (Two Sum style)

```python
def two_sum(nums, target):
    index_of = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index_of:
            return [index_of[need], i]
        index_of[x] = i
    return []
```

Example:

```python
two_sum([2, 7, 11, 15], 9)  # [0, 1]
two_sum([3, 2, 4], 6)  # [1, 2]
```

### 4) Prefix Sum + Hash Map (Subarray Sum Equals K)

```python
def count_subarrays_sum_k(nums, k):
    prefix_count = {0: 1}  # empty prefix
    prefix = 0
    ans = 0

    for x in nums:
        prefix += x
        ans += prefix_count.get(prefix - k, 0)
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    return ans
```

Example:

```python
count_subarrays_sum_k([1, 1, 1], 2)  # 2
count_subarrays_sum_k([1, -1, 0], 0)  # 3
```

## Complexity

Let:

- `n` = number of input elements.
- `u` = number of unique keys inserted into hash (`u <= n`).

Per-operation cost:

- Hash lookup/insert/delete: average `O(1)`, worst-case `O(n)` (pathological collisions).

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| membership (`set`) | `O(n)` | `O(u)` |
| frequency map | `O(n)` | `O(u)` |
| Two Sum (`value -> index`) | `O(n)` | `O(u)` |
| prefix-sum hash map | `O(n)` | `O(u)` |
| two-pass count + select | `O(n)` | `O(u)` |

Interview note:

- State average-case complexity as above.
- Mention worst-case hash behavior only as a caveat: total can degrade toward `O(n^2)` if each hash op is `O(n)`.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: boolean, index pair, count, value, or list.
- No-solution behavior is explicit and correct (`[]`, `-1`, `False`, or `0`).
- If indices are required, you return indices (not values).
- If 1-based indexing is required, convert before returning.

### Data-Rule Checks

- Self-reuse rule is respected (same element cannot be used twice unless allowed).
- Duplicate handling matches problem semantics (presence vs frequency).
- Overwrite policy is intentional (keep first index vs keep latest index).
- For strings, case handling is correct (case-sensitive unless prompt says otherwise).
- For strings, normalization assumptions are explicit (letters only vs any character).

### Input Boundary Checks

- Empty input and single-element input are handled safely.
- All-equal input is handled (for example `[5, 5, 5]`).
- All-unique input is handled (no false positives).
- Negative numbers and zero are handled where relevant.
- Large `n` does not trigger accidental `O(n^2)` logic.

### Pattern-Specific Checks

- Two Sum style: query complement before insert to avoid self-match bugs.
- Prefix-sum style: seed map with `{0: 1}` when counting subarrays.
- Prefix-sum style: use frequency map, not just membership map.
- First-unique style: use two-pass approach when global counts are needed.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| empty input | `[]` | returns defined default without crash |
| duplicate exists | `[1, 2, 1]` | duplicate detector returns `True` |
| no duplicate | `[1, 2, 3]` | duplicate detector returns `False` |
| self-reuse trap | `nums=[3, 3], target=6` | returns two different indices |
| negatives/zero in prefix sum | `[1, -1, 0], k=0` | counts all valid subarrays |

## Common Pitfalls

- Using `set` when multiplicity is required.
- Updating hash too early and accidentally using current element against itself.
- Overwriting first occurrence when question needs earliest index.
- Forgetting to seed prefix hash with `{0: 1}` for subarray-sum count.
- Returning values when prompt asks indices.

## When Not Ideal

- If data is sorted and relation is monotonic, Two Pointers may be simpler.
- If values are from a tiny fixed range, array counting can be faster and smaller.
- If memory is very constrained, sort + scan (`O(n log n)`, lower extra space) may be preferred.

## Variations

- Frequency equality: Valid Anagram, Ransom Note.
- Signature buckets: Group Anagrams.
- Last-seen index: Longest Substring Without Repeating Characters.
- Prefix hash: Subarray Sum Equals K, equal 0/1 count variants.
- Sliding window + counts: permutation/anagram windows.

## Interview Tips

- Use this 20-second opener:
  "Brute force is `O(n^2)` because we rescan previous elements. I will store `key -> state` in a hash table so each step is constant-time on average."
- Say key/value meaning before coding:
  "Map stores `value -> index`" or "Map stores `prefix_sum -> frequency`."
- Say the loop invariant explicitly:
  "Before processing index `i`, hash contains information from already-processed elements."
- Call out update order out loud:
  "I will query first, then update, to avoid self-match bugs."
- While coding, narrate only decision points:
  key computed -> lookup hit/miss -> update action.
- Before finishing, run 2 quick tests verbally:
  one normal case and one edge case (empty/single/duplicate/self-reuse).
- Close with complexity in one line:
  "Time `O(n)` average, space `O(u)`; worst-case hash collisions are a caveat."

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why hash map/set here instead of brute force? | Brute force rescans prior elements (`O(n^2)`); hash stores prior state so lookups are average `O(1)` and total is `O(n)`. |
| Why query before update? | To avoid self-match/self-reuse bugs in complement problems like Two Sum. |
| What exactly does your map store? | State the contract clearly: `value -> index`, `char -> count`, or `prefix_sum -> frequency`. |
| What happens with duplicates? | Define policy: keep first index, keep latest index, or track frequency. |
| What is the space tradeoff? | Extra memory is `O(u)` unique keys for faster runtime. |
| Can this fail in worst case? | Theoretical caveat: pathological hash collisions can degrade operation cost. |
| How would this work on streaming input? | Keep updating the same hash incrementally per new element. |
| What if memory is tight? | Consider sort + scan or bounded-range array counting when constraints allow. |
| Which edge case breaks this most often? | Self-reuse bug, wrong default return, or missing prefix seed `{0: 1}`. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Two Sum (Return Indices)

Problem:

- Given `nums` and `target`, return indices of two numbers that sum to target.

What interviewer is testing:

- Can you move from brute force to better complexity?
- Can you define hash map contract clearly?
- Can you avoid self-reuse bugs by correct query/update order?

#### What to Say in First 30 Seconds

Use this script:

"I will start with brute force pair checking, which is `O(n^2)`.  
To optimize, I will store `value -> index` in a hash map while scanning once.  
At each index, I compute `need = target - x`, query first, then update map to avoid self-reuse.  
This gives `O(n)` average time with `O(n)` extra space."

#### Solution A: Brute Force

Idea:

- Try every pair `(i, j)` with `i < j`.

```python
def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Sort + Two Pointers (with index recovery)

Idea:

- Sort `(value, index)` pairs, then use two pointers.

```python
def two_sum_sorted(nums, target):
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

Complexity:

- Time `O(n log n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "This improves brute force but sorting costs `n log n`; we can do linear average with hash map."

#### Solution C: Hash Map (Optimal for this prompt)

Idea:

- Store `value -> index` for elements seen so far.
- For each `x`, query complement `target - x` first, then insert `x`.

```python
def two_sum_optimal(nums, target):
    index_of = {}

    for i, x in enumerate(nums):
        need = target - x
        if need in index_of:
            return [index_of[need], i]
        index_of[x] = i

    return []
```

Complexity:

- Time `O(n)` average, Space `O(u)` (worst `O(n)`).

What to say while solving with interviewer:

1. "Map meaning is `value -> index of earlier element`."
2. "I must query before update to avoid matching the same element."
3. "If interviewer asks about duplicates: latest overwrite is fine here because any valid pair works."
4. "I will test with `[2,7,11,15], 9` and `[3,3], 6`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why not update first? | Could cause self-match in some variants; query-first is safer for complement lookup. |
| What if no solution exists? | Return prompt-defined default, usually `[]` or `[-1, -1]`. |
| Why hash map over two pointers? | Two pointers needs sorting, which adds `O(n log n)` and may complicate index semantics. |

### 2) Subarray Sum Equals K (Count Subarrays)

Problem:

- Given `nums` and `k`, return count of continuous subarrays with sum exactly `k`.

What interviewer is testing:

- Do you know prefix sum transformation?
- Can you use frequency map, not only membership?
- Do you remember the seed case `{0: 1}`?

#### What to Say in First 30 Seconds

Use this script:

"Brute force checks every subarray, so it is `O(n^2)`.  
I will use prefix sum plus a hash map of frequencies: `prefix_sum -> count`.  
For each position, subarrays ending here with sum `k` are counted by prior `prefix - k`.  
I seed `{0: 1}` to count subarrays starting at index `0`, giving `O(n)` average time."

#### Solution A: Brute Force

Idea:

- Fix start index and expand end index while tracking running sum.

```python
def subarray_sum_bruteforce(nums, k):
    n = len(nums)
    ans = 0

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s == k:
                ans += 1

    return ans
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Prefix Array (still quadratic queries)

Idea:

- Precompute prefix sums so range sum is `prefix[j+1] - prefix[i]`.
- Still checks all pairs `(i, j)`.

```python
def subarray_sum_prefix_array(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    ans = 0
    for i in range(n):
        for j in range(i, n):
            if prefix[j + 1] - prefix[i] == k:
                ans += 1

    return ans
```

Complexity:

- Time `O(n^2)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Prefix array simplifies range-sum math but still compares all ranges; we need hash on prefix frequencies for linear average."

#### Solution C: Prefix Sum + Hash Map Frequency (Optimal)

Idea:

- Let current prefix sum be `p`.
- Any earlier prefix sum `p - k` forms a subarray ending here with sum `k`.
- Add frequency of `p - k` to answer.

```python
def subarray_sum_optimal(nums, k):
    prefix_freq = {0: 1}
    prefix = 0
    ans = 0

    for x in nums:
        prefix += x
        ans += prefix_freq.get(prefix - k, 0)
        prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1

    return ans
```

Complexity:

- Time `O(n)` average, Space `O(u)` (worst `O(n)`).

What to say while solving with interviewer:

1. "Map meaning is `prefix_sum -> count of times seen`."
2. "I seed `{0: 1}` so subarrays starting at index `0` are counted."
3. "This must be frequency, not set membership, because multiple starts may exist."
4. "I will test with `[1,1,1], k=2` and `[1,-1,0], k=0`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why store counts instead of boolean presence? | Same prefix can appear multiple times; each occurrence creates additional valid subarrays. |
| Does this work with negatives? | Yes. Unlike sliding window, prefix-hash does not require monotonic sums. |
| What is the key bug to avoid? | Forgetting seed `{0: 1}` or using set instead of frequency map. |
