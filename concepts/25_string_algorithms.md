# String Algorithm Lookup — Deep Structured Explanation

---

## 1. The Basics — Definition & Core Components

### What is a String?

A **string** is a finite sequence of characters drawn from some alphabet (letters, digits, symbols). Think of it as a necklace — each bead is a character, and the order matters.

```
"hello" → [ h | e | l | l | o ]
index  →    0   1   2   3   4
```

### What is String Lookup?

String lookup (also called **string searching** or **pattern matching**) is the process of finding whether a smaller string (the **pattern**) exists inside a larger string (the **text**), and if so, *where*.

> **Formal Definition:** Given text T of length n and pattern P of length m (where m ≤ n), find all positions i such that T[i..i+m-1] = P.

---

### Core Components

| Component | Role | Example |
|---|---|---|
| **Text (T)** | The haystack — the string you search *in* | `"the cat sat on the mat"` |
| **Pattern (P)** | The needle — what you're looking *for* | `"cat"` |
| **Index / Position** | Where a match begins (0-based) | Position `4` |
| **Match** | A confirmed occurrence of P in T | ✅ |
| **Mismatch** | A position where characters don't align | ❌ |
| **Shift** | How far P is slid right after a mismatch | Move by 1, 2, or more |
| **Alphabet (Σ)** | The set of possible characters | `{a–z}`, ASCII, Unicode |

---

### The Sliding Window Mental Model

The most important intuition: **imagine sliding the pattern like a stencil across the text**, comparing at each position.

```
Text:    t h e   c a t   s a t   o n   t h e   m a t
Pattern:         c a t
                 ↑ try here → MATCH at index 4

Pattern:                   s a t
                           ↑ try here → MATCH at index 8
```

Every algorithm is essentially a smarter version of this sliding process.

---

## 2. How It Works — The Algorithm Family

There is no single "string lookup" algorithm. There is a **family**, each using a different strategy to slide more intelligently. Here's the landscape:

```
String Lookup Algorithms
│
├── Naive (Brute Force)
├── Knuth-Morris-Pratt (KMP)
├── Boyer-Moore
├── Rabin-Karp (Hashing)
└── Aho-Corasick (Multi-pattern)
```

---

### Algorithm 1 — Naive (Brute Force)

**Strategy:** Try every possible position. Compare character by character. Move by 1 on mismatch.

**Process:**
```
Text:    A B C A B D A B C
Pattern: A B C
─────────────────────────
Step 1:  A B C           → MATCH at 0
Step 2:    B C ?         → A≠B, mismatch
Step 3:      C ?         → A≠C, mismatch
Step 4:        A B C     → nope (D at 5)
...
```

**Pseudocode:**
```
for i from 0 to n - m:
    for j from 0 to m - 1:
        if T[i+j] ≠ P[j]: break
    if j == m: report match at i
```

**Complexity:**
- Time: O(n × m) — worst case (e.g., `"AAAAAAB"` searching for `"AAAB"`)
- Space: O(1)

**Analogy:** Like manually re-reading a book from scratch every time you want to find a word, even if you just read that page.

---

### Algorithm 2 — Knuth-Morris-Pratt (KMP)

**Core Insight:** When a mismatch occurs, you've already matched some characters. That matched prefix tells you how far you can skip — you don't need to re-compare what you already know.

#### Step 1 — Build the Failure Function (LPS Array)

LPS = **Longest Proper Prefix which is also a Suffix**. It encodes self-overlap in the pattern.

```
Pattern:  A  B  A  B  C
Index:    0  1  2  3  4
LPS:      0  0  1  2  0

Meaning: "ABAB" has a prefix "AB" that is also a suffix → overlap length = 2
```

#### Step 2 — Use LPS to Skip

```
Text:    A B A B C A B A B D
Pattern: A B A B C
─────────────────────────────
i=0..4:  A B A B C → MATCH at 0
i=5:     Continue with j = LPS[4] = 0, start fresh
```

