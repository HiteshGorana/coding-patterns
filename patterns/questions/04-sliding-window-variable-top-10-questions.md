# Pattern 04 Interview Playbook: Sliding Window (Variable Size)

This playbook is aligned with [Pattern 04: Sliding Window (Variable Size)](../04-sliding-window-variable.md).

Use it when window size is not fixed and validity depends on current window state.

## Pattern Snapshot

| Prompt shape | Window state to store | Validity rule |
|---|---|---|
| longest substring/subarray under constraint | `freq` / counters | shrink while invalid |
| shortest window covering requirement | `need` / `missing` | shrink while still valid |
| at most `k` distinct | `value -> frequency`, `distinct` | `distinct <= k` |
| sum/product threshold windows | running `sum` / `product` | threshold-based shrink |
| replacement/deletion budget | violations counter (`zeros`, replacements) | budget not exceeded |
| exact `k` style counts | helper `atMost(k)` | exact = `atMost(k) - atMost(k-1)` |

## Query-Update Rules

- Expand right pointer and update incoming element first.
- While constraint is broken, shrink from left and rollback state.
- For longest-window goals, update answer after repair.
- For minimum-window goals, update answer while valid and keep shrinking.

---

## Q1. Longest Substring Without Repeating Characters

### Problem
Given string `s`, return length of the longest substring without repeating characters.

Example: `s = "abcabcbb" -> 3`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    seen = empty set
    FOR j from i to n - 1:
        IF s[j] in seen:
            BREAK
        ADD s[j] to seen
        best = max(best, j - i + 1)
RETURN best
```

#### Python
```python
def longest_unique_bruteforce(s):
    best = 0

    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(min(n, sigma))`

### Optimal Solution (Last-Seen Window Jump)

#### Pseudocode
```text
last_seen = empty map
left = 0
best = 0

FOR right from 0 to n - 1:
    ch = s[right]
    IF ch in last_seen AND last_seen[ch] >= left:
        left = last_seen[ch] + 1

    last_seen[ch] = right
    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def longest_unique_optimal(s):
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(min(n, sigma))`

---

## Q2. Minimum Window Substring

### Problem
Given strings `s` and `t`, return the minimum window in `s` containing all chars of `t` (with multiplicity). If none, return `""`.

Example: `s = "ADOBECODEBANC", t = "ABC" -> "BANC"`

### Brute Force Solution

#### Pseudocode
```text
need = frequency map of t
best_len = infinity
best_start = 0

FOR i from 0 to n - 1:
    have = empty map
    missing = length(t)

    FOR j from i to n - 1:
        ch = s[j]
        IF ch in need:
            have[ch] += 1
            IF have[ch] <= need[ch]:
                missing -= 1

        IF missing == 0:
            IF j - i + 1 < best_len:
                best_len = j - i + 1
                best_start = i
            BREAK

IF best_len is infinity: RETURN ""
RETURN s[best_start : best_start + best_len]
```

#### Python
```python
def min_window_bruteforce(s, t):
    if not s or not t:
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    best_len = float('inf')
    best_start = 0

    for i in range(len(s)):
        have = {}
        missing = len(t)

        for j in range(i, len(s)):
            ch = s[j]
            if ch in need:
                have[ch] = have.get(ch, 0) + 1
                if have[ch] <= need[ch]:
                    missing -= 1

            if missing == 0:
                if j - i + 1 < best_len:
                    best_len = j - i + 1
                    best_start = i
                break

    if best_len == float('inf'):
        return ""

    return s[best_start:best_start + best_len]
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(sigma_t)`

### Optimal Solution (Expand + Shrink While Valid)

#### Pseudocode
```text
need = frequency map of t
missing = length(t)
left = 0
best_len = infinity
best_start = 0

FOR right from 0 to n - 1:
    ch = s[right]
    IF need[ch] > 0:
        missing -= 1
    need[ch] -= 1

    WHILE missing == 0:
        IF right - left + 1 < best_len:
            best_len = right - left + 1
            best_start = left

        out = s[left]
        need[out] += 1
        IF need[out] > 0:
            missing += 1
        left += 1

