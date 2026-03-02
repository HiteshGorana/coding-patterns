# Pattern 08 Interview Playbook: Sort + Scan

This playbook is aligned with [Pattern 08: Sort + Scan](../08-sort-and-scan.md).

Use it when sorting exposes local structure that one linear sweep can exploit.

## Pattern Snapshot

| Prompt shape | Sort key | Scan state |
|---|---|---|
| merge/interval overlap | start or end time | current merged interval / last end |
| conflict detection | start time | previous interval end |
| min resources over intervals | separate starts/ends or min-end heap | active count |
| maximize/minimize with ordering | custom comparator | running best |
| order reconstruction | primary desc + secondary asc | incremental insertion |
| nearest/group transitions | value/index order | previous item group |

## Query-Update Rules

- Pick a sort key that makes decisions local.
- After sorting, make one pass and only compare with carry state.
- For interval greedies, prove why sorted order makes earlier decisions final.
- For custom string/record sorting, define comparator to match objective.

---

## Q1. Merge Intervals

### Problem
Given intervals, merge all overlapping intervals.

Example: `intervals = [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]`

### Brute Force Solution

#### Pseudocode
```text
arr = copy(intervals)
changed = True

WHILE changed:
    changed = False
    used = [False] * len(arr)
    next_arr = []

    FOR i from 0 to len(arr)-1:
        IF used[i]:
            CONTINUE

        s, e = arr[i]
        FOR j from i+1 to len(arr)-1:
            IF used[j]:
                CONTINUE
            a, b = arr[j]
            IF intervals overlap:
                s = min(s, a)
                e = max(e, b)
                used[j] = True
                changed = True

        next_arr.append([s, e])

    arr = next_arr

RETURN sorted(arr)
```

#### Python
```python
def merge_intervals_bruteforce(intervals):
    arr = [x[:] for x in intervals]
    changed = True

    while changed:
        changed = False
        used = [False] * len(arr)
        nxt = []

        for i in range(len(arr)):
            if used[i]:
                continue

            s, e = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue

                a, b = arr[j]
                if not (e < a or b < s):
                    s = min(s, a)
                    e = max(e, b)
                    used[j] = True
                    changed = True

            nxt.append([s, e])

        arr = nxt

    return sorted(arr)
```

#### Complexity
- Time: up to `O(n^2)` or more across repeated passes
- Space: `O(n)`

### Optimal Solution (Sort by Start + One Scan)

#### Pseudocode
```text
SORT intervals by start
merged = []

FOR [s, e] in intervals:
    IF merged empty OR merged[-1].end < s:
        APPEND [s, e]
    ELSE:
        merged[-1].end = max(merged[-1].end, e)

RETURN merged
```

#### Python
```python
def merge_intervals_optimal(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for s, e in intervals:
        if not merged or merged[-1][1] < s:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    return merged
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)`

---

## Q2. Insert Interval

### Problem
Given non-overlapping sorted intervals and one new interval, insert and merge as needed.

Example: `intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]]`

### Brute Force Solution

#### Pseudocode
```text
arr = intervals + [newInterval]
RETURN merge_intervals_bruteforce(arr)
```

#### Python
```python
def insert_interval_bruteforce(intervals, newInterval):
    arr = intervals + [newInterval]
    return merge_intervals_bruteforce(arr)
```

#### Complexity
- Time: `O(n^2)` or worse from brute merging
- Space: `O(n)`

### Optimal Solution (Single Pass on Sorted Input)

#### Pseudocode
```text
ans = []
i = 0
n = len(intervals)

WHILE i < n AND intervals[i].end < new.start:
    APPEND intervals[i]
    i += 1

WHILE i < n AND intervals[i].start <= new.end:
    new.start = min(new.start, intervals[i].start)
    new.end = max(new.end, intervals[i].end)
    i += 1

APPEND new

WHILE i < n:
    APPEND intervals[i]
    i += 1

RETURN ans
```

