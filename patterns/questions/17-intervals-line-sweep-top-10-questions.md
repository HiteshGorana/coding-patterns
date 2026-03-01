# Pattern 17 Interview Playbook: Intervals Line Sweep

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Tracks how many intervals are active at each timeline point by processing start/end events in order.
- Core intuition: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Trigger cue 1: Max overlaps, active intervals over time.
- Quick self-check: Can intervals be converted to enter/exit events?
- Target complexity: Time O(n log n) from sorting events, Space O(n) for events

---

## Q1. Meeting Rooms II

### Problem Statement (Concrete)
Solve **Meeting Rooms II** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
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

## Q2. Number of Airplanes in the Sky

### Problem Statement (Concrete)
Solve **Number of Airplanes in the Sky** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **Number of Airplanes in the Sky** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_number_of_airplanes_in_the_sky(intervals):
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
def better_number_of_airplanes_in_the_sky(intervals):
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
def solve_number_of_airplanes_in_the_sky(intervals):
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

## Q3. Car Pooling

### Problem Statement (Concrete)
Solve **Car Pooling** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **Car Pooling** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_car_pooling(intervals):
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
def better_car_pooling(intervals):
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
def solve_car_pooling(intervals):
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

## Q4. Maximum Population Year

### Problem Statement (Concrete)
Solve **Maximum Population Year** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **Maximum Population Year** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_maximum_population_year(intervals):
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
def better_maximum_population_year(intervals):
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
def solve_maximum_population_year(intervals):
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

## Q5. My Calendar I

### Problem Statement (Concrete)
Solve **My Calendar I** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **My Calendar I** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_my_calendar_i(intervals):
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
def better_my_calendar_i(intervals):
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
def solve_my_calendar_i(intervals):
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

## Q6. My Calendar II

### Problem Statement (Concrete)
Solve **My Calendar II** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **My Calendar II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_my_calendar_ii(intervals):
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
def better_my_calendar_ii(intervals):
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
def solve_my_calendar_ii(intervals):
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

## Q7. The Skyline Problem

### Problem Statement (Concrete)
Solve **The Skyline Problem** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **The Skyline Problem** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_the_skyline_problem(intervals):
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
def better_the_skyline_problem(intervals):
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
def solve_the_skyline_problem(intervals):
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

## Q8. Brightest Position on Street

### Problem Statement (Concrete)
Solve **Brightest Position on Street** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **Brightest Position on Street** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_brightest_position_on_street(intervals):
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
def better_brightest_position_on_street(intervals):
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
def solve_brightest_position_on_street(intervals):
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

## Q9. Employee Free Time

### Problem Statement (Concrete)
Solve **Employee Free Time** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **Employee Free Time** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_employee_free_time(intervals):
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
def better_employee_free_time(intervals):
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
def solve_employee_free_time(intervals):
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

## Q10. Minimum Number of Platforms

### Problem Statement (Concrete)
Solve **Minimum Number of Platforms** using **Intervals Line Sweep**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Intervals Line Sweep**.
- Red flags: brute force for **Minimum Number of Platforms** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_minimum_number_of_platforms(intervals):
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
def better_minimum_number_of_platforms(intervals):
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
def solve_minimum_number_of_platforms(intervals):
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
