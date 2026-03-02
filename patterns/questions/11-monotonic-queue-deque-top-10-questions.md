# Pattern 11 Interview Playbook: Monotonic Queue / Deque

This playbook is aligned with [Pattern 11: Monotonic Queue / Deque](../11-monotonic-queue-deque.md).

Use it when the prompt needs fast max/min or best-candidate queries over a moving window.

## Pattern Snapshot

| Prompt shape | Deque type | Core rule |
|---|---|---|
| fixed-window maximum | decreasing deque of indices | pop back while `nums[back] <= nums[i]` |
| fixed-window minimum | increasing deque of indices | pop back while `nums[back] >= nums[i]` |
| shortest subarray sum >= `k` | increasing deque of prefix indices | pop front while condition holds |
| DP transition over last `k` states | decreasing deque by DP value | front gives current best transition |
| window with max + running sum constraint | decreasing max deque + sliding sum | shrink left until budget valid |
| first negative per window | deque of negative indices | expire front by index, front is answer |

## Query-Update Rules

- Store indices when candidates expire by window position.
- Expire invalid front indices before reading the answer.
- Remove dominated candidates from the back before pushing current index.
- Choose comparator strictness (`<`, `<=`, `>`, `>=`) based on duplicate semantics.
- Amortized proof: each index enters and exits deque at most once.

---

## Q1. Sliding Window Maximum

### Problem
Given an array `nums` and window size `k`, return max value for each window of size `k`.

Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]`

### Brute Force Solution

#### Pseudocode
```text
IF k <= 0 OR k > n:
    RETURN []

ans = []
FOR i from 0 to n - k:
    window_max = -infinity
    FOR j from i to i + k - 1:
        window_max = max(window_max, nums[j])
    APPEND window_max to ans

RETURN ans
```

#### Python
```python
def sliding_window_max_bruteforce(nums, k):
    n = len(nums)
    if k <= 0 or k > n:
        return []

    ans = []
    for i in range(n - k + 1):
        window_max = -10**18
        for j in range(i, i + k):
            window_max = max(window_max, nums[j])
        ans.append(window_max)

    return ans
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)` extra

### Optimal Solution (Decreasing Deque)

#### Pseudocode
```text
IF k <= 0 OR k > n:
    RETURN []

dq = empty deque  # indices, values decreasing
ans = []

FOR i from 0 to n - 1:
    WHILE dq not empty AND dq.front <= i - k:
        dq.pop_front()

    WHILE dq not empty AND nums[dq.back] <= nums[i]:
        dq.pop_back()

    dq.push_back(i)

    IF i >= k - 1:
        APPEND nums[dq.front] to ans

RETURN ans
```

#### Python
```python
from collections import deque


def sliding_window_max_optimal(nums, k):
    n = len(nums)
    if k <= 0 or k > n:
        return []

    dq = deque()
    ans = []

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= x:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(k)`

---

## Q2. Shortest Subarray with Sum at Least K

### Problem
Given integer array `nums` (can include negatives) and integer `k`, return length of the shortest non-empty subarray with sum at least `k`, else `-1`.

Example: `nums = [2,-1,2], k = 3 -> 3`

### Brute Force Solution

#### Pseudocode
```text
best = n + 1

FOR i from 0 to n - 1:
    s = 0
    FOR j from i to n - 1:
        s += nums[j]
        IF s >= k:
            best = min(best, j - i + 1)
            BREAK

RETURN best if best <= n else -1
```

#### Python
```python
def shortest_subarray_at_least_k_bruteforce(nums, k):
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

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Sum + Increasing Deque)

#### Pseudocode
```text
prefix[0] = 0
FOR i from 0 to n - 1:
    prefix[i + 1] = prefix[i] + nums[i]

dq = empty deque  # indices of prefix in increasing prefix value
best = n + 1

FOR i from 0 to n:
    WHILE dq not empty AND prefix[i] - prefix[dq.front] >= k:
        best = min(best, i - dq.pop_front())

    WHILE dq not empty AND prefix[dq.back] >= prefix[i]:
        dq.pop_back()

    dq.push_back(i)

RETURN best if best <= n else -1
```