#### Python
```python
def insert_interval_optimal(intervals, newInterval):
    ans = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        ans.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    ans.append(newInterval)

    while i < n:
        ans.append(intervals[i])
        i += 1

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q3. Non-overlapping Intervals

### Problem
Given intervals, return minimum number of intervals to remove so remaining intervals are non-overlapping.

Example: `intervals = [[1,2],[2,3],[3,4],[1,3]] -> 1`

### Brute Force Solution

#### Pseudocode
```text
best_keep = 0

FUNCTION dfs(index, kept_intervals):
    IF index == n:
        best_keep = max(best_keep, len(kept_intervals))
        RETURN

    # skip current
    dfs(index + 1, kept_intervals)

    # keep current if no overlap with all kept
    IF current interval does not overlap any kept:
        add current
        dfs(index + 1, kept_intervals)
        remove current

CALL dfs(0, [])
RETURN n - best_keep
```

#### Python
```python
def erase_overlap_bruteforce(intervals):
    n = len(intervals)
    best_keep = 0

    def overlap(a, b):
        return not (a[1] <= b[0] or b[1] <= a[0])

    def dfs(i, kept):
        nonlocal best_keep
        if i == n:
            best_keep = max(best_keep, len(kept))
            return

        dfs(i + 1, kept)

        ok = True
        for it in kept:
            if overlap(it, intervals[i]):
                ok = False
                break

        if ok:
            kept.append(intervals[i])
            dfs(i + 1, kept)
            kept.pop()

    dfs(0, [])
    return n - best_keep
```

#### Complexity
- Time: exponential `O(2^n)`
- Space: `O(n)` recursion

### Optimal Solution (Greedy by End Time)

#### Pseudocode
```text
SORT intervals by end ascending
kept = 0
last_end = -infinity

FOR [s, e] in intervals:
    IF s >= last_end:
        kept += 1
        last_end = e

RETURN n - kept
```

#### Python
```python
def erase_overlap_optimal(intervals):
    intervals.sort(key=lambda x: x[1])

    kept = 0
    last_end = float('-inf')

    for s, e in intervals:
        if s >= last_end:
            kept += 1
            last_end = e

    return len(intervals) - kept
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(1)` extra

---

## Q4. Meeting Rooms

### Problem
Given meeting intervals, return `True` if a person can attend all meetings.

Example: `intervals = [[0,30],[5,10],[15,20]] -> False`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        IF intervals i and j overlap:
            RETURN False
RETURN True
```

#### Python
```python
def can_attend_meetings_bruteforce(intervals):
    n = len(intervals)

    for i in range(n):
        for j in range(i + 1, n):
            a, b = intervals[i]
            c, d = intervals[j]
            if not (b <= c or d <= a):
                return False

    return True
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Sort by Start)

#### Pseudocode
```text
SORT intervals by start
FOR i from 1 to n - 1:
    IF intervals[i].start < intervals[i - 1].end:
        RETURN False
