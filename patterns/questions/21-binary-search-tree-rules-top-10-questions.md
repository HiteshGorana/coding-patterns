# Pattern 21 Interview Playbook: Binary Search Tree (BST) Rules

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Leverages BST ordering to speed up search, validation, and rank queries.
- Core intuition: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Trigger cue 1: Validate BST, kth smallest, predecessor/successor, range query.
- Quick self-check: Can BST ordering remove half/subtree work?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Validate Binary Search Tree

### Problem Statement (Specific)
Solve **Validate Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root`: binary tree

### Output
- Boolean validity of BST ordering.

### Constraints (Typical)
- 1 <= n <= 1e5

### Example (Exact)
```text
Input:  root = [2,1,3]
Output: true
Explanation: Use range bounds, not local parent-child checks only.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Validate Binary Search Tree directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_validate_binary_search_tree(data):
    """Brute-force baseline for: Validate Binary Search Tree."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Validate Binary Search Tree to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_validate_binary_search_tree(data):
    """Intermediate optimized approach for: Validate Binary Search Tree."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Validate Binary Search Tree: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_validate_binary_search_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q2. Kth Smallest Element in a BST

### Problem Statement (Specific)
Solve **Kth Smallest Element in a BST** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root`: BST
- `k`: int

### Output
- k-th smallest value.

### Constraints (Typical)
- 1 <= k <= n <= 1e5

### Example (Exact)
```text
Input:  root = [3,1,4,null,2], k = 1
Output: 1
Explanation: Inorder traversal of BST is sorted.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Kth Smallest Element in a BST directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_kth_smallest_element_in_a_bst(data):
    """Brute-force baseline for: Kth Smallest Element in a BST."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Kth Smallest Element in a BST to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_kth_smallest_element_in_a_bst(data):
    """Intermediate optimized approach for: Kth Smallest Element in a BST."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Kth Smallest Element in a BST: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_kth_smallest_element_in_a_bst(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q3. Lowest Common Ancestor of a BST

### Problem Statement (Specific)
Solve **Lowest Common Ancestor of a BST** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 2
Output: 4
Explanation: For Lowest Common Ancestor of a BST, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Lowest Common Ancestor of a BST directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_lowest_common_ancestor_of_a_bst(data):
    """Brute-force baseline for: Lowest Common Ancestor of a BST."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Lowest Common Ancestor of a BST to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_lowest_common_ancestor_of_a_bst(data):
    """Intermediate optimized approach for: Lowest Common Ancestor of a BST."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Lowest Common Ancestor of a BST: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_lowest_common_ancestor_of_a_bst(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q4. Binary Search Tree Iterator

### Problem Statement (Specific)
Solve **Binary Search Tree Iterator** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 3
Output: 4
Explanation: For Binary Search Tree Iterator, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Binary Search Tree Iterator directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_binary_search_tree_iterator(data):
    """Brute-force baseline for: Binary Search Tree Iterator."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Binary Search Tree Iterator to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_binary_search_tree_iterator(data):
    """Intermediate optimized approach for: Binary Search Tree Iterator."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Binary Search Tree Iterator: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_binary_search_tree_iterator(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q5. Convert Sorted Array to BST

### Problem Statement (Specific)
Solve **Convert Sorted Array to BST** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 4
Output: 4
Explanation: For Convert Sorted Array to BST, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Convert Sorted Array to BST directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_convert_sorted_array_to_bst(data):
    """Brute-force baseline for: Convert Sorted Array to BST."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Convert Sorted Array to BST to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_convert_sorted_array_to_bst(data):
    """Intermediate optimized approach for: Convert Sorted Array to BST."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Convert Sorted Array to BST: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_convert_sorted_array_to_bst(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q6. Insert into a Binary Search Tree

### Problem Statement (Specific)
Solve **Insert into a Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 2
Output: 4
Explanation: For Insert into a Binary Search Tree, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Insert into a Binary Search Tree directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_insert_into_a_binary_search_tree(data):
    """Brute-force baseline for: Insert into a Binary Search Tree."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Insert into a Binary Search Tree to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_insert_into_a_binary_search_tree(data):
    """Intermediate optimized approach for: Insert into a Binary Search Tree."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Insert into a Binary Search Tree: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_insert_into_a_binary_search_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q7. Delete Node in a BST

### Problem Statement (Specific)
Solve **Delete Node in a BST** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 3
Output: 4
Explanation: For Delete Node in a BST, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Delete Node in a BST directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_delete_node_in_a_bst(data):
    """Brute-force baseline for: Delete Node in a BST."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Delete Node in a BST to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_delete_node_in_a_bst(data):
    """Intermediate optimized approach for: Delete Node in a BST."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Delete Node in a BST: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_delete_node_in_a_bst(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q8. Trim a Binary Search Tree

### Problem Statement (Specific)
Solve **Trim a Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 4
Output: 4
Explanation: For Trim a Binary Search Tree, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Trim a Binary Search Tree directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_trim_a_binary_search_tree(data):
    """Brute-force baseline for: Trim a Binary Search Tree."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Trim a Binary Search Tree to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_trim_a_binary_search_tree(data):
    """Intermediate optimized approach for: Trim a Binary Search Tree."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Trim a Binary Search Tree: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_trim_a_binary_search_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q9. Two Sum IV - Input is a BST

### Problem Statement (Specific)
Solve **Two Sum IV - Input is a BST** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `target`: int

### Output
- Two indices `[i, j]` such that `nums[i] + nums[j] == target`.

### Constraints (Typical)
- 2 <= n <= 1e5
- -1e9 <= nums[i], target <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15], target = 9
Output: [0, 1]
Explanation: Check complement before insert to avoid reusing same index.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Two Sum IV - Input is a BST directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_two_sum_iv_input_is_a_bst(data):
    """Brute-force baseline for: Two Sum IV - Input is a BST."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Two Sum IV - Input is a BST to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_two_sum_iv_input_is_a_bst(data):
    """Intermediate optimized approach for: Two Sum IV - Input is a BST."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Two Sum IV - Input is a BST: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_two_sum_iv_input_is_a_bst(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q10. Recover Binary Search Tree

### Problem Statement (Specific)
Solve **Recover Binary Search Tree** using **Binary Search Tree (BST) Rules**. Return exactly what the problem asks and justify complexity.

### Input
- `root` or `(n, edges)`

### Output
- Tree metric/list/boolean per prompt.

### Constraints (Typical)
- 1 <= n <= 2e5

### Example (Exact)
```text
Input:  tree = [5,3,8,2,4,7,9], k = 3
Output: 4
Explanation: For Recover Binary Search Tree, combine subtree/ancestor state efficiently.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Recover Binary Search Tree directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_recover_binary_search_tree(data):
    """Brute-force baseline for: Recover Binary Search Tree."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Recover Binary Search Tree to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_recover_binary_search_tree(data):
    """Intermediate optimized approach for: Recover Binary Search Tree."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search Tree (BST) Rules invariant to Recover Binary Search Tree: Inorder traversal of valid BST yields sorted sequence. Use value bounds during DFS to validate global constraints, not just local child checks.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_recover_binary_search_tree(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def is_valid_bst(root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float("-inf"), float("inf"))
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---
