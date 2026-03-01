# Pattern 11: Monotonic Queue / Deque

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need max/min or best candidate over a moving window with strict `O(n)` target |
| Main tradeoff | Extra deque state for fast updates; must handle expiry and comparator direction carefully |
| Typical runtime | `O(n)` amortized |
| Main structures | deque of indices in monotonic value (or prefix) order |
| Common prompts | sliding window maximum/minimum, shortest subarray sum >= `k` (prefix deque), constrained DP windows |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 11 Top 10 Questions Playbook](./questions/11-monotonic-queue-deque-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Window max (decreasing deque of indices):

left ... right
  |      |
[ ... current window ... ]

Deque operations each step:
1) expire: pop front if index < left
2) dominate: pop back while nums[back] <= nums[right]
3) push current index at back
4) answer at front (best in window)
```

### Read-the-Question Trigger Cues

- Need max/min for every moving window.
- Prompt asks strict linear time where heap approach may be too slow or messy.
- Elements expire by index as window moves.
- Need "best so far among valid candidates" with frequent insert/remove.

### Intuition Anchor

- "Deque stores only candidates that can still win future windows."

### 3-Second Pattern Check

- Do candidates expire by position as window moves?
- Can weaker candidates be safely removed when a better one arrives?
- Is each index added once and removed at most once?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| max of each fixed window | decreasing deque | index -> value | front is window max |
| min of each fixed window | increasing deque | index -> value | front is window min |
| shortest subarray sum >= `k` | increasing deque of prefix indices | index -> prefix sum | pop front while condition met |
| constrained DP best in last `k` | decreasing deque on DP values | index -> dp[index] | front gives best prior dp |
| threshold existence in windows | monotonic deque + check | index -> candidate value | window best >= threshold? |
| window-boundary index reporting | deque of indices | index positions | return `dq[0]` instead of value |

## Universal Invariant

Before coding, say this sentence out loud:

- "After processing index `i`, deque indices are valid for current constraints and ordered so front is always the best candidate for the current window/prefix rule."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write default return first (`[]`, `0`, `False`, or `-1`).
2. Decide deque direction:
   decreasing for max, increasing for min, increasing prefix for shortest sum.
3. Iterate index `i` left to right.
4. Evict expired indices from deque front.
5. Pop dominated indices from deque back using comparator.
6. Push current index.
7. Read answer from deque front when window/condition is valid.

Fill-in template:

```python
from collections import deque

def solve(nums, k):
    dq = deque()  # store indices
    out = []

    for i, x in enumerate(nums):
        while dq and expired(dq[0], i, k):
            dq.popleft()

        while dq and dominated(nums[dq[-1]], x):
            dq.pop()

        dq.append(i)

        if window_ready(i, k):
            out.append(read_answer(nums, dq[0]))

    return out
```

## Query/Update Order Rules

### A) Expire front, remove dominated back, push, then query (most common)

Use for sliding window max/min.

```python
for i, x in enumerate(nums):
    while dq and dq[0] <= i - k:
        dq.popleft()
    while dq and nums[dq[-1]] <= x:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        ans.append(nums[dq[0]])
```

### B) Prefix-deque: pop front for valid answer, pop back for monotonicity

Use for shortest subarray sum at least `k`.

```python
for i in range(len(prefix)):
    while dq and prefix[i] - prefix[dq[0]] >= k:
        ans = min(ans, i - dq.popleft())
    while dq and prefix[dq[-1]] >= prefix[i]:
        dq.pop()
    dq.append(i)
```

### C) Two-pass DP window optimization

Use when transition depends on best value in recent range.

```python
for i in range(n):
    best_prev = dp[dq[0]] if dq else 0
    dp[i] = nums[i] + max(0, best_prev)
    while dq and dq[0] < i - k + 1:
        dq.popleft()
    while dq and dp[dq[-1]] <= dp[i]:
        dq.pop()
    dq.append(i)
```

## Detailed Example (Sliding Window Maximum)

**Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`

