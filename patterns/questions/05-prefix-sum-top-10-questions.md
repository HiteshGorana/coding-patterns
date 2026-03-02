# Pattern 05 Interview Playbook: Prefix Sum

This playbook is aligned with [Pattern 05: Prefix Sum](../05-prefix-sum.md).

Use it when repeated range aggregation or cumulative-state comparisons are needed.

## Pattern Snapshot

| Prompt shape | Store this state | Query |
|---|---|---|
| range sum query | `prefix[i] = sum(nums[:i])` | `sum(l..r) = prefix[r+1] - prefix[l]` |
| count subarrays by sum | prefix frequency map | add `freq[prefix - target]` |
| modulo divisibility subarrays | remainder frequency map | count equal remainders |
| max-length exact sum | first index of prefix sum | use earliest occurrence |
| range increment updates | difference array | prefix-rebuild final values |
| balance of two values (0/1) | transformed prefix/balance | same balance => valid interval |

## Query-Update Rules

- For immutable range queries, precompute prefix once and answer in O(1).
- For counting subarrays, update answer before inserting current prefix when needed.
- For longest-length objectives, store first occurrence only.
- For interval add updates, use difference array then one prefix pass to materialize.

---

## Q1. Range Sum Query - Immutable

### Problem
Design a structure for immutable array range-sum queries.

Example: `nums = [-2,0,3,-5,2,-1], sumRange(0,2) = 1`

### Brute Force Solution

#### Pseudocode
```text
STORE nums

FUNCTION sumRange(left, right):
    total = 0
    FOR i from left to right:
        total += nums[i]
    RETURN total
```

#### Python
```python
class NumArrayBruteforce:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total
```

#### Complexity
- Build: `O(1)`
- Query: `O(right - left + 1)`
- Space: `O(1)` extra

### Optimal Solution (Prefix Sum Array)

#### Pseudocode
```text
BUILD prefix where prefix[0] = 0
FOR each x in nums:
    APPEND prefix[-1] + x

FUNCTION sumRange(left, right):
    RETURN prefix[right + 1] - prefix[left]
```

#### Python
```python
class NumArrayOptimal:
    def __init__(self, nums):
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

#### Complexity
- Build: `O(n)`
- Query: `O(1)`
- Space: `O(n)`

---

## Q2. Subarray Sum Equals K

### Problem
Given `nums` and `k`, return number of contiguous subarrays with sum exactly `k`.

Example: `nums = [1,1,1], k = 2 -> 2`

### Brute Force Solution

#### Pseudocode
```text
count = 0
FOR i from 0 to n - 1:
    total = 0
    FOR j from i to n - 1:
        total += nums[j]
        IF total == k:
            count += 1
RETURN count
```

#### Python
```python
def subarray_sum_equals_k_bruteforce(nums, k):
    count = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1

    return count
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Frequency Hash Map)

#### Pseudocode
```text
freq = {0: 1}
prefix = 0
count = 0

FOR x in nums:
    prefix += x
    count += freq.get(prefix - k, 0)
    freq[prefix] = freq.get(prefix, 0) + 1

RETURN count
```

#### Python
```python
def subarray_sum_equals_k_optimal(nums, k):
    freq = {0: 1}
    prefix = 0
    count = 0

    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    return count
```

#### Complexity
- Time: `O(n)` average
- Space: `O(n)`

---

## Q3. Continuous Subarray Sum

### Problem
Given `nums` and `k`, return `True` if there exists a subarray of length at least 2 whose sum is a multiple of `k`.

Example: `nums = [23,2,4,6,7], k = 6 -> True`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    total = 0
    FOR j from i to n - 1:
        total += nums[j]
        IF j - i + 1 >= 2:
            IF k == 0 AND total == 0:
                RETURN True
            IF k != 0 AND total mod k == 0:
                RETURN True
RETURN False
```

#### Python
```python
def continuous_subarray_sum_bruteforce(nums, k):
    n = len(nums)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if j - i + 1 < 2:
                continue

            if k == 0:
                if total == 0:
                    return True
            else:
                if total % k == 0:
                    return True

    return False
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Remainder First-Index Map)

#### Pseudocode
```text
IF k == 0:
    first = {0: -1}
    prefix = 0
    FOR i from 0 to n - 1:
        prefix += nums[i]
        IF prefix in first AND i - first[prefix] >= 2:
            RETURN True
        IF prefix not in first:
            first[prefix] = i
    RETURN False

first = {0: -1}
prefix = 0

FOR i from 0 to n - 1:
    prefix = (prefix + nums[i]) mod k
    IF prefix in first:
        IF i - first[prefix] >= 2:
            RETURN True
    ELSE:
        first[prefix] = i

RETURN False
```

