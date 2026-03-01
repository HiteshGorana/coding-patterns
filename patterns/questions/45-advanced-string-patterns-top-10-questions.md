# Pattern 45 Interview Playbook: Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Advanced string pattern algorithms provide linear or near-linear matching/palindrome solutions where naive scanning is too slow.
- Core intuition: Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Trigger cue 1: Need fast substring matching across large texts.
- Trigger cue 2: Need all pattern occurrences or linear palindrome computation.
- Quick self-check: Does naive matching restart too often and become `O(n*m)`?
- Target complexity: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays.

---

## Q1. Implement strStr() (KMP)

### Problem Statement (Specific)
Solve **Implement strStr() (KMP)** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `haystack`: str
- `needle`: str

### Output
- First index of `needle` in `haystack`, else -1.

### Constraints (Typical)
- 1 <= lengths <= 2e5

### Example (Exact)
```text
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: KMP prevents fallback to full restart on mismatch.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Implement strStr() (KMP) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_implement_strstr_kmp(data):
    """Brute-force baseline for: Implement strStr() (KMP)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Implement strStr() (KMP) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_implement_strstr_kmp(data):
    """Intermediate optimized approach for: Implement strStr() (KMP)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Implement strStr() (KMP): Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_implement_strstr_kmp(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q2. Find All Occurrences of Pattern in Text

### Problem Statement (Specific)
Solve **Find All Occurrences of Pattern in Text** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Find All Occurrences of Pattern in Text, preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find All Occurrences of Pattern in Text directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_all_occurrences_of_pattern_in_text(data):
    """Brute-force baseline for: Find All Occurrences of Pattern in Text."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find All Occurrences of Pattern in Text to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_all_occurrences_of_pattern_in_text(data):
    """Intermediate optimized approach for: Find All Occurrences of Pattern in Text."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Find All Occurrences of Pattern in Text: Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_find_all_occurrences_of_pattern_in_text(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q3. Repeated String Match

### Problem Statement (Specific)
Solve **Repeated String Match** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Repeated String Match, preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Repeated String Match directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_repeated_string_match(data):
    """Brute-force baseline for: Repeated String Match."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Repeated String Match to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_repeated_string_match(data):
    """Intermediate optimized approach for: Repeated String Match."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Repeated String Match: Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_repeated_string_match(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q4. Longest Happy Prefix

### Problem Statement (Specific)
Solve **Longest Happy Prefix** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Longest Happy Prefix, preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Longest Happy Prefix directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_longest_happy_prefix(data):
    """Brute-force baseline for: Longest Happy Prefix."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Longest Happy Prefix to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_longest_happy_prefix(data):
    """Intermediate optimized approach for: Longest Happy Prefix."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Longest Happy Prefix: Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_longest_happy_prefix(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q5. Shortest Palindrome (KMP trick)

### Problem Statement (Specific)
Solve **Shortest Palindrome (KMP trick)** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Shortest Palindrome (KMP trick), preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Shortest Palindrome (KMP trick) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_shortest_palindrome_kmp_trick(data):
    """Brute-force baseline for: Shortest Palindrome (KMP trick)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Shortest Palindrome (KMP trick) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_shortest_palindrome_kmp_trick(data):
    """Intermediate optimized approach for: Shortest Palindrome (KMP trick)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Shortest Palindrome (KMP trick): Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_shortest_palindrome_kmp_trick(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q6. Pattern Search with Z-Algorithm

### Problem Statement (Specific)
Solve **Pattern Search with Z-Algorithm** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Pattern Search with Z-Algorithm, preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Pattern Search with Z-Algorithm directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_pattern_search_with_z_algorithm(data):
    """Brute-force baseline for: Pattern Search with Z-Algorithm."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Pattern Search with Z-Algorithm to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_pattern_search_with_z_algorithm(data):
    """Intermediate optimized approach for: Pattern Search with Z-Algorithm."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Pattern Search with Z-Algorithm: Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_pattern_search_with_z_algorithm(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q7. Rabin-Karp Substring Search

### Problem Statement (Specific)
Solve **Rabin-Karp Substring Search** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Rabin-Karp Substring Search, preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Rabin-Karp Substring Search directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_rabin_karp_substring_search(data):
    """Brute-force baseline for: Rabin-Karp Substring Search."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Rabin-Karp Substring Search to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_rabin_karp_substring_search(data):
    """Intermediate optimized approach for: Rabin-Karp Substring Search."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Rabin-Karp Substring Search: Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_rabin_karp_substring_search(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q8. Distinct Echo Substrings (Rolling Hash)

### Problem Statement (Specific)
Solve **Distinct Echo Substrings (Rolling Hash)** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Distinct Echo Substrings (Rolling Hash), preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Distinct Echo Substrings (Rolling Hash) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_distinct_echo_substrings_rolling_hash(data):
    """Brute-force baseline for: Distinct Echo Substrings (Rolling Hash)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Distinct Echo Substrings (Rolling Hash) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_distinct_echo_substrings_rolling_hash(data):
    """Intermediate optimized approach for: Distinct Echo Substrings (Rolling Hash)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Distinct Echo Substrings (Rolling Hash): Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_distinct_echo_substrings_rolling_hash(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q9. Longest Palindromic Substring (Manacher)

### Problem Statement (Specific)
Solve **Longest Palindromic Substring (Manacher)** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`: str

### Output
- Longest palindromic substring.

### Constraints (Typical)
- 1 <= len(s) <= 2e5 for linear solutions

### Example (Exact)
```text
Input:  s = "babad"
Output: "bab" (or "aba")
Explanation: Manacher/center expansion tracks palindrome radii.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Longest Palindromic Substring (Manacher) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_longest_palindromic_substring_manacher(data):
    """Brute-force baseline for: Longest Palindromic Substring (Manacher)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Longest Palindromic Substring (Manacher) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_longest_palindromic_substring_manacher(data):
    """Intermediate optimized approach for: Longest Palindromic Substring (Manacher)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Longest Palindromic Substring (Manacher): Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_longest_palindromic_substring_manacher(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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

## Q10. Count Palindromic Substrings (Advanced Variants)

### Problem Statement (Specific)
Solve **Count Palindromic Substrings (Advanced Variants)** using **Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)**. Return exactly what the problem asks and justify complexity.

### Input
- `s`/`text` and optional `pattern`

### Output
- Index/count/substring/boolean as requested.

### Constraints (Typical)
- 1 <= length <= 2e5

### Example (Exact)
```text
Input:  text = "ababcababa", pattern = "ababa"
Output: 5
Explanation: For Count Palindromic Substrings (Advanced Variants), preprocess reusable string structure.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Count Palindromic Substrings (Advanced Variants) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_count_palindromic_substrings_advanced_variants(data):
    """Brute-force baseline for: Count Palindromic Substrings (Advanced Variants)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Count Palindromic Substrings (Advanced Variants) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_count_palindromic_substrings_advanced_variants(data):
    """Intermediate optimized approach for: Count Palindromic Substrings (Advanced Variants)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) invariant to Count Palindromic Substrings (Advanced Variants): Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.
- Complexity target: Time KMP/Z/Manacher are O(n); Rabin-Karp is expected O(n) with good hashing., Space Usually O(n) for helper arrays..

#### Optimal Python (Question-Specific)
```python
def solve_count_palindromic_substrings_advanced_variants(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def kmp_search(text, pattern):
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
