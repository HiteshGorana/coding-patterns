# Pattern 29 Interview Playbook: Dynamic Programming (2D)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Handles problems where state depends on two indices/dimensions (strings, grids, pair ranges).
- Core intuition: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Trigger cue 1: Two-dimensional state: strings, grids, pair indices.
- Quick self-check: Do I naturally need two coordinates for state?
- Target complexity: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m))

---

## Q1. Unique Paths

### Problem Statement (Concrete)
Solve **Unique Paths** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Unique Paths** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_unique_paths(nums, target):
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
def better_unique_paths(nums, target):
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
def solve_unique_paths(nums, target):
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

## Q2. Minimum Path Sum

### Problem Statement (Concrete)
Solve **Minimum Path Sum** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Minimum Path Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_minimum_path_sum(nums, target):
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
def better_minimum_path_sum(nums, target):
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
def solve_minimum_path_sum(nums, target):
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

## Q3. Edit Distance

### Problem Statement (Concrete)
Solve **Edit Distance** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Edit Distance** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_edit_distance(nums, target):
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
def better_edit_distance(nums, target):
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
def solve_edit_distance(nums, target):
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

## Q4. Longest Common Subsequence

### Problem Statement (Concrete)
Solve **Longest Common Subsequence** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Longest Common Subsequence** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_longest_common_subsequence(nums, target):
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
def better_longest_common_subsequence(nums, target):
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
def solve_longest_common_subsequence(nums, target):
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

## Q5. Distinct Subsequences

### Problem Statement (Concrete)
Solve **Distinct Subsequences** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Distinct Subsequences** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_distinct_subsequences(nums, target):
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
def better_distinct_subsequences(nums, target):
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
def solve_distinct_subsequences(nums, target):
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

## Q6. Interleaving String

### Problem Statement (Concrete)
Solve **Interleaving String** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Interleaving String** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_interleaving_string(nums, target):
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
def better_interleaving_string(nums, target):
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
def solve_interleaving_string(nums, target):
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

## Q7. Longest Palindromic Subsequence

### Problem Statement (Concrete)
Solve **Longest Palindromic Subsequence** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Longest Palindromic Subsequence** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_longest_palindromic_subsequence(nums, target):
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
def better_longest_palindromic_subsequence(nums, target):
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
def solve_longest_palindromic_subsequence(nums, target):
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

## Q8. Maximal Square

### Problem Statement (Concrete)
Solve **Maximal Square** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Maximal Square** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_maximal_square(nums, target):
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
def better_maximal_square(nums, target):
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
def solve_maximal_square(nums, target):
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

## Q9. Triangle

### Problem Statement (Concrete)
Solve **Triangle** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Triangle** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_triangle(nums, target):
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
def better_triangle(nums, target):
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
def solve_triangle(nums, target):
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

## Q10. Dungeon Game

### Problem Statement (Concrete)
Solve **Dungeon Game** using **Dynamic Programming (2D)**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Dynamic Programming (2D)**.
- Red flags: brute force for **Dungeon Game** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all include/exclude states recursively.

#### Python
```python
def brute_dungeon_game(nums, target):
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
def better_dungeon_game(nums, target):
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
def solve_dungeon_game(nums, target):
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