#### Python
```python
def continuous_subarray_sum_optimal(nums, k):
    if k == 0:
        first = {0: -1}
        prefix = 0

        for i, x in enumerate(nums):
            prefix += x
            if prefix in first:
                if i - first[prefix] >= 2:
                    return True
            else:
                first[prefix] = i

        return False

    first = {0: -1}
    prefix = 0

    for i, x in enumerate(nums):
        prefix = (prefix + x) % k
        if prefix in first:
            if i - first[prefix] >= 2:
                return True
        else:
            first[prefix] = i

    return False
```

#### Complexity
- Time: `O(n)`
- Space: `O(min(n, |k|))`

---

## Q4. Contiguous Array

### Problem
Given binary array `nums`, return max length of contiguous subarray with equal number of `0` and `1`.

Example: `nums = [0,1,0] -> 2`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    balance = 0
    FOR j from i to n - 1:
        IF nums[j] == 1: balance += 1
        ELSE: balance -= 1

        IF balance == 0:
            best = max(best, j - i + 1)

RETURN best
```

#### Python
```python
def contiguous_array_bruteforce(nums):
    best = 0

    for i in range(len(nums)):
        balance = 0
        for j in range(i, len(nums)):
            if nums[j] == 1:
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                best = max(best, j - i + 1)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Balance + First Occurrence)

#### Pseudocode
```text
first = {0: -1}
balance = 0
best = 0

FOR i from 0 to n - 1:
    IF nums[i] == 1: balance += 1
    ELSE: balance -= 1

    IF balance in first:
        best = max(best, i - first[balance])
    ELSE:
        first[balance] = i

RETURN best
```

#### Python
```python
def contiguous_array_optimal(nums):
    first = {0: -1}
    balance = 0
    best = 0

    for i, x in enumerate(nums):
        if x == 1:
            balance += 1
        else:
            balance -= 1

        if balance in first:
            best = max(best, i - first[balance])
        else:
            first[balance] = i

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q5. Product of Array Except Self

### Problem
Given `nums`, return array `answer` where `answer[i]` is product of all elements except `nums[i]`, without division.

Example: `nums = [1,2,3,4] -> [24,12,8,6]`

### Brute Force Solution

#### Pseudocode
```text
answer = empty list
FOR i from 0 to n - 1:
    product = 1
    FOR j from 0 to n - 1:
        IF j != i:
            product *= nums[j]
    APPEND product to answer
RETURN answer
```

#### Python
```python
def product_except_self_bruteforce(nums):
    out = []

    for i in range(len(nums)):
        product = 1
        for j, x in enumerate(nums):
            if j != i:
                product *= x
        out.append(product)

    return out
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)` extra

### Optimal Solution (Prefix Product * Suffix Product)

#### Pseudocode
```text
out = array of 1s size n
prefix = 1

FOR i from 0 to n - 1:
    out[i] = prefix
    prefix *= nums[i]

suffix = 1
FOR i from n - 1 down to 0:
    out[i] *= suffix
    suffix *= nums[i]

RETURN out
```

#### Python
```python
def product_except_self_optimal(nums):
    n = len(nums)
    out = [1] * n

    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]

    return out
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)` extra (excluding output)

---

## Q6. Find Pivot Index

### Problem
Given `nums`, return leftmost pivot index where left sum equals right sum. If none, return `-1`.

Example: `nums = [1,7,3,6,5,6] -> 3`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    left_sum = sum(nums[0 .. i - 1])
    right_sum = sum(nums[i + 1 .. n - 1])
    IF left_sum == right_sum:
        RETURN i
RETURN -1
```

#### Python
```python
def pivot_index_bruteforce(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i
    return -1
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Total Sum + Running Left)

#### Pseudocode
```text
total = sum(nums)
left = 0

FOR i from 0 to n - 1:
    IF left == total - left - nums[i]:
        RETURN i
    left += nums[i]

RETURN -1
```

#### Python
```python
def pivot_index_optimal(nums):
    total = sum(nums)
    left = 0

    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x

    return -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q7. Corporate Flight Bookings

### Problem
Given bookings `[first, last, seats]` and `n` flights (1-indexed), return seats booked for each flight.

Example: `bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5 -> [10,55,45,25,25]`

### Brute Force Solution

#### Pseudocode
```text
ans = array of 0 size n

FOR each booking [first, last, seats]:
    FOR i from first - 1 to last - 1:
        ans[i] += seats

RETURN ans
```

#### Python
```python
def corp_flight_bookings_bruteforce(bookings, n):
    ans = [0] * n

    for first, last, seats in bookings:
        for i in range(first - 1, last):
            ans[i] += seats

    return ans
```

#### Complexity
- Time: `O(m * n)` worst case
- Space: `O(1)` extra

### Optimal Solution (Difference Array + Prefix)

#### Pseudocode
```text
diff = array of 0 size n

FOR each booking [first, last, seats]:
    diff[first - 1] += seats
    IF last < n:
        diff[last] -= seats

ans[0] = diff[0]
FOR i from 1 to n - 1:
    ans[i] = ans[i - 1] + diff[i]

RETURN ans
```

