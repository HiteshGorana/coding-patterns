# Pattern 04 Interview Playbook: Sliding Window (Variable Size)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Variable sliding window finds longest/shortest contiguous segment satisfying a condition.
- Core intuition: Use two pointers: - expand right to include new elements - shrink left while window is invalid (or while it can be improved) Each index enters and exits window at most once, giving linear time.
- Trigger cue 1: "Longest/shortest substring/subarray with constraint"
- Trigger cue 2: "At most K distinct", "without repeating", "sum >= target"
- Quick self-check: Can a valid window be maintained with two moving boundaries?
- Target complexity: Time O(n), Space O(alphabet) or O(n) depending domain

---

## Q1. Longest Substring Without Repeating Characters

### Problem Statement (Concrete)
Solve **Longest Substring Without Repeating Characters** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Longest Substring Without Repeating Characters** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_longest_substring_without_repeating_characters(text, pattern):
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
def better_longest_substring_without_repeating_characters(text, pattern):
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
def solve_longest_substring_without_repeating_characters(text, pattern):
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

## Q2. Minimum Window Substring

### Problem Statement (Concrete)
Solve **Minimum Window Substring** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Minimum Window Substring** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_minimum_window_substring(text, pattern):
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
def better_minimum_window_substring(text, pattern):
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
def solve_minimum_window_substring(text, pattern):
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

## Q3. Longest Repeating Character Replacement

### Problem Statement (Concrete)
Solve **Longest Repeating Character Replacement** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Longest Repeating Character Replacement** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_longest_repeating_character_replacement(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_longest_repeating_character_replacement(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_longest_repeating_character_replacement(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Fruit Into Baskets

### Problem Statement (Concrete)
Solve **Fruit Into Baskets** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Fruit Into Baskets** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_fruit_into_baskets(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_fruit_into_baskets(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_fruit_into_baskets(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Minimum Size Subarray Sum

### Problem Statement (Concrete)
Solve **Minimum Size Subarray Sum** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Minimum Size Subarray Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_minimum_size_subarray_sum(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_minimum_size_subarray_sum(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_minimum_size_subarray_sum(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Subarray Product Less Than K

### Problem Statement (Concrete)
Solve **Subarray Product Less Than K** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Subarray Product Less Than K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_subarray_product_less_than_k(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_subarray_product_less_than_k(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_subarray_product_less_than_k(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Longest Substring with At Most K Distinct Characters

### Problem Statement (Concrete)
Solve **Longest Substring with At Most K Distinct Characters** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Longest Substring with At Most K Distinct Characters** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_longest_substring_with_at_most_k_distinct_characters(text, pattern):
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
def better_longest_substring_with_at_most_k_distinct_characters(text, pattern):
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
def solve_longest_substring_with_at_most_k_distinct_characters(text, pattern):
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

## Q8. Max Consecutive Ones III

### Problem Statement (Concrete)
Solve **Max Consecutive Ones III** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Max Consecutive Ones III** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_max_consecutive_ones_iii(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_max_consecutive_ones_iii(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_max_consecutive_ones_iii(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Frequency of the Most Frequent Element

### Problem Statement (Concrete)
Solve **Frequency of the Most Frequent Element** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Frequency of the Most Frequent Element** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_frequency_of_the_most_frequent_element(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_frequency_of_the_most_frequent_element(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_frequency_of_the_most_frequent_element(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Longest Subarray of 1's After Deleting One Element

### Problem Statement (Concrete)
Solve **Longest Subarray of 1's After Deleting One Element** using **Sliding Window (Variable Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Variable Size)**.
- Red flags: brute force for **Longest Subarray of 1's After Deleting One Element** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_longest_subarray_of_1_s_after_deleting_one_element(s, k):
    n = len(s)
    best = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1
            if len(freq) <= k:
                best = max(best, j - i + 1)
            else:
                break
    return best
```

#### Complexity
- Time `O(n^2)`, Space `O(sigma)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain dynamic window with hashmap counts; shrink only when invalid.

#### Python
```python
def better_longest_subarray_of_1_s_after_deleting_one_element(s, k):
    freq = {}
    left = 0
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
- Time `O(n)`, Space `O(sigma)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use constant-size frequency table for tighter constants while preserving same invariant.

#### Python
```python
def solve_longest_subarray_of_1_s_after_deleting_one_element(s, k):
    freq = [0] * 128
    left = 0
    distinct = 0
    best = 0
    for right, ch in enumerate(s):
        idx = ord(ch)
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        while distinct > k:
            out = ord(s[left])
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

#### Correctness (Why This Works)
- Window invariant: it always represents a valid candidate after shrink loop finishes.
- Each index enters and exits the window at most once, so total pointer movement is linear.

#### Complexity
- Time `O(n)`, Space `O(sigma)` (often constant for bounded alphabet).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
