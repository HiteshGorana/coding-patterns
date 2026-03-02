# Pattern 07 Interview Playbook: Binary Search on Answer

This playbook is aligned with [Pattern 07: Binary Search on Answer](../07-binary-search-on-answer.md).

Use it when answer is numeric and feasibility is monotonic.

## Pattern Snapshot

| Prompt shape | Search target | Feasibility direction |
|---|---|---|
| minimum feasible rate/capacity/day | first `True` boundary | infeasible -> feasible |
| maximum feasible distance/value | last `True` boundary | feasible -> infeasible |
| partition/load minimization | `max(nums)` to `sum(nums)` | larger limit => easier |
| distribution/rate minimization | `1` to max quantity | larger divisor/rate => easier |
| spacing maximization | `1` to max gap | larger gap => harder |
| floating-time constraints | integer speed + real check | larger speed => easier |

## Query-Update Rules

- Build a predicate `can(x)` that is monotonic.
- Derive safe search bounds that must include the answer.
- For minimum feasible answer: keep left side when `can(mid)` is true.
- For maximum feasible answer: keep right side when `can(mid)` is true.

---

## Q1. Koko Eating Bananas

### Problem
Given `piles` and `h`, return minimum integer eating speed `k` so Koko finishes within `h` hours.

Example: `piles = [3,6,7,11], h = 8 -> 4`

### Brute Force Solution

#### Pseudocode
```text
FOR k from 1 to max(piles):
    hours = 0
    FOR p in piles:
        hours += ceil(p / k)
    IF hours <= h:
        RETURN k
RETURN -1
```

#### Python
```python
def koko_bruteforce(piles, h):
    max_p = max(piles)

    for k in range(1, max_p + 1):
        hours = 0
        for p in piles:
            hours += (p + k - 1) // k
        if hours <= h:
            return k

    return -1
```

#### Complexity
- Time: `O(max(piles) * n)`
- Space: `O(1)`

### Optimal Solution (Min Feasible Speed)

#### Pseudocode
```text
l = 1, r = max(piles)

WHILE l < r:
    mid = l + (r - l) // 2
    hours = sum(ceil(p / mid) for p in piles)

    IF hours <= h:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def koko_optimal(piles, h):
    l, r = 1, max(piles)

    while l < r:
        mid = l + (r - l) // 2
        hours = 0
        for p in piles:
            hours += (p + mid - 1) // mid

        if hours <= h:
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(n log max(piles))`
- Space: `O(1)`

---

## Q2. Capacity To Ship Packages Within D Days

### Problem
Given `weights` and `days`, return minimum ship capacity to deliver all packages in order within `days`.

Example: `weights = [1,2,3,4,5,6,7,8,9,10], days = 5 -> 15`

### Brute Force Solution

#### Pseudocode
```text
FOR cap from max(weights) to sum(weights):
    needed_days = 1
    curr = 0
    FOR w in weights:
        IF curr + w <= cap:
            curr += w
        ELSE:
            needed_days += 1
            curr = w
    IF needed_days <= days:
        RETURN cap
RETURN -1
```

#### Python
```python
def ship_capacity_bruteforce(weights, days):
    lo = max(weights)
    hi = sum(weights)

    for cap in range(lo, hi + 1):
        needed_days = 1
        curr = 0

        for w in weights:
            if curr + w <= cap:
                curr += w
            else:
                needed_days += 1
                curr = w

        if needed_days <= days:
            return cap

    return -1
```

#### Complexity
- Time: `O((sum-max) * n)`
- Space: `O(1)`

### Optimal Solution (Min Feasible Capacity)

#### Pseudocode
```text
l = max(weights), r = sum(weights)

WHILE l < r:
    mid = l + (r - l) // 2
    needed_days = days_required(mid)

    IF needed_days <= days:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def ship_capacity_optimal(weights, days):
    def required_days(cap):
        needed = 1
        curr = 0

        for w in weights:
            if curr + w <= cap:
                curr += w
            else:
                needed += 1
                curr = w

        return needed

    l, r = max(weights), sum(weights)

    while l < r:
        mid = l + (r - l) // 2
        if required_days(mid) <= days:
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(n log(sum(weights)))`
- Space: `O(1)`

---

## Q3. Split Array Largest Sum

### Problem
Given `nums` and `m`, split into `m` non-empty contiguous subarrays minimizing largest subarray sum.

Example: `nums = [7,2,5,10,8], m = 2 -> 18`

### Brute Force Solution

#### Pseudocode
```text
DP solution:
Let dp[i][k] = min possible largest sum by splitting first i elements into k groups
Transition over cut point j
RETURN dp[n][m]
```

