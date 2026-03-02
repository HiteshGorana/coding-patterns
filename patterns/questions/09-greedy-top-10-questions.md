# Pattern 09 Interview Playbook: Greedy

This playbook is aligned with [Pattern 09: Greedy](../09-greedy.md).

Use it when a local choice can be proven globally safe.

## Pattern Snapshot

| Prompt shape | Greedy choice | Why it works |
|---|---|---|
| reachability / jumps | maximize current reach | stay-ahead frontier |
| interval scheduling/removal | keep earliest finishing | leaves max room for future |
| resource reset candidate | reset after negative prefix | failed prefix can never help |
| maximize count/score | take immediate positive gain | decomposition into independent gains |
| segment partition | cut at farthest required boundary | all required elements closed |
| task packing with cooldown | arrange most frequent tasks first | lower bound is tight |

## Query-Update Rules

- Define one local rule and one-line safety proof before coding.
- If order matters, sort first by the proof-driven key.
- Commit decisions and do not backtrack.
- Keep minimal state (`reach`, `last_end`, `tank`, counters).

---

## Q1. Jump Game

### Problem
Given `nums`, where `nums[i]` is max jump length from index `i`, return `True` if you can reach the last index.

Example: `nums = [2,3,1,1,4] -> True`

### Brute Force Solution

#### Pseudocode
```text
FUNCTION can_reach(i):
    IF i >= n - 1: RETURN True

    FOR step from 1 to nums[i]:
        IF can_reach(i + step):
            RETURN True

    RETURN False

RETURN can_reach(0)
```

#### Python
```python
def jump_game_bruteforce(nums):
    n = len(nums)

    def dfs(i):
        if i >= n - 1:
            return True

        max_step = nums[i]
        for step in range(1, max_step + 1):
            if dfs(i + step):
                return True

        return False

    return dfs(0)
```

#### Complexity
- Time: exponential in worst case
- Space: `O(n)` recursion

### Optimal Solution (Greedy Farthest Reach)

#### Pseudocode
```text
reach = 0
FOR i from 0 to n - 1:
    IF i > reach:
        RETURN False
    reach = max(reach, i + nums[i])
RETURN True
```

#### Python
```python
def jump_game_optimal(nums):
    reach = 0

    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)

    return True
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q2. Jump Game II

### Problem
Given `nums`, return minimum number of jumps to reach last index.

Example: `nums = [2,3,1,1,4] -> 2`

### Brute Force Solution

#### Pseudocode
```text
dp = [infinity] * n
dp[0] = 0

FOR i from 0 to n - 1:
    FOR step from 1 to nums[i]:
        j = i + step
        IF j < n:
            dp[j] = min(dp[j], dp[i] + 1)

RETURN dp[n - 1]
```

#### Python
```python
def jump_game_ii_bruteforce(nums):
    n = len(nums)
    dp = [10**9] * n
    dp[0] = 0

    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)

    return dp[-1]
```

#### Complexity
- Time: `O(n^2)` worst case
- Space: `O(n)`

### Optimal Solution (Greedy BFS Layers)

#### Pseudocode
```text
jumps = 0
cur_end = 0
farthest = 0

FOR i from 0 to n - 2:
    farthest = max(farthest, i + nums[i])

    IF i == cur_end:
        jumps += 1
        cur_end = farthest

RETURN jumps
```

#### Python
```python
def jump_game_ii_optimal(nums):
    jumps = 0
    cur_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == cur_end:
            jumps += 1
            cur_end = farthest

    return jumps
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q3. Gas Station

### Problem
Given `gas` and `cost`, return start index to complete circuit once, else `-1`.

Example: `gas = [1,2,3,4,5], cost = [3,4,5,1,2] -> 3`

### Brute Force Solution

#### Pseudocode
```text
FOR start from 0 to n - 1:
    tank = 0
    success = True

    FOR step from 0 to n - 1:
        i = (start + step) mod n
        tank += gas[i] - cost[i]
        IF tank < 0:
            success = False
            BREAK

    IF success:
        RETURN start

RETURN -1
```

