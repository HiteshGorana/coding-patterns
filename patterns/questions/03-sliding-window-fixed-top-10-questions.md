# Pattern 03 Interview Playbook: Sliding Window (Fixed Size)

This playbook is aligned with [Pattern 03: Sliding Window (Fixed)](../03-sliding-window-fixed.md).

Use it when every answer depends on a contiguous window of exact size `k`.

## Pattern Snapshot

| Prompt shape | Window state to store | Update rule |
|---|---|---|
| max/min/sum/avg over size `k` | running sum or counter | `+ incoming`, `- outgoing` |
| fixed-size frequency match | char frequency array/map | add right char, remove left char |
| count valid size-`k` windows | running sum + threshold check | compare each full window |
| circular fixed window | duplicated array + running sum | slide one step for each index |
| fixed-size best metric | base score + window gain | maintain best gain while sliding |

## Query-Update Rules

- Build the first full window once.
- Then slide by one index: add new right element and remove old left element.
- Only evaluate answer after window reaches exact size `k`.
- For frequency windows, keep state deterministic (array for lowercase alphabets when possible).

---

## Q1. Maximum Average Subarray I

### Problem
Given `nums` and integer `k`, return the maximum average value among all subarrays of length `k`.

Example: `nums = [1,12,-5,-6,50,3], k = 4 -> 12.75`

### Brute Force Solution

#### Pseudocode
```text
best_sum = -infinity
FOR i from 0 to n - k:
    window_sum = sum(nums[i .. i + k - 1])
    best_sum = max(best_sum, window_sum)
RETURN best_sum / k
```

#### Python
```python
def max_average_bruteforce(nums, k):
    best_sum = float('-inf')

    for i in range(len(nums) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += nums[j]
        best_sum = max(best_sum, window_sum)

    return best_sum / k
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)`

### Optimal Solution (Fixed Window Sum)

#### Pseudocode
```text
window_sum = sum(first k elements)
best_sum = window_sum

FOR r from k to n - 1:
    window_sum += nums[r]
    window_sum -= nums[r - k]
    best_sum = max(best_sum, window_sum)

RETURN best_sum / k
```

#### Python
```python
def max_average_optimal(nums, k):
    window_sum = sum(nums[:k])
    best_sum = window_sum

    for r in range(k, len(nums)):
        window_sum += nums[r] - nums[r - k]
        best_sum = max(best_sum, window_sum)

    return best_sum / k
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q2. Max Sum Subarray of Size K

### Problem
Given `nums` and `k`, return the maximum sum of any contiguous subarray of size `k`.

Example: `nums = [2,1,5,1,3,2], k = 3 -> 9`

### Brute Force Solution

#### Pseudocode
```text
best = -infinity
FOR i from 0 to n - k:
    curr = sum(nums[i .. i + k - 1])
    best = max(best, curr)
RETURN best
```

#### Python
```python
def max_sum_size_k_bruteforce(nums, k):
    best = float('-inf')

    for i in range(len(nums) - k + 1):
        curr = 0
        for j in range(i, i + k):
            curr += nums[j]
        best = max(best, curr)

    return best
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)`

### Optimal Solution (Fixed Window Sum)

#### Pseudocode
```text
window = sum(first k elements)
best = window

FOR r from k to n - 1:
    window += nums[r]
    window -= nums[r - k]
    best = max(best, window)

RETURN best
```

#### Python
```python
def max_sum_size_k_optimal(nums, k):
    window = sum(nums[:k])
    best = window

    for r in range(k, len(nums)):
        window += nums[r] - nums[r - k]
        best = max(best, window)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q3. Find All Anagrams in a String

### Problem
Given strings `s` and `p`, return all start indices of `p`'s anagrams in `s`.

Example: `s = "cbaebabacd", p = "abc" -> [0, 6]`

### Brute Force Solution

#### Pseudocode
```text
need = sort(p)
ans = []
m = length(p)

FOR i from 0 to n - m:
    IF sort(s[i .. i + m - 1]) == need:
        APPEND i to ans

RETURN ans
```

#### Python
```python
def find_anagrams_bruteforce(s, p):
    m, n = len(p), len(s)
    if m > n:
        return []

    need = ''.join(sorted(p))
    ans = []

    for i in range(n - m + 1):
        if ''.join(sorted(s[i:i + m])) == need:
            ans.append(i)

    return ans
```

#### Complexity
- Time: `O((n - m + 1) * m log m)`
- Space: `O(m)`

### Optimal Solution (Fixed Frequency Window)

