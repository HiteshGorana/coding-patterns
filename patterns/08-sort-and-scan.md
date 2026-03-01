# Pattern 08: Sort + Scan

## At a Glance

| Item | Summary |
|---|---|
| Use when | Sorting reveals local adjacency/order that makes one linear sweep sufficient |
| Main tradeoff | Pay `O(n log n)` sort cost to simplify logic and avoid pairwise brute force |
| Typical runtime | `O(n log n)` |
| Main structures | sorted array/list, sweep pointer, carry state (current merged range/group/count) |
| Common prompts | merge intervals, remove overlaps, meeting conflicts, dedupe/group runs, closest neighbors |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 08 Top 10 Questions Playbook](./questions/08-sort-and-scan-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
1) sort by the right key
2) scan once with carry state

sorted items:  a0, a1, a2, a3, ...
carry state:   current merged/group/answer-in-progress

for each next item:
  compare with carry
  merge/update if related
  otherwise flush carry and start new carry
```

### Read-the-Question Trigger Cues

- Intervals/conflicts/ordering where "what comes next" matters.
- Brute force compares many pairs/ranges.
- Output depends on global order, but adjacent relation after sort is enough.
- Prompt allows reordering (or only needs count/boolean/value unaffected by original order).

### Intuition Anchor

- "Sorting exposes structure; scanning consumes it deterministically."

### 3-Second Pattern Check

- After sorting, can I solve in one pass using only current and previous/carry state?
- Is there a natural comparison key and tie-break?
- Can I finalize processed prefix decisions without revisiting?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| merge overlapping intervals | sorted intervals + carry interval | current merged `[start,end]` | overlap with next? |
| minimum removals to avoid overlap | sort by end | last kept end | does current start conflict? |
| meeting room count (line sweep) | sorted starts + sorted ends | `used_rooms` / pointer to ended meetings | start < earliest end? |
| dedupe/group equal values | sorted array + run-length scan | `value -> run length` | boundary change? |
| closest neighbor metrics | sorted values | adjacent difference | update minimum gap |
| deterministic output ordering | sorted records | ordered prefix state | append or combine |

## Universal Invariant

Before coding, say this sentence out loud:

- "After processing position `i` in sorted order, every decision for elements before `i` is final, and my carry state exactly summarizes the active group/range still open."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`[]`, `0`, `False`, or `-1`).
2. Choose sort key and tie-break rule that matches prompt semantics.
3. Sort data (copy or in-place intentionally).
4. Initialize sweep/carry state from first element (or neutral state for empty input).
5. Scan left to right in sorted order.
6. Apply rule: merge/update count/flush-and-restart on boundary changes.
7. Return accumulated output/count.

Fill-in template:

```python
def solve(items):
    if not items:
        return ...

    items = sorted(items, key=lambda x: (...))
    out = []
    carry = init_from(items[0])

    for x in items[1:]:
        if can_merge_or_extend(carry, x):
            carry = merge_or_update(carry, x)
        else:
            out.append(carry)
            carry = init_from(x)

    out.append(carry)
    return out_or_count(out)
```

## Query/Update Order Rules

### A) Compare with carry, then merge or flush (most common)

Use for interval merge and run grouping.

```python
for item in sorted_items[1:]:
    if overlaps_or_same_group(carry, item):
        carry = combine(carry, item)
    else:
        output.append(carry)
        carry = item
```

### B) Sort by end, greedily keep best-so-far

Use for minimum removals / maximum non-overlapping selection.

```python
intervals.sort(key=lambda x: x[1])  # end time
kept = 0
last_end = -inf
for s, e in intervals:
    if s >= last_end:
        kept += 1
        last_end = e
```

### C) Two-pass event scan (starts and ends)

Use for room/concurrency counting.

```python
starts = sorted(s for s, e in intervals)
ends = sorted(e for s, e in intervals)
i = j = 0
while i < n:
    if starts[i] < ends[j]:
        rooms += 1
        i += 1
    else:
        rooms -= 1
        j += 1
```

## Detailed Example (Merge Intervals)

**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`

