# Pattern 03 Interview Playbook: Sliding Window (Fixed Size)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Fixed-size sliding window optimizes repeated computations over all subarrays/substrings of length `k`.
- Core intuition: Adjacent windows overlap heavily. Instead of recomputing, update window result incrementally: - add incoming element - remove outgoing element This turns `O(n*k)` into `O(n)`.
- Trigger cue 1: Window size `k` is fixed.
- Trigger cue 2: Need max/min/sum/avg over every size-k segment.
- Quick self-check: Can current window answer be updated with +incoming -outgoing?
- Target complexity: Time O(n), Space O(1) or O(alphabet) if frequency table needed

---

## Q1. Maximum Average Subarray I

### Problem Statement (Concrete)
Solve **Maximum Average Subarray I** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Maximum Average Subarray I** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute each length-`k` window sum independently.

#### Python
```python
def brute_maximum_average_subarray_i(nums, k):
    best = -10**18
    for i in range(len(nums) - k + 1):
        best = max(best, sum(nums[i:i+k]))
    return best / k
```

#### Complexity
- Time `O(n*k)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Slide fixed-size window by adding entering and removing leaving element.

#### Python
```python
def better_maximum_average_subarray_i(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Fixed window update is already asymptotically optimal.

#### Python
```python
def better_maximum_average_subarray_i(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k
```

#### Correctness (Why This Works)
- Every window differs from previous by exactly two elements.
- Maintaining running sum yields exact value for each window in O(1) update.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Max Sum Subarray of Size K

### Problem Statement (Concrete)
Solve **Max Sum Subarray of Size K** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Max Sum Subarray of Size K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute each length-`k` window sum independently.

#### Python
```python
def brute_max_sum_subarray_of_size_k(nums, k):
    best = -10**18
    for i in range(len(nums) - k + 1):
        best = max(best, sum(nums[i:i+k]))
    return best / k
```

#### Complexity
- Time `O(n*k)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Slide fixed-size window by adding entering and removing leaving element.

#### Python
```python
def better_max_sum_subarray_of_size_k(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Fixed window update is already asymptotically optimal.

#### Python
```python
def better_max_sum_subarray_of_size_k(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k
```

#### Correctness (Why This Works)
- Every window differs from previous by exactly two elements.
- Maintaining running sum yields exact value for each window in O(1) update.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Find All Anagrams in a String

### Problem Statement (Concrete)
Solve **Find All Anagrams in a String** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Find All Anagrams in a String** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort every fixed-length candidate window.

#### Python
```python
def brute_find_all_anagrams_in_a_string(s, p):
    m = len(p)
    key = sorted(p)
    for i in range(len(s) - m + 1):
        if sorted(s[i:i+m]) == key:
            return True
    return False
```

#### Complexity
- Time `O((n-m+1) * m log m)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fixed-size frequency window for pattern length.

#### Python
```python
def better_find_all_anagrams_in_a_string(s, p):
    m = len(p)
    if m > len(s):
        return False
    need = [0] * 26
    win = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    for i, ch in enumerate(s):
        win[ord(ch) - 97] += 1
        if i >= m:
            win[ord(s[i - m]) - 97] -= 1
        if win == need:
            return True
    return False
```

#### Complexity
- Time `O(n * sigma)` with small alphabet constant.

### Approach 3: Optimal (Best)
#### Intuition
- Frequency-array window is optimal for lowercase alphabet.

#### Python
```python
def better_find_all_anagrams_in_a_string(s, p):
    m = len(p)
    if m > len(s):
        return False
    need = [0] * 26
    win = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    for i, ch in enumerate(s):
        win[ord(ch) - 97] += 1
        if i >= m:
            win[ord(s[i - m]) - 97] -= 1
        if win == need:
            return True
    return False
```

#### Correctness (Why This Works)
- An anagram exists exactly when window frequency vector equals pattern vector.
- Sliding window updates counts in O(1) per move.

#### Complexity
- Time `O(n)`, Space `O(1)` for fixed alphabet.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Permutation in String

### Problem Statement (Concrete)
Solve **Permutation in String** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Permutation in String** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_permutation_in_string(start, target):
    # DFS/backtracking over state graph (practical only for tiny spaces).
    best = 10**9
    seen = set()
    def dfs(state, steps):
        nonlocal best
        if steps >= best or state in seen:
            return
        if state == target:
            best = min(best, steps)
            return
        seen.add(state)
        for i in range(len(state)):
            d = int(state[i])
            for nd in ((d + 1) % 10, (d - 1) % 10):
                nxt = state[:i] + str(nd) + state[i+1:]
                dfs(nxt, steps + 1)
        seen.remove(state)
    dfs(start, 0)
    return -1 if best == 10**9 else best
```

#### Complexity
- Time exponential in branching depth, Space `O(depth)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Classic BFS over state graph gives shortest steps in unweighted transitions.

#### Python
```python
from collections import deque

def better_permutation_in_string(start, target, dead=None):
    dead = set(dead or [])
    if start in dead:
        return -1
    q = deque([(start, 0)])
    seen = {start}
    while q:
        state, d = q.popleft()
        if state == target:
            return d
        for i in range(len(state)):
            x = int(state[i])
            for y in ((x + 1) % 10, (x - 1) % 10):
                nxt = state[:i] + str(y) + state[i+1:]
                if nxt not in seen and nxt not in dead:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
    return -1
```

#### Complexity
- Time `O(V + E)` over reachable states, Space `O(V)`.

### Approach 3: Optimal (Best)
#### Intuition
- Bidirectional BFS shrinks explored frontier dramatically on symmetric state spaces.

#### Python
```python
from collections import deque

def solve_permutation_in_string(start, target, dead=None):
    dead = set(dead or [])
    if start in dead or target in dead:
        return -1
    if start == target:
        return 0

    front = {start}
    back = {target}
    seen = {start, target}
    steps = 0

    while front and back:
        if len(front) > len(back):
            front, back = back, front
        nxt_front = set()
        steps += 1
        for state in front:
            for i in range(len(state)):
                x = int(state[i])
                for y in ((x + 1) % 10, (x - 1) % 10):
                    nxt = state[:i] + str(y) + state[i+1:]
                    if nxt in dead:
                        continue
                    if nxt in back:
                        return steps
                    if nxt not in seen:
                        seen.add(nxt)
                        nxt_front.add(nxt)
        front = nxt_front
    return -1
```

#### Correctness (Why This Works)
- Each frontier expansion adds exactly one step distance from its side.
- First frontier intersection corresponds to minimal combined distance by BFS layering.

#### Complexity
- Time `O(b^(d/2))` typical, Space `O(b^(d/2))`, where `b` is branching factor.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Sliding Window Maximum

### Problem Statement (Concrete)
Solve **Sliding Window Maximum** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Sliding Window Maximum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Take max over each window separately.

#### Python
```python
def brute_sliding_window_maximum(nums, k):
    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
```

#### Complexity
- Time `O(n*k)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Monotonic deque keeps candidate maximum indices for current window.

#### Python
```python
from collections import deque

def better_sliding_window_maximum(nums, k):
    dq = deque()
    out = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

#### Complexity
- Time `O(n)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Each index is inserted and removed at most once in deque.

#### Python
```python
from collections import deque

def better_sliding_window_maximum(nums, k):
    dq = deque()
    out = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

#### Correctness (Why This Works)
- Deque is strictly decreasing by value and contains only in-window indices.
- Front index is always maximum for current window.

#### Complexity
- Time `O(n)`, Space `O(k)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Defuse the Bomb

### Problem Statement (Concrete)
Solve **Defuse the Bomb** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Defuse the Bomb** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_defuse_the_bomb(s, k):
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
def better_defuse_the_bomb(s, k):
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
def solve_defuse_the_bomb(s, k):
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

## Q7. K Radius Subarray Averages

### Problem Statement (Concrete)
Solve **K Radius Subarray Averages** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **K Radius Subarray Averages** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_k_radius_subarray_averages(s, k):
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
def better_k_radius_subarray_averages(s, k):
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
def solve_k_radius_subarray_averages(s, k):
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

## Q8. Number of Sub-arrays of Size K and Average >= Threshold

### Problem Statement (Concrete)
Solve **Number of Sub-arrays of Size K and Average >= Threshold** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Number of Sub-arrays of Size K and Average >= Threshold** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_number_of_sub_arrays_of_size_k_and_average_threshold(s, k):
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
def better_number_of_sub_arrays_of_size_k_and_average_threshold(s, k):
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
def solve_number_of_sub_arrays_of_size_k_and_average_threshold(s, k):
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

## Q9. Maximum Number of Vowels in a Substring of Given Length

### Problem Statement (Concrete)
Solve **Maximum Number of Vowels in a Substring of Given Length** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Maximum Number of Vowels in a Substring of Given Length** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_maximum_number_of_vowels_in_a_substring_of_given_length(text, pattern):
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
def better_maximum_number_of_vowels_in_a_substring_of_given_length(text, pattern):
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
def solve_maximum_number_of_vowels_in_a_substring_of_given_length(text, pattern):
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

## Q10. Grumpy Bookstore Owner

### Problem Statement (Concrete)
Solve **Grumpy Bookstore Owner** using **Sliding Window (Fixed Size)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Sliding Window (Fixed Size)**.
- Red flags: brute force for **Grumpy Bookstore Owner** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every start and extend until constraint breaks.

#### Python
```python
def brute_grumpy_bookstore_owner(s, k):
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
def better_grumpy_bookstore_owner(s, k):
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
def solve_grumpy_bookstore_owner(s, k):
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