#### Python
```python
def split_array_bruteforce(nums, m):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    inf = 10**30
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for k in range(1, min(i, m) + 1):
            for j in range(k - 1, i):
                largest = max(dp[j][k - 1], prefix[i] - prefix[j])
                if largest < dp[i][k]:
                    dp[i][k] = largest

    return dp[n][m]
```

#### Complexity
- Time: `O(n^2 * m)`
- Space: `O(n * m)`

### Optimal Solution (Min Feasible Largest Sum)

#### Pseudocode
```text
l = max(nums), r = sum(nums)

WHILE l < r:
    mid = l + (r - l) // 2
    parts = partitions_needed_with_limit(mid)

    IF parts <= m:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def split_array_optimal(nums, m):
    def parts_needed(limit):
        parts = 1
        curr = 0

        for x in nums:
            if curr + x <= limit:
                curr += x
            else:
                parts += 1
                curr = x

        return parts

    l, r = max(nums), sum(nums)

    while l < r:
        mid = l + (r - l) // 2
        if parts_needed(mid) <= m:
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(n log(sum(nums)))`
- Space: `O(1)`

---

## Q4. Minimized Maximum of Products Distributed to Any Store

### Problem
Given `n` stores and `quantities` for product types, return minimum possible maximum products assigned to any store.

Example: `n = 6, quantities = [11,6] -> 3`

### Brute Force Solution

#### Pseudocode
```text
FOR x from 1 to max(quantities):
    stores_needed = sum(ceil(q / x) for q in quantities)
    IF stores_needed <= n:
        RETURN x
RETURN -1
```

#### Python
```python
def minimized_maximum_bruteforce(n, quantities):
    max_q = max(quantities)

    for x in range(1, max_q + 1):
        needed = 0
        for q in quantities:
            needed += (q + x - 1) // x
        if needed <= n:
            return x

    return -1
```

#### Complexity
- Time: `O(max(quantities) * len(quantities))`
- Space: `O(1)`

### Optimal Solution (Min Feasible Max-per-Store)

#### Pseudocode
```text
l = 1, r = max(quantities)
WHILE l < r:
    mid = l + (r - l) // 2
    needed = sum(ceil(q / mid) for q in quantities)

    IF needed <= n:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def minimized_maximum_optimal(n, quantities):
    l, r = 1, max(quantities)

    while l < r:
        mid = l + (r - l) // 2
        needed = 0

        for q in quantities:
            needed += (q + mid - 1) // mid

        if needed <= n:
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(len(quantities) * log(max(quantities)))`
- Space: `O(1)`

---

## Q5. Magnetic Force Between Two Balls

### Problem
Given basket positions and integer `m`, place `m` balls maximizing minimum pairwise distance.

Example: `position = [1,2,3,4,7], m = 3 -> 3`

### Brute Force Solution

#### Pseudocode
```text
SORT positions
best = 0
FOR d from 1 to max_gap:
    IF can_place_with_distance(d):
        best = d
RETURN best
```

#### Python
```python
def magnetic_force_bruteforce(position, m):
    position.sort()
    max_gap = position[-1] - position[0]

    def can_place(d):
        count = 1
        last = position[0]

        for x in position[1:]:
            if x - last >= d:
                count += 1
                last = x
                if count >= m:
                    return True

        return False

    best = 0
    for d in range(1, max_gap + 1):
        if can_place(d):
            best = d

    return best
```

#### Complexity
- Time: `O(max_gap * n)`
- Space: `O(1)`

### Optimal Solution (Max Feasible Distance)

#### Pseudocode
```text
SORT positions
l = 1, r = max_gap
WHILE l < r:
    mid = l + (r - l + 1) // 2  # upper mid for last true
    IF can_place(mid):
        l = mid
    ELSE:
        r = mid - 1
RETURN l
```

#### Python
```python
def magnetic_force_optimal(position, m):
    position.sort()

    def can_place(d):
        count = 1
        last = position[0]

        for x in position[1:]:
            if x - last >= d:
                count += 1
                last = x
                if count >= m:
                    return True

        return False

    l, r = 1, position[-1] - position[0]

    while l < r:
        mid = l + (r - l + 1) // 2
        if can_place(mid):
            l = mid
        else:
            r = mid - 1

    return l
```

#### Complexity
- Time: `O(n log(max_gap))`
- Space: `O(1)`

---

## Q6. Minimum Number of Days to Make m Bouquets

