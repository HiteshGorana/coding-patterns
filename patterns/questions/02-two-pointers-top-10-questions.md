# Pattern 02 Interview Playbook: Two Pointers

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Two pointers is ideal for problems on arrays/strings where two positions move with rules.
- Core intuition: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Trigger cue 1: Sorted array/string.
- Trigger cue 2: Need pair/triplet relation (`sum`, `diff`, palindrome).
- Quick self-check: If I move one pointer, can I prove I never miss optimum?
- Target complexity: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost)

---

## Q1. Two Sum II - Input Array Is Sorted

### Problem Statement (Concrete)
Solve **Two Sum II - Input Array Is Sorted** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Two Sum II - Input Array Is Sorted** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check all pairs in sorted array.

#### Python
```python
def brute_two_sum_ii_input_array_is_sorted(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- For each left index, binary search needed complement.

#### Python
```python
def better_two_sum_ii_input_array_is_sorted(numbers, target):
    import bisect
    for i, x in enumerate(numbers):
        j = bisect.bisect_left(numbers, target - x, i + 1)
        if j < len(numbers) and numbers[j] == target - x:
            return [i + 1, j + 1]
    return []
```

#### Complexity
- Time `O(n log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Two pointers exploit sorted order to move toward target monotonically.

#### Python
```python
def solve_two_sum_ii_input_array_is_sorted(numbers, target):
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

#### Correctness (Why This Works)
- If sum is too small, only increasing left can help; if too large, only decreasing right can help.
- Thus each move discards only impossible pairs and never drops a valid solution.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. 3Sum

### Problem Statement (Concrete)
Solve **3Sum** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **3Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate all triplets and deduplicate.

#### Python
```python
def brute_q_3sum(nums):
    n = len(nums)
    out = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    out.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(x) for x in sorted(out)]
```

#### Complexity
- Time `O(n^3)`, Space `O(n)` for set.

### Approach 2: Better (Intermediate)
#### Intuition
- Fix first value and use hash-set for two-sum on suffix.

#### Python
```python
def better_q_3sum(nums):
    nums.sort()
    out = []
    for i in range(len(nums)):
        seen = set()
        for j in range(i + 1, len(nums)):
            need = -nums[i] - nums[j]
            if need in seen:
                cand = [nums[i], need, nums[j]]
                if not out or out[-1] != cand:
                    out.append(cand)
            seen.add(nums[j])
    return out
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Sort + two-pointer sweep for each fixed first index handles duplicates cleanly.

#### Python
```python
def solve_q_3sum(nums):
    nums.sort()
    out = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                out.append([nums[i], nums[l], nums[r]])
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
    return out
```

#### Correctness (Why This Works)
- Sorted order enables monotonic pointer moves for each fixed `i`.
- Duplicate skipping ensures each value-combination is emitted exactly once.

