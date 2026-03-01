# Pattern 09 Interview Playbook: Greedy

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Greedy algorithms make the best local decision at each step, aiming for global optimality.
- Core intuition: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Trigger cue 1: Min/max optimization with local decision opportunities.
- Trigger cue 2: Can prove local choice never hurts global optimum.
- Quick self-check: Can I give a short exchange/invariant argument?
- Target complexity: Time often O(n) (after optional sort), Space usually O(1)

---

## Q1. Jump Game

### Problem Statement (Specific)
Solve **Jump Game** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Jump Game, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Jump Game directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_jump_game(data):
    """Brute-force baseline for: Jump Game."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Jump Game to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_jump_game(data):
    """Intermediate optimized approach for: Jump Game."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Jump Game: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_jump_game(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q2. Jump Game II

### Problem Statement (Specific)
Solve **Jump Game II** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Jump Game II, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Jump Game II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_jump_game_ii(data):
    """Brute-force baseline for: Jump Game II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Jump Game II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_jump_game_ii(data):
    """Intermediate optimized approach for: Jump Game II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Jump Game II: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_jump_game_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q3. Gas Station

### Problem Statement (Specific)
Solve **Gas Station** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Gas Station, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Gas Station directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_gas_station(data):
    """Brute-force baseline for: Gas Station."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Gas Station to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_gas_station(data):
    """Intermediate optimized approach for: Gas Station."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Gas Station: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_gas_station(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q4. Partition Labels

### Problem Statement (Specific)
Solve **Partition Labels** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Partition Labels, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Partition Labels directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_partition_labels(data):
    """Brute-force baseline for: Partition Labels."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Partition Labels to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_partition_labels(data):
    """Intermediate optimized approach for: Partition Labels."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Partition Labels: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_partition_labels(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q5. Assign Cookies

### Problem Statement (Specific)
Solve **Assign Cookies** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Assign Cookies, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Assign Cookies directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_assign_cookies(data):
    """Brute-force baseline for: Assign Cookies."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Assign Cookies to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_assign_cookies(data):
    """Intermediate optimized approach for: Assign Cookies."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Assign Cookies: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_assign_cookies(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q6. Non-overlapping Intervals

### Problem Statement (Specific)
Solve **Non-overlapping Intervals** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Non-overlapping Intervals, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Non-overlapping Intervals directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_non_overlapping_intervals(data):
    """Brute-force baseline for: Non-overlapping Intervals."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Non-overlapping Intervals to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_non_overlapping_intervals(data):
    """Intermediate optimized approach for: Non-overlapping Intervals."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Non-overlapping Intervals: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_non_overlapping_intervals(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q7. Minimum Number of Arrows to Burst Balloons

### Problem Statement (Specific)
Solve **Minimum Number of Arrows to Burst Balloons** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Minimum Number of Arrows to Burst Balloons, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Number of Arrows to Burst Balloons directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_number_of_arrows_to_burst_balloons(data):
    """Brute-force baseline for: Minimum Number of Arrows to Burst Balloons."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Number of Arrows to Burst Balloons to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_number_of_arrows_to_burst_balloons(data):
    """Intermediate optimized approach for: Minimum Number of Arrows to Burst Balloons."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Minimum Number of Arrows to Burst Balloons: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_minimum_number_of_arrows_to_burst_balloons(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q8. Task Scheduler

### Problem Statement (Specific)
Solve **Task Scheduler** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Task Scheduler, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Task Scheduler directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_task_scheduler(data):
    """Brute-force baseline for: Task Scheduler."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Task Scheduler to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_task_scheduler(data):
    """Intermediate optimized approach for: Task Scheduler."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Task Scheduler: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_task_scheduler(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q9. Wiggle Subsequence

### Problem Statement (Specific)
Solve **Wiggle Subsequence** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Wiggle Subsequence, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Wiggle Subsequence directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_wiggle_subsequence(data):
    """Brute-force baseline for: Wiggle Subsequence."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Wiggle Subsequence to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_wiggle_subsequence(data):
    """Intermediate optimized approach for: Wiggle Subsequence."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Wiggle Subsequence: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_wiggle_subsequence(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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

## Q10. Best Time to Buy and Sell Stock II

### Problem Statement (Specific)
Solve **Best Time to Buy and Sell Stock II** using **Greedy**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Best Time to Buy and Sell Stock II, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Best Time to Buy and Sell Stock II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_best_time_to_buy_and_sell_stock_ii(data):
    """Brute-force baseline for: Best Time to Buy and Sell Stock II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Best Time to Buy and Sell Stock II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_best_time_to_buy_and_sell_stock_ii(data):
    """Intermediate optimized approach for: Best Time to Buy and Sell Stock II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Greedy invariant to Best Time to Buy and Sell Stock II: If a local choice never hurts an optimal final solution, commit early and move on. Greedy works only when problem structure supports it (matroid-like/exchange properties).
- Complexity target: Time often O(n) (after optional sort), Space usually O(1).

#### Optimal Python (Question-Specific)
```python
def solve_best_time_to_buy_and_sell_stock_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def can_jump(nums):
        reach = 0
        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)
        return True
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
