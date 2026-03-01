# Pattern 45: Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)

## Diagram + Intuition

### Pattern Diagram
```text
KMP: prefix-function fallback
Z: longest prefix match at each index
Rabin-Karp: rolling hash
Manacher: palindrome radii in O(n)
```

### Read-the-Question Trigger Cues
- Need fast substring matching across large texts.
- Need all pattern occurrences or linear palindrome computation.

### Intuition Anchor
- "Preprocess string structure once, then answer matching/palindrome queries without restarting work."

### 3-Second Pattern Check
- Does naive matching restart too often and become `O(n*m)`?

## What This Pattern Solves
Advanced string pattern algorithms provide linear or near-linear matching/palindrome solutions where naive scanning is too slow.

## Recognition Signals
- Repeated pattern/text matching.
- Need border/prefix reuse information.
- Need longest palindromic substring in linear time.

## Core Intuition
Exploit internal string structure (prefix borders, rolling hashes, palindrome symmetry) to avoid redundant comparisons.

## Step-by-Step Method
1. Pick algorithm by requirement: exact match, multiple matches, hash-based, or palindromes.
2. Preprocess pattern/text structure (`lps`, `z`, hashes, radii).
3. Run linear scan transitions.
4. Collect matches or best palindrome.

## Detailed Example
KMP reuses matched prefix length on mismatch, avoiding restart from scratch.

## Complexity
- Time: KMP/Z/Manacher are `O(n)`; Rabin-Karp is expected `O(n)` with good hashing.
- Space: Usually `O(n)` for helper arrays.

## Python Template
```python
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

## Common Pitfalls
- Off-by-one errors in prefix/Z arrays.
- Hash collision assumptions without verification.
- Using Manacher when simpler center expansion suffices for constraints.

## Variations
- KMP exact match
- Z-array pattern search
- Rabin-Karp multi-pattern rolling hash
- Manacher palindrome radius

## Interview Tips
- Choose the simplest algorithm that meets constraints.
- In interviews, explain fallback mechanism of KMP clearly.

## Practice Problems
- Implement strStr()
- Repeated String Match
- Longest Palindromic Substring
- Shortest Palindrome
