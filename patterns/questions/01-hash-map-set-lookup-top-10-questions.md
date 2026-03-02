# Pattern 01 Interview Playbook: Hash Map / Set Lookup

This playbook is aligned with [Pattern 01: Hash Map / Set Lookup](../01-hash-map-set-lookup.md).

Use it when the prompt needs fast lookup over previously seen values or states.

## Pattern Snapshot

| Prompt shape | Store in hash | Query |
|---|---|---|
| duplicate / presence | `seen: set` | `x in seen` |
| frequency / counts | `freq: dict` | `freq.get(x, 0)` |
| pair sum / complement | `index_of: dict` | `need in index_of` |
| first unique | `freq: dict` | two-pass: count then select |
| subarray sum = `k` | `prefix_count: dict` | `prefix - k` frequency |
| grouping anagrams | `signature -> list` | append bucket |

## Query-Update Rules

- Query then update: use when current item cannot reuse itself (Two Sum, duplicate checks).
- Update then query: use when current item must be included first.
- Two-pass count then select: use when selection depends on global frequency.

---

## Q1. Two Sum

### Problem
Given `nums` and `target`, return indices of two numbers such that they add to `target`.

Example: `nums = [2,7,11,15], target = 9 -> [0,1]`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        IF nums[i] + nums[j] == target:
            RETURN [i, j]
RETURN []
```

#### Python
```python
def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Hash Map)

#### Pseudocode
```text
index_of = empty map
FOR each index i and value x in nums:
    need = target - x
    IF need in index_of:
        RETURN [index_of[need], i]
    index_of[x] = i
RETURN []
```

#### Python
```python
def two_sum_optimal(nums, target):
    index_of = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index_of:
            return [index_of[need], i]
        index_of[x] = i
    return []
```

#### Complexity
- Time: `O(n)` average
- Space: `O(n)`

---

## Q2. Contains Duplicate

### Problem
Return `True` if any value appears at least twice, else `False`.

Example: `nums = [1,2,3,1] -> True`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        IF nums[i] == nums[j]:
            RETURN True
RETURN False
```

#### Python
```python
def contains_duplicate_bruteforce(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Hash Set)

#### Pseudocode
```text
seen = empty set
FOR x in nums:
    IF x in seen:
        RETURN True
    ADD x to seen
RETURN False
```

#### Python
```python
def contains_duplicate_optimal(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

#### Complexity
- Time: `O(n)` average
- Space: `O(n)`

---

## Q3. Valid Anagram

### Problem
Return `True` if `t` is an anagram of `s`, else `False`.

Example: `s = "anagram", t = "nagaram" -> True`

### Brute Force Solution

#### Pseudocode
```text
IF length(s) != length(t):
    RETURN False
RETURN sort(s) == sort(t)
```

#### Python
```python
def valid_anagram_bruteforce(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)`

### Optimal Solution (Hash Map Counts)

#### Pseudocode
```text
IF length(s) != length(t):
    RETURN False

freq = empty map
FOR ch in s:
    freq[ch] += 1

FOR ch in t:
    IF freq[ch] == 0:
        RETURN False
    freq[ch] -= 1

RETURN True
```

#### Python
```python
def valid_anagram_optimal(s, t):
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if freq.get(ch, 0) == 0:
            return False
        freq[ch] -= 1

    return True
```

#### Complexity
- Time: `O(n)`
- Space: `O(sigma)` where `sigma` is unique chars

---

## Q4. Group Anagrams

### Problem
Group strings that are anagrams of each other.

Example: `strs = ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]`

### Brute Force Solution

#### Pseudocode
```text
groups = empty list
used = boolean array of size n initialized to False

FOR i from 0 to n - 1:
    IF used[i]:
        CONTINUE

    key = sort(strs[i])
    current_group = [strs[i]]
    used[i] = True

    FOR j from i + 1 to n - 1:
        IF NOT used[j] AND sort(strs[j]) == key:
            APPEND strs[j] to current_group
            used[j] = True

    APPEND current_group to groups

RETURN groups
```

#### Python
```python
def group_anagrams_bruteforce(strs):
    n = len(strs)
    used = [False] * n
    groups = []

    for i in range(n):
        if used[i]:
            continue

        key = ''.join(sorted(strs[i]))
        cur = [strs[i]]
        used[i] = True

        for j in range(i + 1, n):
            if not used[j] and ''.join(sorted(strs[j])) == key:
                cur.append(strs[j])
                used[j] = True

        groups.append(cur)

    return groups
