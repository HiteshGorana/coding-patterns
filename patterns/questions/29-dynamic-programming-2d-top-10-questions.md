# Pattern 29 Interview Playbook: Dynamic Programming (2D)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Handles problems where state depends on two indices/dimensions (strings, grids, pair ranges).
- Core intuition: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Trigger cue 1: Two-dimensional state: strings, grids, pair indices.
- Quick self-check: Do I naturally need two coordinates for state?
- Target complexity: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m))

---

## Q1. Unique Paths

### Problem Statement (Specific)
Solve **Unique Paths** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Unique Paths, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Unique Paths directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_unique_paths(data):
    """Brute-force baseline for: Unique Paths."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Unique Paths to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_unique_paths(data):
    """Intermediate optimized approach for: Unique Paths."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Unique Paths: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_unique_paths(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q2. Minimum Path Sum

### Problem Statement (Specific)
Solve **Minimum Path Sum** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Minimum Path Sum, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Path Sum directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_path_sum(data):
    """Brute-force baseline for: Minimum Path Sum."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Path Sum to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_path_sum(data):
    """Intermediate optimized approach for: Minimum Path Sum."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Minimum Path Sum: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_minimum_path_sum(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q3. Edit Distance

### Problem Statement (Specific)
Solve **Edit Distance** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- `word1`: str
- `word2`: str

### Output
- Minimum operations to convert `word1` into `word2`.

### Constraints (Typical)
- 1 <= len(word1), len(word2) <= 500

### Example (Exact)
```text
Input:  word1 = "horse", word2 = "ros"
Output: 3
Explanation: 2D DP compares insert/delete/replace transitions.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Edit Distance directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_edit_distance(data):
    """Brute-force baseline for: Edit Distance."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Edit Distance to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_edit_distance(data):
    """Intermediate optimized approach for: Edit Distance."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Edit Distance: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_edit_distance(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q4. Longest Common Subsequence

### Problem Statement (Specific)
Solve **Longest Common Subsequence** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Longest Common Subsequence, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Longest Common Subsequence directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_longest_common_subsequence(data):
    """Brute-force baseline for: Longest Common Subsequence."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Longest Common Subsequence to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_longest_common_subsequence(data):
    """Intermediate optimized approach for: Longest Common Subsequence."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Longest Common Subsequence: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_longest_common_subsequence(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q5. Distinct Subsequences

### Problem Statement (Specific)
Solve **Distinct Subsequences** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Distinct Subsequences, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Distinct Subsequences directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_distinct_subsequences(data):
    """Brute-force baseline for: Distinct Subsequences."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Distinct Subsequences to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_distinct_subsequences(data):
    """Intermediate optimized approach for: Distinct Subsequences."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Distinct Subsequences: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_distinct_subsequences(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q6. Interleaving String

### Problem Statement (Specific)
Solve **Interleaving String** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Interleaving String, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Interleaving String directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_interleaving_string(data):
    """Brute-force baseline for: Interleaving String."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Interleaving String to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_interleaving_string(data):
    """Intermediate optimized approach for: Interleaving String."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Interleaving String: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_interleaving_string(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q7. Longest Palindromic Subsequence

### Problem Statement (Specific)
Solve **Longest Palindromic Subsequence** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Longest Palindromic Subsequence, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Longest Palindromic Subsequence directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_longest_palindromic_subsequence(data):
    """Brute-force baseline for: Longest Palindromic Subsequence."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Longest Palindromic Subsequence to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_longest_palindromic_subsequence(data):
    """Intermediate optimized approach for: Longest Palindromic Subsequence."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Longest Palindromic Subsequence: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_longest_palindromic_subsequence(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q8. Maximal Square

### Problem Statement (Specific)
Solve **Maximal Square** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Maximal Square, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Maximal Square directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_maximal_square(data):
    """Brute-force baseline for: Maximal Square."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Maximal Square to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_maximal_square(data):
    """Intermediate optimized approach for: Maximal Square."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Maximal Square: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_maximal_square(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q9. Triangle

### Problem Statement (Specific)
Solve **Triangle** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Triangle, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Triangle directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_triangle(data):
    """Brute-force baseline for: Triangle."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Triangle to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_triangle(data):
    """Intermediate optimized approach for: Triangle."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Triangle: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_triangle(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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

## Q10. Dungeon Game

### Problem Statement (Specific)
Solve **Dungeon Game** using **Dynamic Programming (2D)**. Return exactly what the problem asks and justify complexity.

### Input
- State input arrays/strings/targets

### Output
- Optimal value or count of ways.

### Constraints (Typical)
- State-space must remain polynomial

### Example (Exact)
```text
Input:  nums = [2,7,9,3,1]
Output: 12
Explanation: For Dungeon Game, memoized/bottom-up state prevents exponential recursion.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Dungeon Game directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_dungeon_game(data):
    """Brute-force baseline for: Dungeon Game."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Dungeon Game to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_dungeon_game(data):
    """Intermediate optimized approach for: Dungeon Game."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Dynamic Programming (2D) invariant to Dungeon Game: Define a table where each cell stores answer for subproblem `(i, j)`. Transition combines neighboring states according to problem rules.
- Complexity target: Time often O(n*m), Space O(n*m); sometimes reducible to O(min(n,m)).

#### Optimal Python (Question-Specific)
```python
def solve_dungeon_game(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def lcs(a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        return dp[n][m]
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