#### Python
```python
def gas_station_bruteforce(gas, cost):
    n = len(gas)

    for start in range(n):
        tank = 0
        ok = True

        for step in range(n):
            i = (start + step) % n
            tank += gas[i] - cost[i]
            if tank < 0:
                ok = False
                break

        if ok:
            return start

    return -1
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Greedy Reset + Total Check)

#### Pseudocode
```text
total = 0
tank = 0
start = 0

FOR i from 0 to n - 1:
    diff = gas[i] - cost[i]
    total += diff
    tank += diff

    IF tank < 0:
        start = i + 1
        tank = 0

IF total < 0: RETURN -1
RETURN start
```

#### Python
```python
def gas_station_optimal(gas, cost):
    total = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff

        if tank < 0:
            start = i + 1
            tank = 0

    return start if total >= 0 else -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q4. Partition Labels

### Problem
Given string `s`, split it into as many parts as possible so each letter appears in at most one part. Return part lengths.

Example: `s = "ababcbacadefegdehijhklij" -> [9,7,8]`

### Brute Force Solution

#### Pseudocode
```text
start = 0
ans = []

WHILE start < n:
    FOR end from start to n - 1:
        part_chars = set(s[start..end])
        suffix = s[end+1..n-1]

        valid = True
        FOR ch in part_chars:
            IF ch appears in suffix:
                valid = False
                BREAK

        IF valid:
            APPEND (end - start + 1)
            start = end + 1
            BREAK

RETURN ans
```

#### Python
```python
def partition_labels_bruteforce(s):
    n = len(s)
    start = 0
    ans = []

    while start < n:
        for end in range(start, n):
            chars = set(s[start:end + 1])
            suffix = s[end + 1:]
            valid = True

            for ch in chars:
                if ch in suffix:
                    valid = False
                    break

            if valid:
                ans.append(end - start + 1)
                start = end + 1
                break

    return ans
```

#### Complexity
- Time: `O(n^3)` worst case
- Space: `O(n)`

### Optimal Solution (Last Occurrence Boundary)

#### Pseudocode
```text
last[ch] = last index of each character
start = 0
end = 0
ans = []

FOR i from 0 to n - 1:
    end = max(end, last[s[i]])

    IF i == end:
        APPEND (end - start + 1)
        start = i + 1

RETURN ans
```

#### Python
```python
def partition_labels_optimal(s):
    last = {ch: i for i, ch in enumerate(s)}
    start = 0
    end = 0
    ans = []

    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            ans.append(end - start + 1)
            start = i + 1

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(sigma)`

---

## Q5. Assign Cookies

### Problem
Given children greed factors `g` and cookie sizes `s`, return max number of content children.

Example: `g = [1,2,3], s = [1,1] -> 1`

### Brute Force Solution

#### Pseudocode
```text
used = [False] * len(s)

FUNCTION dfs(i):  # child index
    IF i == len(g):
        RETURN 0

    best = dfs(i + 1)  # skip satisfying child i

    FOR j from 0 to len(s)-1:
        IF not used[j] AND s[j] >= g[i]:
            used[j] = True
            best = max(best, 1 + dfs(i + 1))
            used[j] = False

    RETURN best

RETURN dfs(0)
```

#### Python
```python
def assign_cookies_bruteforce(g, s):
    used = [False] * len(s)

    def dfs(i):
        if i == len(g):
            return 0

        best = dfs(i + 1)

        for j in range(len(s)):
            if not used[j] and s[j] >= g[i]:
                used[j] = True
                best = max(best, 1 + dfs(i + 1))
                used[j] = False

        return best

    return dfs(0)
```

#### Complexity
- Time: exponential
- Space: `O(len(s))` recursion + used

### Optimal Solution (Sort + Two Pointers)

#### Pseudocode
```text
SORT g
SORT s
i = 0  # child pointer
j = 0  # cookie pointer

WHILE i < len(g) AND j < len(s):
    IF s[j] >= g[i]:
        i += 1
    j += 1

RETURN i
```