IF best_len is infinity: RETURN ""
RETURN s[best_start : best_start + best_len]
```

#### Python
```python
def min_window_optimal(s, t):
    if not s or not t:
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    missing = len(t)
    left = 0
    best_len = float('inf')
    best_start = 0

    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1

        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left

            out = s[left]
            need[out] = need.get(out, 0) + 1
            if need[out] > 0:
                missing += 1
            left += 1

    if best_len == float('inf'):
        return ""

    return s[best_start:best_start + best_len]
```

#### Complexity
- Time: `O(n + m)`
- Space: `O(sigma_t)`

---

## Q3. Longest Repeating Character Replacement

### Problem
Given uppercase string `s` and integer `k`, return length of longest substring that can be turned into all same char by replacing at most `k` chars.

Example: `s = "AABABBA", k = 1 -> 4`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    freq[26] = all zeros
    max_freq = 0

    FOR j from i to n - 1:
        idx = index(s[j])
        freq[idx] += 1
        max_freq = max(max_freq, freq[idx])

        IF (j - i + 1) - max_freq <= k:
            best = max(best, j - i + 1)
        ELSE:
            BREAK

RETURN best
```

#### Python
```python
def char_replace_bruteforce(s, k):
    best = 0

    for i in range(len(s)):
        freq = [0] * 26
        max_freq = 0

        for j in range(i, len(s)):
            idx = ord(s[j]) - ord('A')
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

            if (j - i + 1) - max_freq <= k:
                best = max(best, j - i + 1)
            else:
                break

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Variable Window + Max Freq)

#### Pseudocode
```text
freq[26] = all zeros
left = 0
max_freq = 0
best = 0

FOR right from 0 to n - 1:
    idx = index(s[right])
    freq[idx] += 1
    max_freq = max(max_freq, freq[idx])

    WHILE (right - left + 1) - max_freq > k:
        freq[index(s[left])] -= 1
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def char_replace_optimal(s, k):
    freq = [0] * 26
    left = 0
    max_freq = 0
    best = 0

    for right, ch in enumerate(s):
        idx = ord(ch) - ord('A')
        freq[idx] += 1
        max_freq = max(max_freq, freq[idx])

        while (right - left + 1) - max_freq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q4. Fruit Into Baskets

### Problem
Given array `fruits`, return max number of fruits you can pick from a contiguous subarray containing at most 2 distinct values.

Example: `fruits = [1,2,1] -> 3`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    freq = empty map
    FOR j from i to n - 1:
        freq[fruits[j]] += 1
        IF distinct keys in freq > 2:
            BREAK
        best = max(best, j - i + 1)
RETURN best
```

#### Python
```python
def fruit_baskets_bruteforce(fruits):
    best = 0

    for i in range(len(fruits)):
        freq = {}
        for j in range(i, len(fruits)):
            x = fruits[j]
            freq[x] = freq.get(x, 0) + 1
            if len(freq) > 2:
                break
            best = max(best, j - i + 1)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)` (at most 3 keys transiently)

### Optimal Solution (At Most 2 Distinct)

#### Pseudocode
```text
left = 0
freq = empty map
best = 0

FOR right from 0 to n - 1:
    freq[fruits[right]] += 1

    WHILE distinct keys in freq > 2:
        freq[fruits[left]] -= 1
        IF freq[fruits[left]] == 0:
            remove key
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def fruit_baskets_optimal(fruits):
    left = 0
    freq = {}
    best = 0

    for right, x in enumerate(fruits):
        freq[x] = freq.get(x, 0) + 1

        while len(freq) > 2:
            out = fruits[left]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)` (bounded by distinct limit)

---

## Q5. Minimum Size Subarray Sum

### Problem
Given positive integer array `nums` and target `target`, return minimal length of a subarray with sum >= `target`. If none, return `0`.

Example: `target = 7, nums = [2,3,1,2,4,3] -> 2`

### Brute Force Solution

#### Pseudocode
```text
best = infinity
FOR i from 0 to n - 1:
    total = 0
    FOR j from i to n - 1:
        total += nums[j]
        IF total >= target:
            best = min(best, j - i + 1)
            BREAK