#### Python
```python
from collections import deque


def shortest_subarray_at_least_k_optimal(nums, k):
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

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q3. Constrained Subsequence Sum

### Problem
Given `nums` and `k`, return max subsequence sum where for any two consecutive chosen indices `i < j`, we must have `j - i <= k`.

Example: `nums = [10,2,-10,5,20], k = 2 -> 37`

### Brute Force Solution

#### Pseudocode
```text
dp = [0] * n
best = -infinity

FOR i from 0 to n - 1:
    best_prev = 0
    FOR j from max(0, i - k) to i - 1:
        best_prev = max(best_prev, dp[j])

    dp[i] = nums[i] + best_prev
    best = max(best, dp[i])

RETURN best
```

#### Python
```python
def constrained_subsequence_sum_bruteforce(nums, k):
    n = len(nums)
    dp = [0] * n
    best = -10**18

    for i in range(n):
        best_prev = 0
        for j in range(max(0, i - k), i):
            best_prev = max(best_prev, dp[j])

        dp[i] = nums[i] + best_prev
        best = max(best, dp[i])

    return best
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(n)`

### Optimal Solution (DP + Decreasing Deque)

#### Pseudocode
```text
dp = [0] * n
dq = empty deque  # indices with decreasing dp value
best = -infinity

FOR i from 0 to n - 1:
    WHILE dq not empty AND dq.front < i - k:
        dq.pop_front()

    best_prev = dp[dq.front] if dq not empty else 0
    dp[i] = nums[i] + max(0, best_prev)
    best = max(best, dp[i])

    WHILE dq not empty AND dp[dq.back] <= dp[i]:
        dq.pop_back()

    dq.push_back(i)

RETURN best
```

#### Python
```python
from collections import deque


def constrained_subsequence_sum_optimal(nums, k):
    n = len(nums)
    dp = [0] * n
    dq = deque()
    best = -10**18

    for i in range(n):
        while dq and dq[0] < i - k:
            dq.popleft()

        best_prev = dp[dq[0]] if dq else 0
        dp[i] = nums[i] + max(0, best_prev)
        best = max(best, dp[i])

        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        dq.append(i)

    return best
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q4. Jump Game VI

### Problem
Given array `nums` and integer `k`, start at index `0` and reach `n-1`. From index `i`, jump to `[i+1 .. i+k]`. Return maximum score.

Example: `nums = [1,-1,-2,4,-7,3], k = 2 -> 7`

### Brute Force Solution

#### Pseudocode
```text
dp[0] = nums[0]

FOR i from 1 to n - 1:
    best_prev = -infinity
    FOR j from max(0, i - k) to i - 1:
        best_prev = max(best_prev, dp[j])
    dp[i] = nums[i] + best_prev

RETURN dp[n - 1]
```

#### Python
```python
def jump_game_vi_bruteforce(nums, k):
    n = len(nums)
    dp = [-10**18] * n
    dp[0] = nums[0]

    for i in range(1, n):
        best_prev = -10**18
        for j in range(max(0, i - k), i):
            best_prev = max(best_prev, dp[j])
        dp[i] = nums[i] + best_prev

    return dp[-1]
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(n)`

### Optimal Solution (DP + Decreasing Deque)

#### Pseudocode
```text
dp[0] = nums[0]
dq = deque([0])  # decreasing dp values

FOR i from 1 to n - 1:
    WHILE dq not empty AND dq.front < i - k:
        dq.pop_front()

    dp[i] = nums[i] + dp[dq.front]

    WHILE dq not empty AND dp[dq.back] <= dp[i]:
        dq.pop_back()

    dq.push_back(i)

RETURN dp[n - 1]
```

#### Python
```python
from collections import deque


def jump_game_vi_optimal(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dq = deque([0])

    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()

        dp[i] = nums[i] + dp[dq[0]]

        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        dq.append(i)

    return dp[-1]
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q5. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

### Problem
Given `nums` and `limit`, return length of longest subarray where `max(nums[l:r]) - min(nums[l:r]) <= limit`.

Example: `nums = [8,2,4,7], limit = 4 -> 2`

### Brute Force Solution

#### Pseudocode
```text
best = 0