#### Python
```python
def assign_cookies_optimal(g, s):
    g.sort()
    s.sort()

    i = 0
    j = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1

    return i
```

#### Complexity
- Time: `O(n log n + m log m)`
- Space: `O(1)` extra

---

## Q6. Non-overlapping Intervals

### Problem
Given intervals, return minimum number to remove to make rest non-overlapping.

Example: `intervals = [[1,2],[2,3],[3,4],[1,3]] -> 1`

### Brute Force Solution

#### Pseudocode
```text
best_keep = 0

FUNCTION dfs(index, kept):
    IF index == n:
        best_keep = max(best_keep, len(kept))
        RETURN

    dfs(index + 1, kept)  # skip

    IF intervals[index] does not overlap with any in kept:
        add intervals[index]
        dfs(index + 1, kept)
        remove intervals[index]

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

### Optimal Solution (Greedy by Earliest End)

#### Pseudocode
```text
SORT intervals by end
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

## Q7. Minimum Number of Arrows to Burst Balloons

### Problem
Given balloon intervals `points`, return minimum arrows to burst all balloons.

Example: `points = [[10,16],[2,8],[1,6],[7,12]] -> 2`

### Brute Force Solution

#### Pseudocode
```text
candidate_positions = unique interval endpoints
best = infinity

FUNCTION dfs(remaining_intervals, arrows_used):
    IF remaining empty:
        best = min(best, arrows_used)
        RETURN
    IF arrows_used >= best:
        RETURN

    FOR x in candidate_positions:
        next_remaining = intervals not containing x
        IF next_remaining size < remaining size:
            dfs(next_remaining, arrows_used + 1)

CALL dfs(all intervals, 0)
RETURN best
```

#### Python
```python
def min_arrows_bruteforce(points):
    if not points:
        return 0

    candidates = sorted({p[0] for p in points} | {p[1] for p in points})
    best = [10**9]

    def dfs(rem, used):
        if not rem:
            best[0] = min(best[0], used)
            return
        if used >= best[0]:
            return

        for x in candidates:
            nxt = []
            for a, b in rem:
                if not (a <= x <= b):
                    nxt.append([a, b])
            if len(nxt) < len(rem):
                dfs(nxt, used + 1)

    dfs([p[:] for p in points], 0)
    return best[0]
```

#### Complexity
- Time: exponential
- Space: recursion + copies

### Optimal Solution (Greedy by End)

#### Pseudocode
```text
IF points empty: RETURN 0
SORT points by end ascending
arrows = 1
x = first end

FOR [s, e] in points from second onward:
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

## Q8. Task Scheduler

### Problem
Given tasks and cooldown `n`, return least intervals needed to execute all tasks.

Example: `tasks = ["A","A","A","B","B","B"], n = 2 -> 8`

### Brute Force Solution

#### Pseudocode
```text
Backtracking by time:
track remaining counts and next allowed time for each task
at each time choose any available task or idle
minimize finish time
```

#### Python
```python
def task_scheduler_bruteforce(tasks, n):
    from collections import Counter

    freq = Counter(tasks)
    keys = list(freq.keys())
    next_ok = {k: 0 for k in keys}
    total = len(tasks)
    best = [10**9]

    def dfs(time, done):
        if done == total:
            best[0] = min(best[0], time)
            return
        if time >= best[0]:
            return

        moved = False
        for k in keys:
            if freq[k] > 0 and time >= next_ok[k]:
                moved = True
                freq[k] -= 1
                prev = next_ok[k]
                next_ok[k] = time + n + 1
                dfs(time + 1, done + 1)
                next_ok[k] = prev
                freq[k] += 1

        if not moved:
            dfs(time + 1, done)

    dfs(0, 0)
    return best[0]
```

#### Complexity
- Time: exponential
- Space: recursion + maps

### Optimal Solution (Frequency Formula)

#### Pseudocode
```text
count frequencies
max_freq = maximum frequency
num_max = number of tasks with max_freq