### Problem
Given `bloomDay`, integers `m` and `k`, return minimum day to make `m` bouquets of `k` adjacent flowers. If impossible, return `-1`.

Example: `bloomDay = [1,10,3,10,2], m = 3, k = 1 -> 3`

### Brute Force Solution

#### Pseudocode
```text
IF m * k > n: RETURN -1
FOR day from min(bloomDay) to max(bloomDay):
    bouquets = bouquets_possible(day)
    IF bouquets >= m:
        RETURN day
RETURN -1
```

#### Python
```python
def min_days_bouquets_bruteforce(bloomDay, m, k):
    n = len(bloomDay)
    if m * k > n:
        return -1

    low = min(bloomDay)
    high = max(bloomDay)

    for day in range(low, high + 1):
        bouquets = 0
        run = 0

        for b in bloomDay:
            if b <= day:
                run += 1
                if run == k:
                    bouquets += 1
                    run = 0
            else:
                run = 0

        if bouquets >= m:
            return day

    return -1
```

#### Complexity
- Time: `O((max_day - min_day + 1) * n)`
- Space: `O(1)`

### Optimal Solution (Min Feasible Day)

#### Pseudocode
```text
IF m * k > n: RETURN -1
l = min(bloomDay), r = max(bloomDay)

WHILE l < r:
    mid = l + (r - l) // 2
    bouquets = bouquets_possible(mid)

    IF bouquets >= m:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def min_days_bouquets_optimal(bloomDay, m, k):
    n = len(bloomDay)
    if m * k > n:
        return -1

    def can(day):
        bouquets = 0
        run = 0

        for b in bloomDay:
            if b <= day:
                run += 1
                if run == k:
                    bouquets += 1
                    run = 0
            else:
                run = 0

        return bouquets >= m

    l, r = min(bloomDay), max(bloomDay)

    while l < r:
        mid = l + (r - l) // 2
        if can(mid):
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(n log(max_day))`
- Space: `O(1)`

---

## Q7. Find the Smallest Divisor Given a Threshold

### Problem
Given integer array `nums` and `threshold`, return smallest divisor so sum of rounded-up divisions is <= `threshold`.

Example: `nums = [1,2,5,9], threshold = 6 -> 5`

### Brute Force Solution

#### Pseudocode
```text
FOR d from 1 to max(nums):
    total = sum(ceil(x / d) for x in nums)
    IF total <= threshold:
        RETURN d
RETURN -1
```

#### Python
```python
def smallest_divisor_bruteforce(nums, threshold):
    max_v = max(nums)

    for d in range(1, max_v + 1):
        total = 0
        for x in nums:
            total += (x + d - 1) // d
        if total <= threshold:
            return d

    return -1
```

#### Complexity
- Time: `O(max(nums) * n)`
- Space: `O(1)`

### Optimal Solution (Min Feasible Divisor)

#### Pseudocode
```text
l = 1, r = max(nums)
WHILE l < r:
    mid = l + (r - l) // 2
    total = sum(ceil(x / mid) for x in nums)

    IF total <= threshold:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def smallest_divisor_optimal(nums, threshold):
    l, r = 1, max(nums)

    while l < r:
        mid = l + (r - l) // 2
        total = 0

        for x in nums:
            total += (x + mid - 1) // mid

        if total <= threshold:
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(n log(max(nums)))`
- Space: `O(1)`

---

## Q8. Aggressive Cows

### Problem
Given stall positions and number of cows `k`, place cows to maximize minimum pairwise distance.

Example: `stalls = [1,2,4,8,9], k = 3 -> 3`

### Brute Force Solution

#### Pseudocode
```text
SORT stalls
best = 0
FOR d from 1 to max_gap:
    IF can_place(d):
        best = d
RETURN best
```

#### Python
```python
def aggressive_cows_bruteforce(stalls, k):
    stalls.sort()
    max_gap = stalls[-1] - stalls[0]

    def can_place(d):
        count = 1
        last = stalls[0]

        for x in stalls[1:]:
            if x - last >= d:
                count += 1
                last = x
                if count >= k:
                    return True

        return False

    best = 0
    for d in range(1, max_gap + 1):
        if can_place(d):
            best = d

    return best
```

#### Complexity
- Time: `O(max_gap * n)`
- Space: `O(1)`

### Optimal Solution (Max Feasible Distance)

#### Pseudocode
```text
SORT stalls
l = 1, r = max_gap
WHILE l < r:
    mid = l + (r - l + 1) // 2
    IF can_place(mid):
        l = mid
    ELSE:
        r = mid - 1
RETURN l
```

