# Pattern 32 Interview Playbook: Bit Manipulation

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Uses binary-level operations for efficient state handling, parity tricks, and constant-space solutions.
- Core intuition: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Trigger cue 1: XOR uniqueness, subset masks, bit count/power-of-two checks.
- Quick self-check: Can binary properties replace heavier data structures?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Single Number

### Problem Statement (Specific)
Solve **Single Number** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- Unique element under XOR-style frequency condition.

### Constraints (Typical)
- 1 <= len(nums) <= 1e5

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR cancels paired values.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Single Number directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_single_number(data):
    """Brute-force baseline for: Single Number."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Single Number to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_single_number(data):
    """Intermediate optimized approach for: Single Number."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Single Number: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_single_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q2. Single Number II

### Problem Statement (Specific)
Solve **Single Number II** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- Unique element under XOR-style frequency condition.

### Constraints (Typical)
- 1 <= len(nums) <= 1e5

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR cancels paired values.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Single Number II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_single_number_ii(data):
    """Brute-force baseline for: Single Number II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Single Number II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_single_number_ii(data):
    """Intermediate optimized approach for: Single Number II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Single Number II: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_single_number_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q3. Single Number III

### Problem Statement (Specific)
Solve **Single Number III** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]

### Output
- Unique element under XOR-style frequency condition.

### Constraints (Typical)
- 1 <= len(nums) <= 1e5

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR cancels paired values.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Single Number III directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_single_number_iii(data):
    """Brute-force baseline for: Single Number III."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Single Number III to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_single_number_iii(data):
    """Intermediate optimized approach for: Single Number III."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Single Number III: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_single_number_iii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q4. Counting Bits

### Problem Statement (Specific)
Solve **Counting Bits** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int] or integer bit values

### Output
- Bit-derived numeric result.

### Constraints (Typical)
- Use O(n) scans with O(1) bit ops

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: For Counting Bits, apply XOR/mask identities.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Counting Bits directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_counting_bits(data):
    """Brute-force baseline for: Counting Bits."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Counting Bits to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_counting_bits(data):
    """Intermediate optimized approach for: Counting Bits."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Counting Bits: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_counting_bits(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q5. Number of 1 Bits

### Problem Statement (Specific)
Solve **Number of 1 Bits** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int] or integer bit values

### Output
- Bit-derived numeric result.

### Constraints (Typical)
- Use O(n) scans with O(1) bit ops

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: For Number of 1 Bits, apply XOR/mask identities.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Number of 1 Bits directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_1_bits(data):
    """Brute-force baseline for: Number of 1 Bits."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of 1 Bits to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_1_bits(data):
    """Intermediate optimized approach for: Number of 1 Bits."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Number of 1 Bits: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_number_of_1_bits(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q6. Power of Two

### Problem Statement (Specific)
Solve **Power of Two** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `x`: float
- `n`: int

### Output
- x raised to n.

### Constraints (Typical)
- -100 <= x <= 100
- -2^31 <= n <= 2^31-1

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Exponentiation by squaring runs in O(log n).
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Power of Two directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_power_of_two(data):
    """Brute-force baseline for: Power of Two."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Power of Two to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_power_of_two(data):
    """Intermediate optimized approach for: Power of Two."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Power of Two: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_power_of_two(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q7. Subsets

### Problem Statement (Specific)
Solve **Subsets** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

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
- Apply Bit Manipulation invariant to Subsets: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_subsets(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q8. Missing Number

### Problem Statement (Specific)
Solve **Missing Number** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int] or integer bit values

### Output
- Bit-derived numeric result.

### Constraints (Typical)
- Use O(n) scans with O(1) bit ops

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: For Missing Number, apply XOR/mask identities.
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
- Apply Bit Manipulation invariant to Missing Number: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_missing_number(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q9. Sum of Two Integers

### Problem Statement (Specific)
Solve **Sum of Two Integers** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int] or integer bit values

### Output
- Bit-derived numeric result.

### Constraints (Typical)
- Use O(n) scans with O(1) bit ops

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: For Sum of Two Integers, apply XOR/mask identities.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sum of Two Integers directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sum_of_two_integers(data):
    """Brute-force baseline for: Sum of Two Integers."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sum of Two Integers to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sum_of_two_integers(data):
    """Intermediate optimized approach for: Sum of Two Integers."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Sum of Two Integers: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_sum_of_two_integers(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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

## Q10. Bitwise AND of Numbers Range

### Problem Statement (Specific)
Solve **Bitwise AND of Numbers Range** using **Bit Manipulation**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int] or integer bit values

### Output
- Bit-derived numeric result.

### Constraints (Typical)
- Use O(n) scans with O(1) bit ops

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: For Bitwise AND of Numbers Range, apply XOR/mask identities.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Bitwise AND of Numbers Range directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_bitwise_and_of_numbers_range(data):
    """Brute-force baseline for: Bitwise AND of Numbers Range."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Bitwise AND of Numbers Range to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_bitwise_and_of_numbers_range(data):
    """Intermediate optimized approach for: Bitwise AND of Numbers Range."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Bit Manipulation invariant to Bitwise AND of Numbers Range: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Complexity target: Time pattern-optimal, Space pattern-optimal.

#### Optimal Python (Question-Specific)
```python
def solve_bitwise_and_of_numbers_range(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def single_number(nums):
        ans = 0
        for x in nums:
            ans ^= x
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