When mismatch at j, jump to `j = LPS[j-1]` instead of restarting from j=0.

**Complexity:**
- Time: O(n + m) — guaranteed linear
- Space: O(m) — for LPS array

**Analogy:** Like a detective who remembers what they've already read. If a chapter starts with the same words as another, they skip re-reading the overlap.

---

### Algorithm 3 — Boyer-Moore

**Core Insight:** Compare the pattern **right to left**. Use two heuristics to make large jumps.

#### Bad Character Heuristic
When a mismatch occurs at text character `c`, shift the pattern so that the **rightmost occurrence of `c` in the pattern** aligns with it. If `c` doesn't appear in the pattern at all, shift the entire pattern past `c`.

```
Text:    X Y Z A B C D
Pattern:         B C D
                   ↑ mismatch: text has 'A', pattern has 'B'
                   'A' doesn't appear in pattern → shift entire pattern past 'A'
```

#### Good Suffix Heuristic
When a mismatch occurs after matching a suffix, shift using the last occurrence of that matched suffix elsewhere in the pattern.

**Complexity:**
- Time: O(n/m) best case (faster than linear!), O(n × m) worst case
- Space: O(m + Σ)

**Analogy:** Like proofreading backwards — you catch the most distinctive characters first and can skip large chunks of text instantly.

---

### Algorithm 4 — Rabin-Karp (Hashing)

**Core Insight:** Instead of comparing character-by-character, **hash the pattern** and compare hashes. Recompute the hash of each text window in O(1) using a **rolling hash**.

```
Pattern: "cat"  → hash = 312
Text window "the" → hash = 201  ≠ skip
Text window "he " → hash = 198  ≠ skip
Text window "e c" → hash = 290  ≠ skip
Text window "cat" → hash = 312  = verify character by character → MATCH
```

**Rolling Hash Formula:**
```
hash("cat") = (c × p² + a × p¹ + t × p⁰) mod q
New window hash = (old_hash - T[i] × p^(m-1)) × p + T[i+m]
```

**Complexity:**
- Average Time: O(n + m)
- Worst case: O(n × m) — hash collisions
- Space: O(1)

**Analogy:** Like checking book ISBNs instead of reading entire books. Only open the book if the ISBN matches.

---

### Algorithm 5 — Aho-Corasick (Multi-Pattern)

**Core Insight:** When you have **many patterns** to find simultaneously, build a finite automaton (trie + failure links) from all patterns and scan the text only once.

```
Patterns: {"he", "she", "his", "hers"}
Text:     "ushers"
Result:   Found "she" at 1, "he" at 2, "hers" at 2
```

**Complexity:**
- Build: O(sum of all pattern lengths)
- Search: O(n + total matches)

**Analogy:** Instead of sending one detective per suspect, brief a single detective on all suspects at once and let them scan the scene once.

---

## 3. Side-by-Side Algorithm Comparison

```
Algorithm      | Best Case  | Worst Case | Space  | Key Idea
──────────────────────────────────────────────────────────────
Naive          | O(n)       | O(n×m)     | O(1)   | Try everything
KMP            | O(n+m)     | O(n+m)     | O(m)   | Failure function / LPS
Boyer-Moore    | O(n/m)     | O(n×m)     | O(m+Σ) | Right-to-left + skip tables
Rabin-Karp     | O(n+m)     | O(n×m)     | O(1)   | Rolling hash
Aho-Corasick   | O(n+Σpat)  | O(n+Σpat)  | O(Σpat)| Trie automaton
```

---

## 4. Why & What If — Edge Cases & Variations

### Why does KMP guarantee O(n+m)?

Because the two pointers `i` (text) and `j` (pattern) **never go backwards together**. `i` only ever moves forward, and `j` resets using the LPS — so total work is bounded by `n + m`.

### What if the pattern is longer than the text?

Immediately return "not found" — no algorithm even starts. This is an O(1) early exit.

