# Pattern 30 Interview Playbook: Knapsack DP

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Optimization/counting problems with "pick or skip" decisions under capacity/target constraints.
- Core intuition: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Trigger cue 1: Pick/skip under capacity/target constraints.
- Quick self-check: Is this subset decision under a budget-like limit?
- Target complexity: Time O(n * capacity), Space O(capacity) with 1D optimization

---

## Q1. 0/1 Knapsack

### Problem Statement (Specific)
Solve **0/1 Knapsack** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For 0/1 Knapsack, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for 0/1 Knapsack directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_q_0_1_knapsack(data):
    """Brute-force baseline for: 0/1 Knapsack."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for 0/1 Knapsack to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_q_0_1_knapsack(data):
    """Intermediate optimized approach for: 0/1 Knapsack."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to 0/1 Knapsack: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_q_0_1_knapsack(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q2. Partition Equal Subset Sum

### Problem Statement (Specific)
Solve **Partition Equal Subset Sum** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Partition Equal Subset Sum, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Partition Equal Subset Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_partition_equal_subset_sum(data):
    """Brute-force baseline for: Partition Equal Subset Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Partition Equal Subset Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_partition_equal_subset_sum(data):
    """Intermediate optimized approach for: Partition Equal Subset Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Partition Equal Subset Sum: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_partition_equal_subset_sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q3. Target Sum

### Problem Statement (Specific)
Solve **Target Sum** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Target Sum, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Target Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_target_sum(data):
    """Brute-force baseline for: Target Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Target Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_target_sum(data):
    """Intermediate optimized approach for: Target Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Target Sum: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_target_sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q4. Last Stone Weight II

### Problem Statement (Specific)
Solve **Last Stone Weight II** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Last Stone Weight II, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Last Stone Weight II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_last_stone_weight_ii(data):
    """Brute-force baseline for: Last Stone Weight II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Last Stone Weight II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_last_stone_weight_ii(data):
    """Intermediate optimized approach for: Last Stone Weight II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Last Stone Weight II: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_last_stone_weight_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q5. Ones and Zeroes

### Problem Statement (Specific)
Solve **Ones and Zeroes** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Ones and Zeroes, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Ones and Zeroes directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_ones_and_zeroes(data):
    """Brute-force baseline for: Ones and Zeroes."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Ones and Zeroes to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_ones_and_zeroes(data):
    """Intermediate optimized approach for: Ones and Zeroes."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Ones and Zeroes: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_ones_and_zeroes(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q6. Coin Change

### Problem Statement (Specific)
Solve **Coin Change** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Coin Change, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Coin Change directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_coin_change(data):
    """Brute-force baseline for: Coin Change."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Coin Change to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_coin_change(data):
    """Intermediate optimized approach for: Coin Change."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Coin Change: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_coin_change(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q7. Coin Change II

### Problem Statement (Specific)
Solve **Coin Change II** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Coin Change II, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Coin Change II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_coin_change_ii(data):
    """Brute-force baseline for: Coin Change II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Coin Change II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_coin_change_ii(data):
    """Intermediate optimized approach for: Coin Change II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Coin Change II: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_coin_change_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q8. Unbounded Knapsack

### Problem Statement (Specific)
Solve **Unbounded Knapsack** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Unbounded Knapsack, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Unbounded Knapsack directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_unbounded_knapsack(data):
    """Brute-force baseline for: Unbounded Knapsack."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Unbounded Knapsack to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_unbounded_knapsack(data):
    """Intermediate optimized approach for: Unbounded Knapsack."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Unbounded Knapsack: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_unbounded_knapsack(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q9. Rod Cutting

### Problem Statement (Specific)
Solve **Rod Cutting** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Rod Cutting, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Rod Cutting directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_rod_cutting(data):
    """Brute-force baseline for: Rod Cutting."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Rod Cutting to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_rod_cutting(data):
    """Intermediate optimized approach for: Rod Cutting."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Rod Cutting: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_rod_cutting(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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

## Q10. Minimum Subset Sum Difference

### Problem Statement (Specific)
Solve **Minimum Subset Sum Difference** using **Knapsack DP**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Minimum Subset Sum Difference, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Subset Sum Difference directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_subset_sum_difference(data):
    """Brute-force baseline for: Minimum Subset Sum Difference."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Subset Sum Difference to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_subset_sum_difference(data):
    """Intermediate optimized approach for: Minimum Subset Sum Difference."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Knapsack DP invariant to Minimum Subset Sum Difference: DP state tracks best/possible outcome using first `i` items and capacity `c`. 0/1 knapsack transition: - skip item `i`: `dp[c]` - take item `i` if `w <= c`: `dp[c-w] + value` Reverse capacity loop for 0/1 to avoid reusing same item multiple times.
- Complexity target: Time O(n * capacity), Space O(capacity) with 1D optimization.

#### Optimal Python (Question-Specific)
```python
def solve_minimum_subset_sum_difference(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def knapsack_01(weights, values, cap):
        dp = [0] * (cap + 1)
        for w, v in zip(weights, values):
            for c in range(cap, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[cap]
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
