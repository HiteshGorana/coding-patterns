# Pattern 01 Interview Playbook: Hash Map / Set Lookup

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Use this pattern when you need constant-time lookups for values you have already seen.
- Core intuition: Trade extra memory for speed. Instead of repeatedly searching the array/string, store useful facts in a hash table: - set for membership (`seen`) - map for counts (`freq[x]`) - map for metadata (`last_index[x]`, `first_position[x]`)
- Trigger cue 1: "duplicate", "frequency", "first unique", "pair sum"
- Trigger cue 2: Brute force would compare many pairs.
- Quick self-check: Can I answer faster if I store `value -> count/index/state`?
- Target complexity: Time O(n) average, Space O(n)

---

## Q1. Two Sum

### Problem Statement (Concrete)
Solve **Two Sum** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]
- `target`/`k`: int (if required by the variant)

### Output
- Indices, count, or value requested by the exact statement.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i], target <= 10^9`

### Example (Exact)
```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Complement lookup identifies the pair in one linear scan.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Two Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check every candidate pair directly.

#### Python
```python
def brute_two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort values and use two pointers with index recovery.

#### Python
```python
def better_two_sum(nums, target):
    pairs = sorted((x, i) for i, x in enumerate(nums))
    l, r = 0, len(pairs) - 1
    while l < r:
        s = pairs[l][0] + pairs[r][0]
        if s == target:
            return sorted([pairs[l][1], pairs[r][1]])
        if s < target:
            l += 1
        else:
            r -= 1
    return []
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Store complement-ready information in a hashmap for one-pass lookup.

#### Python
```python
def solve_two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At index `i`, hashmap stores all prior candidates exactly once.
- If complement exists earlier, it is found immediately when processing current element.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Contains Duplicate

### Problem Statement (Concrete)
Solve **Contains Duplicate** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]

### Output
- `True` if any value appears at least twice, otherwise `False`.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 1]
Output: True
Explanation: Duplicate `1` appears more than once.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Contains Duplicate** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compare each pair for equality.

#### Python
```python
def brute_contains_duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once, then equal neighbors indicate duplicates.

#### Python
```python
def better_contains_duplicate(nums):
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place sort is allowed.

### Approach 3: Optimal (Best)
#### Intuition
- Hash-set membership catches repeats in average constant time.

#### Python
```python
def solve_contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

#### Correctness (Why This Works)
- A value repeats iff it appears in the `seen` set before insertion.
- Single pass checks exactly that condition for every element.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Valid Anagram

### Problem Statement (Concrete)
Solve **Valid Anagram** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `s`: str
- `t`/`p`: str

### Output
- Boolean or list of start indices, depending on variant.

### Constraints
- `1 <= len(s), len(t) <= 2 * 10^5`
- `s`/`t` are lowercase English letters unless stated otherwise.

### Example (Exact)
```text
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: Window frequency count equals pattern frequency at matching starts.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Valid Anagram** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort both strings and compare.

#### Python
```python
def brute_valid_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use hashmap counts to track character balance.

#### Python
```python
def better_valid_anagram(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]
    return not freq
```

#### Complexity
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use fixed-size frequency array for lowercase alphabet.

#### Python
```python
def solve_valid_anagram(s, t):
    if len(s) != len(t):
        return False
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - 97] += 1
    for ch in t:
        idx = ord(ch) - 97
        cnt[idx] -= 1
        if cnt[idx] < 0:
            return False
    return True
```

#### Correctness (Why This Works)
- Anagrams require identical character multiplicities.
- Frequency balance after full scan is zero exactly for an anagram pair.

#### Complexity
- Time `O(n)`, Space `O(1)` for fixed alphabet.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Group Anagrams

### Problem Statement (Concrete)
Solve **Group Anagrams** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `strs`: list[str]

### Output
- List of groups, where each group contains anagram strings.

### Constraints
- `1 <= len(strs) <= 10^4`
- `0 <= len(strs[i]) <= 100`

### Example (Exact)
```text
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Explanation: Strings with same sorted-character signature belong to one group.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Group Anagrams** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Match each string against all others with sorted comparison.

#### Python
```python
def brute_group_anagrams(strs):
    groups = []
    used = [False] * len(strs)
    for i in range(len(strs)):
        if used[i]:
            continue
        cur = [strs[i]]
        used[i] = True
        for j in range(i + 1, len(strs)):
            if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                used[j] = True
                cur.append(strs[j])
        groups.append(cur)
    return groups
```

#### Complexity
- Time `O(n^2 * k log k)`, Space `O(nk)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash by sorted-string signature.