### What if the pattern is empty?

By convention, an empty pattern matches at every position (0 through n). Most implementations handle this as a special case.

### What if there are hash collisions in Rabin-Karp?

A hash match triggers a **character-by-character verification**. True collisions are rare with a good hash, but they're why worst-case is O(n×m).

### What if the text is a stream (you can't store it all)?

Sliding window approaches like KMP and Rabin-Karp naturally handle streaming because they process characters left to right without backtracking on the text.

### What if the alphabet is huge (Unicode)?

Boyer-Moore's bad-character table grows with alphabet size. For Unicode (130,000+ characters), you'd use a hash map instead of an array to store the table.

### What if you need fuzzy/approximate matching?

Exact lookup algorithms won't help. You need **edit distance** (Levenshtein) or **bitap algorithm** — a fundamentally different class of problem.

---

## 5. Practical Real-World Applications

### Text Editors — Ctrl+F / Find & Replace
Every "find in file" feature uses a variant of Boyer-Moore or KMP under the hood. The pattern is your search query; the text is the file content.

### Search Engines — Web Crawlers & Indexing
Rabin-Karp's rolling hash is used to detect **duplicate content** across billions of web pages by fingerprinting document chunks.

### Antivirus / Malware Detection
Aho-Corasick powers signature scanning — thousands of malware signatures (patterns) are matched simultaneously against file contents (text) in one pass.

### Bioinformatics — DNA Sequence Matching
Genomes like human DNA (~3 billion characters) are searched for gene sequences using Boyer-Moore variants optimized for the 4-character alphabet `{A, T, G, C}`.

### Network Intrusion Detection (IDS)
Tools like Snort use Aho-Corasick to scan network packets for thousands of attack signatures in real time.

### Plagiarism Detection
Rabin-Karp's rolling hash detects copied substrings across documents by comparing hash fingerprints of overlapping chunks.

### Database Query Optimization — LIKE Operator
`SQL LIKE '%cat%'` internally uses a string search algorithm. Databases optimize this with indexes (like trigram indexes in PostgreSQL) to avoid full table scans.

---

## 6. Comparisons with Related Concepts

| Concept | Similarity | Key Difference |
|---|---|---|
| **Binary Search** | Also a lookup algorithm | Works on *sorted arrays*, not strings |
| **Regular Expressions** | Also searches text for patterns | Patterns can be *non-literal* (wildcards, quantifiers) — compiled to automata |
| **Edit Distance (Levenshtein)** | Also compares strings | Measures *similarity*, not exact location |
| **Suffix Arrays / Trees** | Also used for string search | Preprocesses the *text* (not pattern) for repeated queries |
| **Hash Tables** | Also uses hashing | Looks up *whole keys*, not substrings |
| **Tries** | Used in Aho-Corasick | A data structure that *builds on* string lookup |

---

## 7. Long-Term Retention Tips

**Build a mental hierarchy of the problem, not the algorithms.** Every algorithm answers: *"How cleverly can I shift the pattern after a mismatch?"* Naive = shift 1. KMP = shift using prefix overlap. Boyer-Moore = shift using character tables.

**Anchor each algorithm to an analogy:**
- Naive → Reading every word in a book to find one
- KMP → A detective who remembers what they've read
- Boyer-Moore → Proofreading backwards and skipping chunks
- Rabin-Karp → Checking ISBNs before opening books
- Aho-Corasick → One detective briefed on all suspects at once

**Remember the trade-off axes:**
- Preprocessing cost vs. search speed
- Space used vs. shifts gained
- Single pattern vs. multi-pattern

**Practice one concrete example by hand** for Naive and KMP — trace the LPS array manually at least once. The muscle memory of building the failure function makes KMP stick permanently.

**The master question to ask yourself:** *"When a mismatch happens, what information did I just learn, and how can I use it to shift farther than 1?"* That question is the entire intellectual history of string search algorithms from 1970 to today.
