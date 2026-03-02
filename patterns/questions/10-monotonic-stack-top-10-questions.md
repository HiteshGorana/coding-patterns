# Pattern 10 Interview Playbook: Monotonic Stack

This playbook is aligned with [Pattern 10: Monotonic Stack](../10-monotonic-stack.md).

Use it when you need nearest greater/smaller boundaries in linear time.

## Pattern Snapshot

| Prompt shape | Stack type | Pop condition |
|---|---|---|
| next greater to right | decreasing stack | pop while `stack_top < current` |
| next smaller to right | increasing stack | pop while `stack_top > current` |
| previous boundary queries | monotonic stack by index | cleanup then read top |
| histogram/subarray spans | increasing stack of indices | pop on smaller incoming bar |
| circular next-greater | decreasing + 2-pass index trick | same as NGE with modulo index |
| collision/transition simulation | stack of unresolved entities | pop invalid/stale candidates |

## Query-Update Rules

- Store indices on stack, not just values, when distance or boundaries are needed.
- Pop until monotonic invariant is restored.
- Resolve popped indices immediately from current index.
- If unresolved after scan, keep default answer (e.g., `-1`, `0`, or `-1.0`).

---

## Q1. Daily Temperatures

### Problem
Given daily temperatures, return for each day how many days until a warmer temperature. If none, return `0`.

Example: `temps = [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]`

### Brute Force Solution

#### Pseudocode
```text
ans = [0] * n
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        IF temps[j] > temps[i]:
            ans[i] = j - i
            BREAK
RETURN ans
```

#### Python
```python
def daily_temperatures_bruteforce(temps):
    n = len(temps)
    ans = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temps[j] > temps[i]:
                ans[i] = j - i
                break

    return ans
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)` extra

### Optimal Solution (Decreasing Stack of Indices)

#### Pseudocode
```text
ans = [0] * n
stack = []  # indices with decreasing temperatures

FOR i from 0 to n - 1:
    WHILE stack not empty AND temps[stack.top] < temps[i]:
        j = stack.pop()
        ans[j] = i - j
    PUSH i

RETURN ans
```

#### Python
```python
def daily_temperatures_optimal(temps):
    ans = [0] * len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q2. Next Greater Element I

### Problem
Given `nums1` subset of `nums2`, for each value in `nums1` find next greater element in `nums2`, else `-1`.

Example: `nums1 = [4,1,2], nums2 = [1,3,4,2] -> [-1,3,-1]`

### Brute Force Solution

#### Pseudocode
```text
ans = []
FOR x in nums1:
    find index i of x in nums2
    next = -1
    FOR j from i+1 to len(nums2)-1:
        IF nums2[j] > x:
            next = nums2[j]
            BREAK
    APPEND next
RETURN ans
```

#### Python
```python
def next_greater_i_bruteforce(nums1, nums2):
    ans = []

    for x in nums1:
        i = nums2.index(x)
        nxt = -1

        for j in range(i + 1, len(nums2)):
            if nums2[j] > x:
                nxt = nums2[j]
                break

        ans.append(nxt)

    return ans
```

#### Complexity
- Time: `O(len(nums1) * len(nums2))`
- Space: `O(1)` extra

### Optimal Solution (Monotonic Stack + Map)

#### Pseudocode
```text
next_map = {}
stack = []  # decreasing values

FOR x in nums2:
    WHILE stack not empty AND stack.top < x:
        next_map[stack.pop()] = x
    PUSH x

FOR remaining values in stack:
    next_map[value] = -1

RETURN [next_map[x] for x in nums1]
```

#### Python
```python
def next_greater_i_optimal(nums1, nums2):
    next_map = {}
    stack = []

    for x in nums2:
        while stack and stack[-1] < x:
            next_map[stack.pop()] = x
        stack.append(x)

    while stack:
        next_map[stack.pop()] = -1

    return [next_map[x] for x in nums1]
```

#### Complexity
- Time: `O(len(nums1) + len(nums2))`
- Space: `O(len(nums2))`

---

## Q3. Next Greater Element II

### Problem
Given circular array `nums`, return next greater element for each index, else `-1`.

Example: `nums = [1,2,1] -> [2,-1,2]`

### Brute Force Solution

#### Pseudocode
```text
ans = [-1] * n
FOR i from 0 to n - 1:
    FOR step from 1 to n - 1:
        j = (i + step) mod n
        IF nums[j] > nums[i]:
            ans[i] = nums[j]
            BREAK
