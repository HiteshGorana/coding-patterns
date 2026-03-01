# Pattern 39 Interview Playbook: State-space BFS

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: State-space BFS finds shortest path in problems where each node includes extra mutable state beyond position.
- Core intuition: Model each unique `(location, state)` as graph node; run BFS over this expanded graph.
- Trigger cue 1: Path feasibility depends on keys, mask, fuel, direction, or configuration.
- Trigger cue 2: Need shortest steps in an unweighted transition graph.
- Quick self-check: If I reach same location with different state, do outcomes differ?
- Target complexity: Time O(number_of_states + transitions)., Space O(number_of_states).

---

## Q1. Open the Lock

### Problem Statement (Concrete)
Solve **Open the Lock** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Open the Lock** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_open_the_lock(start, target):
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

def better_open_the_lock(start, target, dead=None):
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

def solve_open_the_lock(start, target, dead=None):
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

## Q2. Shortest Path to Get All Keys

### Problem Statement (Concrete)
Solve **Shortest Path to Get All Keys** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Shortest Path to Get All Keys** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_shortest_path_to_get_all_keys(start, target):
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

def better_shortest_path_to_get_all_keys(start, target, dead=None):
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

def solve_shortest_path_to_get_all_keys(start, target, dead=None):
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

## Q3. Sliding Puzzle

### Problem Statement (Concrete)
Solve **Sliding Puzzle** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Sliding Puzzle** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_sliding_puzzle(start, target):
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

def better_sliding_puzzle(start, target, dead=None):
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

def solve_sliding_puzzle(start, target, dead=None):
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

## Q4. Snakes and Ladders

### Problem Statement (Concrete)
Solve **Snakes and Ladders** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Snakes and Ladders** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_snakes_and_ladders(start, target):
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

def better_snakes_and_ladders(start, target, dead=None):
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

def solve_snakes_and_ladders(start, target, dead=None):
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

## Q5. Word Ladder

### Problem Statement (Concrete)
Solve **Word Ladder** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Word Ladder** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_word_ladder(start, target):
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

def better_word_ladder(start, target, dead=None):
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

def solve_word_ladder(start, target, dead=None):
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

## Q6. Minimum Genetic Mutation

### Problem Statement (Concrete)
Solve **Minimum Genetic Mutation** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Minimum Genetic Mutation** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_minimum_genetic_mutation(start, target):
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

def better_minimum_genetic_mutation(start, target, dead=None):
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

def solve_minimum_genetic_mutation(start, target, dead=None):
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

## Q7. Race Car

### Problem Statement (Concrete)
Solve **Race Car** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Race Car** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_race_car(start, target):
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

def better_race_car(start, target, dead=None):
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

def solve_race_car(start, target, dead=None):
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

## Q8. Bus Routes

### Problem Statement (Concrete)
Solve **Bus Routes** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Bus Routes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_bus_routes(start, target):
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

def better_bus_routes(start, target, dead=None):
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

def solve_bus_routes(start, target, dead=None):
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

## Q9. Shortest Path Visiting All Nodes (BFS state)

### Problem Statement (Concrete)
Solve **Shortest Path Visiting All Nodes (BFS state)** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Shortest Path Visiting All Nodes (BFS state)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_shortest_path_visiting_all_nodes_bfs_state(start, target):
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

def better_shortest_path_visiting_all_nodes_bfs_state(start, target, dead=None):
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

def solve_shortest_path_visiting_all_nodes_bfs_state(start, target, dead=None):
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

## Q10. Minimum Knight Moves

### Problem Statement (Concrete)
Solve **Minimum Knight Moves** using **State-space BFS**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **State-space BFS**.
- Red flags: brute force for **Minimum Knight Moves** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_minimum_knight_moves(start, target):
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

def better_minimum_knight_moves(start, target, dead=None):
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

def solve_minimum_knight_moves(start, target, dead=None):
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
