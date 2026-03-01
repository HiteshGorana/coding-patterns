# Pattern 15 Interview Playbook: Linked List Reversal / In-place Operations

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Efficiently rewires linked list pointers without extra arrays/stacks.
- Core intuition: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Trigger cue 1: Reverse list/all/part/k-group in O(1) extra space.
- Quick self-check: Can I do this with `prev, curr, next` safely?
- Target complexity: Time O(n), Space O(1)

---

## Q1. Reverse Linked List

### Problem Statement (Specific)
Solve **Reverse Linked List** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list head

### Output
- Head of reversed linked list (full or subrange variant).

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: Three-pointer rewiring preserves remaining list access.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reverse Linked List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reverse_linked_list(data):
    """Brute-force baseline for: Reverse Linked List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reverse Linked List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reverse_linked_list(data):
    """Intermediate optimized approach for: Reverse Linked List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Reverse Linked List: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reverse_linked_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q2. Reverse Linked List II

### Problem Statement (Specific)
Solve **Reverse Linked List II** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list head

### Output
- Head of reversed linked list (full or subrange variant).

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: Three-pointer rewiring preserves remaining list access.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reverse Linked List II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reverse_linked_list_ii(data):
    """Brute-force baseline for: Reverse Linked List II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reverse Linked List II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reverse_linked_list_ii(data):
    """Intermediate optimized approach for: Reverse Linked List II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Reverse Linked List II: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reverse_linked_list_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q3. Reverse Nodes in k-Group

### Problem Statement (Specific)
Solve **Reverse Nodes in k-Group** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Reverse Nodes in k-Group, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reverse Nodes in k-Group directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reverse_nodes_in_k_group(data):
    """Brute-force baseline for: Reverse Nodes in k-Group."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reverse Nodes in k-Group to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reverse_nodes_in_k_group(data):
    """Intermediate optimized approach for: Reverse Nodes in k-Group."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Reverse Nodes in k-Group: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reverse_nodes_in_k_group(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q4. Swap Nodes in Pairs

### Problem Statement (Specific)
Solve **Swap Nodes in Pairs** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Swap Nodes in Pairs, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Swap Nodes in Pairs directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_swap_nodes_in_pairs(data):
    """Brute-force baseline for: Swap Nodes in Pairs."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Swap Nodes in Pairs to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_swap_nodes_in_pairs(data):
    """Intermediate optimized approach for: Swap Nodes in Pairs."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Swap Nodes in Pairs: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_swap_nodes_in_pairs(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q5. Reorder List

### Problem Statement (Specific)
Solve **Reorder List** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Reorder List, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reorder List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reorder_list(data):
    """Brute-force baseline for: Reorder List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reorder List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reorder_list(data):
    """Intermediate optimized approach for: Reorder List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Reorder List: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reorder_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q6. Rotate List

### Problem Statement (Specific)
Solve **Rotate List** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Rotate List, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Rotate List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_rotate_list(data):
    """Brute-force baseline for: Rotate List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Rotate List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_rotate_list(data):
    """Intermediate optimized approach for: Rotate List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Rotate List: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_rotate_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q7. Palindrome Linked List

### Problem Statement (Specific)
Solve **Palindrome Linked List** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Palindrome Linked List, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Palindrome Linked List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_palindrome_linked_list(data):
    """Brute-force baseline for: Palindrome Linked List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Palindrome Linked List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_palindrome_linked_list(data):
    """Intermediate optimized approach for: Palindrome Linked List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Palindrome Linked List: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_palindrome_linked_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q8. Reverse Even Length Groups of Nodes in Linked List

### Problem Statement (Specific)
Solve **Reverse Even Length Groups of Nodes in Linked List** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Reverse Even Length Groups of Nodes in Linked List, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reverse Even Length Groups of Nodes in Linked List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reverse_even_length_groups_of_nodes_in_linked_list(data):
    """Brute-force baseline for: Reverse Even Length Groups of Nodes in Linked List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reverse Even Length Groups of Nodes in Linked List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reverse_even_length_groups_of_nodes_in_linked_list(data):
    """Intermediate optimized approach for: Reverse Even Length Groups of Nodes in Linked List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Reverse Even Length Groups of Nodes in Linked List: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reverse_even_length_groups_of_nodes_in_linked_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q9. Add Two Numbers II

### Problem Statement (Specific)
Solve **Add Two Numbers II** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list
- optional parameters from prompt

### Output
- List head / boolean / index result.

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5], k = 2
Output: [5,4,3,2,1]
Explanation: For Add Two Numbers II, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Add Two Numbers II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_add_two_numbers_ii(data):
    """Brute-force baseline for: Add Two Numbers II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Add Two Numbers II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_add_two_numbers_ii(data):
    """Intermediate optimized approach for: Add Two Numbers II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Add Two Numbers II: Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_add_two_numbers_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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

## Q10. Reverse Linked List in k-Group (Variant)

### Problem Statement (Specific)
Solve **Reverse Linked List in k-Group (Variant)** using **Linked List Reversal / In-place Operations**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list head

### Output
- Head of reversed linked list (full or subrange variant).

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: Three-pointer rewiring preserves remaining list access.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reverse Linked List in k-Group (Variant) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reverse_linked_list_in_k_group_variant(data):
    """Brute-force baseline for: Reverse Linked List in k-Group (Variant)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reverse Linked List in k-Group (Variant) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reverse_linked_list_in_k_group_variant(data):
    """Intermediate optimized approach for: Reverse Linked List in k-Group (Variant)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Linked List Reversal / In-place Operations invariant to Reverse Linked List in k-Group (Variant): Track three pointers per step: - `prev` - `curr` - `next_node` Reverse one pointer direction at a time while preserving access to remaining list.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reverse_linked_list_in_k_group_variant(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def reverse_list(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
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