RETURN ans
```

#### Python
```python
def next_greater_ii_bruteforce(nums):
    n = len(nums)
    ans = [-1] * n

    for i in range(n):
        for step in range(1, n):
            j = (i + step) % n
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break

    return ans
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)` extra

### Optimal Solution (2N Reverse Pass + Decreasing Stack)

#### Pseudocode
```text
ans = [-1] * n
stack = []  # decreasing values

FOR i from 2n - 1 down to 0:
    x = nums[i mod n]

    WHILE stack not empty AND stack.top <= x:
        stack.pop()

    IF i < n:
        ans[i] = stack.top if stack not empty else -1

    PUSH x

RETURN ans
```

#### Python
```python
def next_greater_ii_optimal(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):
        x = nums[i % n]

        while stack and stack[-1] <= x:
            stack.pop()

        if i < n:
            ans[i] = stack[-1] if stack else -1

        stack.append(x)

    return ans
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q4. Largest Rectangle in Histogram

### Problem
Given bar heights, return largest rectangle area in histogram.

Example: `heights = [2,1,5,6,2,3] -> 10`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    min_h = infinity
    FOR j from i to n - 1:
        min_h = min(min_h, heights[j])
        best = max(best, min_h * (j - i + 1))
RETURN best
```

#### Python
```python
def largest_rectangle_bruteforce(heights):
    n = len(heights)
    best = 0

    for i in range(n):
        min_h = 10**18
        for j in range(i, n):
            min_h = min(min_h, heights[j])
            best = max(best, min_h * (j - i + 1))

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Increasing Stack + Sentinel)

#### Pseudocode
```text
best = 0
stack = []  # increasing heights indices

FOR i from 0 to n:
    curr = 0 if i == n else heights[i]

    WHILE stack not empty AND heights[stack.top] > curr:
        h = heights[stack.pop()]
        left = stack.top if stack not empty else -1
        width = i - left - 1
        best = max(best, h * width)

    PUSH i

RETURN best
```

#### Python
```python
def largest_rectangle_optimal(heights):
    best = 0
    stack = []

    for i in range(len(heights) + 1):
        curr = 0 if i == len(heights) else heights[i]

        while stack and heights[stack[-1]] > curr:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, h * width)

        stack.append(i)

    return best
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q5. Trapping Rain Water

### Problem
Given elevation map `height`, return total trapped rain water.

Example: `height = [0,1,0,2,1,0,1,3,2,1,2,1] -> 6`

### Brute Force Solution

#### Pseudocode
```text
water = 0
FOR i from 0 to n - 1:
    left_max = max(height[0..i])
    right_max = max(height[i..n-1])
    water += min(left_max, right_max) - height[i]
RETURN water
```

#### Python
```python
def trap_rain_bruteforce(height):
    water = 0

    for i in range(len(height)):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]

    return water
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Monotonic Stack of Bars)

#### Pseudocode
```text
stack = []  # decreasing heights indices
water = 0

FOR i from 0 to n - 1:
    WHILE stack not empty AND height[i] > height[stack.top]:
        mid = stack.pop()
        IF stack empty:
            BREAK

        left = stack.top
        width = i - left - 1
        bounded = min(height[left], height[i]) - height[mid]
        water += width * bounded

    PUSH i

RETURN water
```

#### Python
```python
def trap_rain_optimal(height):
    stack = []
    water = 0

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            mid = stack.pop()
            if not stack:
                break

            left = stack[-1]
            width = i - left - 1
            bounded = min(height[left], h) - height[mid]
            water += width * bounded

        stack.append(i)

    return water
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q6. Remove K Digits

### Problem
Given numeric string `num` and `k`, remove `k` digits to get smallest possible number.

Example: `num = "1432219", k = 3 -> "1219"`

### Brute Force Solution

#### Pseudocode
```text
best = infinity_string

FUNCTION dfs(curr_string, k_left, start_index):
    IF k_left == 0:
        candidate = strip_leading_zeros(curr_string)
        update best
        RETURN

    FOR i from start_index to len(curr_string)-1:
        next = curr_string without char i
        dfs(next, k_left - 1, i)

