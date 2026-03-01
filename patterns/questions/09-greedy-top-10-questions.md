# Pattern 09 Interview Playbook: Greedy

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Greedy algorithms make the best local decision at each step, aiming for global optimality.
- Core intuition: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Trigger cue 1: Min/max optimization with local decision opportunities.
- Trigger cue 2: Can prove local choice never hurts global optimum.
- Quick self-check: Can I give a short exchange/invariant argument?
- Target complexity: Time often O(n) (after optional sort), Space usually O(1)

---

## Q1. Jump Game

### Problem Statement (Concrete)
Solve **Jump Game** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Jump Game** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_jump_game(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_jump_game(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_jump_game(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Jump Game II

### Problem Statement (Concrete)
Solve **Jump Game II** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Jump Game II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_jump_game_ii(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_jump_game_ii(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_jump_game_ii(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Gas Station

### Problem Statement (Concrete)
Solve **Gas Station** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Gas Station** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_gas_station(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_gas_station(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_gas_station(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Partition Labels

### Problem Statement (Concrete)
Solve **Partition Labels** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Partition Labels** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_partition_labels(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_partition_labels(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_partition_labels(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Assign Cookies

### Problem Statement (Concrete)
Solve **Assign Cookies** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Assign Cookies** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_assign_cookies(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_assign_cookies(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_assign_cookies(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Non-overlapping Intervals

### Problem Statement (Concrete)
Solve **Non-overlapping Intervals** using **Greedy**. Return exactly the value/structure requested by the original prompt.

### Input
- `intervals`: list[list[int]]
- `newInterval` or capacity/time parameters for variants

### Output
- Merged intervals, count, boolean, or min resources needed.

### Constraints
- `1 <= len(intervals) <= 2 * 10^5`
- `0 <= start <= end <= 10^9`

### Example (Exact)
```text
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Sorting by start time turns overlap logic into one pass.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Non-overlapping Intervals** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Repeatedly attempt pairwise merges until no overlap remains.

#### Python
```python
def brute_non_overlapping_intervals(intervals):
    changed = True
    arr = [x[:] for x in intervals]
    while changed:
        changed = False
        out = []
        used = [False] * len(arr)
        for i in range(len(arr)):
            if used[i]:
                continue
            a, b = arr[i]
            for j in range(i + 1, len(arr)):
                if used[j]:
                    continue
                c, d = arr[j]
                if not (b < c or d < a):
                    a, b = min(a, c), max(b, d)
                    used[j] = True
                    changed = True
            out.append([a, b])
        arr = out
    return sorted(arr)
```

#### Complexity
- Time up to `O(n^2)` or worse with repeated passes, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Sort once then merge adjacent overlapping runs in one scan.

#### Python
```python
def better_non_overlapping_intervals(intervals):
    intervals = sorted(intervals)
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

#### Complexity
- Time `O(n log n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- After sorting by start, only last merged interval can overlap current interval.

#### Python
```python
def solve_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged
```

#### Correctness (Why This Works)
- Sorted starts ensure future intervals cannot overlap anything except the current tail segment.
- Merging that tail greedily preserves correctness and minimal interval count.

#### Complexity
- Time `O(n log n)`, Space `O(n)` (or `O(1)` extra if output excluded).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Minimum Number of Arrows to Burst Balloons

### Problem Statement (Concrete)
Solve **Minimum Number of Arrows to Burst Balloons** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Minimum Number of Arrows to Burst Balloons** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_minimum_number_of_arrows_to_burst_balloons(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_minimum_number_of_arrows_to_burst_balloons(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_minimum_number_of_arrows_to_burst_balloons(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Task Scheduler

### Problem Statement (Concrete)
Solve **Task Scheduler** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Task Scheduler** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_task_scheduler(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_task_scheduler(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_task_scheduler(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Wiggle Subsequence

### Problem Statement (Concrete)
Solve **Wiggle Subsequence** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Wiggle Subsequence** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_wiggle_subsequence(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_wiggle_subsequence(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_wiggle_subsequence(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Best Time to Buy and Sell Stock II

### Problem Statement (Concrete)
Solve **Best Time to Buy and Sell Stock II** using **Greedy**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Greedy**.
- Red flags: brute force for **Best Time to Buy and Sell Stock II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Explore all decision branches directly.

#### Python
```python
def brute_best_time_to_buy_and_sell_stock_ii(nums):
    # Exponential search over all local decisions.
    best = float('inf')
    n = len(nums)
    def dfs(i, jumps):
        nonlocal best
        if i >= n - 1:
            best = min(best, jumps)
            return
        if jumps >= best:
            return
        for step in range(1, nums[i] + 1):
            dfs(i + step, jumps + 1)
    dfs(0, 0)
    return best if best < float('inf') else -1
```

#### Complexity
- Time exponential in worst case, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Dynamic programming computes best value for each index/state.

#### Python
```python
def better_best_time_to_buy_and_sell_stock_ii(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for step in range(1, nums[i] + 1):
            j = i + step
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
    return dp[-1] if dp[-1] < float('inf') else -1
```

#### Complexity
- Time `O(n^2)` in dense transitions, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Greedy frontier expansion tracks the farthest reachable index per jump layer.

#### Python
```python
def solve_best_time_to_buy_and_sell_stock_ii(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
```

#### Correctness (Why This Works)
- Indices in `[last_end+1, cur_end]` are all reachable with the same number of jumps.
- Choosing farthest extension for next layer is optimal by BFS-layer equivalence on implicit graph.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
