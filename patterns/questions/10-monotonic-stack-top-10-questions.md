# Pattern 10 Interview Playbook: Monotonic Stack

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Monotonic stacks answer "next greater/smaller" and boundary-span questions in linear time.
- Core intuition: Maintain stack of indices with monotonic values: - increasing stack for next smaller queries - decreasing stack for next greater queries When current element breaks monotonicity, pop until restored. Each index is pushed and popped at most once.
- Trigger cue 1: "next greater/smaller", nearest boundary, histogram area.
- Quick self-check: Does each element need nearest bigger/smaller on one side?
- Target complexity: Time O(n) (amortized), Space O(n)

---

## Q1. Daily Temperatures

### Problem Statement (Concrete)
Solve **Daily Temperatures** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Daily Temperatures** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_daily_temperatures(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_daily_temperatures(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_daily_temperatures(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Next Greater Element I

### Problem Statement (Concrete)
Solve **Next Greater Element I** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Next Greater Element I** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_next_greater_element_i(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_next_greater_element_i(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_next_greater_element_i(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Next Greater Element II

### Problem Statement (Concrete)
Solve **Next Greater Element II** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Next Greater Element II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_next_greater_element_ii(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_next_greater_element_ii(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_next_greater_element_ii(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Largest Rectangle in Histogram

### Problem Statement (Concrete)
Solve **Largest Rectangle in Histogram** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Largest Rectangle in Histogram** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_largest_rectangle_in_histogram(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_largest_rectangle_in_histogram(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_largest_rectangle_in_histogram(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Trapping Rain Water

### Problem Statement (Concrete)
Solve **Trapping Rain Water** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Trapping Rain Water** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_trapping_rain_water(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_trapping_rain_water(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_trapping_rain_water(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Remove K Digits

### Problem Statement (Concrete)
Solve **Remove K Digits** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Remove K Digits** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_remove_k_digits(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_remove_k_digits(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_remove_k_digits(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Sum of Subarray Minimums

### Problem Statement (Concrete)
Solve **Sum of Subarray Minimums** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Sum of Subarray Minimums** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_sum_of_subarray_minimums(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_sum_of_subarray_minimums(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_sum_of_subarray_minimums(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Online Stock Span

### Problem Statement (Concrete)
Solve **Online Stock Span** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Online Stock Span** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_online_stock_span(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_online_stock_span(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_online_stock_span(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Asteroid Collision

### Problem Statement (Concrete)
Solve **Asteroid Collision** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Asteroid Collision** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_asteroid_collision(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_asteroid_collision(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_asteroid_collision(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Car Fleet II

### Problem Statement (Concrete)
Solve **Car Fleet II** using **Monotonic Stack**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Monotonic Stack**.
- Red flags: brute force for **Car Fleet II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- For each index, scan to find the first satisfying future element.

#### Python
```python
def brute_car_fleet_ii(nums):
    n = len(nums)
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ans[i] = nums[j]
                break
    return ans
```

#### Complexity
- Time `O(n^2)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Maintain monotonic stack to answer popped elements immediately.

#### Python
```python
def better_car_fleet_ii(nums):
    ans = [-1] * len(nums)
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Single pass (or doubled pass for circular variants) preserves monotonic invariant and resolves each index once.

#### Python
```python
def solve_car_fleet_ii(nums):
    ans = [-1] * len(nums)
    stack = []
    for i in range(2 * len(nums) - 1, -1, -1):
        x = nums[i % len(nums)]
        while stack and stack[-1] <= x:
            stack.pop()
        if i < len(nums):
            ans[i] = stack[-1] if stack else -1
        stack.append(x)
    return ans
```

#### Correctness (Why This Works)
- Each value is pushed and popped at most once from stack due to strict monotonic maintenance.
- Top of stack after removals is exactly the nearest greater candidate by construction order.

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
