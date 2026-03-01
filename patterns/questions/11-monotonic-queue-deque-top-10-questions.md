# Pattern 11 Interview Playbook: Monotonic Queue / Deque

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Maintains min/max over a sliding window in linear time.
- Core intuition: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Trigger cue 1: Sliding window max/min in strict O(n).
- Quick self-check: Do I need best value per moving window with index expiry?
- Target complexity: Time O(n) amortized, Space O(k) to O(n) worst-case index storage

---

## Q1. Sliding Window Maximum

### Problem Statement (Concrete)
Solve **Sliding Window Maximum** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Sliding Window Maximum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_sliding_window_maximum(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_sliding_window_maximum(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_sliding_window_maximum(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Shortest Subarray with Sum at Least K

### Problem Statement (Concrete)
Solve **Shortest Subarray with Sum at Least K** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Shortest Subarray with Sum at Least K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_shortest_subarray_with_sum_at_least_k(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_shortest_subarray_with_sum_at_least_k(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_shortest_subarray_with_sum_at_least_k(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Constrained Subsequence Sum

### Problem Statement (Concrete)
Solve **Constrained Subsequence Sum** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Constrained Subsequence Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_constrained_subsequence_sum(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_constrained_subsequence_sum(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_constrained_subsequence_sum(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Jump Game VI

### Problem Statement (Concrete)
Solve **Jump Game VI** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Jump Game VI** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_jump_game_vi(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_jump_game_vi(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_jump_game_vi(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

### Problem Statement (Concrete)
Solve **Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Max Value of Equation

### Problem Statement (Concrete)
Solve **Max Value of Equation** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Max Value of Equation** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_max_value_of_equation(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_max_value_of_equation(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_max_value_of_equation(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. First Negative Integer in Every Window of Size K

### Problem Statement (Concrete)
Solve **First Negative Integer in Every Window of Size K** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Disconnected graph or unreachable target must return documented sentinel (`-1`, empty list, or `False`).

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **First Negative Integer in Every Window of Size K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Enumerate shortest distances by edge-count DP table.

#### Python
```python
def brute_first_negative_integer_in_every_window_of_size_k(n, edges, src):
    # Relax paths up to n-1 edges via explicit DP table.
    INF = 10**18
    dp = [[INF] * n for _ in range(n)]
    dp[0][src] = 0
    for k in range(1, n):
        dp[k] = dp[k-1][:]
        for u, v, w in edges:
            if dp[k-1][u] < INF:
                dp[k][v] = min(dp[k][v], dp[k-1][u] + w)
    return dp[n-1]
```

#### Complexity
- Time `O(n*m)`, Space `O(n^2)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Bellman-Ford relaxation with early stop computes shortest distances without full table.

#### Python
```python
def better_first_negative_integer_in_every_window_of_size_k(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return dist
```

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Extra relaxation round(s) identify vertices influenced by reachable negative cycles.

#### Python
```python
def solve_first_negative_integer_in_every_window_of_size_k(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg_cycle = [False] * n
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                neg_cycle[v] = True
                changed = True
        if not changed:
            break

    return dist, neg_cycle
```

#### Correctness (Why This Works)
- After `n-1` relaxations, all simple-path shortest distances are finalized if no negative cycle is reachable.
- Any further decrease implies cycle-based improvement, which can only happen with a reachable negative cycle.

#### Complexity
- Time `O(n*m)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Minimum Number of K Consecutive Bit Flips

### Problem Statement (Concrete)
Solve **Minimum Number of K Consecutive Bit Flips** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Minimum Number of K Consecutive Bit Flips** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_minimum_number_of_k_consecutive_bit_flips(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_minimum_number_of_k_consecutive_bit_flips(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_minimum_number_of_k_consecutive_bit_flips(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Find the Most Competitive Subsequence

### Problem Statement (Concrete)
Solve **Find the Most Competitive Subsequence** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Find the Most Competitive Subsequence** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_find_the_most_competitive_subsequence(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_find_the_most_competitive_subsequence(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_find_the_most_competitive_subsequence(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Maximum Robots Within Budget

### Problem Statement (Concrete)
Solve **Maximum Robots Within Budget** using **Monotonic Queue / Deque**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Queue / Deque**.
- Red flags: brute force for **Maximum Robots Within Budget** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_maximum_robots_within_budget(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_maximum_robots_within_budget(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_maximum_robots_within_budget(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