#### Pseudocode
```text
IF m > n: RETURN []

need[26] = freq of p
win[26] = freq of first m chars in s
matches = count of indices where need[i] == win[i]
ans = []
IF matches == 26: APPEND 0

FOR r from m to n - 1:
    add_idx = index(s[r])
    rem_idx = index(s[r - m])

    UPDATE matches for add_idx before/after increment
    UPDATE matches for rem_idx before/after decrement

    IF matches == 26:
        APPEND r - m + 1

RETURN ans
```

#### Python
```python
def find_anagrams_optimal(s, p):
    m, n = len(p), len(s)
    if m > n:
        return []

    need = [0] * 26
    win = [0] * 26

    for ch in p:
        need[ord(ch) - ord('a')] += 1
    for i in range(m):
        win[ord(s[i]) - ord('a')] += 1

    matches = sum(1 for i in range(26) if need[i] == win[i])
    ans = []
    if matches == 26:
        ans.append(0)

    for r in range(m, n):
        add_idx = ord(s[r]) - ord('a')
        rem_idx = ord(s[r - m]) - ord('a')

        if win[add_idx] == need[add_idx]:
            matches -= 1
        win[add_idx] += 1
        if win[add_idx] == need[add_idx]:
            matches += 1

        if win[rem_idx] == need[rem_idx]:
            matches -= 1
        win[rem_idx] -= 1
        if win[rem_idx] == need[rem_idx]:
            matches += 1

        if matches == 26:
            ans.append(r - m + 1)

    return ans
```

#### Complexity
- Time: `O(n)` for fixed lowercase alphabet
- Space: `O(1)` for fixed lowercase alphabet

---

## Q4. Permutation in String

### Problem
Given `s1` and `s2`, return `True` if some permutation of `s1` is a substring of `s2`.

Example: `s1 = "ab", s2 = "eidbaooo" -> True`

### Brute Force Solution

#### Pseudocode
```text
need = sort(s1)
m = length(s1)

FOR i from 0 to n - m:
    IF sort(s2[i .. i + m - 1]) == need:
        RETURN True

RETURN False
```

#### Python
```python
def permutation_in_string_bruteforce(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False

    need = ''.join(sorted(s1))

    for i in range(n - m + 1):
        if ''.join(sorted(s2[i:i + m])) == need:
            return True

    return False
```

#### Complexity
- Time: `O((n - m + 1) * m log m)`
- Space: `O(m)`

### Optimal Solution (Fixed Frequency Window)

#### Pseudocode
```text
IF m > n: RETURN False

need[26] = freq of s1
win[26] = freq of first m chars in s2
matches = count equal positions between need and win

IF matches == 26: RETURN True

FOR r from m to n - 1:
    add_idx = index(s2[r])
    rem_idx = index(s2[r - m])

    UPDATE matches for add_idx and rem_idx

    IF matches == 26:
        RETURN True

RETURN False
```

#### Python
```python
def permutation_in_string_optimal(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False

    need = [0] * 26
    win = [0] * 26

    for ch in s1:
        need[ord(ch) - ord('a')] += 1
    for i in range(m):
        win[ord(s2[i]) - ord('a')] += 1

    matches = sum(1 for i in range(26) if need[i] == win[i])
    if matches == 26:
        return True

    for r in range(m, n):
        add_idx = ord(s2[r]) - ord('a')
        rem_idx = ord(s2[r - m]) - ord('a')

        if win[add_idx] == need[add_idx]:
            matches -= 1
        win[add_idx] += 1
        if win[add_idx] == need[add_idx]:
            matches += 1

        if win[rem_idx] == need[rem_idx]:
            matches -= 1
        win[rem_idx] -= 1
        if win[rem_idx] == need[rem_idx]:
            matches += 1

        if matches == 26:
            return True

    return False
```

#### Complexity
- Time: `O(n)` for fixed lowercase alphabet
- Space: `O(1)` for fixed lowercase alphabet

---

## Q5. Sliding Window Maximum

### Problem
Given `nums` and `k`, return the maximum in each sliding window of size `k`.

Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]`

### Brute Force Solution

#### Pseudocode
```text
ans = []
FOR i from 0 to n - k:
    APPEND max(nums[i .. i + k - 1]) to ans
RETURN ans
```

#### Python
```python
def sliding_window_max_bruteforce(nums, k):
    ans = []

    for i in range(len(nums) - k + 1):
        ans.append(max(nums[i:i + k]))

    return ans
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)` extra

### Optimal Solution (Monotonic Deque)

#### Pseudocode
```text
dq = empty deque of indices
ans = []

FOR i from 0 to n - 1:
    REMOVE indices from front if out of window (<= i - k)
    REMOVE indices from back while nums[back] <= nums[i]
    PUSH i to back
    IF i >= k - 1:
        APPEND nums[dq.front] to ans

RETURN ans
```

#### Python
```python
from collections import deque