FOR i from 0 to n - 1:
    mn = +infinity
    mx = -infinity

    FOR j from i to n - 1:
        mn = min(mn, nums[j])
        mx = max(mx, nums[j])

        IF mx - mn <= limit:
            best = max(best, j - i + 1)
        ELSE:
            BREAK

RETURN best
```

#### Python
```python
def longest_subarray_limit_bruteforce(nums, limit):
    n = len(nums)
    best = 0

    for i in range(n):
        mn = 10**18
        mx = -10**18

        for j in range(i, n):
            mn = min(mn, nums[j])
            mx = max(mx, nums[j])

            if mx - mn <= limit:
                best = max(best, j - i + 1)
            else:
                break

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Two Deques + Sliding Window)

#### Pseudocode
```text
max_dq = empty deque  # decreasing values by index
min_dq = empty deque  # increasing values by index
left = 0
best = 0

FOR right from 0 to n - 1:
    WHILE max_dq not empty AND nums[max_dq.back] <= nums[right]:
        max_dq.pop_back()
    max_dq.push_back(right)

    WHILE min_dq not empty AND nums[min_dq.back] >= nums[right]:
        min_dq.pop_back()
    min_dq.push_back(right)

    WHILE nums[max_dq.front] - nums[min_dq.front] > limit:
        IF max_dq.front == left:
            max_dq.pop_front()
        IF min_dq.front == left:
            min_dq.pop_front()
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
from collections import deque


def longest_subarray_limit_optimal(nums, limit):
    max_dq = deque()
    min_dq = deque()
    left = 0
    best = 0

    for right, x in enumerate(nums):
        while max_dq and nums[max_dq[-1]] <= x:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and nums[min_dq[-1]] >= x:
            min_dq.pop()
        min_dq.append(right)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            if max_dq[0] == left:
                max_dq.popleft()
            if min_dq[0] == left:
                min_dq.popleft()
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)` worst case

---

## Q6. Max Value of Equation

### Problem
Given points sorted by `x`: `points[i] = [xi, yi]`, find max of `yi + yj + |xi - xj|` for `i < j` and `xj - xi <= k`.

Example: `points = [[1,3],[2,0],[5,10],[6,-10]], k = 1 -> 4`

### Brute Force Solution

#### Pseudocode
```text
best = -infinity

FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        IF points[j].x - points[i].x > k:
            BREAK

        val = points[i].y + points[j].y + points[j].x - points[i].x
        best = max(best, val)

RETURN best
```

#### Python
```python
def max_value_of_equation_bruteforce(points, k):
    n = len(points)
    best = -10**18

    for i in range(n):
        xi, yi = points[i]

        for j in range(i + 1, n):
            xj, yj = points[j]
            if xj - xi > k:
                break

            best = max(best, yi + yj + xj - xi)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Deque on `y - x` Candidates)

#### Pseudocode
```text
best = -infinity
dq = empty deque  # candidate indices with decreasing (y - x)

FOR j from 0 to n - 1:
    xj, yj = points[j]

    WHILE dq not empty AND xj - points[dq.front].x > k:
        dq.pop_front()

    IF dq not empty:
        i = dq.front
        candidate = yj + xj + (points[i].y - points[i].x)
        best = max(best, candidate)

    curr = yj - xj
    WHILE dq not empty AND (points[dq.back].y - points[dq.back].x) <= curr:
        dq.pop_back()

    dq.push_back(j)

RETURN best
```

#### Python
```python
from collections import deque


def max_value_of_equation_optimal(points, k):
    best = -10**18
    dq = deque()

    for j, (xj, yj) in enumerate(points):
        while dq and xj - points[dq[0]][0] > k:
            dq.popleft()

        if dq:
            i = dq[0]
            best = max(best, yj + xj + points[i][1] - points[i][0])

        curr = yj - xj
        while dq and (points[dq[-1]][1] - points[dq[-1]][0]) <= curr:
            dq.pop()

        dq.append(j)

    return best
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q7. First Negative Integer in Every Window of Size K

### Problem
Given array `nums` and `k`, return first negative integer in each window of size `k`; return `0` if a window has no negative.

Example: `nums = [12,-1,-7,8,-15,30,16,28], k = 3 -> [-1,-1,-7,-15,-15,0]`

### Brute Force Solution