1. Sort by start: unchanged.
2. Carry starts as `[1,3]`.
3. Next `[2,6]` overlaps (`2 <= 3`), merge carry -> `[1,6]`.
4. Next `[8,10]` does not overlap (`8 > 6`), flush `[1,6]`, new carry `[8,10]`.
5. Next `[15,18]` does not overlap, flush `[8,10]`, new carry `[15,18]`.
6. Flush final carry -> result `[[1,6],[8,10],[15,18]]`.

Why it works: after sorting by start, all possible overlaps for current carry appear contiguously in scan order.

## Reusable Python Templates

### 1) Membership (Contains Duplicate via Sort)

```python
def contains_duplicate_sorted(nums):
    if len(nums) < 2:
        return False

    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

Example:

```python
contains_duplicate_sorted([1, 2, 3, 1])  # True
contains_duplicate_sorted([1, 2, 3, 4])  # False
```

### 2) Frequency Count (Run-Length Encoding)

```python
def run_length_counts(nums):
    if not nums:
        return []

    nums = sorted(nums)
    out = []
    curr = nums[0]
    cnt = 1

    for x in nums[1:]:
        if x == curr:
            cnt += 1
        else:
            out.append((curr, cnt))
            curr, cnt = x, 1

    out.append((curr, cnt))
    return out
```

Example:

```python
run_length_counts([4, 4, 2])  # [(2, 1), (4, 2)]
run_length_counts([1, 1, 1, 2, 3, 3])  # [(1, 3), (2, 1), (3, 2)]
```

### 3) Value -> Index (Sort Pairs, Keep Original Index)

```python
def closest_pair_original_indices(nums):
    if len(nums) < 2:
        return []

    arr = sorted((x, i) for i, x in enumerate(nums))
    best_gap = float("inf")
    best_pair = None

    for i in range(1, len(arr)):
        gap = arr[i][0] - arr[i - 1][0]
        if gap < best_gap:
            best_gap = gap
            best_pair = (arr[i - 1][1], arr[i][1])

    return list(best_pair)
```

Example:

```python
closest_pair_original_indices([8, 1, 5, 10])  # [2, 0] or [0, 2] (values 5 and 8)
closest_pair_original_indices([3, 3, 9])  # [0, 1]
```

### 4) Interval Merge (Canonical Sort + Scan)

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]

    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])

    return merged
```

Example:

```python
merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])  # [[1, 6], [8, 10], [15, 18]]
merge_intervals([[1, 4], [4, 5]])  # [[1, 5]]
```

## Complexity

Let:

- `n` = number of input items.
- `g` = number of output groups/merged segments.

Per-operation cost:

- Sorting by comparison key: `O(n log n)`.
- Single sweep update/compare: `O(1)` per item.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| merge intervals | `O(n log n)` | `O(g)` output |
| non-overlap removal (sort by end) | `O(n log n)` | `O(1)` extra |
| dedupe/group run-length | `O(n log n)` | `O(g)` |
| closest neighbor after sort | `O(n log n)` | `O(1)` to `O(n)` (if keep index pairs) |
| starts/ends room sweep | `O(n log n)` | `O(n)` for separate arrays |

Interview note:

- Sorting dominates runtime; scan is linear.
- Distinguish extra working memory from unavoidable output memory.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: intervals/count/boolean/index pair/list.
- For interval outputs, endpoints and inclusivity rules match prompt.
- No-solution behavior is explicit and correct (`[]`, `0`, or `False`).
- If original order/index is required, preserve it before sorting.

### Data-Rule Checks

- Sort key and tie-break are correct for the specific greedy logic.
- Overlap condition is intentional (`<=` vs `<` for closed/open intervals).
- Carry state is flushed at correct boundaries.
- Mutability is controlled (copy interval rows when needed).
- Counting logic updates in the right branch only.

### Input Boundary Checks

- Empty and single-item input handled safely.
- All-overlapping and no-overlap extremes handled.
- Duplicate-heavy inputs handled correctly.
- Negative and mixed ranges handled where relevant.
- Large `n` does not trigger accidental nested comparisons.

### Pattern-Specific Checks

