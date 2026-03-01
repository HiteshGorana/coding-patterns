# Pattern 06: Binary Search (Index Space)

## At a Glance

| Item | Summary |
|---|---|
| Use when | Data is sorted (or index predicate is monotonic) and you need position/threshold quickly |
| Main tradeoff | Very fast `O(log n)` time, but boundary/invariant mistakes cause subtle bugs |
| Typical runtime | `O(log n)` |
| Main structures | index interval (`left`, `right`), midpoint `mid`, comparison/predicate |
| Common prompts | exact index, first/last occurrence, lower/upper bound, insert position |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 06 Top 10 Questions Playbook](./questions/06-binary-search-index-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Inclusive interval form:

left                 mid                right
  v                   v                    v
[ .... candidates .... .... candidates .... ]

comparison at mid decides one half to discard:
  nums[mid] < target  -> discard left half incl. mid
  nums[mid] > target  -> discard right half incl. mid
  equal               -> return or tighten (bound search)
```

### Read-the-Question Trigger Cues

- Input is sorted or can be treated as monotonic by index.
- Prompt asks for position/first/last/insertion boundary.
- Brute force scan is too slow for large `n`.
- You can prove one side of midpoint cannot contain the answer.

### Intuition Anchor

- "After each comparison, I keep only the half that can still be correct."

### 3-Second Pattern Check

- Is there a monotonic condition across indices?
- Can I eliminate half the remaining indices each step?
- Can I state exactly what interval still contains the answer?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| exact target index | inclusive interval | `index -> nums[index] vs target` | equality / less / greater |
| first index `>= target` | half-open interval | `index -> nums[index] >= target` | first true |
| first index `> target` | half-open interval | `index -> nums[index] > target` | upper bound |
| last index `<= target` | derived from upper bound | `index -> nums[index] > target` | `upper_bound - 1` |
| search insert position | lower bound | `index -> nums[index] >= target` | insertion index |
| index threshold by predicate | boolean predicate | `index -> pred(index)` | first/last true boundary |

## Universal Invariant

Before coding, say this sentence out loud:

- "At every step, my current interval contains all possible valid answers, and every discarded index is proven impossible."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write default return first (`-1`, `n`, or `[ -1, -1 ]` by prompt).
2. Choose one interval model and stay consistent:
   inclusive `[left, right]` or half-open `[left, right)`.
3. Compute midpoint safely: `mid = left + (right - left) // 2`.
4. Query comparison/predicate at `mid`.
5. Shrink interval with strict progress (`left = mid + 1`, `right = mid - 1`, or `right = mid`).
6. Stop when loop condition fails (`left > right` or `left == right`).
7. Validate boundary and return prompt-defined result.

Fill-in template:

```python
def solve(nums, target):
    ans_default = ...
    left, right = 0, len(nums) - 1  # or right = len(nums) for half-open

    while left <= right:  # or while left < right
        mid = left + (right - left) // 2
        state = compare_or_check(nums[mid], target)

        if hit(state):
            return ...
        if go_right(state):
            left = mid + 1
        else:
            right = mid - 1

    return ans_default
```

## Query/Update Order Rules

### A) Query, then shrink toward target (exact match)

Use for classic exact-index search.

```python
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### B) Query predicate, keep first-true half (lower bound)

Use for first index satisfying a monotonic predicate.

```python
left, right = 0, len(nums)  # [left, right)
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] >= target:  # predicate true
        right = mid
    else:
        left = mid + 1
