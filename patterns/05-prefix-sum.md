# Pattern 05: Prefix Sum

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need repeated range aggregates or subarray counts based on cumulative totals |
| Main tradeoff | Extra memory for precomputed cumulative state to get faster queries |
| Typical runtime | `O(n)` preprocessing, then `O(1)` range query / `O(n)` single-scan counting |
| Main structures | prefix array (`n+1`), running prefix scalar, hash map (`prefix -> freq/index`) |
| Common prompts | range sum query, subarray sum `= k`, longest subarray with target sum, equal 0/1 balance |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 05 Top 10 Questions Playbook](./questions/05-prefix-sum-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Prefix (exclusive):
prefix[0] = 0
prefix[i + 1] = prefix[i] + nums[i]

Range sum:
sum(l..r) = prefix[r + 1] - prefix[l]

Counting mode:
curr += x
ans += freq[curr - k]
freq[curr] += 1
```

### Read-the-Question Trigger Cues

- Many queries on contiguous ranges after one preprocessing pass.
- Prompt asks for count/length of subarrays with sum/property.
- Brute force keeps recomputing overlapping sums.
- Negative values break simple sliding-window sum logic, but prefix-hash still works.

### Intuition Anchor

- "Any range can be turned into difference of two checkpoints."

### 3-Second Pattern Check

- Can I rewrite `sum(l..r)` as `f(r) - f(l-1)`?
- Can I track previous cumulative values to convert subarray conditions into lookup?
- Would preprocessing once remove repeated scanning work?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| many static range sum queries | prefix array | `i -> sum of first i elements` | `prefix[r+1]-prefix[l]` |
| count subarrays sum `k` | hash frequency | `prefix_sum -> count` | add `freq[curr-k]` |
| longest subarray sum `k` | first-index map | `prefix_sum -> earliest index` | `i - first[curr-k]` |
| divisible-by-`k` subarray | remainder map | `remainder -> earliest index` | repeat remainder implies divisible range |
| equal 0/1 balance | transformed prefix | `balance -> earliest index` | repeated balance gives zero-sum span |
| 2D rectangle sum | 2D prefix matrix | `(r,c) -> area prefix` | inclusion-exclusion in `O(1)` |

## Universal Invariant

Before coding, say this sentence out loud:

- "At index `i`, my prefix state represents exactly the cumulative value up to `i`, and my map/array stores prefixes with a precise policy (frequency or first index) from earlier positions only."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`0`, `[]`, `False`, or `-1`).
2. Pick representation: full prefix array (many queries) or running prefix + hash (single scan).
3. Seed base case (`prefix[0] = 0`, and often `freq[0] = 1` or `first[0] = -1`).
4. Iterate left to right and update current prefix.
5. Query needed prior prefix/remainder (`curr - k`, same remainder, same balance).
6. Update map with chosen policy (increment frequency or keep first index).
7. Return accumulated answer.

Fill-in template:

```python
def solve(nums, k):
    ans = ...
    curr = 0
    table = {0: ...}  # base case by contract

    for i, x in enumerate(nums):
        curr += x

        need = ...  # curr - k / curr % k / curr itself
        if need in table:
            use_hit_to_update_answer()

        update_table_with_curr(curr, i)

    return ans
```

## Query/Update Order Rules

### A) Query, then update (most common)

Use for counting subarrays where current prefix should match only earlier prefixes.

```python
for x in nums:
    curr += x
    ans += freq.get(curr - k, 0)   # query past prefixes
    freq[curr] = freq.get(curr, 0) + 1  # update with current prefix
```

### B) Update while building, then query later

Use for many offline range queries.

```python
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)   # update build phase

# query phase
range_sum = prefix[r + 1] - prefix[l]
```

### C) Two-pass (transform then prefix-match)

Use when input needs transformation before prefix logic (for example `0 -> -1`).

```python
arr = [-1 if x == 0 else 1 for x in nums]  # pass 1
curr = 0
first = {0: -1}
for i, x in enumerate(arr):                # pass 2
    curr += x
    if curr in first:
        best = max(best, i - first[curr])
    else:
        first[curr] = i