- Merge problems sort by start (not end).
- Removal/max non-overlap problems sort by end for greedy optimality.
- Event sweep uses strict `<` or `<=` consistently with meeting endpoint semantics.
- Final carry/group is appended after loop.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| empty input | `[]` | returns defined default without crash |
| touching intervals | `[[1,4],[4,5]]` | merge or separate based on interval rule |
| fully nested | `[[1,10],[2,3],[4,8]]` | one merged interval `[1,10]` |
| no overlaps | `[[1,2],[3,4]]` | unchanged list/count |
| all duplicates | `[2,2,2]` | duplicate/run count logic is correct |

## Common Pitfalls

- Choosing the wrong sort key for the intended greedy proof.
- Using incorrect overlap condition for prompt interval semantics.
- Forgetting to flush last carry segment/group.
- Losing original indices when prompt needs them.
- Assuming sorting is always allowed when output order must remain original.

## When Not Ideal

- Data cannot be reordered and original sequence constraints are essential.
- Streaming/online setting where full sort is not feasible.
- Need dynamic updates between queries (balanced trees/heaps/segment trees may fit better).
- Small fixed-range keys where counting/bucket approaches can beat comparison sort.

## Variations

- Merge Intervals / Insert Interval.
- Non-overlapping Intervals (minimum removals).
- Meeting Rooms / Meeting Rooms II (event sweep).
- Minimum Number of Arrows to Burst Balloons.
- Closest Elements / Minimum Absolute Difference.

## Interview Tips

- Use this 20-second opener:
  "I will sort by the key that makes conflicts local, then do one linear sweep maintaining current state."
- State greedy rationale:
  "Sorted order guarantees that once I pass an item, I never need to revisit it."
- Declare interval semantics explicitly:
  closed vs open endpoints affects overlap condition.
- Mention key choice out loud:
  by `start` for merging, by `end` for max non-overlap.
- Before finishing, test one overlapping case and one disjoint case.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why sort first? | Sorting creates deterministic local structure so one pass can replace pairwise comparisons. |
| Why this sort key? | It aligns with the greedy proof: start for merge, end for maximize non-overlap. |
| Why is one pass enough after sort? | Relevant conflicts/candidates become adjacent in sorted order. |
| Complexity? | `O(n log n)` from sorting plus `O(n)` scan. |
| How do you handle touching intervals? | Define overlap rule per prompt (`<=` vs `<`). |
| Can this be done in-place? | Sometimes yes; depends on output contract and whether mutation is allowed. |
| What if original indices are needed? | Sort `(value, index)` pairs to preserve mapping. |
| Most common bug? | Wrong sort key or forgetting final carry flush. |
| When not to use this pattern? | When reordering is disallowed or data is streaming/dynamic. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Merge Intervals

Problem:

- Given `intervals`, merge all overlapping intervals and return non-overlapping intervals covering same ranges.

What interviewer is testing:

- Can you pick correct sort key and overlap rule?
- Can you maintain carry interval correctly?
- Can you prove linear scan after sort is sufficient?

#### What to Say in First 30 Seconds

Use this script:

"Brute force overlap checking is quadratic.  
I will sort by start time so possible overlaps appear contiguously.  
Then I keep a current merged interval; if next starts before current ends, I extend end, otherwise I flush and start new.  
This is `O(n log n)` time and linear scan after sorting."

#### Solution A: Brute Force Pair Merging

Idea:

- Repeatedly compare and merge overlapping pairs until no change.

```python
def merge_bruteforce(intervals):
    arr = [x[:] for x in intervals]
    changed = True

    while changed:
        changed = False
        used = [False] * len(arr)
        out = []

        for i in range(len(arr)):
            if used[i]:
                continue
            s, e = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                s2, e2 = arr[j]
                if not (e < s2 or e2 < s):
                    s, e = min(s, s2), max(e, e2)
                    used[j] = True
                    changed = True
            used[i] = True
            out.append([s, e])

        arr = out

    return arr
```

Complexity:

- Worst-case superlinear to quadratic per round; inefficient.

#### Solution B: Sort + Build New Output

Idea:

- Sort by start and append merged blocks.

```python
def merge_sorted(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])
    out = [intervals[0][:]]

    for s, e in intervals[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])

    return out
```

