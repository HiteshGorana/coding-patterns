# Pattern 25 Interview Playbook: Topological Sort

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Produces valid ordering of tasks in a directed acyclic graph (DAG) respecting dependencies.
- Core intuition: Nodes with in-degree `0` have no unmet prerequisites and can be processed now. Removing them may unlock new in-degree `0` nodes.
- Trigger cue 1: Prerequisites/dependency ordering.
- Quick self-check: Is graph directed and dependency-based?
- Target complexity: Time O(V + E), Space O(V + E)

---

## Q1. Course Schedule

### Problem Statement (Concrete)
Solve **Course Schedule** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Course Schedule** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_course_schedule(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_course_schedule(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_course_schedule(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Course Schedule II

### Problem Statement (Concrete)
Solve **Course Schedule II** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Course Schedule II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_course_schedule_ii(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_course_schedule_ii(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_course_schedule_ii(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Alien Dictionary

### Problem Statement (Concrete)
Solve **Alien Dictionary** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Alien Dictionary** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_alien_dictionary(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_alien_dictionary(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_alien_dictionary(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Parallel Courses

### Problem Statement (Concrete)
Solve **Parallel Courses** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Parallel Courses** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_parallel_courses(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_parallel_courses(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_parallel_courses(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Sequence Reconstruction

### Problem Statement (Concrete)
Solve **Sequence Reconstruction** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Sequence Reconstruction** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_sequence_reconstruction(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_sequence_reconstruction(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_sequence_reconstruction(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Find All Possible Recipes from Given Supplies

### Problem Statement (Concrete)
Solve **Find All Possible Recipes from Given Supplies** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Find All Possible Recipes from Given Supplies** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_find_all_possible_recipes_from_given_supplies(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_find_all_possible_recipes_from_given_supplies(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_find_all_possible_recipes_from_given_supplies(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Sort Items by Groups Respecting Dependencies

### Problem Statement (Concrete)
Solve **Sort Items by Groups Respecting Dependencies** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Sort Items by Groups Respecting Dependencies** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_sort_items_by_groups_respecting_dependencies(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_sort_items_by_groups_respecting_dependencies(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_sort_items_by_groups_respecting_dependencies(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Build a Matrix With Conditions

### Problem Statement (Concrete)
Solve **Build a Matrix With Conditions** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

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

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Build a Matrix With Conditions** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_build_a_matrix_with_conditions(grid):
    m, n = len(grid), len(grid[0])
    ans = [[10**9] * n for _ in range(m)]
    src = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
    for i in range(m):
        for j in range(n):
            for si, sj in src:
                ans[i][j] = min(ans[i][j], abs(i - si) + abs(j - sj))
    return ans
```

#### Complexity
- Time `O((mn)^2)` in dense-source case, Space `O(mn)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Run BFS from all sources simultaneously so each cell is finalized at first reach.

#### Python
```python
from collections import deque

def better_build_a_matrix_with_conditions(grid):
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

#### Complexity
- Time `O(mn)`, Space `O(mn)`.

### Approach 3: Optimal (Best)
#### Intuition
- Multi-source BFS explores increasing distance layers exactly once per cell.

#### Python
```python
from collections import deque

def better_build_a_matrix_with_conditions(grid):
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

#### Correctness (Why This Works)
- In unweighted grids, BFS layer number equals shortest path length.
- Seeding queue with all sources ensures nearest source claims each cell first.

#### Complexity
- Time `O(mn)`, Space `O(mn)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Loud and Rich

### Problem Statement (Concrete)
Solve **Loud and Rich** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- `numCourses`/`n`: int
- `prerequisites`/`edges`: list[list[int]] directed dependencies

### Output
- Feasibility boolean or a valid topological order, depending on variant.

### Constraints
- `1 <= n <= 2 * 10^5`
- Directed dependency graph; cycle means no valid full order.

### Example (Exact)
```text
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # one valid order
Explanation: Nodes with in-degree 0 can be taken immediately; cycles block completion.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Loud and Rich** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try all possible orderings and validate prerequisites.

#### Python
```python
from itertools import permutations

def brute_loud_and_rich(n, edges):
    prereq = [[False] * n for _ in range(n)]
    for u, v in edges:
        prereq[u][v] = True
    for order in permutations(range(n)):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[u] < pos[v] for u, v in edges):
            return list(order)
    return []
```

#### Complexity
- Time `O(n! * (n+m))`, infeasible beyond tiny `n`.

### Approach 2: Better (Intermediate)
#### Intuition
- Kahn's algorithm removes current zero in-degree nodes iteratively.

#### Python
```python
from collections import deque

def better_loud_and_rich(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Approach 3: Optimal (Best)
#### Intuition
- DFS with recursion-stack cycle detection + reverse finishing order yields topological order.

#### Python
```python
def solve_loud_and_rich(n, edges):
    g = [[] for _ in range(n)]
    state = [0] * n  # 0=unseen,1=visiting,2=done
    for u, v in edges:
        g[u].append(v)

    order = []
    cycle = False

    def dfs(u):
        nonlocal cycle
        state[u] = 1
        for v in g[u]:
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                cycle = True
        state[u] = 2
        order.append(u)

    for i in range(n):
        if state[i] == 0:
            dfs(i)
    if cycle:
        return []
    order.reverse()
    return order
```

#### Correctness (Why This Works)
- A directed cycle exists iff DFS finds a back-edge to a visiting node.
- In DAG case, reverse postorder is a valid topological ordering.

#### Complexity
- Time `O(n+m)`, Space `O(n+m)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Eventual Safe States

### Problem Statement (Concrete)
Solve **Eventual Safe States** using **Topological Sort**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Topological Sort**.
- Red flags: brute force for **Eventual Safe States** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Depth-first exploration tries all paths and tracks best found depth.

#### Python
```python
from collections import deque

def brute_eventual_safe_states(start, target):
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

def better_eventual_safe_states(start, target, dead=None):
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

def solve_eventual_safe_states(start, target, dead=None):
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