```

#### Complexity
- Time: `O(n^2 * k log k)`
- Space: `O(n * k)`

### Optimal Solution (Hash Map by Signature)

#### Pseudocode
```text
groups = empty map from signature -> list of strings

FOR each word w in strs:
    counts = array[26] filled with 0
    FOR each char ch in w:
        counts[ch - 'a'] += 1
    key = tuple(counts)
    APPEND w to groups[key]

RETURN all values of groups
```

#### Python
```python
def group_anagrams_optimal(strs):
    groups = {}
    for w in strs:
        cnt = [0] * 26
        for ch in w:
            cnt[ord(ch) - ord('a')] += 1
        key = tuple(cnt)
        groups.setdefault(key, []).append(w)
    return list(groups.values())
```

#### Complexity
- Time: `O(n * k)`
- Space: `O(n * k)`

---

## Q5. First Unique Character in a String

### Problem
Return index of first non-repeating character, else `-1`.

Example: `s = "leetcode" -> 0`

### Brute Force Solution

#### Pseudocode
```text
FOR i from 0 to n - 1:
    count = 0
    FOR j from 0 to n - 1:
        IF s[j] == s[i]:
            count += 1
    IF count == 1:
        RETURN i
RETURN -1
```

#### Python
```python
def first_unique_char_bruteforce(s):
    n = len(s)
    for i in range(n):
        count = 0
        for j in range(n):
            if s[j] == s[i]:
                count += 1
        if count == 1:
            return i
    return -1
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)` extra

### Optimal Solution (Two-Pass Hash Map)

#### Pseudocode
```text
freq = empty map
FOR ch in s:
    freq[ch] += 1

FOR i from 0 to n - 1:
    IF freq[s[i]] == 1:
        RETURN i

RETURN -1
```

#### Python
```python
def first_unique_char_optimal(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(sigma)`

---

## Q6. Isomorphic Strings

### Problem
Return `True` if `s` and `t` are isomorphic (one-to-one mapping), else `False`.

Example: `s = "egg", t = "add" -> True`

### Brute Force Solution

#### Pseudocode
```text
IF length(s) != length(t):
    RETURN False

FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        same_in_s = (s[i] == s[j])
        same_in_t = (t[i] == t[j])
        IF same_in_s != same_in_t:
            RETURN False

RETURN True
```

#### Python
```python
def isomorphic_bruteforce(s, t):
    if len(s) != len(t):
        return False

    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if (s[i] == s[j]) != (t[i] == t[j]):
                return False

    return True
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Bidirectional Hash Maps)

#### Pseudocode
```text
IF length(s) != length(t):
    RETURN False

s_to_t = empty map
t_to_s = empty map

FOR each pair (a, b) from s and t:
    IF a in s_to_t AND s_to_t[a] != b:
        RETURN False
    IF b in t_to_s AND t_to_s[b] != a:
        RETURN False

    s_to_t[a] = b
    t_to_s[b] = a

RETURN True
```

#### Python
```python
def isomorphic_optimal(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for a, b in zip(s, t):
        if a in s_to_t and s_to_t[a] != b:
            return False
        if b in t_to_s and t_to_s[b] != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a

    return True
```

#### Complexity
- Time: `O(n)`
- Space: `O(sigma)`

---

## Q7. Ransom Note

### Problem
Return `True` if `ransomNote` can be constructed from `magazine` (each char usable once).

Example: `ransomNote = "aa", magazine = "aab" -> True`

### Brute Force Solution

#### Pseudocode
```text
mag = list of characters from magazine

FOR ch in ransomNote:
    FIND ch in mag
    IF not found:
        RETURN False
    REMOVE one occurrence of ch from mag

RETURN True
```

#### Python
```python
def ransom_note_bruteforce(ransomNote, magazine):
    mag = list(magazine)

    for ch in ransomNote:
        if ch not in mag:
            return False
        mag.remove(ch)

    return True
```

#### Complexity
- Time: `O(n * m)` worst case
- Space: `O(m)`

### Optimal Solution (Hash Map Counts)

#### Pseudocode
```text
freq = empty map
FOR ch in magazine:
    freq[ch] += 1

FOR ch in ransomNote:
    IF freq[ch] == 0:
        RETURN False
    freq[ch] -= 1

RETURN True
```