#### Python
```python
def better_group_anagrams(strs):
    groups = {}
    for w in strs:
        key = ''.join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())
```

#### Complexity
- Time `O(n * k log k)`, Space `O(nk)`.

### Approach 3: Optimal (Best)
#### Intuition
- Hash by 26-count signature for linear-time key creation per string.

#### Python
```python
def solve_group_anagrams(strs):
    groups = {}
    for w in strs:
        cnt = [0] * 26
        for ch in w:
            cnt[ord(ch) - 97] += 1
        key = tuple(cnt)
        groups.setdefault(key, []).append(w)
    return list(groups.values())
```

#### Correctness (Why This Works)
- Two strings are anagrams iff their 26-dimensional count vectors are equal.
- Grouping by that invariant partitions all words into exact anagram classes.

#### Complexity
- Time `O(n*k)`, Space `O(n*k)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. First Unique Character in a String

### Problem Statement (Concrete)
Solve **First Unique Character in a String** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `s`: str

### Output
- Index of first non-repeating character, or `-1` if none exists.

### Constraints
- `1 <= len(s) <= 10^5`
- `s` contains lowercase English letters.

### Example (Exact)
```text
Input:  s = "leetcode"
Output: 0
Explanation: `l` is the first character with frequency 1.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **First Unique Character in a String** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count every character by rescanning whole string for each index.

#### Python
```python
def brute_first_unique_character_in_a_string(s):
    for i, ch in enumerate(s):
        if s.count(ch) == 1:
            return i
    return -1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)` (small alphabet).

### Approach 2: Better (Intermediate)
#### Intuition
- One pass for counts, second pass for first index with count 1.