#### Pseudocode
```text
IF k <= 0 OR k > n:
    RETURN []

ans = []
FOR i from 0 to n - k:
    first_neg = 0
    FOR j from i to i + k - 1:
        IF nums[j] < 0:
            first_neg = nums[j]
            BREAK
    APPEND first_neg to ans

RETURN ans
```

#### Python
```python
def first_negative_in_window_bruteforce(nums, k):
    n = len(nums)
    if k <= 0 or k > n:
        return []

    ans = []
    for i in range(n - k + 1):
        first_neg = 0
        for j in range(i, i + k):
            if nums[j] < 0:
                first_neg = nums[j]
                break
        ans.append(first_neg)

    return ans
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)`

### Optimal Solution (Deque of Negative Indices)

#### Pseudocode
```text
IF k <= 0 OR k > n:
    RETURN []

dq = empty deque  # indices where nums[index] < 0
ans = []

FOR i from 0 to n - 1:
    WHILE dq not empty AND dq.front <= i - k:
        dq.pop_front()

    IF nums[i] < 0:
        dq.push_back(i)

    IF i >= k - 1:
        IF dq not empty:
            APPEND nums[dq.front] to ans
        ELSE:
            APPEND 0 to ans

RETURN ans
```

#### Python
```python
from collections import deque


def first_negative_in_window_optimal(nums, k):
    n = len(nums)
    if k <= 0 or k > n:
        return []

    dq = deque()
    ans = []

    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        if x < 0:
            dq.append(i)

        if i >= k - 1:
            ans.append(nums[dq[0]] if dq else 0)

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(k)`

---

## Q8. Minimum Number of K Consecutive Bit Flips

### Problem
Given binary array `nums` and integer `k`, return minimum number of `k`-length consecutive flips needed to make all bits `1`, else `-1`.

Example: `nums = [0,1,0], k = 1 -> 2`

### Brute Force Solution

#### Pseudocode
```text
n = len(nums)
arr = copy(nums)
flips = 0

IF k > n:
    RETURN 0 if all bits already 1 else -1

FOR i from 0 to n - k:
    IF arr[i] == 0:
        flips += 1
        FOR j from i to i + k - 1:
            arr[j] = arr[j] XOR 1

FOR i from n - k + 1 to n - 1:
    IF arr[i] == 0:
        RETURN -1

RETURN flips
```

#### Python
```python
def min_k_bit_flips_bruteforce(nums, k):
    n = len(nums)
    arr = nums[:]
    flips = 0

    if k > n:
        return 0 if all(x == 1 for x in arr) else -1

    for i in range(n - k + 1):
        if arr[i] == 0:
            flips += 1
            for j in range(i, i + k):
                arr[j] ^= 1

    for i in range(n - k + 1, n):
        if arr[i] == 0:
            return -1

    return flips
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(n)` copy

### Optimal Solution (Deque of Active Flips)

#### Pseudocode
```text
n = len(nums)
dq = empty deque  # start indices of active flips
flips = 0

FOR i from 0 to n - 1:
    WHILE dq not empty AND dq.front + k <= i:
        dq.pop_front()

    bit = nums[i]
    IF size(dq) is odd:
        bit = bit XOR 1

    IF bit == 0:
        IF i + k > n:
            RETURN -1
        flips += 1
        dq.push_back(i)

RETURN flips
```

#### Python
```python
from collections import deque


def min_k_bit_flips_optimal(nums, k):
    n = len(nums)
    dq = deque()
    flips = 0

    for i, bit in enumerate(nums):
        while dq and dq[0] + k <= i:
            dq.popleft()

        effective = bit
        if len(dq) % 2 == 1:
            effective ^= 1

        if effective == 0:
            if i + k > n:
                return -1
            flips += 1
            dq.append(i)

    return flips
```

#### Complexity
- Time: `O(n)`
- Space: `O(k)`

---

## Q9. Find the Most Competitive Subsequence

### Problem
Given `nums` and `k`, return lexicographically smallest subsequence of length `k`.

Example: `nums = [3,5,2,6], k = 2 -> [2,6]`

### Brute Force Solution

