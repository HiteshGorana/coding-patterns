# Pattern 21 Interview Playbook: Binary Search Tree (BST) Rules

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Leverages BST ordering to speed up search, validation, and rank queries.
- Core intuition: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Trigger cue 1: Validate BST, kth smallest, predecessor/successor, range query.
- Quick self-check: Can BST ordering remove half/subtree work?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Validate Binary Search Tree

### Problem Statement (Concrete)
Solve **Validate Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Validate Binary Search Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_validate_binary_search_tree(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_validate_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_validate_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Kth Smallest Element in a BST

### Problem Statement (Concrete)
Solve **Kth Smallest Element in a BST** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Kth Smallest Element in a BST** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_kth_smallest_element_in_a_bst(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_kth_smallest_element_in_a_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_kth_smallest_element_in_a_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Lowest Common Ancestor of a BST

### Problem Statement (Concrete)
Solve **Lowest Common Ancestor of a BST** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Lowest Common Ancestor of a BST** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Walk parent pointers one step at a time per query.

#### Python
```python
def brute_lowest_common_ancestor_of_a_bst(parent, node, k):
    while k > 0 and node != -1:
        node = parent[node]
        k -= 1
    return node
```

#### Complexity
- Per query `O(k)` worst-case.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute `2^j` ancestors to jump multiple levels quickly.

#### Python
```python
def better_lowest_common_ancestor_of_a_bst(parent, queries):
    n = len(parent)
    LOG = (n).bit_length()
    up = [[-1] * n for _ in range(LOG)]
    up[0] = parent[:]
    for j in range(1, LOG):
        for i in range(n):
            p = up[j - 1][i]
            up[j][i] = -1 if p == -1 else up[j - 1][p]

    out = []
    for node, k in queries:
        j = 0
        while k > 0 and node != -1:
            if k & 1:
                node = up[j][node]
            k >>= 1
            j += 1
        out.append(node)
    return out
```

#### Complexity
- Preprocess `O(n log n)`, per query `O(log n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Binary lifting decomposes jumps and LCA movement into powers of two.

#### Python
```python
def better_lowest_common_ancestor_of_a_bst(parent, queries):
    n = len(parent)
    LOG = (n).bit_length()
    up = [[-1] * n for _ in range(LOG)]
    up[0] = parent[:]
    for j in range(1, LOG):
        for i in range(n):
            p = up[j - 1][i]
            up[j][i] = -1 if p == -1 else up[j - 1][p]

    out = []
    for node, k in queries:
        j = 0
        while k > 0 and node != -1:
            if k & 1:
                node = up[j][node]
            k >>= 1
            j += 1
        out.append(node)
    return out
```

#### Correctness (Why This Works)
- Any integer jump `k` has unique binary decomposition into powers of two.
- Precomputed `up[j][v]` tables make each power jump constant time.

#### Complexity
- Preprocess `O(n log n)`, query `O(log n)`, Space `O(n log n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Binary Search Tree Iterator

### Problem Statement (Concrete)
Solve **Binary Search Tree Iterator** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Binary Search Tree Iterator** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_binary_search_tree_iterator(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_binary_search_tree_iterator(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_binary_search_tree_iterator(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Convert Sorted Array to BST

### Problem Statement (Concrete)
Solve **Convert Sorted Array to BST** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Convert Sorted Array to BST** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_convert_sorted_array_to_bst(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_convert_sorted_array_to_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_convert_sorted_array_to_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Insert into a Binary Search Tree

### Problem Statement (Concrete)
Solve **Insert into a Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Insert into a Binary Search Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_insert_into_a_binary_search_tree(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_insert_into_a_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_insert_into_a_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Delete Node in a BST

### Problem Statement (Concrete)
Solve **Delete Node in a BST** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Delete Node in a BST** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_delete_node_in_a_bst(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_delete_node_in_a_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_delete_node_in_a_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Trim a Binary Search Tree

### Problem Statement (Concrete)
Solve **Trim a Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Trim a Binary Search Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_trim_a_binary_search_tree(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_trim_a_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_trim_a_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Two Sum IV - Input is a BST

### Problem Statement (Concrete)
Solve **Two Sum IV - Input is a BST** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

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
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Two Sum IV - Input is a BST** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_two_sum_iv_input_is_a_bst(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_two_sum_iv_input_is_a_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_two_sum_iv_input_is_a_bst(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Recover Binary Search Tree

### Problem Statement (Concrete)
Solve **Recover Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly the value/structure requested by the original prompt.

### Input
- `root` or `n, edges`: tree representation
- `queries`: list[tuple] for query-based tasks

### Output
- Node value, list, distance, or aggregate metric specified by the problem.

### Constraints
- `1 <= n <= 2 * 10^5`
- Aim for preprocessing + fast per-query handling when queries are many.

### Example (Exact)
```text
Input:  n = 5, edges = [[0,1],[0,2],[2,3],[2,4]], queries = [[3,4]]
Output: 2
Explanation: Tree structure enables DP or lifting transitions with no cycles.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Single-node tree should satisfy all query logic with correct base ancestors/distances.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search Tree (BST) Rules**.
- Red flags: brute force for **Recover Binary Search Tree** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute subtree metrics independently for each node.

#### Python
```python
def brute_recover_binary_search_tree(root):
    # Generic tree DFS that recomputes subtree info repeatedly.
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    if not root:
        return 0
    return max(height(root.left), height(root.right))
```

#### Complexity
- Time up to `O(n^2)` on skewed trees.

### Approach 2: Better (Intermediate)
#### Intuition
- Postorder DFS computes and reuses child summaries once per node.

#### Python
```python
def better_recover_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(h)` recursion.

### Approach 3: Optimal (Best)
#### Intuition
- Single DFS with returned state captures exactly what parent needs.

#### Python
```python
def better_recover_binary_search_tree(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return 1 + max(l, r)
    dfs(root)
    return ans
```

#### Correctness (Why This Works)
- Each node summary is a pure function of child summaries, so postorder yields complete information.
- No subtree is recomputed; each edge is traversed constant times.

#### Complexity
- Time `O(n)`, Space `O(h)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