#### Python
```python
def better_first_unique_character_in_a_string(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Two-pass frequency strategy is optimal for first-unique lookup.

#### Python
```python
def better_first_unique_character_in_a_string(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1
```

#### Correctness (Why This Works)
- First pass computes exact multiplicity for each character.
- Second pass preserves original order and returns earliest multiplicity-1 index.

#### Complexity
- Time `O(n)`, Space `O(sigma)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Isomorphic Strings

### Problem Statement (Concrete)
Solve **Isomorphic Strings** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `s`: str
- `t`: str

### Output
- `True` if characters in `s` can map one-to-one to `t`, else `False`.

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`
- `len(s) == len(t)`

### Example (Exact)
```text
Input:  s = "egg", t = "add"
Output: True
Explanation: `e -> a` and `g -> d` is a consistent bijection.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Isomorphic Strings** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check pairwise consistency across all position pairs.

#### Python
```python
def brute_isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[i] == s[j]) != (t[i] == t[j]):
                return False
    return True
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain forward and reverse maps to enforce bijection.

#### Python
```python
def better_isomorphic_strings(s, t):
    st = {}
    ts = {}
    for a, b in zip(s, t):
        if a in st and st[a] != b:
            return False
        if b in ts and ts[b] != a:
            return False
        st[a] = b
        ts[b] = a
    return True
```

#### Complexity
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Bidirectional hash mapping gives linear validation with exact constraints.

#### Python
```python
def better_isomorphic_strings(s, t):
    st = {}
    ts = {}
    for a, b in zip(s, t):
        if a in st and st[a] != b:
            return False
        if b in ts and ts[b] != a:
            return False
        st[a] = b
        ts[b] = a
    return True
```

#### Correctness (Why This Works)
- Forward map prevents one source char mapping to multiple targets.
- Reverse map prevents multiple source chars mapping to same target; together they enforce bijection.

#### Complexity
- Time `O(n)`, Space `O(sigma)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Ransom Note

### Problem Statement (Concrete)
Solve **Ransom Note** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `ransomNote`: str
- `magazine`: str

### Output
- `True` if ransom note can be constructed from magazine letters, else `False`.

### Constraints
- `1 <= len(ransomNote), len(magazine) <= 10^5`
- Each magazine character can be used at most once.

### Example (Exact)
```text
Input:  ransomNote = "aa", magazine = "aab"
Output: True
Explanation: Magazine contains enough counts for all required letters.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Ransom Note** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Remove used characters from a mutable magazine list.

#### Python
```python
def brute_ransom_note(ransomNote, magazine):
    mag = list(magazine)
    for ch in ransomNote:
        if ch not in mag:
            return False
        mag.remove(ch)
    return True
```

#### Complexity
- Time `O(n*m)` in worst case, Space `O(m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use frequency map of magazine letters and consume counts.

#### Python
```python
def better_ransom_note(ransomNote, magazine):
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
- Time `O(n+m)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count comparison directly models one-time consumable characters.

#### Python
```python
def better_ransom_note(ransomNote, magazine):
    freq = {}
    for ch in magazine:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in ransomNote:
        if freq.get(ch, 0) == 0:
            return False
        freq[ch] -= 1
    return True
```

#### Correctness (Why This Works)
- Each ransom character is feasible iff remaining magazine count is positive.
- Decrementing counts preserves exact remaining resource invariant.

#### Complexity
- Time `O(n+m)`, Space `O(sigma)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Longest Consecutive Sequence

### Problem Statement (Concrete)
Solve **Longest Consecutive Sequence** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]

### Output
- Length of the longest run of consecutive integer values.

### Constraints
- `0 <= n <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Example (Exact)
```text
Input:  nums = [100,4,200,1,3,2]
Output: 4
Explanation: Sequence `[1,2,3,4]` has maximum length 4.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Longest Consecutive Sequence** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each value, walk forward while next value exists.

#### Python
```python
def brute_longest_consecutive_sequence(nums):
    best = 0
    for x in nums:
        cur = x
        length = 1
        while cur + 1 in nums:
            cur += 1
            length += 1
        best = max(best, length)
    return best
```

#### Complexity
- Time up to `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort unique values and count longest adjacent +1 streak.

#### Python
```python
def better_longest_consecutive_sequence(nums):
    arr = sorted(set(nums))
    if not arr:
        return 0
    best = cur = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Only start streak expansion at sequence starts (`x-1` absent).

#### Python
```python
def solve_longest_consecutive_sequence(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y in s:
                y += 1
            best = max(best, y - x)
    return best
```

#### Correctness (Why This Works)
- Each consecutive run is expanded exactly once from its minimum element.
- No run is missed because every run has a unique minimum lacking predecessor.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Subarray Sum Equals K

### Problem Statement (Concrete)
Solve **Subarray Sum Equals K** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]
- `k`: int

### Output
- Count of contiguous subarrays whose sum equals `k`.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^4 <= nums[i], k <= 10^4`

### Example (Exact)
```text
Input:  nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays `[1,1]` at indices `(0,1)` and `(1,2)` both sum to 2.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Subarray Sum Equals K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_subarray_sum_equals_k(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_subarray_sum_equals_k(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_subarray_sum_equals_k(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Find All Anagrams in a String

### Problem Statement (Concrete)
Solve **Find All Anagrams in a String** using **Hash Map / Set Lookup**. Return exactly the value/structure requested by the original prompt.

### Input
- `s`: str
- `t`/`p`: str

### Output
- Boolean or list of start indices, depending on variant.

### Constraints
- `1 <= len(s), len(t) <= 2 * 10^5`
- `s`/`t` are lowercase English letters unless stated otherwise.

### Example (Exact)
```text
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: Window frequency count equals pattern frequency at matching starts.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Hash Map / Set Lookup**.
- Red flags: brute force for **Find All Anagrams in a String** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort every window and compare with sorted pattern.

#### Python
```python
def brute_find_all_anagrams_in_a_string(s, p):
    m = len(p)
    key = sorted(p)
    ans = []
    for i in range(len(s) - m + 1):
        if sorted(s[i:i+m]) == key:
            ans.append(i)
    return ans
```

#### Complexity
- Time `O((n-m+1) * m log m)`, Space `O(m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain hashmap counts for current window.

#### Python
```python
def better_find_all_anagrams_in_a_string(s, p):
    m = len(p)
    if m > len(s):
        return []
    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1
    win = {}
    ans = []
    for i, ch in enumerate(s):
        win[ch] = win.get(ch, 0) + 1
        if i >= m:
            out = s[i - m]
            win[out] -= 1
            if win[out] == 0:
                del win[out]
        if win == need:
            ans.append(i - m + 1)
    return ans
```

#### Complexity
- Time `O(n * sigma)` worst with dict equality checks, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use fixed-size frequency arrays for O(1) window update and direct frequency comparison.

#### Python
```python
def solve_find_all_anagrams_in_a_string(s, p):
    m, n = len(p), len(s)
    if m > n:
        return []
    need = [0] * 26
    win = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    ans = []
    for i, ch in enumerate(s):
        win[ord(ch) - 97] += 1
        if i >= m:
            win[ord(s[i - m]) - 97] -= 1
        if win == need:
            ans.append(i - m + 1)
    return ans
```

#### Correctness (Why This Works)
- Window always has length `m`; equality with pattern counts is exactly the anagram condition.
- Sliding by one character updates counts incrementally without rescanning full window.

#### Complexity
- Time `O(n * sigma)` with small constant alphabet (effectively linear), Space `O(sigma)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