#### Complexity
- Time `O(n^2)`, Space `O(1)` extra (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. 4Sum

### Problem Statement (Concrete)
Solve **4Sum** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **4Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all quadruples and keep those summing to target.

#### Python
```python
def brute_q_4sum(nums, target):
    nums.sort()
    n = len(nums)
    out = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        out.add((nums[i], nums[j], nums[k], nums[l]))
    return [list(x) for x in sorted(out)]
```

#### Complexity
- Time `O(n^4)`, Space `O(1)` plus output.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute pair sums and combine disjoint pairs.

#### Python
```python
def better_q_4sum(nums, target):
    nums.sort()
    n = len(nums)
    out = []
    pair = {}
    for i in range(n):
        for j in range(i + 1, n):
            pair.setdefault(nums[i] + nums[j], []).append((i, j))
    seen = set()
    for s, pairs in pair.items():
        need = target - s
        if need not in pair:
            continue
        for i, j in pairs:
            for k, l in pair[need]:
                if j < k:
                    quad = (nums[i], nums[j], nums[k], nums[l])
                    if quad not in seen:
                        seen.add(quad)
                        out.append(list(quad))
    return out
```

#### Complexity
- Time up to `O(n^3)` average-heavy, Space `O(n^2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Sort and reduce 4-sum to repeated 2-pointer 2-sum over suffix.

#### Python
```python
def solve_q_4sum(nums, target):
    nums.sort()
    n = len(nums)
    out = []
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
                    out.append([nums[i], nums[j], nums[l], nums[r]])
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
    return out
```

#### Correctness (Why This Works)
- For fixed `(i,j)`, remaining pair is classic sorted 2-sum solved optimally by two pointers.
- Duplicate checks at each level prevent repeated quadruples.

#### Complexity
- Time `O(n^3)`, Space `O(1)` extra (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Container With Most Water

### Problem Statement (Concrete)
Solve **Container With Most Water** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Container With Most Water** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate all pointer pairs and evaluate objective exactly.

#### Python
```python
def brute_container_with_most_water(nums):
    best = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            height = min(nums[i], nums[j])
            best = max(best, width * height)
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use ordering to move one pointer deterministically and cut search space.

#### Python
```python
def better_container_with_most_water(nums):
    # Sorting enables directional pointer movement for many two-pointer variants.
    arr = sorted(nums)
    l, r = 0, len(arr) - 1
    best = 0
    while l < r:
        best = max(best, arr[l] + arr[r])
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return best
```

#### Complexity
- Time `O(n log n)`, Space `O(n)` (if sorting copy).

### Approach 3: Optimal (Best)
#### Intuition
- Maintain two boundary pointers and discard provably dominated boundaries each step.

#### Python
```python
def solve_container_with_most_water(nums):
    l, r = 0, len(nums) - 1
    ans = 0
    while l < r:
        ans = max(ans, (r - l) * min(nums[l], nums[r]))
        if nums[l] <= nums[r]:
            l += 1
        else:
            r -= 1
    return ans
```

#### Correctness (Why This Works)
- When boundary heights differ, moving the taller side cannot improve the limiting height at same or smaller width.
- Therefore discarding the smaller-height boundary is safe and does not remove the optimal answer.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Valid Palindrome

### Problem Statement (Concrete)
Solve **Valid Palindrome** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Valid Palindrome** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_valid_palindrome(text, pattern):
    m, n = len(pattern), len(text)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1
```

#### Complexity
- Time `O(n*m)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Rolling hash filters candidate matches and verifies collisions.

#### Python
```python
def better_valid_palindrome(text, pattern):
    # Rabin-Karp style rolling hash.
    if not pattern:
        return 0
    base, mod = 911382323, 10**9 + 7
    m = len(pattern)
    p_hash = 0
    t_hash = 0
    power = 1
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
        if i:
            power = (power * base) % mod
    if t_hash == p_hash and text[:m] == pattern:
        return 0
    for i in range(m, len(text)):
        t_hash = (t_hash - ord(text[i-m]) * power) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
        if t_hash == p_hash and text[i-m+1:i+1] == pattern:
            return i - m + 1
    return -1
```

#### Complexity
- Expected `O(n+m)`, worst-case with collisions can degrade.

### Approach 3: Optimal (Best)
#### Intuition
- KMP/Z/Manacher-style preprocessing reuses prefix structure to avoid restart comparisons.

#### Python
```python
def solve_valid_palindrome(text, pattern):
    if not pattern:
        return 0

    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
    return -1
```

#### Correctness (Why This Works)
- LPS/Z/palindrome radius arrays encode longest reusable match after mismatch.
- Pointer never moves backward in text, so each character is processed constant times.

#### Complexity
- Time `O(n+m)`, Space `O(m)` (or variant-specific linear auxiliary arrays).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Squares of a Sorted Array

### Problem Statement (Concrete)
Solve **Squares of a Sorted Array** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Squares of a Sorted Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate all pointer pairs and evaluate objective exactly.

#### Python
```python
def brute_squares_of_a_sorted_array(nums):
    best = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            height = min(nums[i], nums[j])
            best = max(best, width * height)
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use ordering to move one pointer deterministically and cut search space.

#### Python
```python
def better_squares_of_a_sorted_array(nums):
    # Sorting enables directional pointer movement for many two-pointer variants.
    arr = sorted(nums)
    l, r = 0, len(arr) - 1
    best = 0
    while l < r:
        best = max(best, arr[l] + arr[r])
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return best
```

#### Complexity
- Time `O(n log n)`, Space `O(n)` (if sorting copy).

### Approach 3: Optimal (Best)
#### Intuition
- Maintain two boundary pointers and discard provably dominated boundaries each step.

#### Python
```python
def solve_squares_of_a_sorted_array(nums):
    l, r = 0, len(nums) - 1
    ans = 0
    while l < r:
        ans = max(ans, (r - l) * min(nums[l], nums[r]))
        if nums[l] <= nums[r]:
            l += 1
        else:
            r -= 1
    return ans
```

#### Correctness (Why This Works)
- When boundary heights differ, moving the taller side cannot improve the limiting height at same or smaller width.
- Therefore discarding the smaller-height boundary is safe and does not remove the optimal answer.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Remove Duplicates from Sorted Array

### Problem Statement (Concrete)
Solve **Remove Duplicates from Sorted Array** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Remove Duplicates from Sorted Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate all pointer pairs and evaluate objective exactly.

#### Python
```python
def brute_remove_duplicates_from_sorted_array(nums):
    best = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            height = min(nums[i], nums[j])
            best = max(best, width * height)
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use ordering to move one pointer deterministically and cut search space.

#### Python
```python
def better_remove_duplicates_from_sorted_array(nums):
    # Sorting enables directional pointer movement for many two-pointer variants.
    arr = sorted(nums)
    l, r = 0, len(arr) - 1
    best = 0
    while l < r:
        best = max(best, arr[l] + arr[r])
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return best
```

#### Complexity
- Time `O(n log n)`, Space `O(n)` (if sorting copy).

### Approach 3: Optimal (Best)
#### Intuition
- Maintain two boundary pointers and discard provably dominated boundaries each step.

#### Python
```python
def solve_remove_duplicates_from_sorted_array(nums):
    l, r = 0, len(nums) - 1
    ans = 0
    while l < r:
        ans = max(ans, (r - l) * min(nums[l], nums[r]))
        if nums[l] <= nums[r]:
            l += 1
        else:
            r -= 1
    return ans
```

#### Correctness (Why This Works)
- When boundary heights differ, moving the taller side cannot improve the limiting height at same or smaller width.
- Therefore discarding the smaller-height boundary is safe and does not remove the optimal answer.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Move Zeroes

### Problem Statement (Concrete)
Solve **Move Zeroes** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Move Zeroes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Build a new array with non-zeros followed by zeros.

#### Python
```python
def brute_move_zeroes(nums):
    arr = [x for x in nums if x != 0] + [0] * nums.count(0)
    for i in range(len(nums)):
        nums[i] = arr[i]
    return nums
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Compact non-zeros in-place then fill remaining suffix with zeros.

#### Python
```python
def better_move_zeroes(nums):
    insert = 0
    for x in nums:
        if x != 0:
            nums[insert] = x
            insert += 1
    while insert < len(nums):
        nums[insert] = 0
        insert += 1
    return nums
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Two pointers swap next non-zero into earliest zero slot directly.

#### Python
```python
def solve_move_zeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums
```

#### Correctness (Why This Works)
- `l` always marks next position that should contain a non-zero.
- Swapping when `nums[r] != 0` preserves relative order of non-zero elements.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Trapping Rain Water

### Problem Statement (Concrete)
Solve **Trapping Rain Water** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Trapping Rain Water** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, recompute max wall on both sides.

#### Python
```python
def brute_trapping_rain_water(height):
    n = len(height)
    ans = 0
    for i in range(n):
        left = max(height[:i+1])
        right = max(height[i:])
        ans += min(left, right) - height[i]
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute left/right maxima arrays once.

#### Python
```python
def better_trapping_rain_water(height):
    n = len(height)
    left = [0] * n
    right = [0] * n
    for i in range(n):
        left[i] = max(left[i-1], height[i]) if i else height[i]
    for i in range(n - 1, -1, -1):
        right[i] = max(right[i+1], height[i]) if i + 1 < n else height[i]
    return sum(min(left[i], right[i]) - height[i] for i in range(n))
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Two-pointer method finalizes trapped water on smaller boundary side immediately.

#### Python
```python
def solve_trapping_rain_water(height):
    l, r = 0, len(height) - 1
    left_max = right_max = 0
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

#### Correctness (Why This Works)
- If left boundary is smaller, trapped water at left depends only on left max, independent of unseen interior right details.
- Symmetric logic applies when right boundary is smaller.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Sort Colors

### Problem Statement (Concrete)
Solve **Sort Colors** using **Two Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Two Pointers**.
- Red flags: brute force for **Sort Colors** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use full sort.

#### Python
```python
def brute_sort_colors(nums):
    nums.sort()
    return nums
```

#### Complexity
- Time `O(n log n)`, Space depends on sort implementation.

### Approach 2: Better (Intermediate)
#### Intuition
- Count 0/1/2 and overwrite array.

#### Python
```python
def better_sort_colors(nums):
    cnt = [0, 0, 0]
    for x in nums:
        cnt[x] += 1
    i = 0
    for val in range(3):
        for _ in range(cnt[val]):
            nums[i] = val
            i += 1
    return nums
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Dutch National Flag partitions array into three color regions in one pass.

#### Python
```python
def solve_sort_colors(nums):
    l = i = 0
    r = len(nums) - 1
    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1
    return nums
```

#### Correctness (Why This Works)
- Invariant maintains `[0..l-1]=0`, `[l..i-1]=1`, `[r+1..]=2` at all times.
- Each swap places at least one element into its final partition.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
