# Pattern 02 Interview Playbook: Two Pointers

This playbook is aligned with [Pattern 02: Two Pointers](../02-two-pointers.md).

Use it when two moving indices can eliminate impossible candidates in arrays/strings.

## Pattern Snapshot

| Prompt shape | Pointer setup | Move rule |
|---|---|---|
| sorted pair/target | `l = 0, r = n-1` | move `l` if sum small, `r` if sum large |
| palindrome check | `l = 0, r = n-1` | move inward while chars match/skip invalid |
| merge/partition in-place | read pointer + write pointer | write valid values forward |
| max area/water walls | two boundaries | move smaller boundary |
| k-sum on sorted array | fixed outer + inner `l/r` | skip duplicates + monotonic moves |

## Pointer Movement Rules

- Prove each pointer move removes only impossible states.
- In sorted arrays, movement is monotonic; do not move both pointers blindly.
- For de-dup problems (3Sum/4Sum), sort first and skip equal neighbors.
- For in-place compaction, separate read pointer from write pointer.

---

## Q1. Two Sum II - Input Array Is Sorted

### Problem
Given sorted array `numbers` and `target`, return 1-indexed positions of two numbers adding to `target`.

Example: `numbers = [2,7,11,15], target = 9 -> [1,2]`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        IF numbers[i] + numbers[j] == target:
            RETURN [i + 1, j + 1]
RETURN []
```

#### Python
```python
def two_sum_ii_bruteforce(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Two Pointers)

#### Pseudocode
```text
l = 0, r = n - 1
WHILE l < r:
    s = numbers[l] + numbers[r]
    IF s == target:
        RETURN [l + 1, r + 1]
    IF s < target:
        l += 1
    ELSE:
        r -= 1
RETURN []
```

#### Python
```python
def two_sum_ii_optimal(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1
        else:
            r -= 1

    return []
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q2. 3Sum

### Problem
Return all unique triplets `[a, b, c]` such that `a + b + c = 0`.

Example: `nums = [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]`

### Brute Force Solution

#### Pseudocode
```text
triplets = empty set
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        FOR k from j + 1 to n - 1:
            IF nums[i] + nums[j] + nums[k] == 0:
                ADD sorted triple to set
RETURN set converted to list
```

#### Python
```python
def three_sum_bruteforce(nums):
    n = len(nums)
    out = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    out.add(tuple(sorted((nums[i], nums[j], nums[k]))))

    return [list(t) for t in sorted(out)]
```

#### Complexity
- Time: `O(n^3)`
- Space: `O(n)` plus output

### Optimal Solution (Sort + Two Pointers)

#### Pseudocode
```text
SORT nums
ans = []
FOR i from 0 to n - 1:
    IF i > 0 AND nums[i] == nums[i - 1]:
        CONTINUE

    l = i + 1, r = n - 1
    WHILE l < r:
        s = nums[i] + nums[l] + nums[r]
        IF s == 0:
            APPEND [nums[i], nums[l], nums[r]]
            l += 1, r -= 1
            SKIP duplicates at l
            SKIP duplicates at r
        ELSE IF s < 0:
            l += 1
        ELSE:
            r -= 1
RETURN ans
```

#### Python
```python
def three_sum_optimal(nums):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1

    return ans
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)` extra (excluding output)

---

## Q3. 4Sum

### Problem
Return all unique quadruplets `[a,b,c,d]` such that `a + b + c + d = target`.

Example: `nums = [1,0,-1,0,-2,2], target = 0 -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

### Brute Force Solution

#### Pseudocode
```text
quads = empty set
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        FOR k from j + 1 to n - 1:
            FOR l from k + 1 to n - 1:
                IF nums[i] + nums[j] + nums[k] + nums[l] == target:
                    ADD sorted quadruplet to set
RETURN set converted to list
```

#### Python
```python
def four_sum_bruteforce(nums, target):
    n = len(nums)
    out = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        out.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))

    return [list(q) for q in sorted(out)]
```

#### Complexity
- Time: `O(n^4)`
- Space: `O(n)` plus output

### Optimal Solution (Sort + Nested Fix + Two Pointers)

#### Pseudocode
```text
SORT nums
ans = []
FOR i from 0 to n - 1:
    SKIP duplicate nums[i]
    FOR j from i + 1 to n - 1:
        SKIP duplicate nums[j]
        l = j + 1, r = n - 1
        WHILE l < r:
            s = nums[i] + nums[j] + nums[l] + nums[r]
            IF s == target:
                APPEND quadruplet
                l += 1, r -= 1
                SKIP duplicates at l and r
            ELSE IF s < target:
                l += 1
            ELSE:
                r -= 1
RETURN ans
```

#### Python
```python
def four_sum_optimal(nums, target):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            l, r = j + 1, n - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

    return ans
```

#### Complexity
- Time: `O(n^3)`
- Space: `O(1)` extra (excluding output)

---

## Q4. Container With Most Water

### Problem
Given heights, return max water area between two lines.

Example: `height = [1,8,6,2,5,4,8,3,7] -> 49`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        area = (j - i) * min(height[i], height[j])
        best = max(best, area)
RETURN best
```

#### Python
```python
def container_bruteforce(height):
    n = len(height)
    best = 0

    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            best = max(best, area)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Two Boundary Pointers)

#### Pseudocode
```text
l = 0, r = n - 1
best = 0
WHILE l < r:
    area = (r - l) * min(height[l], height[r])
    best = max(best, area)
    IF height[l] <= height[r]:
        l += 1
    ELSE:
        r -= 1
RETURN best
```

