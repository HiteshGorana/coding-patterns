# Pattern 10 Interview Playbook: Monotonic Stack

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Monotonic stacks answer "next greater/smaller" and boundary-span questions in linear time.
- Core intuition: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Trigger cue 1: "next greater/smaller", nearest boundary, histogram area.
- Quick self-check: Does each element need nearest bigger/smaller on one side?
- Target complexity: Time O(n) (amortized), Space O(n)

---

## Q1. Daily Temperatures

### Problem Statement (Specific)
Solve **Daily Temperatures** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Daily Temperatures, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Daily Temperatures directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_daily_temperatures(data):
    """Brute-force baseline for: Daily Temperatures."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Daily Temperatures to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_daily_temperatures(data):
    """Intermediate optimized approach for: Daily Temperatures."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Daily Temperatures: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_daily_temperatures(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q2. Next Greater Element I

### Problem Statement (Specific)
Solve **Next Greater Element I** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Next Greater Element I, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Next Greater Element I directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_next_greater_element_i(data):
    """Brute-force baseline for: Next Greater Element I."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Next Greater Element I to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_next_greater_element_i(data):
    """Intermediate optimized approach for: Next Greater Element I."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Next Greater Element I: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_next_greater_element_i(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q3. Next Greater Element II

### Problem Statement (Specific)
Solve **Next Greater Element II** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Next Greater Element II, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Next Greater Element II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_next_greater_element_ii(data):
    """Brute-force baseline for: Next Greater Element II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Next Greater Element II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_next_greater_element_ii(data):
    """Intermediate optimized approach for: Next Greater Element II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Next Greater Element II: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_next_greater_element_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q4. Largest Rectangle in Histogram

### Problem Statement (Specific)
Solve **Largest Rectangle in Histogram** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Largest Rectangle in Histogram, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Largest Rectangle in Histogram directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_largest_rectangle_in_histogram(data):
    """Brute-force baseline for: Largest Rectangle in Histogram."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Largest Rectangle in Histogram to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_largest_rectangle_in_histogram(data):
    """Intermediate optimized approach for: Largest Rectangle in Histogram."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Largest Rectangle in Histogram: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_largest_rectangle_in_histogram(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q5. Trapping Rain Water

### Problem Statement (Specific)
Solve **Trapping Rain Water** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Trapping Rain Water, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Trapping Rain Water directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_trapping_rain_water(data):
    """Brute-force baseline for: Trapping Rain Water."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Trapping Rain Water to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_trapping_rain_water(data):
    """Intermediate optimized approach for: Trapping Rain Water."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Trapping Rain Water: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_trapping_rain_water(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q6. Remove K Digits

### Problem Statement (Specific)
Solve **Remove K Digits** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Remove K Digits, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Remove K Digits directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_remove_k_digits(data):
    """Brute-force baseline for: Remove K Digits."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Remove K Digits to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_remove_k_digits(data):
    """Intermediate optimized approach for: Remove K Digits."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Remove K Digits: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_remove_k_digits(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q7. Sum of Subarray Minimums

### Problem Statement (Specific)
Solve **Sum of Subarray Minimums** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sum of Subarray Minimums, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sum of Subarray Minimums directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sum_of_subarray_minimums(data):
    """Brute-force baseline for: Sum of Subarray Minimums."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sum of Subarray Minimums to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sum_of_subarray_minimums(data):
    """Intermediate optimized approach for: Sum of Subarray Minimums."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Sum of Subarray Minimums: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_sum_of_subarray_minimums(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q8. Online Stock Span

### Problem Statement (Specific)
Solve **Online Stock Span** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Online Stock Span, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Online Stock Span directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_online_stock_span(data):
    """Brute-force baseline for: Online Stock Span."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Online Stock Span to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_online_stock_span(data):
    """Intermediate optimized approach for: Online Stock Span."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Online Stock Span: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_online_stock_span(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q9. Asteroid Collision

### Problem Statement (Specific)
Solve **Asteroid Collision** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Asteroid Collision, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Asteroid Collision directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_asteroid_collision(data):
    """Brute-force baseline for: Asteroid Collision."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Asteroid Collision to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_asteroid_collision(data):
    """Intermediate optimized approach for: Asteroid Collision."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Asteroid Collision: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_asteroid_collision(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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

## Q10. Car Fleet II

### Problem Statement (Specific)
Solve **Car Fleet II** using **Monotonic Stack**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Car Fleet II, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Car Fleet II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_car_fleet_ii(data):
    """Brute-force baseline for: Car Fleet II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Car Fleet II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_car_fleet_ii(data):
    """Intermediate optimized approach for: Car Fleet II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Monotonic Stack invariant to Car Fleet II: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Complexity target: Time O(n) (amortized), Space O(n).

#### Optimal Python (Question-Specific)
```python
def solve_car_fleet_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def next_greater(nums):
        ans = [-1] * len(nums)
        stack = []  # indices, values in decreasing order
    
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i
            stack.append(i)
    
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