frame = (max_freq - 1) * (n + 1) + num_max
RETURN max(len(tasks), frame)
```

#### Python
```python
def task_scheduler_optimal(tasks, n):
    from collections import Counter

    freq = Counter(tasks)
    max_freq = max(freq.values())
    num_max = sum(1 for v in freq.values() if v == max_freq)

    frame = (max_freq - 1) * (n + 1) + num_max
    return max(len(tasks), frame)
```

#### Complexity
- Time: `O(T)` where `T = len(tasks)`
- Space: `O(sigma)`

---

## Q9. Wiggle Subsequence

### Problem
Given `nums`, return length of longest wiggle subsequence.

Example: `nums = [1,7,4,9,2,5] -> 6`

### Brute Force Solution

#### Pseudocode
```text
best = 0

FUNCTION dfs(i, prev_value, prev_sign, length):
    best = max(best, length)

    FOR j from i to n - 1:
        diff = nums[j] - prev_value
        IF diff == 0: CONTINUE
        sign = +1 if diff > 0 else -1
        IF prev_sign == 0 OR sign != prev_sign:
            dfs(j + 1, nums[j], sign, length + 1)

TRY each index as start
RETURN best
```

#### Python
```python
def wiggle_bruteforce(nums):
    n = len(nums)
    best = 1 if n else 0

    def dfs(i, prev_val, prev_sign, length):
        nonlocal best
        best = max(best, length)

        for j in range(i, n):
            diff = nums[j] - prev_val
            if diff == 0:
                continue
            sign = 1 if diff > 0 else -1
            if prev_sign == 0 or sign != prev_sign:
                dfs(j + 1, nums[j], sign, length + 1)

    for i in range(n):
        dfs(i + 1, nums[i], 0, 1)

    return best
```

#### Complexity
- Time: exponential
- Space: recursion depth `O(n)`

### Optimal Solution (Greedy Up/Down Lengths)

#### Pseudocode
```text
IF n <= 1: RETURN n
up = 1
down = 1

FOR i from 1 to n - 1:
    IF nums[i] > nums[i - 1]:
        up = down + 1
    ELSE IF nums[i] < nums[i - 1]:
        down = up + 1

RETURN max(up, down)
```

#### Python
```python
def wiggle_optimal(nums):
    n = len(nums)
    if n <= 1:
        return n

    up = 1
    down = 1

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1

    return max(up, down)
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q10. Best Time to Buy and Sell Stock II

### Problem
Given prices, return max profit with unlimited transactions (cannot hold multiple shares).

Example: `prices = [7,1,5,3,6,4] -> 7`

### Brute Force Solution

#### Pseudocode
```text
FUNCTION dfs(i, holding):
    IF i == n: RETURN 0

    best = dfs(i + 1, holding)  # skip

    IF holding:
        best = max(best, prices[i] + dfs(i + 1, False))
    ELSE:
        best = max(best, -prices[i] + dfs(i + 1, True))

    RETURN best

RETURN dfs(0, False)
```

#### Python
```python
def stock_ii_bruteforce(prices):
    n = len(prices)

    def dfs(i, holding):
        if i == n:
            return 0

        best = dfs(i + 1, holding)

        if holding:
            best = max(best, prices[i] + dfs(i + 1, False))
        else:
            best = max(best, -prices[i] + dfs(i + 1, True))

        return best

    return dfs(0, False)
```

#### Complexity
- Time: exponential
- Space: recursion depth `O(n)`

### Optimal Solution (Sum of Positive Deltas)

#### Pseudocode
```text
profit = 0
FOR i from 1 to n - 1:
    IF prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
RETURN profit
```

#### Python
```python
def stock_ii_optimal(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Rapid Recall Checklist

- State greedy rule and proof sketch before implementation.
- Prefer sorted order when a tie-break makes decisions final.
- Track minimal state only; avoid reversible choices.
- Validate tricky edges (empty input, impossible case, ties/equal values).