Complexity:

- Time `O(n log n)`, Space `O(n)` output.

Interviewer tradeoff answer:

- "Sorting removes repeated conflict checks and gives a clean single sweep."

#### Solution C: Sort + In-Place Compaction Style

Idea:

- Sort and reuse same list with write pointer.

```python
def merge_in_place_style(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    write = 0

    for read in range(1, len(intervals)):
        if intervals[read][0] <= intervals[write][1]:
            intervals[write][1] = max(intervals[write][1], intervals[read][1])
        else:
            write += 1
            intervals[write] = intervals[read]

    return intervals[:write + 1]
```

Complexity:

- Time `O(n log n)`, extra space `O(1)` excluding output slice.

What to say while solving with interviewer:

1. "Sort key is start time."
2. "Carry interval is last merged interval."
3. "On overlap, extend end; on gap, flush carry."
4. "I will test `[[1,4],[4,5]]` to confirm boundary rule."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why sort by start and not end? | Start order ensures all possible overlaps for current carry appear next. |
| How do you define overlap? | For closed intervals, overlap if `next_start <= current_end`. |
| Can this be O(n) without sort? | Not generally for arbitrary unsorted intervals. |

### 2) Non-overlapping Intervals (Minimum Removals)

Problem:

- Given intervals, return minimum number to remove so remaining intervals are non-overlapping.

What interviewer is testing:

- Can you switch from merge to selection objective?
- Can you justify end-time greedy optimality?
- Can you translate kept count to removals?

#### What to Say in First 30 Seconds

Use this script:

"To minimize removals, I maximize number of non-overlapping intervals kept.  
Classic greedy: sort by end time and always keep the interval that ends earliest when possible.  
This preserves maximum room for future intervals.  
Then removals are `n - kept`."

#### Solution A: Brute Force Subset Search

Idea:

- Try all subsets and keep largest valid non-overlapping set.

```python
def min_remove_bruteforce(intervals):
    n = len(intervals)
    best_keep = 0

    def non_overlapping(chosen):
        chosen = sorted(chosen, key=lambda x: x[0])
        for i in range(1, len(chosen)):
            if chosen[i][0] < chosen[i - 1][1]:
                return False
        return True

    for mask in range(1 << n):
        chosen = [intervals[i] for i in range(n) if (mask >> i) & 1]
        if non_overlapping(chosen):
            best_keep = max(best_keep, len(chosen))

    return n - best_keep
```

Complexity:

- Exponential; impractical.

#### Solution B: Sort by Start and Keep Smaller End on Conflict

Idea:

- Valid greedy variant scanning start order.

```python
def min_remove_start_scan(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])
    removals = 0
    prev_end = intervals[0][1]

    for s, e in intervals[1:]:
        if s < prev_end:  # conflict
            removals += 1
            prev_end = min(prev_end, e)  # keep tighter ending interval
        else:
            prev_end = e

    return removals
```

Complexity:

- Time `O(n log n)`, Space `O(1)` extra.

Interviewer tradeoff answer:

- "This works, but sorting by end gives a cleaner classical proof."

#### Solution C: Sort by End (Canonical Greedy)

Idea:

- Keep intervals that start after or at last chosen end.

```python
def min_remove_optimal(intervals):
    intervals.sort(key=lambda x: x[1])  # end ascending
    kept = 0
    last_end = float("-inf")

    for s, e in intervals:
        if s >= last_end:
            kept += 1
            last_end = e

    return len(intervals) - kept
```

Complexity:

- Time `O(n log n)`, Space `O(1)` extra.

What to say while solving with interviewer:

1. "Equivalent objective is maximize kept non-overlapping intervals."
2. "Earliest finishing interval is safest greedy choice."
3. "Count kept, then convert to removals."
4. "I will test nested and touching intervals."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why sort by end? | Earliest end leaves maximum space for future intervals, giving optimal interval scheduling. |
| Why `s >= last_end` and not `>`? | Non-overlap allows touching boundaries in this prompt variant. |
| Could start-sorted greedy fail if careless? | Yes, if you keep wrong end on conflict; must keep smaller end. |
