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
- Check every candidate pair/map relation directly; simple but expensive.

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
- Sort to prune comparisons with two pointers while retaining original index mapping.

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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_two_sum(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

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
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1,2,3,4]
Output: problem-specific result
Explanation: Use the pattern invariant to avoid repeated recomputation.
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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_contains_duplicate(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_contains_duplicate(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_contains_duplicate(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_valid_anagram(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_valid_anagram(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_valid_anagram(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

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
- Red flags: brute force for **Group Anagrams** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_group_anagrams(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_group_anagrams(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_group_anagrams(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

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
- `text`/`s`: str
- `pattern`/`queries`: variant-specific

### Output
- Index, boolean, count, or transformed string as required.

### Constraints
- `1 <= length <= 2 * 10^5`
- Use near-linear processing to avoid `O(n*m)` restarts.

### Example (Exact)
```text
Input:  text = "sadbutsad", pattern = "sad"
Output: 0
Explanation: Efficient preprocessing avoids rechecking already-matched characters.
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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_first_unique_character_in_a_string(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_first_unique_character_in_a_string(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_first_unique_character_in_a_string(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

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
- `text`/`s`: str
- `pattern`/`queries`: variant-specific

### Output
- Index, boolean, count, or transformed string as required.

### Constraints
- `1 <= length <= 2 * 10^5`
- Use near-linear processing to avoid `O(n*m)` restarts.

### Example (Exact)
```text
Input:  text = "sadbutsad", pattern = "sad"
Output: 0
Explanation: Efficient preprocessing avoids rechecking already-matched characters.
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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_isomorphic_strings(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_isomorphic_strings(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_isomorphic_strings(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

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
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1,2,3,4]
Output: problem-specific result
Explanation: Use the pattern invariant to avoid repeated recomputation.
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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_ransom_note(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_ransom_note(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_ransom_note(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

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
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1,2,3,4]
Output: problem-specific result
Explanation: Use the pattern invariant to avoid repeated recomputation.
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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_longest_consecutive_sequence(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_longest_consecutive_sequence(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_longest_consecutive_sequence(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

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
    freq = {{0: 1}}
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
- Check every candidate pair/map relation directly; simple but expensive.

#### Python
```python
def brute_find_all_anagrams_in_a_string(nums, target):
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
- Sort to prune comparisons with two pointers while retaining original index mapping.

#### Python
```python
def better_find_all_anagrams_in_a_string(nums, target):
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
- Store visited facts in hash tables so each element contributes to the answer once.

#### Python
```python
def solve_find_all_anagrams_in_a_string(nums, target):
    seen = {{}}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []
```

#### Correctness (Why This Works)
- At iteration `i`, hash state stores exactly all prior elements needed for constant-time complement/count checks.
- If a valid partner exists before `i`, it is detected when processing `i`; if none exists, no missed pair remains.

#### Complexity
- Time `O(n)` average, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
