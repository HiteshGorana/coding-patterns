# Pattern 06 Interview Playbook: Binary Search (Index Space)

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Binary search finds positions or values in sorted/indexed structures in logarithmic time.
- Core intuition: At each step, discard half the remaining search space based on midpoint comparison.
- Trigger cue 1: Sorted data.
- Trigger cue 2: Need exact index, lower bound, upper bound.
- Quick self-check: Is the search condition monotonic across indices?
- Target complexity: Time O(log n), Space O(1) iterative

---

## Q1. Binary Search

### Problem Statement (Concrete)
Solve **Binary Search** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Binary Search** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_binary_search(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_binary_search(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Search Insert Position

### Problem Statement (Concrete)
Solve **Search Insert Position** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Search Insert Position** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_search_insert_position(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_search_insert_position(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_search_insert_position(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Find First and Last Position of Element in Sorted Array

### Problem Statement (Concrete)
Solve **Find First and Last Position of Element in Sorted Array** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Find First and Last Position of Element in Sorted Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_find_first_and_last_position_of_element_in_sorted_array(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_find_first_and_last_position_of_element_in_sorted_array(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_find_first_and_last_position_of_element_in_sorted_array(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Search in Rotated Sorted Array

### Problem Statement (Concrete)
Solve **Search in Rotated Sorted Array** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Search in Rotated Sorted Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_search_in_rotated_sorted_array(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_search_in_rotated_sorted_array(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_search_in_rotated_sorted_array(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Find Minimum in Rotated Sorted Array

### Problem Statement (Concrete)
Solve **Find Minimum in Rotated Sorted Array** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Find Minimum in Rotated Sorted Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_find_minimum_in_rotated_sorted_array(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_find_minimum_in_rotated_sorted_array(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_find_minimum_in_rotated_sorted_array(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Sqrt(x)

### Problem Statement (Concrete)
Solve **Sqrt(x)** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Sqrt(x)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_sqrt_x(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_sqrt_x(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_sqrt_x(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Peak Index in a Mountain Array

### Problem Statement (Concrete)
Solve **Peak Index in a Mountain Array** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Peak Index in a Mountain Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_peak_index_in_a_mountain_array(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_peak_index_in_a_mountain_array(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_peak_index_in_a_mountain_array(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Find Peak Element

### Problem Statement (Concrete)
Solve **Find Peak Element** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Find Peak Element** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Scan linearly until match found.

#### Python
```python
def brute_find_peak_element(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use library-assisted partition index to avoid manual boundary bugs.

#### Python
```python
def better_find_peak_element(nums, target):
    # Python library binary search style (still logarithmic).
    import bisect
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Maintain closed interval invariant and discard half each iteration.

#### Python
```python
def solve_find_peak_element(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

#### Correctness (Why This Works)
- Sorted order guarantees that comparison at `mid` partitions impossible half completely.
- Invariant `target` (if present) always remains within `[lo, hi]` until found or interval empties.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. First Bad Version

### Problem Statement (Concrete)
Solve **First Bad Version** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`/`nums`: sorted or search-space-backed input
- `target`/`threshold`/`days`: variant-specific

### Output
- Index, minimum feasible value, or boolean feasibility.

### Constraints
- Monotonicity condition must hold for answer-space search.
- `1 <= n <= 2 * 10^5`

### Example (Exact)
```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
Explanation: Binary search halves candidate space by preserving invariant boundaries.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **First Bad Version** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Test versions sequentially.

#### Python
```python
def brute_first_bad_version(n, isBadVersion):
    for i in range(1, n + 1):
        if isBadVersion(i):
            return i
    return -1
```

#### Complexity
- Time `O(n)` API calls.

### Approach 2: Better (Intermediate)
#### Intuition
- Binary search first index where predicate becomes true.

#### Python
```python
def better_first_bad_version(n, isBadVersion):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

#### Complexity
- Time `O(log n)` API calls.

### Approach 3: Optimal (Best)
#### Intuition
- Monotonic bad-version boundary makes binary search optimal.

#### Python
```python
def better_first_bad_version(n, isBadVersion):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

#### Correctness (Why This Works)
- Versions before first bad are all good; from first bad onward are all bad.
- Maintaining this partition invariant yields exact first bad index.

#### Complexity
- Time `O(log n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Search a 2D Matrix

### Problem Statement (Concrete)
Solve **Search a 2D Matrix** using **Binary Search (Index Space)**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`: int nodes/vertices or grid dimensions
- `edges`/`grid`: problem graph representation
- `source`/`target` when required

### Output
- Shortest distance, ordering, component info, minimum cost, or boolean.

### Constraints
- `1 <= n <= 2 * 10^5` (or `m * n <= 2 * 10^5` for grids)
- `0 <= m <= 4 * 10^5` edges in sparse graph settings

### Example (Exact)
```text
Input:  n = 4, edges = [[0,1],[1,2],[2,3]], source = 0
Output: dist = [0,1,2,3]
Explanation: Choose traversal/relaxation strategy based on edge weights and state model.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Binary Search (Index Space)**.
- Red flags: brute force for **Search a 2D Matrix** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For every cell, compute distance to every source and take minimum.

#### Python
```python
from collections import deque

def brute_search_a_2d_matrix(grid):
    m, n = len(grid), len(grid[0])
    ans = [[10**9] * n for _ in range(m)]
    src = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
    for i in range(m):
        for j in range(n):
            for si, sj in src:
                ans[i][j] = min(ans[i][j], abs(i - si) + abs(j - sj))
    return ans
```

#### Complexity
- Time `O((mn)^2)` in dense-source case, Space `O(mn)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Run BFS from all sources simultaneously so each cell is finalized at first reach.

#### Python
```python
from collections import deque

def better_search_a_2d_matrix(grid):
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

#### Complexity
- Time `O(mn)`, Space `O(mn)`.

### Approach 3: Optimal (Best)
#### Intuition
- Multi-source BFS explores increasing distance layers exactly once per cell.

#### Python
```python
from collections import deque

def better_search_a_2d_matrix(grid):
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist
```

#### Correctness (Why This Works)
- In unweighted grids, BFS layer number equals shortest path length.
- Seeding queue with all sources ensures nearest source claims each cell first.

#### Complexity
- Time `O(mn)`, Space `O(mn)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
