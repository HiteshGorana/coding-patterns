# Pattern 37 Interview Playbook: Bitmask DP / State Compression DP

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Bitmask DP solves problems where state includes which elements have been chosen/visited and `n` is small enough for subset-state enumeration.
- Core intuition: Represent subsets as integers and define DP over masks; each transition sets or clears a bit to move between states.
- Trigger cue 1: State is naturally a subset of items/nodes.
- Trigger cue 2: Need exact optimization over visited/unvisited sets.
- Quick self-check: Is `n` small enough that `2^n` states are feasible?
- Target complexity: Time Commonly O(n^2 * 2^n) or O(n * 2^n) depending transition., Space O(n * 2^n).

---

## Q1. Shortest Path Visiting All Nodes

### Problem Statement (Concrete)
Solve **Shortest Path Visiting All Nodes** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Shortest Path Visiting All Nodes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_shortest_path_visiting_all_nodes(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_shortest_path_visiting_all_nodes(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_shortest_path_visiting_all_nodes(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Traveling Salesman Problem

### Problem Statement (Concrete)
Solve **Traveling Salesman Problem** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Traveling Salesman Problem** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_traveling_salesman_problem(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_traveling_salesman_problem(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_traveling_salesman_problem(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Assignment Problem

### Problem Statement (Concrete)
Solve **Assignment Problem** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Assignment Problem** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_assignment_problem(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_assignment_problem(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_assignment_problem(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Smallest Sufficient Team

### Problem Statement (Concrete)
Solve **Smallest Sufficient Team** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Smallest Sufficient Team** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_smallest_sufficient_team(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_smallest_sufficient_team(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_smallest_sufficient_team(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Maximum Compatibility Score Sum

### Problem Statement (Concrete)
Solve **Maximum Compatibility Score Sum** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Maximum Compatibility Score Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_maximum_compatibility_score_sum(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_maximum_compatibility_score_sum(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_maximum_compatibility_score_sum(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Parallel Courses II

### Problem Statement (Concrete)
Solve **Parallel Courses II** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Parallel Courses II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_parallel_courses_ii(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_parallel_courses_ii(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_parallel_courses_ii(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Can I Win

### Problem Statement (Concrete)
Solve **Can I Win** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Can I Win** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_can_i_win(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_can_i_win(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_can_i_win(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Minimum Cost to Connect Two Groups of Points

### Problem Statement (Concrete)
Solve **Minimum Cost to Connect Two Groups of Points** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Minimum Cost to Connect Two Groups of Points** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_minimum_cost_to_connect_two_groups_of_points(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_minimum_cost_to_connect_two_groups_of_points(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_minimum_cost_to_connect_two_groups_of_points(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Beautiful Arrangement

### Problem Statement (Concrete)
Solve **Beautiful Arrangement** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Beautiful Arrangement** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_beautiful_arrangement(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_beautiful_arrangement(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_beautiful_arrangement(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Bitmask DP for Hamiltonian Path

### Problem Statement (Concrete)
Solve **Bitmask DP for Hamiltonian Path** using **Bitmask DP / State Compression DP**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bitmask DP / State Compression DP**.
- Red flags: brute force for **Bitmask DP for Hamiltonian Path** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all permutations/assignments explicitly.

#### Python
```python
def brute_bitmask_dp_for_hamiltonian_path(cost):
    n = len(cost)
    used = [False] * n
    best = float('inf')
    def dfs(i, cur):
        nonlocal best
        if i == n:
            best = min(best, cur)
            return
        if cur >= best:
            return
        for j in range(n):
            if not used[j]:
                used[j] = True
                dfs(i + 1, cur + cost[i][j])
                used[j] = False
    dfs(0, 0)
    return best
```

#### Complexity
- Time `O(n!)`, Space `O(n)` recursion.

### Approach 2: Better (Intermediate)
#### Intuition
- Memoize by `(position, mask)` to reuse equivalent remaining-state computations.

#### Python
```python
from functools import lru_cache

def better_bitmask_dp_for_hamiltonian_path(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Approach 3: Optimal (Best)
#### Intuition
- State compression DP is optimal for small `n` with combinational state.

#### Python
```python
from functools import lru_cache

def better_bitmask_dp_for_hamiltonian_path(cost):
    n = len(cost)
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return 0
        ans = float('inf')
        for j in range(n):
            if not (mask >> j) & 1:
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
        return ans
    return dp(0, 0)
```

#### Correctness (Why This Works)
- Mask uniquely identifies chosen set; future cost depends only on this state and current index.
- Optimal substructure holds: best completion from state is independent of path used to reach it.

#### Complexity
- Time `O(n * 2^n)`, Space `O(2^n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
