# Pattern 06 Interview Playbook: Binary Search (Index Space)

This playbook is aligned with [Pattern 06: Binary Search (Index Space)](../06-binary-search-index.md).

Use it when data is sorted or when a predicate over indices is monotonic.

## Pattern Snapshot

| Prompt shape | Search space | Keep which side |
|---|---|---|
| exact target index | sorted array indices | side that may still contain target |
| first index `>= target` | lower-bound index range | first `True` side |
| first/last occurrence | two boundary searches | first `>= target`, first `> target` |
| rotated sorted array | sorted-half detection | half that can contain target |
| answer threshold (first bad, sqrt floor) | value/index range | monotonic feasible side |
| peak/mountain index | slope comparison | uphill side for first peak point |

## Query-Update Rules

- Pick one interval convention and stay consistent: inclusive `[l, r]` or half-open `[l, r)`.
- Compute `mid` once each loop and discard a provably impossible half.
- Ensure strict progress every iteration (`l = mid + 1`, `r = mid - 1`, or `r = mid`).
- For boundary problems, return the converged boundary index and validate if needed.

---

## Q1. Binary Search

### Problem
Given sorted array `nums` and `target`, return its index or `-1` if not found.

Example: `nums = [-1,0,3,5,9,12], target = 9 -> 4`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    IF nums[i] == target:
        RETURN i
RETURN -1
```

#### Python
```python
def binary_search_bruteforce(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Classic Binary Search)

#### Pseudocode
```text
l = 0, r = n - 1
WHILE l <= r:
    mid = l + (r - l) // 2
    IF nums[mid] == target:
        RETURN mid
    IF nums[mid] < target:
        l = mid + 1
    ELSE:
        r = mid - 1
RETURN -1
```

#### Python
```python
def binary_search_optimal(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q2. Search Insert Position

### Problem
Given sorted array `nums` and `target`, return index if found, else insertion index in order.

Example: `nums = [1,3,5,6], target = 2 -> 1`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    IF nums[i] >= target:
        RETURN i
RETURN n
```

#### Python
```python
def search_insert_bruteforce(nums, target):
    for i, x in enumerate(nums):
        if x >= target:
            return i
    return len(nums)
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Lower Bound)

#### Pseudocode
```text
l = 0, r = n
WHILE l < r:
    mid = l + (r - l) // 2
    IF nums[mid] >= target:
        r = mid
    ELSE:
        l = mid + 1