1. Build first window with decreasing deque indices (`[1]` value `3` dominates `1`).
2. For each new index, evict expired front indices (`<= i-k`).
3. Pop smaller/equal values from back before pushing current index.
4. Once `i >= k-1`, front index gives max for current window.
5. Output becomes `[3, 3, 5, 5, 6, 7]`.

Why it works: deque keeps only undominated valid candidates; front is always best among current window indices.

## Reusable Python Templates

### 1) Membership (Any Window Max >= Threshold)

```python
from collections import deque

def any_window_max_at_least(nums, k, threshold):
    if k <= 0 or k > len(nums):
        return False

    dq = deque()  # decreasing values by index

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        if i >= k - 1 and nums[dq[0]] >= threshold:
            return True

    return False
```

Example:

```python
any_window_max_at_least([1, 3, -1, -3, 5], 3, 5)  # True
any_window_max_at_least([1, 2, 1], 2, 3)  # False
```

### 2) Boundary Index (Window Max Index Per Window)

```python
from collections import deque

def sliding_window_max_indices(nums, k):
    if k <= 0 or k > len(nums):
        return []

    dq = deque()
    out = []

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        if i >= k - 1:
            out.append(dq[0])

    return out
```

Example:

```python
sliding_window_max_indices([1,3,-1,-3,5], 3)  # [1, 1, 4]
sliding_window_max_indices([9, 8, 7], 2)  # [0, 1]
```

### 3) Value -> Index (Sliding Window Maximum Values)

```python
from collections import deque

def sliding_window_max(nums, k):
    if k <= 0 or k > len(nums):
        return []

    dq = deque()  # decreasing values by index
    out = []

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        if i >= k - 1:
            out.append(nums[dq[0]])

    return out
```

Example:

```python
sliding_window_max([1,3,-1,-3,5,3,6,7], 3)  # [3,3,5,5,6,7]
sliding_window_max([4,2,12,3], 2)  # [4,12,12]
```

### 4) Prefix Sum + Monotonic Deque (Shortest Subarray >= K)

```python
from collections import deque

def shortest_subarray_at_least_k(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x

    dq = deque()  # increasing prefix values by index
    best = n + 1

    for i in range(n + 1):
        while dq and prefix[i] - prefix[dq[0]] >= k:
            best = min(best, i - dq.popleft())
        while dq and prefix[dq[-1]] >= prefix[i]:
            dq.pop()
        dq.append(i)

    return best if best <= n else -1
```

Example:

```python
shortest_subarray_at_least_k([2, -1, 2], 3)  # 3
shortest_subarray_at_least_k([1, 2], 4)  # -1
```

## Complexity

Let:

- `n` = number of elements.
- `k` = window size for fixed-window variants.

Per-operation cost:

