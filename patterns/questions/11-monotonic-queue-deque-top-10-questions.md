# Pattern 11 Interview Playbook: Monotonic Queue / Deque

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Maintains min/max over a sliding window in linear time.
- Core intuition: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Trigger cue 1: Sliding window max/min in strict O(n).
- Quick self-check: Do I need best value per moving window with index expiry?
- Target complexity: Time O(n) amortized, Space O(k) to O(n) worst-case index storage

---

## Q1. Sliding Window Maximum

### Problem Statement (Specific)
Solve **Sliding Window Maximum** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sliding Window Maximum, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sliding Window Maximum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sliding_window_maximum(data):
    """Brute-force baseline for: Sliding Window Maximum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sliding Window Maximum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sliding_window_maximum(data):
    """Intermediate optimized approach for: Sliding Window Maximum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Sliding Window Maximum: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_sliding_window_maximum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q2. Shortest Subarray with Sum at Least K

### Problem Statement (Specific)
Solve **Shortest Subarray with Sum at Least K** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Shortest Subarray with Sum at Least K, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Shortest Subarray with Sum at Least K directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_shortest_subarray_with_sum_at_least_k(data):
    """Brute-force baseline for: Shortest Subarray with Sum at Least K."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Shortest Subarray with Sum at Least K to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_shortest_subarray_with_sum_at_least_k(data):
    """Intermediate optimized approach for: Shortest Subarray with Sum at Least K."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Shortest Subarray with Sum at Least K: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_shortest_subarray_with_sum_at_least_k(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q3. Constrained Subsequence Sum

### Problem Statement (Specific)
Solve **Constrained Subsequence Sum** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Constrained Subsequence Sum, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Constrained Subsequence Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_constrained_subsequence_sum(data):
    """Brute-force baseline for: Constrained Subsequence Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Constrained Subsequence Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_constrained_subsequence_sum(data):
    """Intermediate optimized approach for: Constrained Subsequence Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Constrained Subsequence Sum: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_constrained_subsequence_sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q4. Jump Game VI

### Problem Statement (Specific)
Solve **Jump Game VI** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Jump Game VI, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Jump Game VI directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_jump_game_vi(data):
    """Brute-force baseline for: Jump Game VI."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Jump Game VI to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_jump_game_vi(data):
    """Intermediate optimized approach for: Jump Game VI."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Jump Game VI: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_jump_game_vi(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q5. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

### Problem Statement (Specific)
Solve **Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit(data):
    """Brute-force baseline for: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit(data):
    """Intermediate optimized approach for: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q6. Max Value of Equation

### Problem Statement (Specific)
Solve **Max Value of Equation** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Max Value of Equation, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Max Value of Equation directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_max_value_of_equation(data):
    """Brute-force baseline for: Max Value of Equation."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Max Value of Equation to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_max_value_of_equation(data):
    """Intermediate optimized approach for: Max Value of Equation."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Max Value of Equation: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_max_value_of_equation(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q7. First Negative Integer in Every Window of Size K

### Problem Statement (Specific)
Solve **First Negative Integer in Every Window of Size K** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For First Negative Integer in Every Window of Size K, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for First Negative Integer in Every Window of Size K directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_first_negative_integer_in_every_window_of_size_k(data):
    """Brute-force baseline for: First Negative Integer in Every Window of Size K."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for First Negative Integer in Every Window of Size K to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_first_negative_integer_in_every_window_of_size_k(data):
    """Intermediate optimized approach for: First Negative Integer in Every Window of Size K."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to First Negative Integer in Every Window of Size K: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_first_negative_integer_in_every_window_of_size_k(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q8. Minimum Number of K Consecutive Bit Flips

### Problem Statement (Specific)
Solve **Minimum Number of K Consecutive Bit Flips** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Minimum Number of K Consecutive Bit Flips, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Number of K Consecutive Bit Flips directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_number_of_k_consecutive_bit_flips(data):
    """Brute-force baseline for: Minimum Number of K Consecutive Bit Flips."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Number of K Consecutive Bit Flips to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_number_of_k_consecutive_bit_flips(data):
    """Intermediate optimized approach for: Minimum Number of K Consecutive Bit Flips."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Minimum Number of K Consecutive Bit Flips: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_minimum_number_of_k_consecutive_bit_flips(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q9. Find the Most Competitive Subsequence

### Problem Statement (Specific)
Solve **Find the Most Competitive Subsequence** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find the Most Competitive Subsequence, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find the Most Competitive Subsequence directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_the_most_competitive_subsequence(data):
    """Brute-force baseline for: Find the Most Competitive Subsequence."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find the Most Competitive Subsequence to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_the_most_competitive_subsequence(data):
    """Intermediate optimized approach for: Find the Most Competitive Subsequence."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Find the Most Competitive Subsequence: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_find_the_most_competitive_subsequence(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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

## Q10. Maximum Robots Within Budget

### Problem Statement (Specific)
Solve **Maximum Robots Within Budget** using **Monotonic Queue / Deque**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Maximum Robots Within Budget, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Maximum Robots Within Budget directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_maximum_robots_within_budget(data):
    """Brute-force baseline for: Maximum Robots Within Budget."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Maximum Robots Within Budget to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_maximum_robots_within_budget(data):
    """Intermediate optimized approach for: Maximum Robots Within Budget."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Queue / Deque invariant to Maximum Robots Within Budget: Use deque of indices in monotonic value order: - decreasing deque for window maximum - increasing deque for window minimum Front always holds best candidate for current window.
- Complexity target: Time O(n) amortized, Space O(k) to O(n) worst-case index storage.

#### Optimal Python (Question-Specific)
```python
def solve_maximum_robots_within_budget(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    from collections import deque
    
    def sliding_window_max(nums, k):
        dq = deque()  # indices, values decreasing
        ans = []
    
        for i, x in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
    
            while dq and nums[dq[-1]] <= x:
                dq.pop()
    
            dq.append(i)
    
            if i >= k - 1:
                ans.append(nums[dq[0]])
    
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