RETURN l
```

#### Python
```python
def search_insert_optimal(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q3. Find First and Last Position of Element in Sorted Array

### Problem
Given sorted `nums` and `target`, return `[first_index, last_index]`, or `[-1,-1]` if absent.

Example: `nums = [5,7,7,8,8,10], target = 8 -> [3,4]`

### Brute Force Solution

#### Pseudocode
```text
first = -1, last = -1
FOR i from 0 to n - 1:
    IF nums[i] == target:
        IF first == -1:
            first = i
        last = i
RETURN [first, last]
```

#### Python
```python
def search_range_bruteforce(nums, target):
    first = -1
    last = -1

    for i, x in enumerate(nums):
        if x == target:
            if first == -1:
                first = i
            last = i

    return [first, last]
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Two Bounds)

#### Pseudocode
```text
FUNCTION lower_bound(x):
    l = 0, r = n
    WHILE l < r:
        mid = l + (r - l) // 2
        IF nums[mid] >= x:
            r = mid
        ELSE:
            l = mid + 1
    RETURN l

left = lower_bound(target)
IF left == n OR nums[left] != target:
    RETURN [-1, -1]

right = lower_bound(target + 1) - 1
RETURN [left, right]
```

#### Python
```python
def search_range_optimal(nums, target):
    n = len(nums)

    def lower_bound(x):
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= x:
                r = mid
            else:
                l = mid + 1
        return l

    left = lower_bound(target)
    if left == n or nums[left] != target:
        return [-1, -1]

    right = lower_bound(target + 1) - 1
    return [left, right]
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q4. Search in Rotated Sorted Array

### Problem
Given rotated sorted array `nums` (distinct values) and `target`, return target index or `-1`.

Example: `nums = [4,5,6,7,0,1,2], target = 0 -> 4`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    IF nums[i] == target:
        RETURN i
RETURN -1
```

#### Python
```python
def search_rotated_bruteforce(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Sorted Half Binary Search)

#### Pseudocode
```text
l = 0, r = n - 1
WHILE l <= r:
    mid = l + (r - l) // 2
    IF nums[mid] == target:
        RETURN mid

    IF nums[l] <= nums[mid]:
        # left half sorted
        IF nums[l] <= target < nums[mid]:
            r = mid - 1
        ELSE:
            l = mid + 1
    ELSE:
        # right half sorted
        IF nums[mid] < target <= nums[r]:
            l = mid + 1
        ELSE:
            r = mid - 1

RETURN -1
```

#### Python
```python
def search_rotated_optimal(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q5. Find Minimum in Rotated Sorted Array

### Problem
Given rotated sorted array `nums` (distinct values), return minimum element.

Example: `nums = [3,4,5,1,2] -> 1`

### Brute Force Solution

#### Pseudocode
```text
best = nums[0]
FOR x in nums:
    best = min(best, x)
RETURN best
```

#### Python
```python
def find_min_rotated_bruteforce(nums):
    best = nums[0]
    for x in nums:
        best = min(best, x)
    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Binary Search by Right Boundary)

#### Pseudocode
```text
l = 0, r = n - 1
WHILE l < r:
    mid = l + (r - l) // 2
    IF nums[mid] > nums[r]:
        l = mid + 1
    ELSE:
        r = mid
RETURN nums[l]
```

#### Python
```python
def find_min_rotated_optimal(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    return nums[l]
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q6. Sqrt(x)

### Problem
Given non-negative integer `x`, return floor of square root of `x`.

Example: `x = 8 -> 2`

### Brute Force Solution

#### Pseudocode
```text
i = 0
WHILE (i + 1) * (i + 1) <= x:
    i += 1
RETURN i
```

#### Python
```python
def sqrt_x_bruteforce(x):
    i = 0
    while (i + 1) * (i + 1) <= x:
        i += 1
    return i
```

#### Complexity
- Time: `O(sqrt(x))`
- Space: `O(1)`

### Optimal Solution (Binary Search on Answer)

#### Pseudocode
```text
l = 0, r = x
ans = 0
WHILE l <= r:
    mid = l + (r - l) // 2
    sq = mid * mid

    IF sq <= x:
        ans = mid
        l = mid + 1
    ELSE:
        r = mid - 1

RETURN ans
```

#### Python
```python
def sqrt_x_optimal(x):
    l, r = 0, x
    ans = 0

    while l <= r:
        mid = l + (r - l) // 2
        sq = mid * mid

        if sq <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans
```

#### Complexity
- Time: `O(log x)`
- Space: `O(1)`

---

## Q7. Peak Index in a Mountain Array

### Problem
Given mountain array `arr`, return index `i` such that `arr[0] < ... < arr[i] > ... > arr[n-1]`.

Example: `arr = [0,2,1,0] -> 1`

### Brute Force Solution

#### Pseudocode
```text
peak = 0
FOR i from 1 to n - 1:
    IF arr[i] > arr[peak]:
        peak = i
RETURN peak
```

#### Python
```python
def peak_index_mountain_bruteforce(arr):
    peak = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[peak]:
            peak = i
    return peak
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Slope Binary Search)

#### Pseudocode
```text
l = 0, r = n - 1
WHILE l < r:
    mid = l + (r - l) // 2
    IF arr[mid] < arr[mid + 1]:
        l = mid + 1
    ELSE:
        r = mid
RETURN l
```