- Deque push/pop from either end: `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| sliding window max/min | `O(n)` amortized | `O(k)` |
| existence/threshold in fixed window | `O(n)` amortized | `O(k)` |
| shortest subarray sum >= `k` (prefix deque) | `O(n)` amortized | `O(n)` |
| constrained subsequence sum (DP + deque) | `O(n)` amortized | `O(n)` |
| heap alternative for max window | `O(n log k)` | `O(k)` |

Interview note:

- Amortized linearity: each index is appended once and removed at most once.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: values, indices, count, length, or boolean.
- Invalid window size behavior is explicit (`k <= 0`, `k > n`).
- Not-found behavior is correct (for example `-1` for shortest-subarray problems).
- If indices are required, return indices not values.

### Data-Rule Checks

- Deque stores indices, not raw values, when expiry by position is needed.
- Expiration step occurs before reading answer.
- Comparator strictness (`<` vs `<=`) matches duplicate semantics.
- Deque monotonic direction matches objective (max vs min).
- Prefix deque maintains monotonic prefix values for shortest-subarray logic.

### Input Boundary Checks

- Empty and single-element arrays handled safely.
- `k = 1` and `k = n` produce correct results.
- All-equal arrays and strictly monotonic arrays handled.
- Negative values handled where relevant (prefix-deque variant).
- Large `n` does not degrade to nested rescans.

### Pattern-Specific Checks

- Sliding-window variant evicts `dq[0] <= i - k`.
- Result is read only when window is full (`i >= k-1`).
- Prefix variant pops front while condition holds to minimize length.
- Prefix variant pops back to keep prefix values increasing.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| `k > n` | `nums=[1,2], k=3` | returns prompt-defined default |
| fixed window max sample | standard LeetCode sample | `[3,3,5,5,6,7]` |
| all equal | `[2,2,2], k=2` | stable outputs with correct comparator |
| shortest-subarray possible | `[2,-1,2], k=3` | returns `3` |
| shortest-subarray impossible | `[1,2], k=4` | returns `-1` |

## Common Pitfalls

- Storing values instead of indices, making expiry impossible.
- Reading answer before evicting expired front index.
- Wrong comparator strictness causing duplicate mis-handling.
- Mixing decreasing/increasing deque direction.
- Using this pattern where no moving-validity or best-candidate structure exists.

## When Not Ideal

- No sliding/online candidate maintenance is needed (simple prefix/sort may be simpler).
- Need arbitrary order-statistics (median/percentile) rather than max/min.
- Updates and queries are dynamic in both directions (segment tree/multiset may be better).
- Tiny constraints where `O(n log k)` heap is acceptable and simpler to reason about.

## Variations

- Sliding window minimum.
- Constrained Subsequence Sum (deque over DP).
- Shortest Subarray with Sum at Least K.
- Max value in each k-sized subarray with index outputs.
- Monotonic deques over transformed prefix/DP states.

## Interview Tips

- Use this 20-second opener:
  "I’ll maintain a deque of candidate indices so expired and dominated elements are removed, and front always gives the best valid answer."
- State invariant explicitly:
  indices are valid for current window and monotonic by value/prefix.
- Mention operation order:
  expire front -> remove dominated back -> push current -> read front.
- Clarify comparator choice for duplicates.
- State amortized proof:
  each index enters and exits deque once.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why deque instead of heap? | Deque gives strict `O(1)` amortized updates and direct expiry without lazy deletion overhead. |
| Why store indices? | Needed for expiry checks and distance/boundary calculations. |
| Why does this run in `O(n)`? | Every index is appended once and popped at most once. |
| Which comparator do you use with duplicates? | For max window typically pop `<=` to keep newest representative; adjust by prompt needs. |
| Why this operation order? | Expiry must happen before reading answer, and dominated candidates must be removed before push. |
| Can this handle negatives? | Yes for max/min windows; prefix-deque variant is specifically useful with negatives. |
| When does deque fail? | If objective is not monotonic best-candidate (for example median), use different data structure. |
| What is the key invariant? | Deque front is always best valid candidate for current state. |
| Most common bug? | Off-by-one window expiry (`i-k`) and wrong comparator strictness. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Sliding Window Maximum

Problem:

- Given `nums` and `k`, return maximum value in every contiguous subarray of size `k`.

What interviewer is testing:

- Can you maintain valid candidate set under expiry?
- Can you remove dominated values correctly?
- Can you explain amortized linear complexity?

#### What to Say in First 30 Seconds

Use this script:

"Brute force recomputes max per window in `O(n*k)`.  
I will use a decreasing deque of indices.  
For each step I evict expired indices, pop smaller or equal values from back, push current index, and read front once window is full.  
This gives `O(n)` amortized time."

#### Solution A: Brute Force

Idea:

- For each window, scan all `k` elements for max.

```python
def max_window_bruteforce(nums, k):
    if k <= 0 or k > len(nums):
        return []

    out = []
    for i in range(len(nums) - k + 1):
        out.append(max(nums[i:i + k]))
    return out
```

Complexity:

- Time `O(n*k)`, Space `O(1)` extra.

#### Solution B: Heap with Lazy Deletion

Idea:

- Use max-heap of `(-value, index)`, discard stale top indices.

```python
import heapq