def sliding_window_max_optimal(nums, k):
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
- Time: `O(n)`
- Space: `O(k)`

---

## Q6. Defuse the Bomb

### Problem
Given circular array `code` and integer `k`:
- if `k > 0`, replace each index with sum of next `k` values,
- if `k < 0`, replace each index with sum of previous `|k|` values,
- if `k == 0`, replace with `0`.

Example: `code = [5,7,1,4], k = 3 -> [12,10,16,13]`

### Brute Force Solution

#### Pseudocode
```text
n = length(code)
ans = array of zeros length n

IF k == 0:
    RETURN ans

FOR i from 0 to n - 1:
    total = 0
    IF k > 0:
        FOR step from 1 to k:
            total += code[(i + step) mod n]
    ELSE:
        FOR step from 1 to abs(k):
            total += code[(i - step + n) mod n]
    ans[i] = total

RETURN ans
```

#### Python
```python
def defuse_bomb_bruteforce(code, k):
    n = len(code)
    ans = [0] * n

    if k == 0:
        return ans

    for i in range(n):
        total = 0
        if k > 0:
            for step in range(1, k + 1):
                total += code[(i + step) % n]
        else:
            for step in range(1, -k + 1):
                total += code[(i - step + n) % n]
        ans[i] = total

    return ans
```

#### Complexity
- Time: `O(n * |k|)`
- Space: `O(n)`

### Optimal Solution (Circular Fixed Window)

#### Pseudocode
```text
n = length(code)
ans = array of zeros length n
IF k == 0: RETURN ans
arr = code + code

IF k > 0:
    left = 1, right = k
ELSE:
    k = abs(k)
    left = n - k, right = n - 1

window = sum(arr[left .. right])

FOR i from 0 to n - 1:
    ans[i] = window
    window -= arr[left]
    left += 1
    right += 1
    window += arr[right]

RETURN ans
```

#### Python
```python
def defuse_bomb_optimal(code, k):
    n = len(code)
    ans = [0] * n

    if k == 0:
        return ans

    arr = code + code

    if k > 0:
        left, right = 1, k
    else:
        k = -k
        left, right = n - k, n - 1

    window = sum(arr[left:right + 1])

    for i in range(n):
        ans[i] = window
        window -= arr[left]
        left += 1
        right += 1
        window += arr[right]

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q7. K Radius Subarray Averages

### Problem
For each index `i`, return average of subarray centered at `i` with radius `k` (`2k+1` size), else `-1` if not enough elements.

Example: `nums = [7,4,3,9,1,8,5,2,6], k = 3 -> [-1,-1,-1,5,4,4,-1,-1,-1]`

### Brute Force Solution

#### Pseudocode
```text
n = length(nums)
ans = array of -1 length n
w = 2k + 1

FOR center from 0 to n - 1:
    left = center - k
    right = center + k
    IF left < 0 OR right >= n:
        CONTINUE

    total = sum(nums[left .. right])
    ans[center] = floor(total / w)

RETURN ans
```

#### Python
```python
def k_radius_averages_bruteforce(nums, k):
    n = len(nums)
    ans = [-1] * n
    w = 2 * k + 1

    for center in range(n):
        left = center - k
        right = center + k
        if left < 0 or right >= n:
            continue

        total = 0
        for i in range(left, right + 1):
            total += nums[i]

        ans[center] = total // w

    return ans
```

#### Complexity
- Time: `O(n * (2k + 1))`
- Space: `O(n)`

### Optimal Solution (Fixed Window Length `2k+1`)

#### Pseudocode
```text
n = length(nums)
ans = array of -1 length n
w = 2k + 1
IF w > n: RETURN ans

window = sum(first w elements)
ans[k] = floor(window / w)

FOR r from w to n - 1:
    window += nums[r]
    window -= nums[r - w]
    center = r - k
    ans[center] = floor(window / w)

RETURN ans
```

#### Python
```python
def k_radius_averages_optimal(nums, k):
    n = len(nums)
    ans = [-1] * n
    w = 2 * k + 1

    if w > n:
        return ans

    window = sum(nums[:w])
    ans[k] = window // w

    for r in range(w, n):
        window += nums[r] - nums[r - w]
        center = r - k
        ans[center] = window // w

    return ans
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## Q8. Number of Sub-arrays of Size K and Average >= Threshold

### Problem
Given `arr`, `k`, and `threshold`, return count of subarrays of size `k` with average at least `threshold`.

Example: `arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4 -> 3`

### Brute Force Solution

#### Pseudocode
```text
count = 0
FOR i from 0 to n - k:
    total = sum(arr[i .. i + k - 1])
    IF total / k >= threshold:
        count += 1
RETURN count
```

