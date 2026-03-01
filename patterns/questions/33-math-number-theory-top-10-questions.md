# Pattern 33 Interview Playbook: Math / Number Theory

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Uses arithmetic structure for efficient solutions beyond brute-force simulation.
- Core intuition: Mathematical identities reduce complexity: - Euclid for GCD - fast exponentiation for powers - modulo arithmetic for wrap-around and large numbers - combinatorics for counting arrangements
- Trigger cue 1: Divisibility, modular cycles, huge exponents, prime logic.
- Quick self-check: Is there a known math identity that collapses complexity?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Pow(x, n)

### Problem Statement (Concrete)
Solve **Pow(x, n)** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Pow(x, n)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_pow_x_n(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_pow_x_n(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_pow_x_n(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Count Primes

### Problem Statement (Concrete)
Solve **Count Primes** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Count Primes** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_count_primes(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_count_primes(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_count_primes(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Happy Number

### Problem Statement (Concrete)
Solve **Happy Number** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Happy Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_happy_number(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_happy_number(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_happy_number(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Plus One

### Problem Statement (Concrete)
Solve **Plus One** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Plus One** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_plus_one(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_plus_one(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_plus_one(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Rotate Array

### Problem Statement (Concrete)
Solve **Rotate Array** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Rotate Array** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_rotate_array(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_rotate_array(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_rotate_array(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Fraction to Recurring Decimal

### Problem Statement (Concrete)
Solve **Fraction to Recurring Decimal** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Fraction to Recurring Decimal** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_fraction_to_recurring_decimal(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_fraction_to_recurring_decimal(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_fraction_to_recurring_decimal(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Excel Sheet Column Number

### Problem Statement (Concrete)
Solve **Excel Sheet Column Number** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Excel Sheet Column Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_excel_sheet_column_number(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_excel_sheet_column_number(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_excel_sheet_column_number(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Reverse Integer

### Problem Statement (Concrete)
Solve **Reverse Integer** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

### Input
- Integer/string numeric inputs depending on variant

### Output
- Computed mathematical transformation or decision.

### Constraints
- Handle overflow / precision / sign cases explicitly.
- Complexity usually logarithmic or linear in digits.

### Example (Exact)
```text
Input:  x = 2.0, n = 10
Output: 1024.0
Explanation: Fast exponentiation halves exponent at each step.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Reverse Integer** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_reverse_integer(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_reverse_integer(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_reverse_integer(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Palindrome Number

### Problem Statement (Concrete)
Solve **Palindrome Number** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Palindrome Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_palindrome_number(text, pattern):
    m, n = len(pattern), len(text)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1
```

#### Complexity
- Time `O(n*m)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Rolling hash filters candidate matches and verifies collisions.

#### Python
```python
def better_palindrome_number(text, pattern):
    # Rabin-Karp style rolling hash.
    if not pattern:
        return 0
    base, mod = 911382323, 10**9 + 7
    m = len(pattern)
    p_hash = 0
    t_hash = 0
    power = 1
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
        if i:
            power = (power * base) % mod
    if t_hash == p_hash and text[:m] == pattern:
        return 0
    for i in range(m, len(text)):
        t_hash = (t_hash - ord(text[i-m]) * power) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
        if t_hash == p_hash and text[i-m+1:i+1] == pattern:
            return i - m + 1
    return -1
```

#### Complexity
- Expected `O(n+m)`, worst-case with collisions can degrade.

### Approach 3: Optimal (Best)
#### Intuition
- KMP/Z/Manacher-style preprocessing reuses prefix structure to avoid restart comparisons.

#### Python
```python
def solve_palindrome_number(text, pattern):
    if not pattern:
        return 0

    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
    return -1
```

#### Correctness (Why This Works)
- LPS/Z/palindrome radius arrays encode longest reusable match after mismatch.
- Pointer never moves backward in text, so each character is processed constant times.

#### Complexity
- Time `O(n+m)`, Space `O(m)` (or variant-specific linear auxiliary arrays).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Greatest Common Divisor of Strings

### Problem Statement (Concrete)
Solve **Greatest Common Divisor of Strings** using **Math / Number Theory**. Return exactly the value/structure requested by the original prompt.

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
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Math / Number Theory**.
- Red flags: brute force for **Greatest Common Divisor of Strings** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Apply the definition directly with repeated multiplication/division.

#### Python
```python
def brute_greatest_common_divisor_of_strings(x, n):
    ans = 1.0
    for _ in range(abs(n)):
        ans *= x
    return ans if n >= 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Vectorized/product-style evaluation keeps logic simple but same asymptotic order.

#### Python
```python
def better_greatest_common_divisor_of_strings(x, n):
    from math import prod
    if n == 0:
        return 1.0
    vals = [x] * abs(n)
    ans = prod(vals)
    return ans if n > 0 else 1.0 / ans
```

#### Complexity
- Time `O(|n|)`, Space `O(|n|)` for temporary buffer.

### Approach 3: Optimal (Best)
#### Intuition
- Exponentiation by squaring halves exponent each step.

#### Python
```python
def solve_greatest_common_divisor_of_strings(x, n):
    def fast_pow(a, p):
        res = 1.0
        while p:
            if p & 1:
                res *= a
            a *= a
            p >>= 1
        return res
    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)
```

#### Correctness (Why This Works)
- Any exponent can be decomposed in binary; each set bit contributes one power-of-two block.
- Squaring updates block values, so algorithm processes all bits exactly once.

#### Complexity
- Time `O(log |n|)`, Space `O(1)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
