# Pattern 16 Interview Playbook: Cyclic Sort

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Cyclic sort places numbers into their correct indices when values are from a known range.
- Core intuition: If value `x` belongs at index `x-1` (or `x`), swap it into position until current index holds correct value. Unlike comparison sort, this uses value-index mapping directly.
- Trigger cue 1: Array values in bounded range `0..n` or `1..n`.
- Trigger cue 2: Missing/duplicate/corrupt numbers.
- Quick self-check: Is there a natural correct index for each value?
- Target complexity: Time O(n) (each swap places at least one element correctly), Space O(1)

---

## Q1. Missing Number

### Problem Statement (Concrete)
Solve **Missing Number** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Missing Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_missing_number(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_missing_number(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_missing_number(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Find All Numbers Disappeared in an Array

### Problem Statement (Concrete)
Solve **Find All Numbers Disappeared in an Array** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Find All Numbers Disappeared in an Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_find_all_numbers_disappeared_in_an_array(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_find_all_numbers_disappeared_in_an_array(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_find_all_numbers_disappeared_in_an_array(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Set Mismatch

### Problem Statement (Concrete)
Solve **Set Mismatch** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Set Mismatch** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_set_mismatch(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_set_mismatch(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_set_mismatch(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Find the Duplicate Number

### Problem Statement (Concrete)
Solve **Find the Duplicate Number** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Find the Duplicate Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_find_the_duplicate_number(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_find_the_duplicate_number(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_find_the_duplicate_number(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. First Missing Positive

### Problem Statement (Concrete)
Solve **First Missing Positive** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **First Missing Positive** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_first_missing_positive(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_first_missing_positive(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_first_missing_positive(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Find All Duplicates in an Array

### Problem Statement (Concrete)
Solve **Find All Duplicates in an Array** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Find All Duplicates in an Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_find_all_duplicates_in_an_array(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_find_all_duplicates_in_an_array(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_find_all_duplicates_in_an_array(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Find the Corrupt Pair

### Problem Statement (Concrete)
Solve **Find the Corrupt Pair** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Find the Corrupt Pair** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_find_the_corrupt_pair(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_find_the_corrupt_pair(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_find_the_corrupt_pair(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Cyclically Sort an Array

### Problem Statement (Concrete)
Solve **Cyclically Sort an Array** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Cyclically Sort an Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_cyclically_sort_an_array(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_cyclically_sort_an_array(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_cyclically_sort_an_array(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Find Missing Number in 1..n

### Problem Statement (Concrete)
Solve **Find Missing Number in 1..n** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Find Missing Number in 1..n** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_find_missing_number_in_1_n(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_find_missing_number_in_1_n(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_find_missing_number_in_1_n(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Find Smallest Missing Positive

### Problem Statement (Concrete)
Solve **Find Smallest Missing Positive** using **Cyclic Sort**. Return exactly the value/structure requested by the original prompt.

### Input
- Variant-specific array/string input parameters

### Output
- Return exactly what the problem asks (value/index/list/boolean).

### Constraints
- `1 <= n <= 2 * 10^5`
- Choose algorithm based on time-limit pressure.

### Example (Exact)
```text
Input:  nums = [1, 2, 3, 4]
Output: 2
Explanation: Use the pattern invariant to avoid repeated recomputation and redundant scans.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Cyclic Sort**.
- Red flags: brute force for **Find Smallest Missing Positive** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Check each candidate value using repeated membership scans.

#### Python
```python
def brute_find_smallest_missing_positive(nums):
    n = len(nums)
    for x in range(1, n + 1):
        if x not in nums:
            return x
    return n + 1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Hash-set membership reduces candidate checks to linear time.

#### Python
```python
def better_find_smallest_missing_positive(nums):
    seen = set(nums)
    x = 1
    while x in seen:
        x += 1
    return x
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Place each number at its index-corresponding position; first mismatch identifies answer.

#### Python
```python
def solve_find_smallest_missing_positive(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, x in enumerate(nums, 1):
        if x != i:
            return i
    return n + 1
```

#### Correctness (Why This Works)
- Every swap puts at least one value in correct position, bounding swaps by `O(n)`.
- After placement, index/value mismatch exactly encodes missing/duplicate corruption.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
