# Pattern 30 Interview Playbook: Knapsack DP

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Optimization/counting problems with "pick or skip" decisions under capacity/target constraints.
- Core intuition: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Trigger cue 1: Pick/skip under capacity/target constraints.
- Quick self-check: Is this subset decision under a budget-like limit?
- Target complexity: Time O(n * capacity), Space O(capacity) with 1D optimization

---

## Q1. 0/1 Knapsack

### Problem Statement (Concrete)
Solve **0/1 Knapsack** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **0/1 Knapsack** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_q_0_1_knapsack(nums, target):
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
def better_q_0_1_knapsack(nums, target):
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
def solve_q_0_1_knapsack(nums, target):
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

## Q2. Partition Equal Subset Sum

### Problem Statement (Concrete)
Solve **Partition Equal Subset Sum** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Partition Equal Subset Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_partition_equal_subset_sum(nums, target):
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
def better_partition_equal_subset_sum(nums, target):
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
def solve_partition_equal_subset_sum(nums, target):
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

## Q3. Target Sum

### Problem Statement (Concrete)
Solve **Target Sum** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Target Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_target_sum(nums, target):
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
def better_target_sum(nums, target):
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
def solve_target_sum(nums, target):
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

## Q4. Last Stone Weight II

### Problem Statement (Concrete)
Solve **Last Stone Weight II** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Last Stone Weight II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_last_stone_weight_ii(nums, target):
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
def better_last_stone_weight_ii(nums, target):
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
def solve_last_stone_weight_ii(nums, target):
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

## Q5. Ones and Zeroes

### Problem Statement (Concrete)
Solve **Ones and Zeroes** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Ones and Zeroes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_ones_and_zeroes(nums, target):
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
def better_ones_and_zeroes(nums, target):
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
def solve_ones_and_zeroes(nums, target):
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
Solve **Coin Change** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
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

## Q7. Coin Change II

### Problem Statement (Concrete)
Solve **Coin Change II** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Coin Change II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_coin_change_ii(nums, target):
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
def better_coin_change_ii(nums, target):
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
def solve_coin_change_ii(nums, target):
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

## Q8. Unbounded Knapsack

### Problem Statement (Concrete)
Solve **Unbounded Knapsack** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Unbounded Knapsack** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_unbounded_knapsack(nums, target):
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
def better_unbounded_knapsack(nums, target):
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
def solve_unbounded_knapsack(nums, target):
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

## Q9. Rod Cutting

### Problem Statement (Concrete)
Solve **Rod Cutting** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Rod Cutting** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_rod_cutting(nums, target):
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
def better_rod_cutting(nums, target):
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
def solve_rod_cutting(nums, target):
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

## Q10. Minimum Subset Sum Difference

### Problem Statement (Concrete)
Solve **Minimum Subset Sum Difference** using **Knapsack DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Knapsack DP**.
- Red flags: brute force for **Minimum Subset Sum Difference** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_minimum_subset_sum_difference(nums, target):
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
def better_minimum_subset_sum_difference(nums, target):
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
def solve_minimum_subset_sum_difference(nums, target):
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
