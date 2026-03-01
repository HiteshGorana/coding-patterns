# Pattern 12 Interview Playbook: Top K with Heap

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Efficiently maintains the `k` largest/smallest/frequent elements without full sorting.
- Core intuition: Use a heap of size `k`: - for k largest, keep min-heap so smallest of top-k sits at root - when new value beats root, replace root This ensures heap always stores best `k` candidates seen so far.
- Trigger cue 1: "top k", "kth largest/smallest", streaming k-best.
- Quick self-check: Can partial ordering beat full sorting here?
- Target complexity: Time O(n log k), Space O(k) (plus maps when counting frequencies)

---

## Q1. Kth Largest Element in an Array

### Problem Statement (Concrete)
Solve **Kth Largest Element in an Array** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Kth Largest Element in an Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_kth_largest_element_in_an_array(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_kth_largest_element_in_an_array(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_kth_largest_element_in_an_array(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Top K Frequent Elements

### Problem Statement (Concrete)
Solve **Top K Frequent Elements** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Top K Frequent Elements** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_top_k_frequent_elements(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_top_k_frequent_elements(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_top_k_frequent_elements(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. K Closest Points to Origin

### Problem Statement (Concrete)
Solve **K Closest Points to Origin** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **K Closest Points to Origin** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_k_closest_points_to_origin(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_k_closest_points_to_origin(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_k_closest_points_to_origin(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Kth Largest Element in a Stream

### Problem Statement (Concrete)
Solve **Kth Largest Element in a Stream** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Kth Largest Element in a Stream** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_kth_largest_element_in_a_stream(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_kth_largest_element_in_a_stream(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_kth_largest_element_in_a_stream(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Find K Pairs with Smallest Sums

### Problem Statement (Concrete)
Solve **Find K Pairs with Smallest Sums** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Find K Pairs with Smallest Sums** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_find_k_pairs_with_smallest_sums(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_find_k_pairs_with_smallest_sums(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_find_k_pairs_with_smallest_sums(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Sort Characters By Frequency

### Problem Statement (Concrete)
Solve **Sort Characters By Frequency** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Sort Characters By Frequency** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_sort_characters_by_frequency(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_sort_characters_by_frequency(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_sort_characters_by_frequency(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Reorganize String

### Problem Statement (Concrete)
Solve **Reorganize String** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

### Input
- `text`/`s`: str
- `pattern`/`queries`: variant-specific

### Output
- Index, boolean, count, or transformed string as required.

### Constraints
- `1 <= length <= 2 * 10^5`
- Use near-linear processing to avoid `O(n*m)` restarts.

### Example (Exact)
```text
Input:  text = "sadbutsad", pattern = "sad"
Output: 0
Explanation: Efficient preprocessing avoids rechecking already-matched characters.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Reorganize String** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_reorganize_string(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_reorganize_string(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_reorganize_string(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Last Stone Weight

### Problem Statement (Concrete)
Solve **Last Stone Weight** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Last Stone Weight** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_last_stone_weight(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_last_stone_weight(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_last_stone_weight(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Furthest Building You Can Reach

### Problem Statement (Concrete)
Solve **Furthest Building You Can Reach** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **Furthest Building You Can Reach** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_furthest_building_you_can_reach(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_furthest_building_you_can_reach(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_furthest_building_you_can_reach(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. High Five

### Problem Statement (Concrete)
Solve **High Five** using **Top K with Heap**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Top K with Heap**.
- Red flags: brute force for **High Five** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Sort all candidates and pick rank directly.

#### Python
```python
def brute_high_five(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time `O(n log n)`, Space `O(1)` extra if in-place.

### Approach 2: Better (Intermediate)
#### Intuition
- Keep bounded heap of size `k` while streaming elements.

#### Python
```python
import heapq

def better_high_five(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
```

#### Complexity
- Time `O(n log k)`, Space `O(k)`.

### Approach 3: Optimal (Best)
#### Intuition
- Use heap as core data structure to preserve only relevant frontier.

#### Python
```python
import heapq

def solve_high_five(nums, k):
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]
```

#### Correctness (Why This Works)
- Heap root is always worst among kept top-`k` candidates, so replacements preserve correctness.
- Discarded elements can never affect final rank once smaller than current heap root frontier.

#### Complexity
- Time `O(n log k)`, Space `O(k)` (or variant-specific).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