#### Python
```python
def ransom_note_optimal(ransomNote, magazine):
    freq = {}

    for ch in magazine:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in ransomNote:
        if freq.get(ch, 0) == 0:
            return False
        freq[ch] -= 1

    return True
```

#### Complexity
- Time: `O(n + m)`
- Space: `O(sigma)`

---

## Q8. Longest Consecutive Sequence

### Problem
Return the length of the longest consecutive sequence in `nums`.

Example: `nums = [100,4,200,1,3,2] -> 4`

### Brute Force Solution

#### Pseudocode
```text
FUNCTION exists(nums, value):
    FOR x in nums:
        IF x == value:
            RETURN True
    RETURN False

best = 0
FOR x in nums:
    length = 1
    y = x + 1

    WHILE exists(nums, y):
        length += 1
        y += 1

    best = max(best, length)

RETURN best
```

#### Python
```python
def longest_consecutive_bruteforce(nums):
    def exists(arr, value):
        for x in arr:
            if x == value:
                return True
        return False

    best = 0
    for x in nums:
        length = 1
        y = x + 1
        while exists(nums, y):
            length += 1
            y += 1
        best = max(best, length)

    return best
```

#### Complexity
- Time: up to `O(n^3)` in worst case
- Space: `O(1)` extra

### Optimal Solution (Hash Set + Start Detection)

#### Pseudocode
```text
s = set(nums)
best = 0

FOR x in s:
    IF x - 1 in s:
        CONTINUE

    y = x
    WHILE y in s:
        y += 1

    best = max(best, y - x)

RETURN best
```

#### Python
```python
def longest_consecutive_optimal(nums):
    s = set(nums)
    best = 0

    for x in s:
        if x - 1 in s:
            continue

        y = x
        while y in s:
            y += 1

        best = max(best, y - x)

    return best
```

#### Complexity
- Time: `O(n)` average
- Space: `O(n)`

---

## Q9. Subarray Sum Equals K

### Problem
Count contiguous subarrays with sum exactly `k`.

Example: `nums = [1,1,1], k = 2 -> 2`

### Brute Force Solution

#### Pseudocode
```text
ans = 0
FOR i from 0 to n - 1:
    current_sum = 0
    FOR j from i to n - 1:
        current_sum += nums[j]
        IF current_sum == k:
            ans += 1
RETURN ans
```

#### Python
```python
def subarray_sum_bruteforce(nums, k):
    ans = 0
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                ans += 1

    return ans
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

### Optimal Solution (Prefix Sum + Hash Map)

#### Pseudocode
```text
prefix_count = {0: 1}
prefix = 0
ans = 0

FOR x in nums:
    prefix += x
    ans += prefix_count.get(prefix - k, 0)
    prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

RETURN ans
```

#### Python
```python
def subarray_sum_optimal(nums, k):
    prefix_count = {0: 1}
    prefix = 0
    ans = 0

    for x in nums:
        prefix += x
        ans += prefix_count.get(prefix - k, 0)
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    return ans
```

#### Complexity
- Time: `O(n)` average
- Space: `O(n)`

---

## Q10. Find All Anagrams in a String

### Problem
Return starting indices of `p`'s anagrams in `s`.

Example: `s = "cbaebabacd", p = "abc" -> [0, 6]`

### Brute Force Solution

#### Pseudocode
```text
m = length(p)
need = sort(p)
ans = empty list

FOR i from 0 to n - m:
    window = s[i : i + m]
    IF sort(window) == need:
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

### Optimal Solution (Sliding Window Counts)

#### Pseudocode
```text
IF m > n:
    RETURN []

need[26] = counts of chars in p
win[26] = counts of first window in s
matches = number of positions where need[i] == win[i]
ans = []

IF matches == 26:
    APPEND 0

FOR r from m to n - 1:
    add_idx = index of s[r]
    rem_idx = index of s[r - m]

    UPDATE win[add_idx] and matches
    UPDATE win[rem_idx] and matches

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

## Rapid Recall Checklist

- State what hash stores before coding (`seen`, `freq`, `index_of`, `prefix_count`).
- Choose query/update order deliberately.
- Seed base cases when needed (`prefix_count = {0: 1}`).
- Mention average-case hash behavior: lookup/insert is `O(1)` on average.
