# Pattern 14 Interview Playbook: Fast & Slow Pointers

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Detects cycles, finds middle points, and identifies phase relationships in linked structures.
- Core intuition: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Trigger cue 1: Linked list cycle, middle node, repeated-state loops.
- Quick self-check: Can two-speed traversal detect cycle/phase alignment?
- Target complexity: Time O(n), Space O(1)

---

## Q1. Linked List Cycle

### Problem Statement (Specific)
Solve **Linked List Cycle** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list head

### Output
- Boolean (cycle exists) or node where cycle begins (variant).

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [3,2,0,-4], pos = 1
Output: true
Explanation: Fast/slow pointers meet iff cycle exists.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Linked List Cycle directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_linked_list_cycle(data):
    """Brute-force baseline for: Linked List Cycle."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Linked List Cycle to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_linked_list_cycle(data):
    """Intermediate optimized approach for: Linked List Cycle."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Linked List Cycle: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_linked_list_cycle(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q2. Linked List Cycle II

### Problem Statement (Specific)
Solve **Linked List Cycle II** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

### Input
- `head`: linked list head

### Output
- Boolean (cycle exists) or node where cycle begins (variant).

### Constraints (Typical)
- 0 <= n <= 1e5

### Example (Exact)
```text
Input:  head = [3,2,0,-4], pos = 1
Output: true
Explanation: Fast/slow pointers meet iff cycle exists.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Linked List Cycle II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_linked_list_cycle_ii(data):
    """Brute-force baseline for: Linked List Cycle II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Linked List Cycle II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_linked_list_cycle_ii(data):
    """Intermediate optimized approach for: Linked List Cycle II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Linked List Cycle II: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_linked_list_cycle_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q3. Middle of the Linked List

### Problem Statement (Specific)
Solve **Middle of the Linked List** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Middle of the Linked List, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Middle of the Linked List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_middle_of_the_linked_list(data):
    """Brute-force baseline for: Middle of the Linked List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Middle of the Linked List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_middle_of_the_linked_list(data):
    """Intermediate optimized approach for: Middle of the Linked List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Middle of the Linked List: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_middle_of_the_linked_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q4. Happy Number

### Problem Statement (Specific)
Solve **Happy Number** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Happy Number, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Happy Number directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_happy_number(data):
    """Brute-force baseline for: Happy Number."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Happy Number to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_happy_number(data):
    """Intermediate optimized approach for: Happy Number."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Happy Number: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_happy_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q5. Find the Duplicate Number

### Problem Statement (Specific)
Solve **Find the Duplicate Number** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find the Duplicate Number, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find the Duplicate Number directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_the_duplicate_number(data):
    """Brute-force baseline for: Find the Duplicate Number."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find the Duplicate Number to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_the_duplicate_number(data):
    """Intermediate optimized approach for: Find the Duplicate Number."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Find the Duplicate Number: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_the_duplicate_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q6. Palindrome Linked List

### Problem Statement (Specific)
Solve **Palindrome Linked List** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
- Apply Fast & Slow Pointers invariant to Palindrome Linked List: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_palindrome_linked_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q7. Reorder List

### Problem Statement (Specific)
Solve **Reorder List** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
- Apply Fast & Slow Pointers invariant to Reorder List: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_reorder_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q8. Circular Array Loop

### Problem Statement (Specific)
Solve **Circular Array Loop** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Circular Array Loop, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Circular Array Loop directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_circular_array_loop(data):
    """Brute-force baseline for: Circular Array Loop."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Circular Array Loop to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_circular_array_loop(data):
    """Intermediate optimized approach for: Circular Array Loop."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Circular Array Loop: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_circular_array_loop(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q9. Find Beginning of Loop in Linked List

### Problem Statement (Specific)
Solve **Find Beginning of Loop in Linked List** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find Beginning of Loop in Linked List, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find Beginning of Loop in Linked List directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_beginning_of_loop_in_linked_list(data):
    """Brute-force baseline for: Find Beginning of Loop in Linked List."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find Beginning of Loop in Linked List to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_beginning_of_loop_in_linked_list(data):
    """Intermediate optimized approach for: Find Beginning of Loop in Linked List."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Find Beginning of Loop in Linked List: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_beginning_of_loop_in_linked_list(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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

## Q10. Split Linked List in Parts

### Problem Statement (Specific)
Solve **Split Linked List in Parts** using **Fast & Slow Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Split Linked List in Parts, maintain pointer safety while transforming.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Split Linked List in Parts directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_split_linked_list_in_parts(data):
    """Brute-force baseline for: Split Linked List in Parts."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Split Linked List in Parts to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_split_linked_list_in_parts(data):
    """Intermediate optimized approach for: Split Linked List in Parts."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Fast & Slow Pointers invariant to Split Linked List in Parts: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Complexity target: Time O(n), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_split_linked_list_in_parts(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
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