#### Python
```python
def corp_flight_bookings_optimal(bookings, n):
    diff = [0] * n

    for first, last, seats in bookings:
        diff[first - 1] += seats
        if last < n:
            diff[last] -= seats

    ans = [0] * n
    ans[0] = diff[0]

    for i in range(1, n):
        ans[i] = ans[i - 1] + diff[i]

    return ans
```

#### Complexity
- Time: `O(m + n)`
- Space: `O(n)`

---

## Q8. Car Pooling

### Problem
Given trips `[numPassengers, from, to]` and `capacity`, return `True` if trips can be completed without exceeding capacity.

Example: `trips = [[2,1,5],[3,3,7]], capacity = 4 -> False`

### Brute Force Solution

#### Pseudocode
```text
max_pos = maximum drop-off position
load = array of 0 size max_pos + 1

FOR each trip [p, start, end]:
    FOR pos from start to end - 1:
        load[pos] += p
        IF load[pos] > capacity:
            RETURN False

RETURN True
```

#### Python
```python
def car_pooling_bruteforce(trips, capacity):
    max_pos = 0
    for _, _, end in trips:
        max_pos = max(max_pos, end)

    load = [0] * (max_pos + 1)

    for p, start, end in trips:
        for pos in range(start, end):
            load[pos] += p
            if load[pos] > capacity:
                return False

    return True
```

#### Complexity
- Time: `O(total_distance)`
- Space: `O(U)` where `U` is max position

### Optimal Solution (Difference Array + Prefix)

#### Pseudocode
```text
max_pos = maximum drop-off position
diff = array of 0 size max_pos + 1

FOR each trip [p, start, end]:
    diff[start] += p
    diff[end] -= p

current = 0
FOR pos from 0 to max_pos:
    current += diff[pos]
    IF current > capacity:
        RETURN False

RETURN True
```

#### Python
```python
def car_pooling_optimal(trips, capacity):
    max_pos = 0
    for _, _, end in trips:
        max_pos = max(max_pos, end)

    diff = [0] * (max_pos + 1)

    for p, start, end in trips:
        diff[start] += p
        diff[end] -= p

    current = 0
    for x in diff:
        current += x
        if current > capacity:
            return False

    return True
```

#### Complexity
- Time: `O(m + U)`
- Space: `O(U)`

---

## Q9. Subarray Sums Divisible by K

### Problem
Given `nums` and `k`, return count of subarrays whose sum is divisible by `k`.

Example: `nums = [4,5,0,-2,-3,1], k = 5 -> 7`

### Brute Force Solution

#### Pseudocode
```text
count = 0
FOR i from 0 to n - 1:
    total = 0
    FOR j from i to n - 1:
        total += nums[j]
        IF total mod k == 0:
            count += 1
RETURN count
```

#### Python
```python
def subarrays_div_by_k_bruteforce(nums, k):
    count = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total % k == 0:
                count += 1

    return count
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Remainder Frequency)

#### Pseudocode
```text
freq = {0: 1}
prefix = 0
count = 0

FOR x in nums:
    prefix = (prefix + x) mod k
    count += freq.get(prefix, 0)
    freq[prefix] = freq.get(prefix, 0) + 1

RETURN count
```

#### Python
```python
def subarrays_div_by_k_optimal(nums, k):
    freq = {0: 1}
    prefix = 0
    count = 0

    for x in nums:
        prefix = (prefix + x) % k
        count += freq.get(prefix, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    return count
```

#### Complexity
- Time: `O(n)`
- Space: `O(min(n, k))`

---

## Q10. Maximum Size Subarray Sum Equals k

### Problem
Given `nums` and `k`, return maximum length of a subarray that sums to `k`.

Example: `nums = [1,-1,5,-2,3], k = 3 -> 4`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    total = 0
    FOR j from i to n - 1:
        total += nums[j]
        IF total == k:
            best = max(best, j - i + 1)
RETURN best
```

#### Python
```python
def max_size_subarray_sum_k_bruteforce(nums, k):
    best = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                best = max(best, j - i + 1)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Sum First Occurrence)

#### Pseudocode
```text
first = {0: -1}
prefix = 0
best = 0

FOR i from 0 to n - 1:
    prefix += nums[i]

    IF (prefix - k) in first:
        best = max(best, i - first[prefix - k])

    IF prefix not in first:
        first[prefix] = i

RETURN best
```

#### Python
```python
def max_size_subarray_sum_k_optimal(nums, k):
    first = {0: -1}
    prefix = 0
    best = 0

    for i, x in enumerate(nums):
        prefix += x

        if prefix - k in first:
            best = max(best, i - first[prefix - k])

        if prefix not in first:
            first[prefix] = i

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Rapid Recall Checklist

- Define `prefix` convention early (exclusive prefix is safest).
- For counts, seed base case like `freq[0] = 1`.
- For max length, keep first prefix occurrence only.
- For range updates, use diff-array endpoints then prefix-reconstruct.