#### Python
```python
def container_optimal(height):
    l, r = 0, len(height) - 1
    best = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        best = max(best, area)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q5. Valid Palindrome

### Problem
Return `True` if string is a palindrome considering only alphanumeric chars and ignoring case.

Example: `s = "A man, a plan, a canal: Panama" -> True`

### Brute Force Solution

#### Pseudocode
```text
clean = lowercase alphanumeric chars from s
RETURN clean == reverse(clean)
```

#### Python
```python
def valid_palindrome_bruteforce(s):
    clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (In-Place Two Pointers)

#### Pseudocode
```text
l = 0, r = len(s) - 1
WHILE l < r:
    WHILE l < r AND s[l] is not alnum:
        l += 1
    WHILE l < r AND s[r] is not alnum:
        r -= 1

    IF lowercase(s[l]) != lowercase(s[r]):
        RETURN False

    l += 1
    r -= 1
RETURN True
```

#### Python
```python
def valid_palindrome_optimal(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q6. Squares of a Sorted Array

### Problem
Given sorted `nums`, return array of squares also sorted.

Example: `nums = [-4,-1,0,3,10] -> [0,1,9,16,100]`

### Brute Force Solution

#### Pseudocode
```text
ans = []
FOR x in nums:
    APPEND x * x to ans
SORT ans
RETURN ans
```

#### Python
```python
def sorted_squares_bruteforce(nums):
    ans = [x * x for x in nums]
    ans.sort()
    return ans
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)`

### Optimal Solution (Two Pointers from Ends)

#### Pseudocode
```text
l = 0, r = n - 1
ans = array size n
write = n - 1
WHILE l <= r:
    left_sq = nums[l] * nums[l]
    right_sq = nums[r] * nums[r]
    IF left_sq > right_sq:
        ans[write] = left_sq
        l += 1
    ELSE:
        ans[write] = right_sq
        r -= 1
    write -= 1
RETURN ans
```

#### Python
```python
def sorted_squares_optimal(nums):
    n = len(nums)
    ans = [0] * n
    l, r = 0, n - 1
    write = n - 1

    while l <= r:
        left_sq = nums[l] * nums[l]
        right_sq = nums[r] * nums[r]

        if left_sq > right_sq:
            ans[write] = left_sq
            l += 1
        else:
            ans[write] = right_sq
            r -= 1

        write -= 1

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q7. Remove Duplicates from Sorted Array

### Problem
Remove duplicates in-place from sorted `nums`, return count `k` of unique values.

Example: `nums = [0,0,1,1,1,2,2,3,3,4] -> k = 5`, prefix becomes `[0,1,2,3,4]`

### Brute Force Solution

#### Pseudocode
```text
IF nums empty:
    RETURN 0

unique = [nums[0]]
FOR i from 1 to n - 1:
    IF nums[i] != nums[i - 1]:
        APPEND nums[i] to unique

FOR i from 0 to len(unique) - 1:
    nums[i] = unique[i]

RETURN len(unique)
```

#### Python
```python
def remove_duplicates_bruteforce(nums):
    if not nums:
        return 0

    unique = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            unique.append(nums[i])

    for i, x in enumerate(unique):
        nums[i] = x

    return len(unique)
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Read/Write Pointers)

#### Pseudocode
```text
IF nums empty:
    RETURN 0

write = 1
FOR read from 1 to n - 1:
    IF nums[read] != nums[write - 1]:
        nums[write] = nums[read]
        write += 1

RETURN write
```

#### Python
```python
def remove_duplicates_optimal(nums):
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q8. Move Zeroes

### Problem
Move all zeroes to end while keeping relative order of non-zero elements.

Example: `nums = [0,1,0,3,12] -> [1,3,12,0,0]`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    IF nums[i] == 0:
        j = i
        WHILE j + 1 < n:
            nums[j] = nums[j + 1]
            j += 1
        nums[n - 1] = 0
RETURN nums
```

#### Python
```python
def move_zeroes_bruteforce(nums):
    n = len(nums)

    i = 0
    while i < n:
        if nums[i] == 0:
            j = i
            while j + 1 < n:
                nums[j] = nums[j + 1]
                j += 1
            nums[n - 1] = 0
            n -= 1
        else:
            i += 1

    return nums
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Two Pointers)

#### Pseudocode
```text
write = 0
FOR read from 0 to n - 1:
    IF nums[read] != 0:
        SWAP nums[write], nums[read]
        write += 1
RETURN nums
```

#### Python
```python
def move_zeroes_optimal(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

    return nums
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q9. Trapping Rain Water

### Problem
Given elevation map `height`, compute total trapped rain water.

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
def trap_bruteforce(height):
    n = len(height)
    water = 0

    for i in range(n):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]

    return water
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Two Pointers with Running Max)

#### Pseudocode
```text
l = 0, r = n - 1
left_max = 0, right_max = 0
water = 0

WHILE l < r:
    IF height[l] <= height[r]:
        left_max = max(left_max, height[l])
        water += left_max - height[l]
        l += 1
    ELSE:
        right_max = max(right_max, height[r])
        water += right_max - height[r]
        r -= 1

RETURN water
```

#### Python
```python
def trap_optimal(height):
    l, r = 0, len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while l < r:
        if height[l] <= height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1

    return water
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q10. Sort Colors

### Problem
Sort array of `0`, `1`, `2` in-place.

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
- Space: depends on sorting implementation

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

## Rapid Recall Checklist

- Start by proving the pointer move rule before coding.
- In sorted arrays, rely on monotonic sum behavior.
- Skip duplicates carefully for 3Sum/4Sum.
- For in-place array edits, use separate read/write boundaries.
