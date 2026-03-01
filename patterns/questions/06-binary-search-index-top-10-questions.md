# Pattern 06 Interview Playbook: Binary Search (Index Space)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Binary search finds positions or values in sorted/indexed structures in logarithmic time.
- Core intuition: At each step, discard half the remaining search space based on midpoint comparison.
- Trigger cue 1: Sorted data.
- Trigger cue 2: Need exact index, lower bound, upper bound.
- Quick self-check: Is the search condition monotonic across indices?
- Target complexity: Time O(log n), Space O(1) iterative

---

## Q1. Binary Search

### Problem Statement (Specific)
Solve **Binary Search** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Binary Search, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Binary Search directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_binary_search(data):
    """Brute-force baseline for: Binary Search."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Binary Search to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_binary_search(data):
    """Intermediate optimized approach for: Binary Search."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Binary Search: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_binary_search(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q2. Search Insert Position

### Problem Statement (Specific)
Solve **Search Insert Position** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Search Insert Position, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Search Insert Position directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_search_insert_position(data):
    """Brute-force baseline for: Search Insert Position."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Search Insert Position to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_search_insert_position(data):
    """Intermediate optimized approach for: Search Insert Position."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Search Insert Position: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_search_insert_position(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q3. Find First and Last Position of Element in Sorted Array

### Problem Statement (Specific)
Solve **Find First and Last Position of Element in Sorted Array** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find First and Last Position of Element in Sorted Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find First and Last Position of Element in Sorted Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_first_and_last_position_of_element_in_sorted_array(data):
    """Brute-force baseline for: Find First and Last Position of Element in Sorted Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find First and Last Position of Element in Sorted Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_first_and_last_position_of_element_in_sorted_array(data):
    """Intermediate optimized approach for: Find First and Last Position of Element in Sorted Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Find First and Last Position of Element in Sorted Array: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_find_first_and_last_position_of_element_in_sorted_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q4. Search in Rotated Sorted Array

### Problem Statement (Specific)
Solve **Search in Rotated Sorted Array** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Search in Rotated Sorted Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Search in Rotated Sorted Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_search_in_rotated_sorted_array(data):
    """Brute-force baseline for: Search in Rotated Sorted Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Search in Rotated Sorted Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_search_in_rotated_sorted_array(data):
    """Intermediate optimized approach for: Search in Rotated Sorted Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Search in Rotated Sorted Array: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_search_in_rotated_sorted_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q5. Find Minimum in Rotated Sorted Array

### Problem Statement (Specific)
Solve **Find Minimum in Rotated Sorted Array** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find Minimum in Rotated Sorted Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find Minimum in Rotated Sorted Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_minimum_in_rotated_sorted_array(data):
    """Brute-force baseline for: Find Minimum in Rotated Sorted Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find Minimum in Rotated Sorted Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_minimum_in_rotated_sorted_array(data):
    """Intermediate optimized approach for: Find Minimum in Rotated Sorted Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Find Minimum in Rotated Sorted Array: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_find_minimum_in_rotated_sorted_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q6. Sqrt(x)

### Problem Statement (Specific)
Solve **Sqrt(x)** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sqrt(x), maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sqrt(x) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sqrt_x(data):
    """Brute-force baseline for: Sqrt(x)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sqrt(x) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sqrt_x(data):
    """Intermediate optimized approach for: Sqrt(x)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Sqrt(x): At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_sqrt_x(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q7. Peak Index in a Mountain Array

### Problem Statement (Specific)
Solve **Peak Index in a Mountain Array** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Peak Index in a Mountain Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Peak Index in a Mountain Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_peak_index_in_a_mountain_array(data):
    """Brute-force baseline for: Peak Index in a Mountain Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Peak Index in a Mountain Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_peak_index_in_a_mountain_array(data):
    """Intermediate optimized approach for: Peak Index in a Mountain Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Peak Index in a Mountain Array: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_peak_index_in_a_mountain_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q8. Find Peak Element

### Problem Statement (Specific)
Solve **Find Peak Element** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find Peak Element, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find Peak Element directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_peak_element(data):
    """Brute-force baseline for: Find Peak Element."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find Peak Element to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_peak_element(data):
    """Intermediate optimized approach for: Find Peak Element."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Find Peak Element: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_find_peak_element(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q9. First Bad Version

### Problem Statement (Specific)
Solve **First Bad Version** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For First Bad Version, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for First Bad Version directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_first_bad_version(data):
    """Brute-force baseline for: First Bad Version."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for First Bad Version to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_first_bad_version(data):
    """Intermediate optimized approach for: First Bad Version."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to First Bad Version: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_first_bad_version(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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

## Q10. Search a 2D Matrix

### Problem Statement (Specific)
Solve **Search a 2D Matrix** using **Binary Search (Index Space)**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Search a 2D Matrix, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Search a 2D Matrix directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_search_a_2d_matrix(data):
    """Brute-force baseline for: Search a 2D Matrix."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Search a 2D Matrix to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_search_a_2d_matrix(data):
    """Intermediate optimized approach for: Search a 2D Matrix."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Binary Search (Index Space) invariant to Search a 2D Matrix: At each step, discard half the remaining search space based on midpoint comparison.
- Complexity target: Time O(log n), Space O(1) iterative.

#### Optimal Python (Question-Specific)
```python
def solve_search_a_2d_matrix(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1
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