IF best is infinity: RETURN 0
RETURN best
```

#### Python
```python
def min_subarray_len_bruteforce(target, nums):
    best = float('inf')

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total >= target:
                best = min(best, j - i + 1)
                break

    return 0 if best == float('inf') else best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Shrink While Sum Valid)

#### Pseudocode
```text
left = 0
total = 0
best = infinity

FOR right from 0 to n - 1:
    total += nums[right]

    WHILE total >= target:
        best = min(best, right - left + 1)
        total -= nums[left]
        left += 1

IF best is infinity: RETURN 0
RETURN best
```

#### Python
```python
def min_subarray_len_optimal(target, nums):
    left = 0
    total = 0
    best = float('inf')

    for right, x in enumerate(nums):
        total += x

        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if best == float('inf') else best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q6. Subarray Product Less Than K

### Problem
Given positive integer array `nums` and integer `k`, return count of contiguous subarrays where product < `k`.

Example: `nums = [10,5,2,6], k = 100 -> 8`

### Brute Force Solution

#### Pseudocode
```text
IF k <= 1: RETURN 0
count = 0

FOR i from 0 to n - 1:
    product = 1
    FOR j from i to n - 1:
        product *= nums[j]
        IF product < k:
            count += 1
        ELSE:
            BREAK

RETURN count
```

#### Python
```python
def subarray_product_bruteforce(nums, k):
    if k <= 1:
        return 0

    count = 0

    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product < k:
                count += 1
            else:
                break

    return count
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Product Window)

#### Pseudocode
```text
IF k <= 1: RETURN 0
left = 0
product = 1
count = 0

FOR right from 0 to n - 1:
    product *= nums[right]

    WHILE product >= k:
        product /= nums[left]
        left += 1

    count += right - left + 1

RETURN count
```

#### Python
```python
def subarray_product_optimal(nums, k):
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right, x in enumerate(nums):
        product *= x

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q7. Longest Substring with At Most K Distinct Characters

### Problem
Given string `s` and integer `k`, return length of longest substring with at most `k` distinct chars.

Example: `s = "eceba", k = 2 -> 3`

### Brute Force Solution

#### Pseudocode
```text
IF k == 0: RETURN 0
best = 0

FOR i from 0 to n - 1:
    freq = empty map
    FOR j from i to n - 1:
        freq[s[j]] += 1
        IF distinct keys in freq > k:
            BREAK
        best = max(best, j - i + 1)

RETURN best
```

#### Python
```python
def longest_k_distinct_bruteforce(s, k):
    if k == 0:
        return 0

    best = 0

    for i in range(len(s)):
        freq = {}
        for j in range(i, len(s)):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) > k:
                break
            best = max(best, j - i + 1)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(min(k, sigma))`

### Optimal Solution (At Most K Distinct Window)

#### Pseudocode
```text
IF k == 0: RETURN 0
left = 0
freq = empty map
best = 0

FOR right from 0 to n - 1:
    freq[s[right]] += 1

    WHILE distinct keys in freq > k:
        freq[s[left]] -= 1
        IF freq[s[left]] == 0:
            remove key
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def longest_k_distinct_optimal(s, k):
    if k == 0:
        return 0

    left = 0
    freq = {}
    best = 0

    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1

        while len(freq) > k:
            out = s[left]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(min(k, sigma))`

---

## Q8. Max Consecutive Ones III

### Problem
Given binary array `nums` and integer `k`, return maximum consecutive ones after flipping at most `k` zeros.

Example: `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 -> 6`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    zeros = 0
    FOR j from i to n - 1:
        IF nums[j] == 0:
            zeros += 1
        IF zeros > k:
            BREAK
        best = max(best, j - i + 1)
RETURN best
```

