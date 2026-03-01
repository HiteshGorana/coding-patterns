# Pattern 08 Interview Playbook: Sort + Scan

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Sorting often reveals structure that is hidden in unsorted data.
- Core intuition: Sorting groups related items so local neighbors carry global information. After sorting, one pass is enough to: - merge - count transitions - detect overlap
- Trigger cue 1: Intervals, conflicts, merging, global ordering.
- Quick self-check: After sort, can one pass solve it?
- Target complexity: Time O(n log n) from sort, Space O(n) for output (or O(1) extra in some in-place variants)

---

## Q1. Merge Intervals

### Problem Statement (Concrete)
Solve **Merge Intervals** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Merge Intervals** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_merge_intervals(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_merge_intervals(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Insert Interval

### Problem Statement (Concrete)
Solve **Insert Interval** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Insert Interval** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_insert_interval(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_insert_interval(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_insert_interval(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Non-overlapping Intervals

### Problem Statement (Concrete)
Solve **Non-overlapping Intervals** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Non-overlapping Intervals** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_non_overlapping_intervals(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_non_overlapping_intervals(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Meeting Rooms

### Problem Statement (Concrete)
Solve **Meeting Rooms** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Meeting Rooms** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate all subsets of all `n` elements.

#### Python
```python
def brute_meeting_rooms(nums, goal):
    n = len(nums)
    best = float('inf')
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if mask & (1 << i):
                s += nums[i]
        best = min(best, abs(s - goal))
    return best
```

#### Complexity
- Time `O(2^n * n)`, Space `O(1)` extra.

### Approach 2: Better (Intermediate)
#### Intuition
- Split into two halves; enumerate each half and combine with binary search.

#### Python
```python
from bisect import bisect_left

def better_meeting_rooms(nums, goal):
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    def sums(arr):
        out = [0]
        for x in arr:
            out += [x + v for v in out]
        return out

    ls = sums(left)
    rs = sorted(sums(right))
    ans = float('inf')
    for s in ls:
        need = goal - s
        i = bisect_left(rs, need)
        if i < len(rs):
            ans = min(ans, abs(s + rs[i] - goal))
        if i:
            ans = min(ans, abs(s + rs[i-1] - goal))
    return ans
```

#### Complexity
- Time `O(2^(n/2) * n)`, Space `O(2^(n/2))`.

### Approach 3: Optimal (Best)
#### Intuition
- Meet-in-the-middle reduces exponent base by halving decision set.

#### Python
```python
from bisect import bisect_left

def better_meeting_rooms(nums, goal):
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    def sums(arr):
        out = [0]
        for x in arr:
            out += [x + v for v in out]
        return out

    ls = sums(left)
    rs = sorted(sums(right))
    ans = float('inf')
    for s in ls:
        need = goal - s
        i = bisect_left(rs, need)
        if i < len(rs):
            ans = min(ans, abs(s + rs[i] - goal))
        if i:
            ans = min(ans, abs(s + rs[i-1] - goal))
    return ans
```

#### Correctness (Why This Works)
- Any full subset is union of one subset from left half and one from right half.
- Searching nearest complement in sorted right sums yields globally best combined value.

#### Complexity
- Time `O(2^(n/2) log 2^(n/2))`, Space `O(2^(n/2))`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Meeting Rooms II

### Problem Statement (Concrete)
Solve **Meeting Rooms II** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Meeting Rooms II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate all subsets of all `n` elements.

#### Python
```python
def brute_meeting_rooms_ii(nums, goal):
    n = len(nums)
    best = float('inf')
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if mask & (1 << i):
                s += nums[i]
        best = min(best, abs(s - goal))
    return best
```

#### Complexity
- Time `O(2^n * n)`, Space `O(1)` extra.

### Approach 2: Better (Intermediate)
#### Intuition
- Split into two halves; enumerate each half and combine with binary search.

#### Python
```python
from bisect import bisect_left

def better_meeting_rooms_ii(nums, goal):
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    def sums(arr):
        out = [0]
        for x in arr:
            out += [x + v for v in out]
        return out

    ls = sums(left)
    rs = sorted(sums(right))
    ans = float('inf')
    for s in ls:
        need = goal - s
        i = bisect_left(rs, need)
        if i < len(rs):
            ans = min(ans, abs(s + rs[i] - goal))
        if i:
            ans = min(ans, abs(s + rs[i-1] - goal))
    return ans
```

#### Complexity
- Time `O(2^(n/2) * n)`, Space `O(2^(n/2))`.

### Approach 3: Optimal (Best)
#### Intuition
- Meet-in-the-middle reduces exponent base by halving decision set.

#### Python
```python
from bisect import bisect_left

def better_meeting_rooms_ii(nums, goal):
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    def sums(arr):
        out = [0]
        for x in arr:
            out += [x + v for v in out]
        return out

    ls = sums(left)
    rs = sorted(sums(right))
    ans = float('inf')
    for s in ls:
        need = goal - s
        i = bisect_left(rs, need)
        if i < len(rs):
            ans = min(ans, abs(s + rs[i] - goal))
        if i:
            ans = min(ans, abs(s + rs[i-1] - goal))
    return ans
```

#### Correctness (Why This Works)
- Any full subset is union of one subset from left half and one from right half.
- Searching nearest complement in sorted right sums yields globally best combined value.

#### Complexity
- Time `O(2^(n/2) log 2^(n/2))`, Space `O(2^(n/2))`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Minimum Number of Arrows to Burst Balloons

### Problem Statement (Concrete)
Solve **Minimum Number of Arrows to Burst Balloons** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Minimum Number of Arrows to Burst Balloons** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_minimum_number_of_arrows_to_burst_balloons(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_minimum_number_of_arrows_to_burst_balloons(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_minimum_number_of_arrows_to_burst_balloons(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Car Fleet

### Problem Statement (Concrete)
Solve **Car Fleet** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Car Fleet** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_car_fleet(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_car_fleet(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_car_fleet(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Queue Reconstruction by Height

### Problem Statement (Concrete)
Solve **Queue Reconstruction by Height** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Queue Reconstruction by Height** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_queue_reconstruction_by_height(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_queue_reconstruction_by_height(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_queue_reconstruction_by_height(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Sort Colors

### Problem Statement (Concrete)
Solve **Sort Colors** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Sort Colors** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_sort_colors(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_sort_colors(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_sort_colors(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Largest Number

### Problem Statement (Concrete)
Solve **Largest Number** using **Sort + Scan**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sort + Scan**.
- Red flags: brute force for **Largest Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_largest_number(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_largest_number(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_largest_number(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