#### Python
```python
def count_subarrays_avg_threshold_bruteforce(arr, k, threshold):
    count = 0

    for i in range(len(arr) - k + 1):
        total = 0
        for j in range(i, i + k):
            total += arr[j]
        if total / k >= threshold:
            count += 1

    return count
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)`

### Optimal Solution (Fixed Window Sum)

#### Pseudocode
```text
target = k * threshold
window = sum(first k elements)
count = 1 if window >= target else 0

FOR r from k to n - 1:
    window += arr[r]
    window -= arr[r - k]
    IF window >= target:
        count += 1

RETURN count
```

#### Python
```python
def count_subarrays_avg_threshold_optimal(arr, k, threshold):
    target = k * threshold
    window = sum(arr[:k])
    count = 1 if window >= target else 0

    for r in range(k, len(arr)):
        window += arr[r] - arr[r - k]
        if window >= target:
            count += 1

    return count
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q9. Maximum Number of Vowels in a Substring of Given Length

### Problem
Given string `s` and integer `k`, return max number of vowels in any substring of length `k`.

Example: `s = "abciiidef", k = 3 -> 3`

### Brute Force Solution

#### Pseudocode
```text
vowels = {a,e,i,o,u}
best = 0

FOR i from 0 to n - k:
    count = 0
    FOR j from i to i + k - 1:
        IF s[j] in vowels:
            count += 1
    best = max(best, count)

RETURN best
```

#### Python
```python
def max_vowels_bruteforce(s, k):
    vowels = set('aeiou')
    best = 0

    for i in range(len(s) - k + 1):
        count = 0
        for j in range(i, i + k):
            if s[j] in vowels:
                count += 1
        best = max(best, count)

    return best
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(1)`

### Optimal Solution (Fixed Window Count)

#### Pseudocode
```text
vowels = {a,e,i,o,u}
count = number of vowels in first k chars
best = count

FOR r from k to n - 1:
    IF s[r] is vowel: count += 1
    IF s[r - k] is vowel: count -= 1
    best = max(best, count)

RETURN best
```

#### Python
```python
def max_vowels_optimal(s, k):
    vowels = set('aeiou')

    count = 0
    for i in range(k):
        if s[i] in vowels:
            count += 1

    best = count

    for r in range(k, len(s)):
        if s[r] in vowels:
            count += 1
        if s[r - k] in vowels:
            count -= 1
        best = max(best, count)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q10. Grumpy Bookstore Owner

### Problem
Given `customers`, `grumpy`, and `minutes`, maximize satisfied customers by choosing one `minutes`-length window where owner is not grumpy.

Example: `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3 -> 16`

### Brute Force Solution

#### Pseudocode
```text
base = sum(customers[i] where grumpy[i] == 0)
best = 0

FOR start from 0 to n - minutes:
    extra = 0
    FOR i from start to start + minutes - 1:
        IF grumpy[i] == 1:
            extra += customers[i]
    best = max(best, extra)

RETURN base + best
```

#### Python
```python
def grumpy_bookstore_bruteforce(customers, grumpy, minutes):
    n = len(customers)
    base = 0

    for i in range(n):
        if grumpy[i] == 0:
            base += customers[i]

    best = 0

    for start in range(n - minutes + 1):
        extra = 0
        for i in range(start, start + minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        best = max(best, extra)

    return base + best
```

#### Complexity
- Time: `O(n * minutes)`
- Space: `O(1)`

### Optimal Solution (Base + Sliding Extra Gain)

#### Pseudocode
```text
base = sum(customers[i] where grumpy[i] == 0)

window_extra = sum(customers[i] for i in first minutes where grumpy[i] == 1)
best_extra = window_extra

FOR r from minutes to n - 1:
    IF grumpy[r] == 1: window_extra += customers[r]
    IF grumpy[r - minutes] == 1: window_extra -= customers[r - minutes]
    best_extra = max(best_extra, window_extra)

RETURN base + best_extra
```

#### Python
```python
def grumpy_bookstore_optimal(customers, grumpy, minutes):
    n = len(customers)

    base = 0
    for i in range(n):
        if grumpy[i] == 0:
            base += customers[i]

    window_extra = 0
    for i in range(minutes):
        if grumpy[i] == 1:
            window_extra += customers[i]

    best_extra = window_extra

    for r in range(minutes, n):
        if grumpy[r] == 1:
            window_extra += customers[r]
        if grumpy[r - minutes] == 1:
            window_extra -= customers[r - minutes]
        best_extra = max(best_extra, window_extra)

    return base + best_extra
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Rapid Recall Checklist

- Confirm the window size is fixed before choosing this pattern.
- Initialize first full window explicitly, then slide with `+in -out`.
- Record answers only when window has exact size `k`.
- For string frequency problems, prefer fixed arrays when alphabet is bounded.