#### Python
```python
def aggressive_cows_optimal(stalls, k):
    stalls.sort()

    def can_place(d):
        count = 1
        last = stalls[0]

        for x in stalls[1:]:
            if x - last >= d:
                count += 1
                last = x
                if count >= k:
                    return True

        return False

    l, r = 1, stalls[-1] - stalls[0]

    while l < r:
        mid = l + (r - l + 1) // 2
        if can_place(mid):
            l = mid
        else:
            r = mid - 1

    return l
```

#### Complexity
- Time: `O(n log(max_gap))`
- Space: `O(1)`

---

## Q9. Maximum Candies Allocated to K Children

### Problem
Given `candies` piles and `k` children, each child gets equal candies from one pile split, return maximum candies per child.

Example: `candies = [5,8,6], k = 3 -> 5`

### Brute Force Solution

#### Pseudocode
```text
IF sum(candies) < k: RETURN 0
best = 0
FOR x from 1 to max(candies):
    children = sum(floor(pile / x) for pile in candies)
    IF children >= k:
        best = x
RETURN best
```

#### Python
```python
def max_candies_bruteforce(candies, k):
    if sum(candies) < k:
        return 0

    best = 0
    max_c = max(candies)

    for x in range(1, max_c + 1):
        children = 0
        for pile in candies:
            children += pile // x
        if children >= k:
            best = x

    return best
```

#### Complexity
- Time: `O(max(candies) * n)`
- Space: `O(1)`

### Optimal Solution (Max Feasible Candies Per Child)

#### Pseudocode
```text
IF sum(candies) < k: RETURN 0
l = 1, r = max(candies)
WHILE l < r:
    mid = l + (r - l + 1) // 2
    children = sum(floor(pile / mid) for pile in candies)

    IF children >= k:
        l = mid
    ELSE:
        r = mid - 1

RETURN l
```

#### Python
```python
def max_candies_optimal(candies, k):
    if sum(candies) < k:
        return 0

    l, r = 1, max(candies)

    while l < r:
        mid = l + (r - l + 1) // 2
        children = 0

        for pile in candies:
            children += pile // mid

        if children >= k:
            l = mid
        else:
            r = mid - 1

    return l
```

#### Complexity
- Time: `O(n log(max(candies)))`
- Space: `O(1)`

---

## Q10. Minimum Speed to Arrive on Time

### Problem
Given `dist` and real `hour`, return minimum integer speed to arrive on time, where all but last segment times are rounded up. If impossible, return `-1`.

Example: `dist = [1,3,2], hour = 6 -> 1`

### Brute Force Solution

#### Pseudocode
```text
n = length(dist)
IF hour <= n - 1: RETURN -1

FOR speed from 1 to 10^7:
    time = 0
    FOR i from 0 to n - 2:
        time += ceil(dist[i] / speed)
    time += dist[n - 1] / speed

    IF time <= hour:
        RETURN speed

RETURN -1
```

#### Python
```python
def min_speed_on_time_bruteforce(dist, hour):
    n = len(dist)
    if hour <= n - 1:
        return -1

    for speed in range(1, 10**7 + 1):
        total = 0.0

        for i in range(n - 1):
            total += (dist[i] + speed - 1) // speed
        total += dist[-1] / speed

        if total <= hour:
            return speed

    return -1
```

#### Complexity
- Time: `O(10^7 * n)` worst case
- Space: `O(1)`

### Optimal Solution (Min Feasible Speed)

#### Pseudocode
```text
n = length(dist)
IF hour <= n - 1: RETURN -1
l = 1, r = 10^7

WHILE l < r:
    mid = l + (r - l) // 2
    time = travel_time(mid)

    IF time <= hour:
        r = mid
    ELSE:
        l = mid + 1

RETURN l
```

#### Python
```python
def min_speed_on_time_optimal(dist, hour):
    n = len(dist)
    if hour <= n - 1:
        return -1

    def can(speed):
        total = 0.0

        for i in range(n - 1):
            total += (dist[i] + speed - 1) // speed
        total += dist[-1] / speed

        return total <= hour

    l, r = 1, 10**7

    while l < r:
        mid = l + (r - l) // 2
        if can(mid):
            r = mid
        else:
            l = mid + 1

    return l if can(l) else -1
```

#### Complexity
- Time: `O(n log 10^7)`
- Space: `O(1)`

---

## Rapid Recall Checklist

- Prove monotonicity of `can(x)` before searching.
- Set bounds that definitely contain the answer.
- Use lower-mid for first true, upper-mid for last true.
- Keep feasibility check pure and deterministic.
