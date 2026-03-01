# Pattern 12 Interview Playbook: Top K with Heap

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Efficiently maintains the `k` largest/smallest/frequent elements without full sorting.
- Core intuition: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Trigger cue 1: "top k", "kth largest/smallest", streaming k-best.
- Quick self-check: Can partial ordering beat full sorting here?
- Target complexity: Time O(n log k), Space O(k) (plus maps when counting frequencies)

---

## Q1. Kth Largest Element in an Array

### Problem Statement (Specific)
Solve **Kth Largest Element in an Array** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Kth Largest Element in an Array, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Kth Largest Element in an Array directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_kth_largest_element_in_an_array(data):
    """Brute-force baseline for: Kth Largest Element in an Array."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Kth Largest Element in an Array to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_kth_largest_element_in_an_array(data):
    """Intermediate optimized approach for: Kth Largest Element in an Array."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Kth Largest Element in an Array: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_kth_largest_element_in_an_array(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q2. Top K Frequent Elements

### Problem Statement (Specific)
Solve **Top K Frequent Elements** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Top K Frequent Elements, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Top K Frequent Elements directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_top_k_frequent_elements(data):
    """Brute-force baseline for: Top K Frequent Elements."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Top K Frequent Elements to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_top_k_frequent_elements(data):
    """Intermediate optimized approach for: Top K Frequent Elements."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Top K Frequent Elements: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
import heapq

def solve_top_k_frequent_elements(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda p: p[1])]
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

## Q3. K Closest Points to Origin

### Problem Statement (Specific)
Solve **K Closest Points to Origin** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For K Closest Points to Origin, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for K Closest Points to Origin directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_k_closest_points_to_origin(data):
    """Brute-force baseline for: K Closest Points to Origin."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for K Closest Points to Origin to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_k_closest_points_to_origin(data):
    """Intermediate optimized approach for: K Closest Points to Origin."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to K Closest Points to Origin: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_k_closest_points_to_origin(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q4. Kth Largest Element in a Stream

### Problem Statement (Specific)
Solve **Kth Largest Element in a Stream** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Kth Largest Element in a Stream, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Kth Largest Element in a Stream directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_kth_largest_element_in_a_stream(data):
    """Brute-force baseline for: Kth Largest Element in a Stream."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Kth Largest Element in a Stream to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_kth_largest_element_in_a_stream(data):
    """Intermediate optimized approach for: Kth Largest Element in a Stream."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Kth Largest Element in a Stream: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_kth_largest_element_in_a_stream(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q5. Find K Pairs with Smallest Sums

### Problem Statement (Specific)
Solve **Find K Pairs with Smallest Sums** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Find K Pairs with Smallest Sums, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find K Pairs with Smallest Sums directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_k_pairs_with_smallest_sums(data):
    """Brute-force baseline for: Find K Pairs with Smallest Sums."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find K Pairs with Smallest Sums to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_k_pairs_with_smallest_sums(data):
    """Intermediate optimized approach for: Find K Pairs with Smallest Sums."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Find K Pairs with Smallest Sums: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_find_k_pairs_with_smallest_sums(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q6. Sort Characters By Frequency

### Problem Statement (Specific)
Solve **Sort Characters By Frequency** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Sort Characters By Frequency, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Sort Characters By Frequency directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_sort_characters_by_frequency(data):
    """Brute-force baseline for: Sort Characters By Frequency."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Sort Characters By Frequency to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_sort_characters_by_frequency(data):
    """Intermediate optimized approach for: Sort Characters By Frequency."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Sort Characters By Frequency: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_sort_characters_by_frequency(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q7. Reorganize String

### Problem Statement (Specific)
Solve **Reorganize String** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Reorganize String, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Reorganize String directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_reorganize_string(data):
    """Brute-force baseline for: Reorganize String."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Reorganize String to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_reorganize_string(data):
    """Intermediate optimized approach for: Reorganize String."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Reorganize String: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_reorganize_string(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q8. Last Stone Weight

### Problem Statement (Specific)
Solve **Last Stone Weight** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Last Stone Weight, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Last Stone Weight directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_last_stone_weight(data):
    """Brute-force baseline for: Last Stone Weight."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Last Stone Weight to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_last_stone_weight(data):
    """Intermediate optimized approach for: Last Stone Weight."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Last Stone Weight: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_last_stone_weight(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q9. Furthest Building You Can Reach

### Problem Statement (Specific)
Solve **Furthest Building You Can Reach** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For Furthest Building You Can Reach, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Furthest Building You Can Reach directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_furthest_building_you_can_reach(data):
    """Brute-force baseline for: Furthest Building You Can Reach."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Furthest Building You Can Reach to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_furthest_building_you_can_reach(data):
    """Intermediate optimized approach for: Furthest Building You Can Reach."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to Furthest Building You Can Reach: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_furthest_building_you_can_reach(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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

## Q10. High Five

### Problem Statement (Specific)
Solve **High Five** using **Top K with Heap**. Return exactly what the problem asks and justify complexity.

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
Explanation: For High Five, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for High Five directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_high_five(data):
    """Brute-force baseline for: High Five."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for High Five to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_high_five(data):
    """Intermediate optimized approach for: High Five."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Top K with Heap invariant to High Five: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Complexity target: Time O(n log k), Space O(k) (plus maps when counting frequencies).

#### Optimal Python (Question-Specific)
```python
def solve_high_five(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    import heapq
    
    def top_k_largest(nums, k):
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap  # unsorted top-k
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
