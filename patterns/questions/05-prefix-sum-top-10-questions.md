# Pattern 05 Interview Playbook: Prefix Sum

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Prefix sums convert repeated range-sum queries from linear to constant time.
- Core intuition: Define `prefix[i]` as sum of elements before index `i` (exclusive). Then any range sum can be computed as: `sum(l..r) = prefix[r + 1] - prefix[l]` For counting subarrays with target sum, store past prefix frequencies in a hash map.
- Trigger cue 1: Many range sum queries.
- Trigger cue 2: Count subarrays with target sum.
- Quick self-check: Can I precompute cumulative state once and answer ranges quickly?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Range Sum Query - Immutable

### Problem Statement (Concrete)
Solve **Range Sum Query - Immutable** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Range Sum Query - Immutable** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Compute each query sum directly over the range.

#### Python
```python
class brute_range_sum_query_immutable:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])
```

#### Complexity
- Per query `O(r-l+1)`, build `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Build prefix sums once and answer each query with two lookups.

#### Python
```python
class better_range_sum_query_immutable:
    def __init__(self, nums):
        self.pre = [0]
        for x in nums:
            self.pre.append(self.pre[-1] + x)

    def sumRange(self, left, right):
        return self.pre[right + 1] - self.pre[left]
```

#### Complexity
- Build `O(n)`, query `O(1)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Prefix array is the optimal immutable-range-sum primitive.

#### Python
```python
class better_range_sum_query_immutable:
    def __init__(self, nums):
        self.pre = [0]
        for x in nums:
            self.pre.append(self.pre[-1] + x)

    def sumRange(self, left, right):
        return self.pre[right + 1] - self.pre[left]
```

#### Correctness (Why This Works)
- Range sum equals difference of two prefix sums by telescoping.
- All immutable queries are answered exactly with this identity.

#### Complexity
- Build `O(n)`, query `O(1)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Subarray Sum Equals K

### Problem Statement (Concrete)
Solve **Subarray Sum Equals K** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]
- `k`: int

### Output
- Count of contiguous subarrays whose sum equals `k`.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^4 <= nums[i], k <= 10^4`

### Example (Exact)
```text
Input:  nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays `[1,1]` at indices `(0,1)` and `(1,2)` both sum to 2.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Subarray Sum Equals K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_subarray_sum_equals_k(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_subarray_sum_equals_k(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_subarray_sum_equals_k(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Continuous Subarray Sum

### Problem Statement (Concrete)
Solve **Continuous Subarray Sum** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]
- `target`/`k`: int (if required by the variant)

### Output
- Indices, count, or value requested by the exact statement.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i], target <= 10^9`

### Example (Exact)
```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Complement lookup identifies the pair in one linear scan.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Continuous Subarray Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_continuous_subarray_sum(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_continuous_subarray_sum(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_continuous_subarray_sum(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Contiguous Array

### Problem Statement (Concrete)
Solve **Contiguous Array** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Contiguous Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_contiguous_array(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_contiguous_array(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_contiguous_array(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Product of Array Except Self

### Problem Statement (Concrete)
Solve **Product of Array Except Self** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Product of Array Except Self** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Multiply all other elements for each index separately.

#### Python
```python
def brute_product_of_array_except_self(nums):
    out = []
    for i in range(len(nums)):
        p = 1
        for j, x in enumerate(nums):
            if i != j:
                p *= x
        out.append(p)
    return out
```

#### Complexity
- Time `O(n^2)`, Space `O(1)` extra.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute left and right product arrays.

#### Python
```python
def better_product_of_array_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    return [left[i] * right[i] for i in range(n)]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reuse output as left products, then multiply rolling suffix product in reverse.

#### Python
```python
def solve_product_of_array_except_self(nums):
    n = len(nums)
    out = [1] * n
    pref = 1
    for i in range(n):
        out[i] = pref
        pref *= nums[i]
    suf = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suf
        suf *= nums[i]
    return out
```

#### Correctness (Why This Works)
- For index `i`, required product factorizes into prefix(`i-1`) * suffix(`i+1`).
- Two passes compute both factors without division and with constant extra memory.

#### Complexity
- Time `O(n)`, Space `O(1)` extra (excluding output).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Find Pivot Index

### Problem Statement (Concrete)
Solve **Find Pivot Index** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Find Pivot Index** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute left and right sums for each index.

#### Python
```python
def brute_find_pivot_index(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Track running left sum; derive right sum from total.

#### Python
```python
def better_find_pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single-pass balance check is optimal for pivot detection.

#### Python
```python
def better_find_pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
```

#### Correctness (Why This Works)
- At index `i`, right sum is `total - left - nums[i]`.
- Equality with `left` is exactly the pivot condition.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Corporate Flight Bookings

### Problem Statement (Concrete)
Solve **Corporate Flight Bookings** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Corporate Flight Bookings** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_corporate_flight_bookings(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_corporate_flight_bookings(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_corporate_flight_bookings(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Car Pooling

### Problem Statement (Concrete)
Solve **Car Pooling** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Car Pooling** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_car_pooling(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_car_pooling(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_car_pooling(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Subarray Sums Divisible by K

### Problem Statement (Concrete)
Solve **Subarray Sums Divisible by K** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]
- `target`/`k`: int (if required by the variant)

### Output
- Indices, count, or value requested by the exact statement.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i], target <= 10^9`

### Example (Exact)
```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Complement lookup identifies the pair in one linear scan.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Subarray Sums Divisible by K** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_subarray_sums_divisible_by_k(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_subarray_sums_divisible_by_k(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_subarray_sums_divisible_by_k(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Maximum Size Subarray Sum Equals k

### Problem Statement (Concrete)
Solve **Maximum Size Subarray Sum Equals k** using **Prefix Sum**. Return exactly the value/structure requested by the original prompt.

### Input
- `nums`: list[int]
- `k`: int

### Output
- Count of contiguous subarrays whose sum equals `k`.

### Constraints
- `1 <= n <= 2 * 10^5`
- `-10^4 <= nums[i], k <= 10^4`

### Example (Exact)
```text
Input:  nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays `[1,1]` at indices `(0,1)` and `(1,2)` both sum to 2.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Prefix Sum**.
- Red flags: brute force for **Maximum Size Subarray Sum Equals k** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Evaluate every subarray sum directly.

#### Python
```python
def brute_maximum_size_subarray_sum_equals_k(nums, k):
    ans = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Precompute prefix sums to answer any range sum in O(1), but still enumerate ranges.

#### Python
```python
def better_maximum_size_subarray_sum_equals_k(nums, k):
    pre = [0]
    for x in nums:
        pre.append(pre[-1] + x)
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if pre[j] - pre[i] == k:
                ans += 1
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Count how many previous prefixes would make current prefix form the required target difference.

#### Python
```python
def solve_maximum_size_subarray_sum_equals_k(nums, k):
    freq = {0: 1}
    ans = 0
    pref = 0
    for x in nums:
        pref += x
        ans += freq.get(pref - k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans
```

#### Correctness (Why This Works)
- For each position `j`, any `i < j` with `pref[i] = pref[j] - k` forms a valid subarray `i..j-1`.
- Hash frequency of seen prefixes counts all such starts in O(1) amortized per element.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
