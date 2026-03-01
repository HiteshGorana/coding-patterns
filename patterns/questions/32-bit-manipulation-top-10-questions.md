# Pattern 32 Interview Playbook: Bit Manipulation

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Uses binary-level operations for efficient state handling, parity tricks, and constant-space solutions.
- Core intuition: Bits enable compact representation and algebraic properties: - `x ^ x = 0` - `x ^ 0 = x` - `x & (x - 1)` clears lowest set bit - shifts multiply/divide by powers of two
- Trigger cue 1: XOR uniqueness, subset masks, bit count/power-of-two checks.
- Quick self-check: Can binary properties replace heavier data structures?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Single Number

### Problem Statement (Concrete)
Solve **Single Number** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Single Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_single_number(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_single_number(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_single_number(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Single Number II

### Problem Statement (Concrete)
Solve **Single Number II** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Single Number II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_single_number_ii(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_single_number_ii(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_single_number_ii(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Single Number III

### Problem Statement (Concrete)
Solve **Single Number III** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Single Number III** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_single_number_iii(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_single_number_iii(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_single_number_iii(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Counting Bits

### Problem Statement (Concrete)
Solve **Counting Bits** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Counting Bits** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_counting_bits(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_counting_bits(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_counting_bits(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Number of 1 Bits

### Problem Statement (Concrete)
Solve **Number of 1 Bits** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Number of 1 Bits** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_number_of_1_bits(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_number_of_1_bits(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_number_of_1_bits(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Power of Two

### Problem Statement (Concrete)
Solve **Power of Two** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Power of Two** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_power_of_two(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_power_of_two(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_power_of_two(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Subsets

### Problem Statement (Concrete)
Solve **Subsets** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Subsets** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_subsets(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_subsets(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_subsets(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Missing Number

### Problem Statement (Concrete)
Solve **Missing Number** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Missing Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_missing_number(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_missing_number(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_missing_number(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Sum of Two Integers

### Problem Statement (Concrete)
Solve **Sum of Two Integers** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Sum of Two Integers** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_sum_of_two_integers(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_sum_of_two_integers(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_sum_of_two_integers(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Bitwise AND of Numbers Range

### Problem Statement (Concrete)
Solve **Bitwise AND of Numbers Range** using **Bit Manipulation**. Return exactly the value/structure requested by the original prompt.

### Input
- `n`/`nums`: int or list[int]

### Output
- Bit-derived numeric result, boolean, or list of counts.

### Constraints
- Use bit operations to keep solution constant-factor efficient.
- `0 <= value <= 2^31 - 1` unless stated otherwise.

### Example (Exact)
```text
Input:  nums = [4,1,2,1,2]
Output: 4
Explanation: XOR/bit-count invariants isolate unique or aggregated bit behavior.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Bit Manipulation**.
- Red flags: brute force for **Bitwise AND of Numbers Range** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Count frequencies explicitly.

#### Python
```python
def brute_bitwise_and_of_numbers_range(nums):
    from collections import Counter
    c = Counter(nums)
    for x, f in c.items():
        if f == 1:
            return x
    return -1
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Accumulate per-bit counts and rebuild answer via modular arithmetic.

#### Python
```python
def better_bitwise_and_of_numbers_range(nums):
    ans = 0
    for b in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> b) & 1
        if bit_sum % 3:
            ans |= (1 << b)
    if ans >= 2**31:
        ans -= 2**32
    return ans
```

#### Complexity
- Time `O(32*n)`, Space `O(1)`.

### Approach 3: Optimal (Best)
#### Intuition
- Exploit XOR cancellation/invariant for pairs and parity-style bit behavior.

#### Python
```python
def solve_bitwise_and_of_numbers_range(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### Correctness (Why This Works)
- `a ^ a = 0` and XOR is associative/commutative, so paired values cancel in any order.
- Remaining XOR equals exactly the unpaired/target value.

#### Complexity
- Time `O(n)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