RETURN True
```

#### Python
```python
def can_attend_meetings_optimal(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(1)` extra

---

## Q5. Meeting Rooms II

### Problem
Given meeting intervals, return minimum number of conference rooms required.

Example: `intervals = [[0,30],[5,10],[15,20]] -> 2`

### Brute Force Solution

#### Pseudocode
```text
SORT intervals by start
room_ends = []

FOR each interval [s, e]:
    placed = False
    FOR each room r in room_ends:
        IF room_ends[r] <= s:
            room_ends[r] = e
            placed = True
            BREAK
    IF not placed:
        APPEND e to room_ends

RETURN number of rooms
```

#### Python
```python
def min_meeting_rooms_bruteforce(intervals):
    intervals.sort(key=lambda x: x[0])
    room_ends = []

    for s, e in intervals:
        placed = False
        for i in range(len(room_ends)):
            if room_ends[i] <= s:
                room_ends[i] = e
                placed = True
                break
        if not placed:
            room_ends.append(e)

    return len(room_ends)
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(n)`

### Optimal Solution (Sort Starts and Ends)

#### Pseudocode
```text
starts = sorted(all starts)
ends = sorted(all ends)
i = 0, j = 0
rooms = 0
best = 0

WHILE i < n:
    IF starts[i] < ends[j]:
        rooms += 1
        best = max(best, rooms)
        i += 1
    ELSE:
        rooms -= 1
        j += 1

RETURN best
```

#### Python
```python
def min_meeting_rooms_optimal(intervals):
    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)

    i = 0
    j = 0
    rooms = 0
    best = 0
    n = len(intervals)

    while i < n:
        if starts[i] < ends[j]:
            rooms += 1
            best = max(best, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1

    return best
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)`

---

## Q6. Minimum Number of Arrows to Burst Balloons

### Problem
Given intervals of balloons, return minimum arrows needed to burst all balloons.

Example: `points = [[10,16],[2,8],[1,6],[7,12]] -> 2`

### Brute Force Solution

#### Pseudocode
```text
remaining = copy(points)
arrows = 0

WHILE remaining not empty:
    pick first interval [s, e]
    shoot at x = e
    arrows += 1

    next_remaining = []
    FOR each interval [a, b] in remaining:
        IF x not in [a, b]:
            APPEND [a, b] to next_remaining

    remaining = next_remaining

RETURN arrows
```

#### Python
```python
def min_arrows_bruteforce(points):
    if not points:
        return 0

    remaining = [p[:] for p in points]
    arrows = 0

    while remaining:
        x = remaining[0][1]
        arrows += 1

        nxt = []
        for a, b in remaining:
            if not (a <= x <= b):
                nxt.append([a, b])
        remaining = nxt

    return arrows
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(n)`

### Optimal Solution (Greedy by End)

#### Pseudocode
```text
SORT points by end
arrows = 1
x = end of first interval

FOR each interval [s, e] from second onward:
    IF s > x:
        arrows += 1
        x = e

RETURN arrows
```

#### Python
```python
def min_arrows_optimal(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1
    x = points[0][1]

    for s, e in points[1:]:
        if s > x:
            arrows += 1
            x = e

    return arrows
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(1)` extra

---

## Q7. Car Fleet

### Problem
Given `target`, `position`, and `speed`, return number of car fleets arriving at target.

Example: `target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] -> 3`

### Brute Force Solution

#### Pseudocode
```text
pairs = cars sorted by position descending
times = [time to target for each car]
changed = True

WHILE changed:
    changed = False
    i = 1
    WHILE i < len(times):
        IF times[i] <= times[i - 1]:
            remove times[i]  # joins front fleet
            changed = True
        ELSE:
            i += 1

RETURN len(times)
```

#### Python
```python
def car_fleet_bruteforce(target, position, speed):
    pairs = sorted(zip(position, speed), reverse=True)
    times = [(target - p) / s for p, s in pairs]

    changed = True
    while changed:
        changed = False
        i = 1
        while i < len(times):
            if times[i] <= times[i - 1]:
                times.pop(i)
                changed = True
            else:
                i += 1

    return len(times)
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(n)`

### Optimal Solution (Sort Desc + One Pass Stack Logic)

#### Pseudocode
```text
pairs = cars sorted by position descending
fleets = 0
last_time = 0

FOR each car in pairs:
    t = (target - position) / speed
    IF t > last_time:
        fleets += 1
        last_time = t

RETURN fleets
```

#### Python
```python
def car_fleet_optimal(target, position, speed):
    pairs = sorted(zip(position, speed), reverse=True)

    fleets = 0
    last_time = 0.0

    for p, s in pairs:
        t = (target - p) / s
        if t > last_time:
            fleets += 1
            last_time = t

    return fleets
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)` from sorting pairs

---

## Q8. Queue Reconstruction by Height

### Problem
Given people `[h, k]` (height and count of people in front with height >= `h`), reconstruct queue.

Example: `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] -> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