CALL dfs(num, k, 0)
RETURN best (or "0")
```

#### Python
```python
def remove_k_digits_bruteforce(num, k):
    best = [None]

    def normalize(s):
        s = s.lstrip('0')
        return s if s else '0'

    def better(a, b):
        if b is None:
            return True
        if len(a) != len(b):
            return len(a) < len(b)
        return a < b

    def dfs(s, k_left, start):
        if k_left == 0:
            cand = normalize(s)
            if better(cand, best[0]):
                best[0] = cand
            return

        for i in range(start, len(s)):
            dfs(s[:i] + s[i + 1:], k_left - 1, i)

    dfs(num, k, 0)
    return best[0] if best[0] is not None else '0'
```

#### Complexity
- Time: exponential in `k`
- Space: recursion + string copies

### Optimal Solution (Increasing Stack Greedy)

#### Pseudocode
```text
stack = []
FOR digit in num:
    WHILE k > 0 AND stack not empty AND stack.top > digit:
        stack.pop()
        k -= 1
    PUSH digit

WHILE k > 0:
    stack.pop()
    k -= 1

result = strip leading zeros from joined stack
RETURN result if non-empty else "0"
```

#### Python
```python
def remove_k_digits_optimal(num, k):
    stack = []

    for ch in num:
        while k > 0 and stack and stack[-1] > ch:
            stack.pop()
            k -= 1
        stack.append(ch)

    while k > 0 and stack:
        stack.pop()
        k -= 1

    res = ''.join(stack).lstrip('0')
    return res if res else '0'
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q7. Sum of Subarray Minimums

### Problem
Given `arr`, return sum of minimum of every subarray, modulo `10^9+7`.

Example: `arr = [3,1,2,4] -> 17`

### Brute Force Solution

#### Pseudocode
```text
ans = 0
FOR i from 0 to n - 1:
    min_val = infinity
    FOR j from i to n - 1:
        min_val = min(min_val, arr[j])
        ans += min_val
RETURN ans mod MOD
```

#### Python
```python
def sum_subarray_mins_bruteforce(arr):
    mod = 10**9 + 7
    ans = 0

    for i in range(len(arr)):
        mn = 10**18
        for j in range(i, len(arr)):
            mn = min(mn, arr[j])
            ans = (ans + mn) % mod

    return ans
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Contribution via Two Monotonic Passes)

#### Pseudocode
```text
left[i] = distance to previous strictly smaller element
right[i] = distance to next smaller-or-equal element

ans = sum(arr[i] * left[i] * right[i]) mod MOD
```

#### Python
```python
def sum_subarray_mins_optimal(arr):
    mod = 10**9 + 7
    n = len(arr)

    left = [0] * n
    right = [0] * n

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = i - (stack[-1] if stack else -1)
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        right[i] = (stack[-1] if stack else n) - i
        stack.append(i)

    ans = 0
    for i in range(n):
        ans = (ans + arr[i] * left[i] * right[i]) % mod

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q8. Online Stock Span

### Problem
Design `StockSpanner` with `next(price)` returning span of current price (consecutive days up to today with price <= current).

Example sequence: prices `[100,80,60,70,60,75,85] -> spans [1,1,1,2,1,4,6]`

### Brute Force Solution

#### Pseudocode
```text
STORE all previous prices

FUNCTION next(price):
    APPEND price
    span = 1
    i = previous index
    WHILE i >= 0 AND prices[i] <= price:
        span += 1
        i -= 1
    RETURN span
```

#### Python
```python
class StockSpannerBruteforce:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2

        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span
```

#### Complexity
- Per call: worst `O(n)`
- Space: `O(n)`

### Optimal Solution (Monotonic Decreasing Stack with Aggregated Span)

#### Pseudocode
```text
stack holds pairs (price, span)

FUNCTION next(price):
    span = 1
    WHILE stack not empty AND stack.top.price <= price:
        span += stack.pop().span

    PUSH (price, span)
    RETURN span
```

#### Python
```python
class StockSpannerOptimal:
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
```

#### Complexity
- Amortized per call: `O(1)`
- Space: `O(n)`

---

## Q9. Asteroid Collision

### Problem
Given asteroid list with signs as directions and magnitude as size, return final state after all collisions.

Example: `asteroids = [5,10,-5] -> [5,10]`

### Brute Force Solution

#### Pseudocode
```text
arr = copy(asteroids)
changed = True

WHILE changed:
    changed = False
    i = 0
    next_arr = []

    WHILE i < len(arr):
        IF i+1 < len(arr) AND arr[i] > 0 AND arr[i+1] < 0:
            resolve collision between pair
            changed = True
            i += 2
        ELSE:
            APPEND arr[i] to next_arr
            i += 1

    arr = next_arr

RETURN arr
```

