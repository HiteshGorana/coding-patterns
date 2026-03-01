# Pattern 22 Interview Playbook: Backtracking

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Explores combinatorial search spaces by building candidates incrementally and undoing choices.
- Core intuition: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Trigger cue 1: Need all combinations/permutations or constrained existence.
- Quick self-check: Is this an exponential choice tree where pruning helps?
- Target complexity: Time pattern-optimal, Space recursion depth + output size

---

## Q1. Subsets

### Problem Statement (Specific)
Solve **Subsets** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- All subsets of `nums`.

### Constraints (Typical)
- 1 <= len(nums) <= 20

### Example (Exact)
```text
Input:  nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
Explanation: Backtracking include/exclude decisions produce power set.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Subsets directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_subsets(data):
    """Brute-force baseline for: Subsets."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Subsets to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_subsets(data):
    """Intermediate optimized approach for: Subsets."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Subsets: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_subsets(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q2. Subsets II

### Problem Statement (Specific)
Solve **Subsets II** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- All subsets of `nums`.

### Constraints (Typical)
- 1 <= len(nums) <= 20

### Example (Exact)
```text
Input:  nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
Explanation: Backtracking include/exclude decisions produce power set.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Subsets II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_subsets_ii(data):
    """Brute-force baseline for: Subsets II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Subsets II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_subsets_ii(data):
    """Intermediate optimized approach for: Subsets II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Subsets II: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_subsets_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q3. Permutations

### Problem Statement (Specific)
Solve **Permutations** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- All permutations of `nums`.

### Constraints (Typical)
- 1 <= len(nums) <= 8

### Example (Exact)
```text
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Explanation: Backtracking with used-set enumerates all orderings.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Permutations directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_permutations(data):
    """Brute-force baseline for: Permutations."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Permutations to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_permutations(data):
    """Intermediate optimized approach for: Permutations."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Permutations: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_permutations(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q4. Permutations II

### Problem Statement (Specific)
Solve **Permutations II** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- All permutations of `nums`.

### Constraints (Typical)
- 1 <= len(nums) <= 8

### Example (Exact)
```text
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Explanation: Backtracking with used-set enumerates all orderings.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Permutations II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_permutations_ii(data):
    """Brute-force baseline for: Permutations II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Permutations II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_permutations_ii(data):
    """Intermediate optimized approach for: Permutations II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Permutations II: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_permutations_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q5. Combination Sum

### Problem Statement (Specific)
Solve **Combination Sum** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 10
Output: 9
Explanation: For Combination Sum, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Combination Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_combination_sum(data):
    """Brute-force baseline for: Combination Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Combination Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_combination_sum(data):
    """Intermediate optimized approach for: Combination Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Combination Sum: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_combination_sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q6. Combination Sum II

### Problem Statement (Specific)
Solve **Combination Sum II** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 11
Output: 9
Explanation: For Combination Sum II, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Combination Sum II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_combination_sum_ii(data):
    """Brute-force baseline for: Combination Sum II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Combination Sum II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_combination_sum_ii(data):
    """Intermediate optimized approach for: Combination Sum II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Combination Sum II: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_combination_sum_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q7. Combinations

### Problem Statement (Specific)
Solve **Combinations** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 12
Output: 9
Explanation: For Combinations, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Combinations directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_combinations(data):
    """Brute-force baseline for: Combinations."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Combinations to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_combinations(data):
    """Intermediate optimized approach for: Combinations."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Combinations: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_combinations(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q8. Letter Combinations of a Phone Number

### Problem Statement (Specific)
Solve **Letter Combinations of a Phone Number** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 9
Output: 9
Explanation: For Letter Combinations of a Phone Number, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Letter Combinations of a Phone Number directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_letter_combinations_of_a_phone_number(data):
    """Brute-force baseline for: Letter Combinations of a Phone Number."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Letter Combinations of a Phone Number to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_letter_combinations_of_a_phone_number(data):
    """Intermediate optimized approach for: Letter Combinations of a Phone Number."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Letter Combinations of a Phone Number: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_letter_combinations_of_a_phone_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q9. N-Queens

### Problem Statement (Specific)
Solve **N-Queens** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 10
Output: 9
Explanation: For N-Queens, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for N-Queens directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_n_queens(data):
    """Brute-force baseline for: N-Queens."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for N-Queens to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_n_queens(data):
    """Intermediate optimized approach for: N-Queens."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to N-Queens: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_n_queens(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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

## Q10. Word Search

### Problem Statement (Specific)
Solve **Word Search** using **Backtracking**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 11
Output: 9
Explanation: For Word Search, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Word Search directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_word_search(data):
    """Brute-force baseline for: Word Search."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Word Search to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_word_search(data):
    """Intermediate optimized approach for: Word Search."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Backtracking invariant to Word Search: Model problem as DFS over decisions: 1. choose an option 2. recurse 3. unchoose (backtrack) to restore state Backtracking differs from brute force by pruning invalid/pointless branches early.
- Complexity target: Time pattern-optimal, Space recursion depth + output size.

#### Optimal Python (Question-Specific)
```python
def solve_word_search(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def backtrack(nums):
        ans = []
        path = []
    
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
    
            # choice 1: skip
            dfs(i + 1)
    
            # choice 2: take
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    
        dfs(0)
        return ans
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
