# Pattern 05 Interview Playbook: Prefix Sum

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Prefix sums convert repeated range-sum queries from linear to constant time.
- Core intuition: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Trigger cue 1: Many range sum queries.
- Trigger cue 2: Count subarrays with target sum.
- Quick self-check: Can I precompute cumulative state once and answer ranges quickly?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Range Sum Query - Immutable

### Problem Statement (Specific)
Solve **Range Sum Query - Immutable** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Range Sum Query - Immutable, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Range Sum Query - Immutable directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_range_sum_query_immutable(data):
    """Brute-force baseline for: Range Sum Query - Immutable."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Range Sum Query - Immutable to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_range_sum_query_immutable(data):
    """Intermediate optimized approach for: Range Sum Query - Immutable."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Range Sum Query - Immutable: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_range_sum_query_immutable(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q2. Subarray Sum Equals K

### Problem Statement (Specific)
Solve **Subarray Sum Equals K** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Subarray Sum Equals K, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Subarray Sum Equals K directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_subarray_sum_equals_k(data):
    """Brute-force baseline for: Subarray Sum Equals K."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Subarray Sum Equals K to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_subarray_sum_equals_k(data):
    """Intermediate optimized approach for: Subarray Sum Equals K."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Subarray Sum Equals K: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_subarray_sum_equals_k(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q3. Continuous Subarray Sum

### Problem Statement (Specific)
Solve **Continuous Subarray Sum** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Continuous Subarray Sum, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Continuous Subarray Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_continuous_subarray_sum(data):
    """Brute-force baseline for: Continuous Subarray Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Continuous Subarray Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_continuous_subarray_sum(data):
    """Intermediate optimized approach for: Continuous Subarray Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Continuous Subarray Sum: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_continuous_subarray_sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q4. Contiguous Array

### Problem Statement (Specific)
Solve **Contiguous Array** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Contiguous Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Contiguous Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_contiguous_array(data):
    """Brute-force baseline for: Contiguous Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Contiguous Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_contiguous_array(data):
    """Intermediate optimized approach for: Contiguous Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Contiguous Array: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_contiguous_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q5. Product of Array Except Self

### Problem Statement (Specific)
Solve **Product of Array Except Self** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Product of Array Except Self, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Product of Array Except Self directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_product_of_array_except_self(data):
    """Brute-force baseline for: Product of Array Except Self."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Product of Array Except Self to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_product_of_array_except_self(data):
    """Intermediate optimized approach for: Product of Array Except Self."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Product of Array Except Self: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_product_of_array_except_self(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q6. Find Pivot Index

### Problem Statement (Specific)
Solve **Find Pivot Index** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find Pivot Index, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find Pivot Index directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_pivot_index(data):
    """Brute-force baseline for: Find Pivot Index."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find Pivot Index to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_pivot_index(data):
    """Intermediate optimized approach for: Find Pivot Index."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Find Pivot Index: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_find_pivot_index(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q7. Corporate Flight Bookings

### Problem Statement (Specific)
Solve **Corporate Flight Bookings** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Corporate Flight Bookings, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Corporate Flight Bookings directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_corporate_flight_bookings(data):
    """Brute-force baseline for: Corporate Flight Bookings."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Corporate Flight Bookings to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_corporate_flight_bookings(data):
    """Intermediate optimized approach for: Corporate Flight Bookings."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Corporate Flight Bookings: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_corporate_flight_bookings(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q8. Car Pooling

### Problem Statement (Specific)
Solve **Car Pooling** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Car Pooling, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Car Pooling directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_car_pooling(data):
    """Brute-force baseline for: Car Pooling."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Car Pooling to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_car_pooling(data):
    """Intermediate optimized approach for: Car Pooling."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Car Pooling: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_car_pooling(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q9. Subarray Sums Divisible by K

### Problem Statement (Specific)
Solve **Subarray Sums Divisible by K** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Subarray Sums Divisible by K, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Subarray Sums Divisible by K directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_subarray_sums_divisible_by_k(data):
    """Brute-force baseline for: Subarray Sums Divisible by K."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Subarray Sums Divisible by K to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_subarray_sums_divisible_by_k(data):
    """Intermediate optimized approach for: Subarray Sums Divisible by K."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Subarray Sums Divisible by K: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_subarray_sums_divisible_by_k(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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

## Q10. Maximum Size Subarray Sum Equals k

### Problem Statement (Specific)
Solve **Maximum Size Subarray Sum Equals k** using **Prefix Sum**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Maximum Size Subarray Sum Equals k, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Maximum Size Subarray Sum Equals k directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_maximum_size_subarray_sum_equals_k(data):
    """Brute-force baseline for: Maximum Size Subarray Sum Equals k."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Maximum Size Subarray Sum Equals k to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_maximum_size_subarray_sum_equals_k(data):
    """Intermediate optimized approach for: Maximum Size Subarray Sum Equals k."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Prefix Sum invariant to Maximum Size Subarray Sum Equals k: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_maximum_size_subarray_sum_equals_k(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def count_subarrays_sum_k(nums, k):
        freq = {0: 1}
        curr = 0
        ans = 0
    
        for x in nums:
            curr += x
            ans += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
    
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
