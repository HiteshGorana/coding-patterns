# Pattern 02 Interview Playbook: Two Pointers

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Two pointers is ideal for problems on arrays/strings where two positions move with rules.
- Core intuition: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Trigger cue 1: Sorted array/string.
- Trigger cue 2: Need pair/triplet relation (`sum`, `diff`, palindrome).
- Quick self-check: If I move one pointer, can I prove I never miss optimum?
- Target complexity: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost)

---

## Q1. Two Sum II - Input Array Is Sorted

### Problem Statement (Specific)
Solve **Two Sum II - Input Array Is Sorted** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `target`: int

### Output
- Two indices `[i, j]` such that `nums[i] + nums[j] == target`.

### Constraints (Typical)
- 2 <= n <= 1e5
- -1e9 <= nums[i], target <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15], target = 9
Output: [0, 1]
Explanation: Check complement before insert to avoid reusing same index.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Two Sum II - Input Array Is Sorted directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_two_sum_ii_input_array_is_sorted(data):
    """Brute-force baseline for: Two Sum II - Input Array Is Sorted."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Two Sum II - Input Array Is Sorted to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_two_sum_ii_input_array_is_sorted(data):
    """Intermediate optimized approach for: Two Sum II - Input Array Is Sorted."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Two Sum II - Input Array Is Sorted: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_two_sum_ii_input_array_is_sorted(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q2. 3Sum

### Problem Statement (Specific)
Solve **3Sum** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For 3Sum, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for 3Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_q_3sum(data):
    """Brute-force baseline for: 3Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for 3Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_q_3sum(data):
    """Intermediate optimized approach for: 3Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to 3Sum: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_q_3sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q3. 4Sum

### Problem Statement (Specific)
Solve **4Sum** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For 4Sum, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for 4Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_q_4sum(data):
    """Brute-force baseline for: 4Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for 4Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_q_4sum(data):
    """Intermediate optimized approach for: 4Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to 4Sum: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_q_4sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q4. Container With Most Water

### Problem Statement (Specific)
Solve **Container With Most Water** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Container With Most Water, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Container With Most Water directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_container_with_most_water(data):
    """Brute-force baseline for: Container With Most Water."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Container With Most Water to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_container_with_most_water(data):
    """Intermediate optimized approach for: Container With Most Water."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Container With Most Water: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_container_with_most_water(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q5. Valid Palindrome

### Problem Statement (Specific)
Solve **Valid Palindrome** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Valid Palindrome, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Valid Palindrome directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_valid_palindrome(data):
    """Brute-force baseline for: Valid Palindrome."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Valid Palindrome to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_valid_palindrome(data):
    """Intermediate optimized approach for: Valid Palindrome."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Valid Palindrome: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_valid_palindrome(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q6. Squares of a Sorted Array

### Problem Statement (Specific)
Solve **Squares of a Sorted Array** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Squares of a Sorted Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Squares of a Sorted Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_squares_of_a_sorted_array(data):
    """Brute-force baseline for: Squares of a Sorted Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Squares of a Sorted Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_squares_of_a_sorted_array(data):
    """Intermediate optimized approach for: Squares of a Sorted Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Squares of a Sorted Array: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_squares_of_a_sorted_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q7. Remove Duplicates from Sorted Array

### Problem Statement (Specific)
Solve **Remove Duplicates from Sorted Array** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Remove Duplicates from Sorted Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Remove Duplicates from Sorted Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_remove_duplicates_from_sorted_array(data):
    """Brute-force baseline for: Remove Duplicates from Sorted Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Remove Duplicates from Sorted Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_remove_duplicates_from_sorted_array(data):
    """Intermediate optimized approach for: Remove Duplicates from Sorted Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Remove Duplicates from Sorted Array: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_remove_duplicates_from_sorted_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q8. Move Zeroes

### Problem Statement (Specific)
Solve **Move Zeroes** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Move Zeroes, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Move Zeroes directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_move_zeroes(data):
    """Brute-force baseline for: Move Zeroes."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Move Zeroes to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_move_zeroes(data):
    """Intermediate optimized approach for: Move Zeroes."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Move Zeroes: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_move_zeroes(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q9. Trapping Rain Water

### Problem Statement (Specific)
Solve **Trapping Rain Water** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
- Apply Two Pointers invariant to Trapping Rain Water: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_trapping_rain_water(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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

## Q10. Sort Colors

### Problem Statement (Specific)
Solve **Sort Colors** using **Two Pointers**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sort Colors, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sort Colors directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sort_colors(data):
    """Brute-force baseline for: Sort Colors."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sort Colors to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sort_colors(data):
    """Intermediate optimized approach for: Sort Colors."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Two Pointers invariant to Sort Colors: Each pointer movement should eliminate impossible candidates. When pointers move with monotonic logic, every element is processed a limited number of times.
- Complexity target: Time usually O(n) after sorting, Space O(1) extra (excluding optional sort cost).

#### Optimal Python (Question-Specific)
```python
def solve_sort_colors(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def two_sum_sorted(nums, target):
        left, right = 0, len(nums) - 1
    
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            if s < target:
                left += 1
            else:
                right -= 1
    
        return [-1, -1]
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
