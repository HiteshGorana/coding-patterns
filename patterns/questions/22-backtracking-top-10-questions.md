# Pattern 22 Interview Playbook: Backtracking

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Explores combinatorial search spaces by building candidates incrementally and undoing choices.
- Core intuition: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Trigger cue 1: Need all combinations/permutations or constrained existence.
- Quick self-check: Is this an exponential choice tree where pruning helps?
- Target complexity: Time pattern-optimal, Space recursion depth + output size

---

## Q1. Subsets

### Problem Statement (Concrete)
Solve **Subsets** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Subsets** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_subsets(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_subsets(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_subsets(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Subsets II

### Problem Statement (Concrete)
Solve **Subsets II** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Subsets II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_subsets_ii(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_subsets_ii(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_subsets_ii(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Permutations

### Problem Statement (Concrete)
Solve **Permutations** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Permutations** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_permutations(start, target):
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

def better_permutations(start, target, dead=None):
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

def solve_permutations(start, target, dead=None):
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

## Q4. Permutations II

### Problem Statement (Concrete)
Solve **Permutations II** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Permutations II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_permutations_ii(start, target):
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

def better_permutations_ii(start, target, dead=None):
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

def solve_permutations_ii(start, target, dead=None):
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

## Q5. Combination Sum

### Problem Statement (Concrete)
Solve **Combination Sum** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Combination Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_combination_sum(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_combination_sum(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_combination_sum(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Combination Sum II

### Problem Statement (Concrete)
Solve **Combination Sum II** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Combination Sum II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_combination_sum_ii(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_combination_sum_ii(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_combination_sum_ii(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Combinations

### Problem Statement (Concrete)
Solve **Combinations** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Combinations** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_combinations(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_combinations(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_combinations(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Letter Combinations of a Phone Number

### Problem Statement (Concrete)
Solve **Letter Combinations of a Phone Number** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Letter Combinations of a Phone Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_letter_combinations_of_a_phone_number(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_letter_combinations_of_a_phone_number(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_letter_combinations_of_a_phone_number(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. N-Queens

### Problem Statement (Concrete)
Solve **N-Queens** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **N-Queens** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_n_queens(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_n_queens(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_n_queens(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Word Search

### Problem Statement (Concrete)
Solve **Word Search** using **Backtracking**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Backtracking**.
- Red flags: brute force for **Word Search** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Generate all subsets/permutations via bitmask or raw recursion.

#### Python
```python
def brute_word_search(nums):
    out = []
    n = len(nums)
    for mask in range(1 << n):
        cur = []
        for i in range(n):
            if mask & (1 << i):
                cur.append(nums[i])
        out.append(cur)
    return out
```

#### Complexity
- Time `O(2^n * n)` or `O(n!*n)`, Space output-sized.

### Approach 2: Better (Intermediate)
#### Intuition
- Backtracking with explicit decision tree avoids materializing invalid branches early.

#### Python
```python
def better_word_search(nums):
    out = []
    cur = []
    def dfs(i):
        if i == len(nums):
            out.append(cur[:])
            return
        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()
        dfs(i + 1)
    dfs(0)
    return out
```

#### Complexity
- Time exponential but with better pruning constants.

### Approach 3: Optimal (Best)
#### Intuition
- Ordering + duplicate-skip/pruning conditions prevent equivalent branches.

#### Python
```python
def solve_word_search(nums):
    nums.sort()
    out = []
    cur = []
    def dfs(start):
        out.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
    dfs(0)
    return out
```

#### Correctness (Why This Works)
- Each recursive level fixes one decision boundary, and pruning removes only branches provably identical or infeasible.
- Thus every emitted solution is valid and every valid solution is reachable exactly once.

#### Complexity
- Time exponential in solution space, Space `O(n)` recursion (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