#### Python
```python
def asteroid_collision_bruteforce(asteroids):
    arr = asteroids[:]
    changed = True

    while changed:
        changed = False
        i = 0
        nxt = []

        while i < len(arr):
            if i + 1 < len(arr) and arr[i] > 0 and arr[i + 1] < 0:
                a = arr[i]
                b = arr[i + 1]

                if abs(a) > abs(b):
                    nxt.append(a)
                elif abs(a) < abs(b):
                    nxt.append(b)
                else:
                    pass

                changed = True
                i += 2
            else:
                nxt.append(arr[i])
                i += 1

        arr = nxt

    return arr
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(n)`

### Optimal Solution (Stack Simulation)

#### Pseudocode
```text
stack = []
FOR x in asteroids:
    alive = True

    WHILE alive AND x < 0 AND stack not empty AND stack.top > 0:
        IF stack.top < -x:
            stack.pop()
            CONTINUE
        IF stack.top == -x:
            stack.pop()
        alive = False

    IF alive:
        PUSH x

RETURN stack
```

#### Python
```python
def asteroid_collision_optimal(asteroids):
    stack = []

    for x in asteroids:
        alive = True

        while alive and x < 0 and stack and stack[-1] > 0:
            if stack[-1] < -x:
                stack.pop()
                continue
            if stack[-1] == -x:
                stack.pop()
            alive = False

        if alive:
            stack.append(x)

    return stack
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Q10. Car Fleet II

### Problem
Given cars `[position, speed]` sorted by position increasing, return collision time for each car with next car ahead, else `-1`.

Example: `cars = [[1,2],[2,1],[4,3],[7,2]] -> [1.0,-1.0,3.0,-1.0]`

### Brute Force Solution

#### Pseudocode
```text
ans = [-1] * n

FOR i from n-1 downto 0:
    best_time = infinity

    FOR j from i+1 to n-1:
        IF speed[i] <= speed[j]:
            CONTINUE

        t = (pos[j] - pos[i]) / (speed[i] - speed[j])

        IF ans[j] == -1 OR t <= ans[j]:
            best_time = min(best_time, t)

    IF best_time != infinity:
        ans[i] = best_time

RETURN ans
```

#### Python
```python
def car_fleet_ii_bruteforce(cars):
    n = len(cars)
    ans = [-1.0] * n

    for i in range(n - 1, -1, -1):
        best = float('inf')
        p, s = cars[i]

        for j in range(i + 1, n):
            p2, s2 = cars[j]
            if s <= s2:
                continue

            t = (p2 - p) / (s - s2)
            if ans[j] == -1.0 or t <= ans[j]:
                best = min(best, t)

        if best < float('inf'):
            ans[i] = best

    return ans
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(n)`

### Optimal Solution (Monotonic Candidate Stack from Right)

#### Pseudocode
```text
ans = [-1] * n
stack = []  # candidate car indices ahead

FOR i from n-1 downto 0:
    p, s = cars[i]

    WHILE stack not empty:
        j = stack.top
        p2, s2 = cars[j]

        IF s <= s2:
            POP stack
            CONTINUE

        t = (p2 - p) / (s - s2)

        IF ans[j] == -1 OR t <= ans[j]:
            BREAK

        POP stack

    IF stack not empty:
        j = stack.top
        ans[i] = (cars[j].pos - p) / (s - cars[j].speed)

    PUSH i

RETURN ans
```

#### Python
```python
def car_fleet_ii_optimal(cars):
    n = len(cars)
    ans = [-1.0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        p, s = cars[i]

        while stack:
            j = stack[-1]
            p2, s2 = cars[j]

            if s <= s2:
                stack.pop()
                continue

            t = (p2 - p) / (s - s2)
            if ans[j] == -1.0 or t <= ans[j]:
                break

            stack.pop()

        if stack:
            j = stack[-1]
            ans[i] = (cars[j][0] - p) / (s - cars[j][1])

        stack.append(i)

    return ans
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(n)`

---

## Rapid Recall Checklist

- Choose increasing vs decreasing stack based on greater/smaller query.
- Push and pop each index at most once (amortized `O(n)` proof).
- Use strict/non-strict comparator carefully to avoid duplicate-count errors.
- Keep defaults for unresolved entries (`0`, `-1`, `-1.0`) and finalize cleanly.
