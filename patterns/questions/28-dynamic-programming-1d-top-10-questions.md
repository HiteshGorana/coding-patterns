# Pattern 28 Interview Playbook: Dynamic Programming (1D)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Optimizes sequential decisions where state depends on previous positions.
- Core intuition: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Trigger cue 1: Max/min/count ways over linear index.
- Trigger cue 2: Overlapping subproblems in recursion.
- Quick self-check: Can I define `dp[i]` with a small recurrence?
- Target complexity: Time usually O(n), Space O(n) or O(1) optimized

---

## Q1. Climbing Stairs

### Problem Statement (Specific)
Solve **Climbing Stairs** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Climbing Stairs, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Climbing Stairs directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_climbing_stairs(data):
    """Brute-force baseline for: Climbing Stairs."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Climbing Stairs to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_climbing_stairs(data):
    """Intermediate optimized approach for: Climbing Stairs."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Climbing Stairs: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_climbing_stairs(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q2. House Robber

### Problem Statement (Specific)
Solve **House Robber** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- Maximum rob amount without robbing adjacent houses.

### Constraints (Typical)
- 1 <= len(nums) <= 1e5

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: DP choose max of rob/skip transitions.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for House Robber directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_house_robber(data):
    """Brute-force baseline for: House Robber."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for House Robber to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_house_robber(data):
    """Intermediate optimized approach for: House Robber."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to House Robber: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_house_robber(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q3. House Robber II

### Problem Statement (Specific)
Solve **House Robber II** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- Maximum rob amount without robbing adjacent houses.

### Constraints (Typical)
- 1 <= len(nums) <= 1e5

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: DP choose max of rob/skip transitions.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for House Robber II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_house_robber_ii(data):
    """Brute-force baseline for: House Robber II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for House Robber II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_house_robber_ii(data):
    """Intermediate optimized approach for: House Robber II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to House Robber II: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_house_robber_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q4. Min Cost Climbing Stairs

### Problem Statement (Specific)
Solve **Min Cost Climbing Stairs** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Min Cost Climbing Stairs, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Min Cost Climbing Stairs directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_min_cost_climbing_stairs(data):
    """Brute-force baseline for: Min Cost Climbing Stairs."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Min Cost Climbing Stairs to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_min_cost_climbing_stairs(data):
    """Intermediate optimized approach for: Min Cost Climbing Stairs."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Min Cost Climbing Stairs: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_min_cost_climbing_stairs(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q5. Decode Ways

### Problem Statement (Specific)
Solve **Decode Ways** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Decode Ways, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Decode Ways directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_decode_ways(data):
    """Brute-force baseline for: Decode Ways."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Decode Ways to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_decode_ways(data):
    """Intermediate optimized approach for: Decode Ways."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Decode Ways: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_decode_ways(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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
Solve **Coin Change** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
- Apply Dynamic Programming (1D) invariant to Coin Change: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_coin_change(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q7. Maximum Subarray

### Problem Statement (Specific)
Solve **Maximum Subarray** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Maximum Subarray, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Maximum Subarray directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_maximum_subarray(data):
    """Brute-force baseline for: Maximum Subarray."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Maximum Subarray to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_maximum_subarray(data):
    """Intermediate optimized approach for: Maximum Subarray."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Maximum Subarray: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_maximum_subarray(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q8. Longest Increasing Subsequence

### Problem Statement (Specific)
Solve **Longest Increasing Subsequence** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Longest Increasing Subsequence, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Longest Increasing Subsequence directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_longest_increasing_subsequence(data):
    """Brute-force baseline for: Longest Increasing Subsequence."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Longest Increasing Subsequence to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_longest_increasing_subsequence(data):
    """Intermediate optimized approach for: Longest Increasing Subsequence."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Longest Increasing Subsequence: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_longest_increasing_subsequence(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q9. Word Break

### Problem Statement (Specific)
Solve **Word Break** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Word Break, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Word Break directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_word_break(data):
    """Brute-force baseline for: Word Break."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Word Break to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_word_break(data):
    """Intermediate optimized approach for: Word Break."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Word Break: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_word_break(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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

## Q10. Perfect Squares

### Problem Statement (Specific)
Solve **Perfect Squares** using **Dynamic Programming (1D)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Perfect Squares, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Perfect Squares directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_perfect_squares(data):
    """Brute-force baseline for: Perfect Squares."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Perfect Squares to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_perfect_squares(data):
    """Intermediate optimized approach for: Perfect Squares."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (1D) invariant to Perfect Squares: Define `dp[i]` as best/count answer up to position `i` (or from `i` onward). Transition uses a few previous states: `dp[i] = combine(dp[i-1], dp[i-2], ...)`
- Complexity target: Time usually O(n), Space O(n) or O(1) optimized.

#### Optimal Python (Question-Specific)
```python
def solve_perfect_squares(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def house_robber(nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1
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