#### Pseudocode
```text
best = null

FUNCTION dfs(i, path):
    IF length(path) == k:
        IF best is null OR path lexicographically smaller than best:
            best = copy(path)
        RETURN

    IF i == n:
        RETURN

    IF length(path) + (n - i) < k:
        RETURN

    # take
    path.push(nums[i])
    dfs(i + 1, path)
    path.pop()

    # skip
    dfs(i + 1, path)

CALL dfs(0, empty path)
RETURN best if exists else []
```

#### Python
```python
def most_competitive_bruteforce(nums, k):
    n = len(nums)
    best = [None]

    def dfs(i, path):
        if len(path) == k:
            cand = path[:]
            if best[0] is None or cand < best[0]:
                best[0] = cand
            return

        if i == n:
            return

        if len(path) + (n - i) < k:
            return

        path.append(nums[i])
        dfs(i + 1, path)
        path.pop()

        dfs(i + 1, path)

    dfs(0, [])
    return best[0] if best[0] is not None else []
```

#### Complexity
- Time: `O(C(n, k) * k)`
- Space: `O(k)` recursion depth (excluding output tracking)

### Optimal Solution (Monotonic Increasing Stack)

#### Pseudocode
```text
to_remove = n - k
stack = []

FOR x in nums:
    WHILE to_remove > 0 AND stack not empty AND stack.top > x:
        stack.pop()
        to_remove -= 1
    stack.push(x)

RETURN first k elements of stack
```

#### Python
```python
def most_competitive_optimal(nums, k):
    to_remove = len(nums) - k
    stack = []

    for x in nums:
        while to_remove > 0 and stack and stack[-1] > x:
            stack.pop()
            to_remove -= 1
        stack.append(x)

    return stack[:k]
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q10. Maximum Robots Within Budget

### Problem
Given `chargeTimes`, `runningCosts`, and `budget`, return max size of a contiguous robot group such that:
`max(chargeTimes[l:r]) + (r-l+1) * sum(runningCosts[l:r]) <= budget`.

Example: `chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25 -> 3`

### Brute Force Solution

#### Pseudocode
```text
best = 0

FOR left from 0 to n - 1:
    max_charge = 0
    sum_run = 0

    FOR right from left to n - 1:
        max_charge = max(max_charge, chargeTimes[right])
        sum_run += runningCosts[right]

        cost = max_charge + (right - left + 1) * sum_run

        IF cost <= budget:
            best = max(best, right - left + 1)
        ELSE:
            BREAK

RETURN best
```

#### Python
```python
def maximum_robots_bruteforce(charge_times, running_costs, budget):
    n = len(charge_times)
    best = 0

    for left in range(n):
        max_charge = 0
        sum_run = 0

        for right in range(left, n):
            max_charge = max(max_charge, charge_times[right])
            sum_run += running_costs[right]

            cost = max_charge + (right - left + 1) * sum_run
            if cost <= budget:
                best = max(best, right - left + 1)
            else:
                break

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Sliding Window + Deque for Max Charge)

#### Pseudocode
```text
left = 0
sum_run = 0
best = 0
dq = empty deque  # indices with decreasing chargeTimes

FOR right from 0 to n - 1:
    sum_run += runningCosts[right]

    WHILE dq not empty AND chargeTimes[dq.back] <= chargeTimes[right]:
        dq.pop_back()
    dq.push_back(right)

    WHILE dq not empty AND chargeTimes[dq.front] + (right - left + 1) * sum_run > budget:
        IF dq.front == left:
            dq.pop_front()
        sum_run -= runningCosts[left]
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
from collections import deque


def maximum_robots_optimal(charge_times, running_costs, budget):
    left = 0
    sum_run = 0
    best = 0
    dq = deque()

    for right in range(len(charge_times)):
        sum_run += running_costs[right]

        while dq and charge_times[dq[-1]] <= charge_times[right]:
            dq.pop()
        dq.append(right)

        while dq and charge_times[dq[0]] + (right - left + 1) * sum_run > budget:
            if dq[0] == left:
                dq.popleft()
            sum_run -= running_costs[left]
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Rapid Recall Checklist

- Deque usually stores indices, not raw values.
- Operation order: expire front -> remove dominated back -> push current -> query front.
- For prefix deque problems, pop front repeatedly to minimize answer.
- For DP window max, keep deque decreasing by DP values.
- Comparator strictness controls duplicate handling and correctness.