#### Python
```python
def peak_index_mountain_optimal(arr):
    l, r = 0, len(arr) - 1

    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid

    return l
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q8. Find Peak Element

### Problem
Given `nums`, return any index `i` where `nums[i]` is greater than neighbors (virtual neighbors outside bounds are `-infinity`).

Example: `nums = [1,2,3,1] -> 2`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    left_ok = (i == 0) OR nums[i] > nums[i - 1]
    right_ok = (i == n - 1) OR nums[i] > nums[i + 1]
    IF left_ok AND right_ok:
        RETURN i
RETURN -1
```

#### Python
```python
def find_peak_element_bruteforce(nums):
    n = len(nums)

    for i in range(n):
        left_ok = i == 0 or nums[i] > nums[i - 1]
        right_ok = i == n - 1 or nums[i] > nums[i + 1]
        if left_ok and right_ok:
            return i

    return -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Binary Search on Slope)

#### Pseudocode
```text
l = 0, r = n - 1
WHILE l < r:
    mid = l + (r - l) // 2
    IF nums[mid] < nums[mid + 1]:
        l = mid + 1
    ELSE:
        r = mid
RETURN l
```

#### Python
```python
def find_peak_element_optimal(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid

    return l
```

#### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## Q9. First Bad Version

### Problem
Given versions `1..n` and API `isBadVersion(version)`, return first bad version.

Example: `n = 5`, bad starts at `4` -> `4`

### Brute Force Solution

#### Pseudocode
```text
FOR version from 1 to n:
    IF isBadVersion(version):
        RETURN version
RETURN -1
```

#### Python
```python
def first_bad_version_bruteforce(n):
    for version in range(1, n + 1):
        if isBadVersion(version):
            return version
    return -1
```

#### Complexity
- Time: `O(n)` API calls
- Space: `O(1)`

### Optimal Solution (First True Binary Search)

#### Pseudocode
```text
l = 1, r = n
WHILE l < r:
    mid = l + (r - l) // 2
    IF isBadVersion(mid):
        r = mid
    ELSE:
        l = mid + 1
RETURN l
```

#### Python
```python
def first_bad_version_optimal(n):
    l, r = 1, n

    while l < r:
        mid = l + (r - l) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1

    return l
```

#### Complexity
- Time: `O(log n)` API calls
- Space: `O(1)`

---

## Q10. Search a 2D Matrix

### Problem
Given `m x n` matrix where each row is sorted and first value of each row is greater than last value of previous row, return `True` if target exists.

Example: `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 -> True`

### Brute Force Solution

#### Pseudocode
```text
FOR each row in matrix:
    FOR each value in row:
        IF value == target:
            RETURN True
RETURN False
```

#### Python
```python
def search_matrix_bruteforce(matrix, target):
    for row in matrix:
        for x in row:
            if x == target:
                return True
    return False
```

#### Complexity
- Time: `O(m * n)`
- Space: `O(1)`

### Optimal Solution (Binary Search on Flattened Index)

#### Pseudocode
```text
rows = number of rows, cols = number of cols
l = 0, r = rows * cols - 1

WHILE l <= r:
    mid = l + (r - l) // 2
    val = matrix[mid // cols][mid % cols]

    IF val == target:
        RETURN True
    IF val < target:
        l = mid + 1
    ELSE:
        r = mid - 1

RETURN False
```

#### Python
```python
def search_matrix_optimal(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    l, r = 0, rows * cols - 1

    while l <= r:
        mid = l + (r - l) // 2
        val = matrix[mid // cols][mid % cols]

        if val == target:
            return True
        if val < target:
            l = mid + 1
        else:
            r = mid - 1

    return False
```

#### Complexity
- Time: `O(log(m * n))`
- Space: `O(1)`

---

## Rapid Recall Checklist

- Choose interval style first (`[l,r]` vs `[l,r)`) and do not mix it.
- For boundary answers, think in terms of first `True` predicate.
- Ensure each loop iteration removes at least one index from search space.
- Validate returned index against bounds/content when needed.