def max_window_heap(nums, k):
    if k <= 0 or k > len(nums):
        return []

    heap = []
    out = []

    for i, x in enumerate(nums):
        heapq.heappush(heap, (-x, i))
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        if i >= k - 1:
            out.append(-heap[0][0])

    return out
```

Complexity:

- Time `O(n log k)`, Space `O(k)`.

Interviewer tradeoff answer:

- "Heap is acceptable, but deque removes lazy deletion overhead and reaches strict linear time."

#### Solution C: Monotonic Deque (Optimal)

Idea:

- Keep deque decreasing by value; front is current window maximum.

```python
from collections import deque

def max_window_optimal(nums, k):
    if k <= 0 or k > len(nums):
        return []

    dq = deque()
    out = []

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        if i >= k - 1:
            out.append(nums[dq[0]])

    return out
```

Complexity:

- Time `O(n)` amortized, Space `O(k)`.

What to say while solving with interviewer:

1. "Deque stores only indices that can still be max candidates."
2. "Front expiry enforces window validity."
3. "Back pops enforce decreasing order."
4. "Front always gives current maximum."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why pop `<=` from back? | Newer equal value lasts longer in future windows, so older equal can be dropped. |
| Why read after push? | We need current index included before reporting current window max. |
| Can this be done with values only? | Not safely; indices are required for expiry. |

### 2) Shortest Subarray with Sum at Least K

Problem:

- Given array `nums` (can include negatives) and `k`, return shortest non-empty subarray length with sum at least `k`, else `-1`.

What interviewer is testing:

- Can you combine prefix sums with monotonic deque?
- Can you handle negatives where normal sliding-window sum fails?
- Can you minimize length by repeated front pops?

#### What to Say in First 30 Seconds

Use this script:

"With negatives, variable sliding window is not monotonic, so classic two pointers can fail.  
I will use prefix sums and a deque of prefix indices with increasing prefix values.  
For current prefix `P[i]`, while `P[i] - P[dq.front] >= k`, I update shortest length and pop front.  
Then I maintain increasing deque by popping larger prefixes from back.  
This yields `O(n)` amortized."

#### Solution A: Brute Force

Idea:

- Check all subarrays and track shortest with sum >= `k`.

```python
def shortest_subarray_bruteforce(nums, k):
    n = len(nums)
    best = n + 1

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s >= k:
                best = min(best, j - i + 1)
                break

    return best if best <= n else -1
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Prefix Array + Pair Scan

Idea:

- Build prefix sums and compare prefix differences for all pairs.

```python
def shortest_subarray_prefix_pairs(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x

    best = n + 1
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if prefix[j] - prefix[i] >= k:
                best = min(best, j - i)
                break

    return best if best <= n else -1
```

Complexity:

- Time `O(n^2)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Prefix math simplifies sum checks, but without deque we still compare too many pairs."

#### Solution C: Prefix + Monotonic Deque (Optimal)

Idea:

- Maintain deque of candidate prefix indices with increasing prefix values.

```python
from collections import deque

def shortest_subarray_optimal(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x

    dq = deque()
    best = n + 1

    for i in range(n + 1):
        while dq and prefix[i] - prefix[dq[0]] >= k:
            best = min(best, i - dq.popleft())
        while dq and prefix[dq[-1]] >= prefix[i]:
            dq.pop()
        dq.append(i)

    return best if best <= n else -1
```

Complexity:

- Time `O(n)` amortized, Space `O(n)`.

What to say while solving with interviewer:

1. "Deque keeps prefix sums increasing."
2. "Front pops give shortest valid length for current end."
3. "Back pops remove dominated larger prefixes."
4. "This handles negatives correctly."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why increasing prefix in deque? | Smaller prefix is always better for achieving larger difference with shorter future index. |
| Why pop front in a loop? | Multiple starts may form valid sums; later pops can yield even shorter length. |
| Why normal sliding window fails here? | Negative values break monotonic sum behavior during shrink/expand. |