#### Python
```python
def max_ones_iii_bruteforce(nums, k):
    best = 0

    for i in range(len(nums)):
        zeros = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            if zeros > k:
                break
            best = max(best, j - i + 1)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (At Most K Zeros Window)

#### Pseudocode
```text
left = 0
zeros = 0
best = 0

FOR right from 0 to n - 1:
    IF nums[right] == 0:
        zeros += 1

    WHILE zeros > k:
        IF nums[left] == 0:
            zeros -= 1
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def max_ones_iii_optimal(nums, k):
    left = 0
    zeros = 0
    best = 0

    for right, x in enumerate(nums):
        if x == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q9. Frequency of the Most Frequent Element

### Problem
Given integer array `nums` and integer `k`, you may increment elements at most `k` times total. Return max possible frequency of any element.

Example: `nums = [1,2,4], k = 5 -> 3`

### Brute Force Solution

#### Pseudocode
```text
SORT nums
prefix_sum[0] = 0
FOR i from 0 to n - 1:
    prefix_sum[i + 1] = prefix_sum[i] + nums[i]

best = 1
FOR right from 0 to n - 1:
    FOR left from 0 to right:
        window_sum = prefix_sum[right + 1] - prefix_sum[left]
        need = nums[right] * (right - left + 1) - window_sum
        IF need <= k:
            best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def freq_most_frequent_bruteforce(nums, k):
    nums = sorted(nums)
    n = len(nums)

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    best = 1

    for right in range(n):
        for left in range(right + 1):
            window_sum = prefix[right + 1] - prefix[left]
            need = nums[right] * (right - left + 1) - window_sum
            if need <= k:
                best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n^2)` after sorting
- Space: `O(n)`

### Optimal Solution (Sorted Window + Cost Formula)

#### Pseudocode
```text
SORT nums
left = 0
window_sum = 0
best = 1

FOR right from 0 to n - 1:
    window_sum += nums[right]

    WHILE nums[right] * (right - left + 1) - window_sum > k:
        window_sum -= nums[left]
        left += 1

    best = max(best, right - left + 1)

RETURN best
```

#### Python
```python
def freq_most_frequent_optimal(nums, k):
    nums.sort()

    left = 0
    window_sum = 0
    best = 1

    for right, x in enumerate(nums):
        window_sum += x

        while x * (right - left + 1) - window_sum > k:
            window_sum -= nums[left]
            left += 1

        best = max(best, right - left + 1)

    return best
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(1)` extra (excluding sort)

---

## Q10. Longest Subarray of 1's After Deleting One Element

### Problem
Given binary array `nums`, delete one element and return longest non-empty subarray containing only `1`s.

Example: `nums = [1,1,0,1] -> 3`

### Brute Force Solution

#### Pseudocode
```text
best = 0
FOR i from 0 to n - 1:
    zeros = 0
    FOR j from i to n - 1:
        IF nums[j] == 0:
            zeros += 1
        IF zeros > 1:
            BREAK
        best = max(best, j - i)  # delete one from this window
RETURN best
```

#### Python
```python
def longest_ones_delete_one_bruteforce(nums):
    best = 0

    for i in range(len(nums)):
        zeros = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            if zeros > 1:
                break
            best = max(best, j - i)

    return best
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (At Most One Zero Window)

#### Pseudocode
```text
left = 0
zeros = 0
best = 0

FOR right from 0 to n - 1:
    IF nums[right] == 0:
        zeros += 1

    WHILE zeros > 1:
        IF nums[left] == 0:
            zeros -= 1
        left += 1

    best = max(best, right - left)  # one deletion enforced

RETURN best
```

#### Python
```python
def longest_ones_delete_one_optimal(nums):
    left = 0
    zeros = 0
    best = 0

    for right, x in enumerate(nums):
        if x == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        best = max(best, right - left)

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Rapid Recall Checklist

- Define one clear window validity condition before coding.
- Expand right first, then shrink left until window is valid again.
- Use `while` (not `if`) when repeated shrinking is required.
- For shortest valid window, update answer inside the shrink loop.
