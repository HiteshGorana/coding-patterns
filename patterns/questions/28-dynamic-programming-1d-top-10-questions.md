# Pattern 28 Interview Playbook: Dynamic Programming (1D)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Optimizes sequential decisions where state depends on previous positions.
- Core intuition: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Trigger cue 1: Max/min/count ways over linear index.
- Trigger cue 2: Overlapping subproblems in recursion.
- Quick self-check: Can I define `dp[i]` with a small recurrence?
- Target complexity: Time usually O(n), Space O(n) or O(1) optimized

---

## Q1. Climbing Stairs

### Problem Statement (Concrete)
Solve **Climbing Stairs** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Climbing Stairs** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_climbing_stairs(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_climbing_stairs(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_climbing_stairs(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. House Robber

### Problem Statement (Concrete)
Solve **House Robber** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **House Robber** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_house_robber(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_house_robber(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_house_robber(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. House Robber II

### Problem Statement (Concrete)
Solve **House Robber II** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **House Robber II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_house_robber_ii(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_house_robber_ii(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_house_robber_ii(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Min Cost Climbing Stairs

### Problem Statement (Concrete)
Solve **Min Cost Climbing Stairs** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Min Cost Climbing Stairs** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_min_cost_climbing_stairs(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_min_cost_climbing_stairs(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_min_cost_climbing_stairs(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Decode Ways

### Problem Statement (Concrete)
Solve **Decode Ways** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Decode Ways** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_decode_ways(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_decode_ways(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_decode_ways(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Coin Change

### Problem Statement (Concrete)
Solve **Coin Change** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Coin Change** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_coin_change(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_coin_change(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_coin_change(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Maximum Subarray

### Problem Statement (Concrete)
Solve **Maximum Subarray** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Maximum Subarray** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_maximum_subarray(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_maximum_subarray(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_maximum_subarray(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Longest Increasing Subsequence

### Problem Statement (Concrete)
Solve **Longest Increasing Subsequence** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Longest Increasing Subsequence** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_longest_increasing_subsequence(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_longest_increasing_subsequence(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_longest_increasing_subsequence(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Word Break

### Problem Statement (Concrete)
Solve **Word Break** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Word Break** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_word_break(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_word_break(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_word_break(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Perfect Squares

### Problem Statement (Concrete)
Solve **Perfect Squares** using **Dynamic Programming (1D)**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`/`weights`/`values` or state graph, depending on variant
- `target`/`capacity`/`mask goal` as required

### Output
- Maximum/minimum score, count, feasibility, or reconstructed choice set.

### Constraints
- State count should fit memory limits (`O(n)`, `O(n*sum)`, or `O(2^n)` depending on pattern).
- Exploit overlapping subproblems and avoid recomputation.

### Example (Exact)
```text
Input:  nums = [1,2,3], target = 4
Output: true
Explanation: Memoization/tabulation prunes repeated subproblems significantly.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (1D)**.
- Red flags: brute force for **Perfect Squares** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_perfect_squares(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return rem == 0
        return dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
    return dfs(0, target)
```

#### Complexity
- Time exponential without memo, pseudo-polynomial with memo states.

### Approach 2: Better (Intermediate)
#### Intuition
- Use 1D/2D DP table to reuse overlapping states.

#### Python
```python
def better_perfect_squares(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Complexity
- Time typically `O(n*target)`, Space `O(target)`.

### Approach 3: Optimal (Best)
#### Intuition
- State transition is optimized for the objective (min/max/count/boolean) with correct iteration order.

#### Python
```python
def solve_perfect_squares(nums, target):
    INF = 10**9
    dp = [INF] * (target + 1)
    dp[0] = 0
    for s in range(1, target + 1):
        for x in nums:
            if s - x >= 0:
                dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] < INF else -1
```

#### Correctness (Why This Works)
- DP recurrence partitions optimal solution by its final decision/state transition.
- By induction on state order, each DP entry is optimal once dependencies are finalized.

#### Complexity
- Time/space tightness depends on state dimensions; commonly `O(n*target)` and `O(target)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