### Brute Force Solution

#### Pseudocode
```text
TRY all permutations of people
FOR each permutation:
    IF every person has exactly k taller-or-equal ahead:
        RETURN permutation
```

#### Python
```python
def reconstruct_queue_bruteforce(people):
    from itertools import permutations

    def valid(order):
        for i, (h, k) in enumerate(order):
            cnt = 0
            for j in range(i):
                if order[j][0] >= h:
                    cnt += 1
            if cnt != k:
                return False
        return True

    for perm in permutations(people):
        if valid(perm):
            return [list(x) for x in perm]

    return []
```

#### Complexity
- Time: `O(n! * n^2)`
- Space: `O(n)` recursion/perm state

### Optimal Solution (Sort + Indexed Insert)

#### Pseudocode
```text
SORT people by height descending, then k ascending
queue = []
FOR person in sorted people:
    INSERT person at index person.k in queue
RETURN queue
```

#### Python
```python
def reconstruct_queue_optimal(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    queue = []

    for p in people:
        queue.insert(p[1], p)

    return queue
```

#### Complexity
- Time: `O(n^2)` (list insertion)
- Space: `O(n)`

---

## Q9. Sort Colors

### Problem
Given array with values `0`, `1`, `2`, sort in-place.

Example: `nums = [2,0,2,1,1,0] -> [0,0,1,1,2,2]`

### Brute Force Solution

#### Pseudocode
```text
SORT nums
RETURN nums
```

#### Python
```python
def sort_colors_bruteforce(nums):
    nums.sort()
    return nums
```

#### Complexity
- Time: `O(n log n)`
- Space: depends on language sort

### Optimal Solution (Dutch National Flag)

#### Pseudocode
```text
low = 0, mid = 0, high = n - 1
WHILE mid <= high:
    IF nums[mid] == 0:
        SWAP nums[low], nums[mid]
        low += 1
        mid += 1
    ELSE IF nums[mid] == 1:
        mid += 1
    ELSE:
        SWAP nums[mid], nums[high]
        high -= 1
RETURN nums
```

#### Python
```python
def sort_colors_optimal(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q10. Largest Number

### Problem
Given list of non-negative integers, arrange them to form the largest possible number.

Example: `nums = [3,30,34,5,9] -> "9534330"`

### Brute Force Solution

#### Pseudocode
```text
best = ""
FOR each permutation perm of nums:
    cand = concatenated string of perm
    IF cand > best (as string with equal length compare):
        best = cand

REMOVE leading zeros case by returning "0" if best starts with 0
RETURN best
```

#### Python
```python
def largest_number_bruteforce(nums):
    from itertools import permutations

    best = ""

    for perm in permutations(nums):
        cand = ''.join(str(x) for x in perm)
        if cand > best:
            best = cand

    return '0' if best and best[0] == '0' else best
```

#### Complexity
- Time: `O(n! * n)`
- Space: `O(n)`

### Optimal Solution (Custom Comparator Sort)

#### Pseudocode
```text
CONVERT nums to strings
SORT strings by comparator:
    a before b if a+b > b+a
JOIN sorted strings
IF result starts with "0": RETURN "0"
RETURN result
```

#### Python
```python
def largest_number_optimal(nums):
    from functools import cmp_to_key

    arr = [str(x) for x in nums]

    def cmp(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0

    arr.sort(key=cmp_to_key(cmp))
    res = ''.join(arr)

    return '0' if res[0] == '0' else res
```

#### Complexity
- Time: `O(n log n * L)` where `L` is max string length
- Space: `O(n)`

---

## Rapid Recall Checklist

- Choose sort key/tie-break that makes local decisions correct globally.
- Keep one carry state while scanning; avoid revisiting processed prefix.
- For interval greedies, justify why earlier end/start is optimal.
- Validate corner cases: empty input, full overlap, all-equal/leading-zero outputs.
