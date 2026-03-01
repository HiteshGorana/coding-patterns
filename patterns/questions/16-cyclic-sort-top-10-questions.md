# Pattern 16 Interview Playbook: Cyclic Sort

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Cyclic sort places numbers into their correct indices when values are from a known range.
- Core intuition: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Trigger cue 1: Array values in bounded range `0..n` or `1..n`.
- Trigger cue 2: Missing/duplicate/corrupt numbers.
- Quick self-check: Is there a natural correct index for each value?
- Target complexity: Time O(n) (each swap places at least one element correctly), Space O(1)

---

## Q1. Missing Number

### Problem Statement (Specific)
Solve **Missing Number** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Missing Number, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Missing Number directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_missing_number(data):
    """Brute-force baseline for: Missing Number."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Missing Number to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_missing_number(data):
    """Intermediate optimized approach for: Missing Number."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Missing Number: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_missing_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q2. Find All Numbers Disappeared in an Array

### Problem Statement (Specific)
Solve **Find All Numbers Disappeared in an Array** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find All Numbers Disappeared in an Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find All Numbers Disappeared in an Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_all_numbers_disappeared_in_an_array(data):
    """Brute-force baseline for: Find All Numbers Disappeared in an Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find All Numbers Disappeared in an Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_all_numbers_disappeared_in_an_array(data):
    """Intermediate optimized approach for: Find All Numbers Disappeared in an Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Find All Numbers Disappeared in an Array: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_all_numbers_disappeared_in_an_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q3. Set Mismatch

### Problem Statement (Specific)
Solve **Set Mismatch** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Set Mismatch, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Set Mismatch directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_set_mismatch(data):
    """Brute-force baseline for: Set Mismatch."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Set Mismatch to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_set_mismatch(data):
    """Intermediate optimized approach for: Set Mismatch."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Set Mismatch: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_set_mismatch(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q4. Find the Duplicate Number

### Problem Statement (Specific)
Solve **Find the Duplicate Number** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find the Duplicate Number, maintain pattern invariant while scanning once.
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
- Apply Cyclic Sort invariant to Find the Duplicate Number: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_the_duplicate_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q5. First Missing Positive

### Problem Statement (Specific)
Solve **First Missing Positive** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For First Missing Positive, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for First Missing Positive directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_first_missing_positive(data):
    """Brute-force baseline for: First Missing Positive."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for First Missing Positive to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_first_missing_positive(data):
    """Intermediate optimized approach for: First Missing Positive."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to First Missing Positive: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_first_missing_positive(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q6. Find All Duplicates in an Array

### Problem Statement (Specific)
Solve **Find All Duplicates in an Array** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find All Duplicates in an Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find All Duplicates in an Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_all_duplicates_in_an_array(data):
    """Brute-force baseline for: Find All Duplicates in an Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find All Duplicates in an Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_all_duplicates_in_an_array(data):
    """Intermediate optimized approach for: Find All Duplicates in an Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Find All Duplicates in an Array: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_all_duplicates_in_an_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q7. Find the Corrupt Pair

### Problem Statement (Specific)
Solve **Find the Corrupt Pair** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find the Corrupt Pair, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find the Corrupt Pair directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_the_corrupt_pair(data):
    """Brute-force baseline for: Find the Corrupt Pair."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find the Corrupt Pair to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_the_corrupt_pair(data):
    """Intermediate optimized approach for: Find the Corrupt Pair."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Find the Corrupt Pair: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_the_corrupt_pair(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q8. Cyclically Sort an Array

### Problem Statement (Specific)
Solve **Cyclically Sort an Array** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Cyclically Sort an Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Cyclically Sort an Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_cyclically_sort_an_array(data):
    """Brute-force baseline for: Cyclically Sort an Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Cyclically Sort an Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_cyclically_sort_an_array(data):
    """Intermediate optimized approach for: Cyclically Sort an Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Cyclically Sort an Array: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_cyclically_sort_an_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q9. Find Missing Number in 1..n

### Problem Statement (Specific)
Solve **Find Missing Number in 1..n** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find Missing Number in 1..n, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find Missing Number in 1..n directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_missing_number_in_1_n(data):
    """Brute-force baseline for: Find Missing Number in 1..n."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find Missing Number in 1..n to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_missing_number_in_1_n(data):
    """Intermediate optimized approach for: Find Missing Number in 1..n."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Find Missing Number in 1..n: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_missing_number_in_1_n(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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

## Q10. Find Smallest Missing Positive

### Problem Statement (Specific)
Solve **Find Smallest Missing Positive** using **Cyclic Sort**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find Smallest Missing Positive, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find Smallest Missing Positive directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_smallest_missing_positive(data):
    """Brute-force baseline for: Find Smallest Missing Positive."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find Smallest Missing Positive to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_smallest_missing_positive(data):
    """Intermediate optimized approach for: Find Smallest Missing Positive."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Cyclic Sort invariant to Find Smallest Missing Positive: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Complexity target: Time O(n) (each swap places at least one element correctly), Space O(1).

#### Optimal Python (Question-Specific)
```python
def solve_find_smallest_missing_positive(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def find_missing(nums):
        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if 0 <= x < n and nums[i] != nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
            else:
                i += 1
    
        for i, x in enumerate(nums):
            if i != x:
                return i
        return n
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