```

### C) Two-pass boundary search (first + last occurrence)

Use when duplicates require full range.

```python
first = lower_bound(nums, target)          # first >= target
last_plus_one = lower_bound(nums, target + 1)  # first > target (int case)
last = last_plus_one - 1
```

## Detailed Example (Lower Bound / Insert Position)

**Input:** `nums = [1, 3, 3, 5, 7], target = 3`

1. Start half-open interval: `left = 0`, `right = 5`.
2. `mid = 2`, `nums[2] = 3` satisfies `>= target`, move `right = 2`.
3. `mid = 1`, `nums[1] = 3` satisfies, move `right = 1`.
4. `mid = 0`, `nums[0] = 1` does not satisfy, move `left = 1`.
5. Stop at `left == right == 1`, return index `1`.

Why it works: binary search converges on the first index where predicate becomes true.

## Reusable Python Templates

### 1) Membership (Exact Index Search)

```python
def binary_search_exact(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Example:

```python
binary_search_exact([1, 3, 5, 7], 5)  # 2
binary_search_exact([1, 3, 5, 7], 4)  # -1
```

### 2) First Index >= Target (Lower Bound)

```python
def lower_bound(nums, target):
    left, right = 0, len(nums)  # [left, right)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

Example:

```python
lower_bound([1, 3, 3, 5], 3)  # 1
lower_bound([1, 3, 3, 5], 4)  # 3
```

### 3) First and Last Position (Duplicates)

```python
def search_range(nums, target):
    def lb(x):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= x:
                right = mid
            else:
                left = mid + 1
        return left

    first = lb(target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = lb(target + 1) - 1
    return [first, last]
```

Example:

```python
search_range([5, 7, 7, 8, 8, 10], 8)  # [3, 4]
search_range([5, 7, 7, 8, 8, 10], 6)  # [-1, -1]
```

### 4) First True in Index Predicate

```python
def first_true_index(n, pred):
    left, right = 0, n  # search [0, n)

    while left < right:
        mid = left + (right - left) // 2
        if pred(mid):
            right = mid
        else:
            left = mid + 1

    return left  # n means no true index
```

Example:

```python
arr = [1, 2, 4, 9, 16]
first_true_index(len(arr), lambda i: arr[i] >= 9)  # 3
first_true_index(len(arr), lambda i: arr[i] >= 20)  # 5
```

## Complexity

Let:

- `n` = number of sorted elements.
- `q` = number of independent binary-search queries.

Per-operation cost:

- Midpoint computation and comparison/predicate check: `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| exact index search | `O(log n)` | `O(1)` |
| lower/upper bound | `O(log n)` | `O(1)` |
| first + last position (two bound searches) | `O(log n)` | `O(1)` |
| `q` independent index queries | `O(q log n)` | `O(1)` |
| recursive implementation | `O(log n)` | `O(log n)` call stack |

Interview note:

- Mention iterative `O(1)` space unless using recursion.
- Explicitly state bound-search variant when duplicates are present.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: index, boundary, pair, or insertion position.
- Not-found behavior is explicit and correct (`-1`, `n`, or `[-1, -1]`).
- If insertion index is requested, return valid index in `[0, n]`.
- If first/last occurrence is requested, duplicates are handled correctly.

### Data-Rule Checks

- Sorted/monotonic assumption is valid and stated.
- Interval model is consistent from start to finish (`[l,r]` vs `[l,r)`).
- Midpoint update always guarantees progress (no infinite loops).
- Predicate is monotonic (false...false true...true or inverse).
- Boundary verification after loop is correct (`left < n`, value check).

### Input Boundary Checks

- Empty array is handled safely.
- Single-element and two-element arrays return correct answers.
- Target less than smallest and greater than largest are handled.
- All-equal arrays and duplicate-heavy arrays behave correctly.
- Large `n` still avoids overflow-prone midpoint formulas in strict languages.

### Pattern-Specific Checks

- Exact match uses `left <= right` with inclusive boundaries.
- Lower bound uses half-open interval and returns first valid index.
- Upper bound/last occurrence derived correctly from lower-bound logic.
- Search-range problem runs two boundary searches, not linear expansion.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| empty input | `nums=[]` | returns defined default without crash |
| target exists once | `[1,3,5], target=3` | returns index `1` |
| target absent middle | `[1,3,5], target=4` | returns not-found/insert index |
| duplicate range | `[2,2,2,2], target=2` | first=`0`, last=`3` |
| outside bounds | `[10,20], target=5` | lower bound returns `0` |

## Common Pitfalls

- Mixing inclusive and half-open interval rules in one function.
- Using wrong loop condition (`<` vs `<=`) for chosen interval model.
- Failing to move boundaries past `mid`, causing infinite loops.
- Returning `left` without validating value for exact-match problems.
- Handling duplicates with exact search when first/last bound was required.

## When Not Ideal

- Data is unsorted and cannot be transformed to monotonic order.
- Predicate is not monotonic across index space.
- Input size is tiny and linear scan is simpler with equal practical performance.
- Frequent inserts/deletes are interleaved with queries (tree/indexed structures may fit better).

## Variations

- Search insert position.
- First/last occurrence (lower/upper bound pair).
- Search in rotated sorted array.
- Peak finding in mountain/bitonic arrays.
- Sparse/implicit index spaces with predicate APIs.

## Interview Tips

- Use this 20-second opener:
  "Because the data is sorted/monotonic, I can compare at midpoint and discard half each step, giving `O(log n)`."
- Declare variant before coding:
  exact match, lower bound, upper bound, or first/last range.
- State interval invariant explicitly:
  "Answer is always inside my current interval."
- Keep one interval model only:
  either inclusive `[left, right]` or half-open `[left, right)`.
- Before finishing, test mentally:
  empty, one element, duplicates, and out-of-range target.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why binary search here? | Sorted/monotonic structure lets us eliminate half the candidates per comparison. |
| Which variant are you implementing? | Exact index or boundary search (first `>=`, first `>`, first/last occurrence). |
| Why this loop condition? | It matches my interval model and guarantees convergence without skipping candidates. |
| How do you avoid infinite loops? | Every branch strictly moves `left` or `right` past `mid` (or shrinks to `mid` in half-open lower bound). |
| How do you handle duplicates? | Use lower/upper bounds; exact match alone does not guarantee first/last index. |
| What is midpoint formula? | `left + (right - left) // 2` to avoid overflow in strict integer languages. |
| Complexity? | `O(log n)` time, `O(1)` iterative space. |
| What if not found? | Return prompt-defined default (`-1`, insertion index, or range `[-1, -1]`). |
| What must be true for correctness? | Monotonic predicate and consistent interval invariant. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Search Insert Position

Problem:

- Given sorted `nums` and `target`, return index if found; otherwise return index where it should be inserted.

What interviewer is testing:

- Can you choose boundary-search variant instead of exact match?
- Can you return insertion boundary in `[0, n]` correctly?
- Can you reason about out-of-range values?

#### What to Say in First 30 Seconds

Use this script:

"This is a lower-bound problem: first index where `nums[i] >= target`.  
If target exists, that index is exact position; otherwise it is insertion point.  
I will use half-open binary search `[left, right)` for clean boundary handling.  
Time is `O(log n)` and space is `O(1)`."

#### Solution A: Linear Scan

Idea:

- Scan left to right and return first index with value `>= target`.

```python
def search_insert_linear(nums, target):
    for i, x in enumerate(nums):
        if x >= target:
            return i
    return len(nums)
```

Complexity:

- Time `O(n)`, Space `O(1)`.

#### Solution B: Library Lower Bound

Idea:

- Use standard library bisect if allowed.

```python
import bisect

def search_insert_bisect(nums, target):
    return bisect.bisect_left(nums, target)
```

Complexity:

- Time `O(log n)`, Space `O(1)`.

Interviewer tradeoff answer:

- "Library is concise and correct, but I can implement manually to show boundary-control skills."

#### Solution C: Manual Lower Bound (Optimal Interview Form)

Idea:

- Half-open interval with first true predicate `nums[mid] >= target`.

```python
def search_insert_optimal(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

Complexity:

- Time `O(log n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "Invariant: answer index is always in `[left, right)`."
2. "If `nums[mid]` can be answer, keep left half (`right = mid`)."
3. "Otherwise discard left half (`left = mid + 1`)."
4. "I will test target smaller than all and larger than all."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why return `left` at end? | In half-open lower bound, convergence index is first valid insertion position. |
| Why not inclusive interval? | Inclusive works too; half-open often makes boundary search cleaner. |
| What if all values are smaller? | Loop ends with `left == n`, valid insertion at end. |

### 2) Find First and Last Position of Element in Sorted Array

Problem:

- Given sorted `nums` and `target`, return `[first, last]` positions of target. If absent, return `[-1, -1]`.

What interviewer is testing:

- Can you distinguish exact-match vs boundary-search requirements?
- Can you implement duplicate-safe first/last logic?
- Can you avoid degenerating to linear scan?

#### What to Say in First 30 Seconds

Use this script:

"Exact binary search only finds one occurrence, not boundaries.  
I will run two lower-bound style searches: first `>= target`, then first `> target`.  
If first index is invalid or value mismatches, target is absent.  
Otherwise range is `[first, second-1]` in `O(log n)` time."

#### Solution A: Linear Range Scan

Idea:

- Scan array and record first/last target index.

```python
def search_range_linear(nums, target):
    first, last = -1, -1
    for i, x in enumerate(nums):
        if x == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
```

Complexity:

- Time `O(n)`, Space `O(1)`.

#### Solution B: Exact Hit + Expansion

Idea:

- Find one hit by binary search, then expand left/right.

```python
def search_range_expand(nums, target):
    left, right = 0, len(nums) - 1
    hit = -1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            hit = mid
            break
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if hit == -1:
        return [-1, -1]

    i, j = hit, hit
    while i - 1 >= 0 and nums[i - 1] == target:
        i -= 1
    while j + 1 < len(nums) and nums[j + 1] == target:
        j += 1
    return [i, j]
```

Complexity:

- Time `O(log n + m)` where `m` is duplicate span, worst `O(n)`.
- Space `O(1)`.

Interviewer tradeoff answer:

- "Expansion can degrade to linear with many duplicates; dual-bound binary search keeps strict `O(log n)`."

#### Solution C: Dual Bound Search (Optimal)

Idea:

- Reuse one `lower_bound` helper.

```python
def search_range_optimal(nums, target):
    def lower_bound(x):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= x:
                right = mid
            else:
                left = mid + 1
        return left

    first = lower_bound(target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = lower_bound(target + 1) - 1
    return [first, last]
```

Complexity:

- Time `O(log n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "I use lower bound to locate first possible target."
2. "I validate presence after first bound."
3. "Second bound gives first greater index, so last is minus one."
4. "I will test absent target and all-equal target arrays."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why two searches? | One gives left boundary, second gives exclusive right boundary; both are needed for duplicates. |
| Could exact search alone solve it? | Not reliably; exact search may land anywhere in duplicate block. |
| What if target absent? | Presence check after first bound handles it cleanly. |