```

## Detailed Example (Subarray Sum Equals K)

**Input:** `nums = [1, 1, 1], k = 2`

1. Start with `freq = {0: 1}`, `curr = 0`, `ans = 0`.
2. Read first `1`: `curr = 1`, need `-1`, no hit, set `freq[1] = 1`.
3. Read second `1`: `curr = 2`, need `0`, hit `1` time, `ans = 1`, set `freq[2] = 1`.
4. Read third `1`: `curr = 3`, need `1`, hit `1` time, `ans = 2`.
5. Return `2`.

Why it works: each subarray ending at current index is counted by how many earlier prefixes equal `curr - k`.

## Reusable Python Templates

### 1) Membership (Zero-Sum Subarray Exists)

```python
def has_zero_sum_subarray(nums):
    seen = {0}
    curr = 0

    for x in nums:
        curr += x
        if curr in seen:
            return True
        seen.add(curr)

    return False
```

Example:

```python
has_zero_sum_subarray([4, 2, -3, 1, 6])  # True
has_zero_sum_subarray([1, 2, 3])  # False
```

### 2) Frequency Count (Count Subarrays Sum = K)

```python
def count_subarrays_sum_k(nums, k):
    freq = {0: 1}
    curr = 0
    ans = 0

    for x in nums:
        curr += x
        ans += freq.get(curr - k, 0)
        freq[curr] = freq.get(curr, 0) + 1

    return ans
```

Example:

```python
count_subarrays_sum_k([1, 1, 1], 2)  # 2
count_subarrays_sum_k([1, -1, 0], 0)  # 3
```

### 3) Value -> Index (Longest Subarray Sum = K)

```python
def longest_subarray_sum_k(nums, k):
    first = {0: -1}  # prefix -> earliest index
    curr = 0
    best = 0

    for i, x in enumerate(nums):
        curr += x
        need = curr - k
        if need in first:
            best = max(best, i - first[need])
        if curr not in first:  # keep earliest occurrence only
            first[curr] = i

    return best
```

Example:

```python
longest_subarray_sum_k([1, -1, 5, -2, 3], 3)  # 4
longest_subarray_sum_k([-2, -1, 2, 1], 1)  # 2
```

### 4) Prefix Array (Range Sum Query - Immutable)

```python
def build_prefix(nums):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return prefix

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

Example:

```python
p = build_prefix([2, 4, 6, 8])
range_sum(p, 1, 3)  # 18
range_sum(p, 0, 0)  # 2
```

## Complexity

Let:

- `n` = number of input elements.
- `q` = number of range queries.
- `u` = number of unique prefix values stored (`u <= n + 1`).

Per-operation cost:

- Prefix arithmetic update/query: `O(1)`.
- Hash map lookup/insert for prefix state: average `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| build prefix + answer `q` range queries | `O(n + q)` | `O(n)` |
| count subarrays sum `k` | `O(n)` | `O(u)` |
| longest subarray sum `k` (first index map) | `O(n)` | `O(u)` |
| divisible-by-`k` remainder map | `O(n)` | `O(min(n, |k|))` |
| 2D prefix matrix build + query | `O(R*C)` build, `O(1)` query | `O(R*C)` |

Interview note:

- Distinguish preprocessing cost from per-query cost.
- Mention average-case hash behavior caveat briefly when relevant.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: count, length, boolean, range value, or indices.
- No-solution behavior is explicit and correct (`0`, `False`, `[]`, or `-1`).
- Query bounds are interpreted correctly (`left/right` inclusive vs exclusive).
- If length is required, verify index arithmetic (`i - j`, `r - l + 1`) is correct.

### Data-Rule Checks

- Prefix definition is consistent throughout (`prefix[i]` means sum of first `i` elements).
- Base seed is correct (`freq[0] = 1` or `first[0] = -1`).
- Query/update order is intentional (usually query before update for counting).
- First-index maps do not overwrite earliest occurrence when longest length is needed.
- Remainder handling is normalized for negative totals when language requires it.

### Input Boundary Checks

- Empty input and single-element input are handled safely.
- All-zero/all-equal arrays are handled.
- Negative numbers and zero are handled correctly (prefix-hash should still work).
- Very large sums avoid overflow if language type can overflow.
- Large `n` does not trigger accidental nested-loop recomputation.

### Pattern-Specific Checks

- Range query uses `prefix[right + 1] - prefix[left]` exactly.
- Counting subarrays seeds `freq` with `{0: 1}`.
- Longest-length variants seed `first` with `{0: -1}`.
- Exactly-`k` style count uses frequency, not simple membership.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| empty input | `[]` | returns defined default without crash |
| subarray starts at index 0 | `[2,1], k=3` | counted due to base seed |
| negatives present | `[1,-1,0], k=0` | counts all valid subarrays |
| longest sum target | `[1,-1,5,-2,3], k=3` | longest length is `4` |
| range query boundaries | `left=right` | returns single element value |

## Common Pitfalls

- Mixing inclusive/exclusive indexing and using wrong prefix difference formula.
- Forgetting base seed (`freq[0] = 1` or `first[0] = -1`).
- Updating map before querying and accidentally counting invalid self cases.
- Overwriting earliest prefix index in longest-length variants.
- Using variable sliding window for sum problems with negatives when prefix-hash is required.

## When Not Ideal

- If there is only one range query, full prefix array may be unnecessary.
- If array updates interleave with queries, use Fenwick/segment tree instead of immutable prefix array.
- If operation is non-associative, prefix subtraction trick may not apply directly.
- If memory is very tight and queries are few, on-demand computation may be acceptable.

## Variations

- 2D prefix sums for rectangle queries.
- Prefix XOR for XOR-range conditions.
- Remainder prefix for divisible subarray problems.
- Balance transforms (e.g., `0 -> -1`) for equal-category counts.
- Difference arrays for range updates + one final prefix sweep.

## Interview Tips

- Use this 20-second opener:
  "I will convert subarray operations into prefix differences, so each query/check becomes constant-time arithmetic or hash lookup."
- State your prefix contract before coding:
  "`prefix[i]` is sum of first `i` elements (exclusive indexing)."
- Call out base case explicitly:
  "I seed `0` prefix so subarrays starting at index `0` are handled."
- Mention update order:
  "I query with current prefix first, then store it."
- Before finishing, run one normal and one edge test:
  a standard case plus one with negatives or start-at-zero subarray.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why prefix sum here? | It converts repeated range calculations to subtraction of cumulative checkpoints. |
| Why `n+1` prefix length? | `prefix[0]=0` simplifies formulas and handles ranges starting at index `0`. |
| Why seed `freq[0]=1`? | It counts subarrays whose sum equals target starting from the first element. |
| Why query before update? | We need matches from earlier prefixes only in counting formulations. |
| How does this handle negatives? | Prefix-hash works regardless of sign because it relies on exact cumulative differences. |
| Why keep earliest index only? | Earliest occurrence gives longest span when computing lengths. |
| What if there are many updates too? | Immutable prefix is not ideal; use Fenwick/segment tree. |
| What is complexity? | Usually `O(n)` scan with `O(u)` map space, or `O(n+q)` for build + query. |
| Most common bug? | Indexing and seed mistakes (`prefix` alignment or missing base case). |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Subarray Sum Equals K (Count)

Problem:

- Given `nums` and integer `k`, return the number of contiguous subarrays whose sum equals `k`.

What interviewer is testing:

- Can you derive prefix-difference condition?
- Do you use frequency map correctly?
- Do you handle negatives (where sliding window often fails)?

#### What to Say in First 30 Seconds

Use this script:

"Brute force checks all start/end pairs in `O(n^2)`.  
I will maintain running prefix sum and a map `prefix -> frequency`.  
At each index, prior prefixes equal to `curr-k` indicate subarrays ending here with sum `k`.  
I add that count to answer, then record current prefix. This is `O(n)` average."

#### Solution A: Brute Force

Idea:

- Try each start, grow end, and track running sum.

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

#### Solution B: Prefix Array + Pair Check

Idea:

- Build prefix array, then compare all `(i, j)` prefix differences.

```python
def subarray_sum_prefix_pairs(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if prefix[j] - prefix[i] == k:
                ans += 1

    return ans
```

Complexity:

- Time `O(n^2)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Prefix array simplifies range-sum calculation but still compares all pairs; hash on prefix frequencies removes that quadratic pairing."

#### Solution C: Prefix Sum + Hash Frequency (Optimal)

Idea:

- One pass with frequency of prior prefix sums.

```python
def subarray_sum_optimal(nums, k):
    freq = {0: 1}
    curr = 0
    ans = 0

    for x in nums:
        curr += x
        ans += freq.get(curr - k, 0)
        freq[curr] = freq.get(curr, 0) + 1

    return ans
```

Complexity:

- Time `O(n)` average, Space `O(u)`.

What to say while solving with interviewer:

1. "Map meaning is `prefix_sum -> frequency seen so far`."
2. "I seed `{0:1}` to count windows that start at index `0`."
3. "I query first (`curr-k`), then update with `curr`."
4. "I will test with `[1,1,1], k=2` and `[1,-1,0], k=0`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why frequency map, not set? | Same prefix can appear multiple times, each giving additional valid subarrays. |
| Does this work with negatives? | Yes. It depends on exact prefix differences, not monotonicity. |
| Key bug to avoid? | Missing base seed `{0:1}` or wrong query/update order. |

### 2) Contiguous Array (Equal 0 and 1)

Problem:

- Given binary array `nums`, return length of the longest contiguous subarray with equal number of `0`s and `1`s.

What interviewer is testing:

- Can you transform problem into zero-sum prefix?
- Can you use first-index map for longest span?
- Can you justify earliest-index preservation?

#### What to Say in First 30 Seconds

Use this script:

"I will map `0 -> -1` and `1 -> +1`.  
Then equal count of 0/1 means subarray sum is zero.  
I track running balance and the first index where each balance appears.  
When the same balance repeats at `i`, span from first occurrence+1 to `i` has sum zero; maximize length.  
This is linear time."

#### Solution A: Brute Force

Idea:

- Check all subarrays and compare zeros vs ones.

```python
def contiguous_array_bruteforce(nums):
    n = len(nums)
    best = 0

    for i in range(n):
        zeros = ones = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                best = max(best, j - i + 1)

    return best
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Prefix Array + Pair Scan

Idea:

- Build transformed prefix balances, then check repeated balance pairs.

```python
def contiguous_array_prefix_pairs(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + (1 if x == 1 else -1)

    best = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if prefix[i] == prefix[j]:
                best = max(best, j - i)

    return best
```

Complexity:

- Time `O(n^2)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Prefix exposes the balance idea, but without hashing it still compares too many pairs."

#### Solution C: Prefix Balance + First Index Map (Optimal)

Idea:

- Store earliest index for each running balance.

```python
def contiguous_array_optimal(nums):
    first = {0: -1}
    balance = 0
    best = 0

    for i, x in enumerate(nums):
        balance += 1 if x == 1 else -1

        if balance in first:
            best = max(best, i - first[balance])
        else:
            first[balance] = i

    return best
```

Complexity:

- Time `O(n)` average, Space `O(u)`.

What to say while solving with interviewer:

1. "Repeated balance means net sum between indices is zero."
2. "I keep earliest balance index for maximum span."
3. "Seed `balance=0` at index `-1` handles prefix windows."
4. "I will test `[0,1]` and `[0,1,0]`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why transform `0` to `-1`? | Equal 0/1 then becomes zero-sum subarray detection. |
| Why earliest index only? | Earliest occurrence creates the longest distance to current index. |
| What base case is needed? | `first[0] = -1` so a balanced prefix is counted correctly. |
