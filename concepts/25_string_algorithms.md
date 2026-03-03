String Algorithm Lookup: A Deep & Structured Guide

1. The Basics — Definition & Core Components
What is a String?
A string is a sequence of characters. Think of it as a necklace of beads, where each bead is a character.

"HELLO" → [H] [E] [L] [L] [O]
            0   1   2   3   4   ← index positions


What is a String Lookup Algorithm?
A string lookup algorithm is a systematic method for finding whether a pattern (a smaller string) exists inside a text (a larger string), and where it exists.

TEXT:    "the cat sat on the mat"
PATTERN: "sat"
RESULT:  Found at index 8 ✓


Core Components



|Component           |Definition                              |Example                    |
|--------------------|----------------------------------------|---------------------------|
|**Text (T)**        |The haystack — string being searched    |`"the cat sat on the mat"` |
|**Pattern (P)**     |The needle — string being looked for    |`"sat"`                    |
|**Index / Position**|Where the match starts in T             |`8`                        |
|**Window**          |A sliding view of T equal to length of P|`"cat"`, `"at "`, `"t s"` …|
|**Match**           |When window == pattern                  |✓                          |
|**Mismatch**        |When window ≠ pattern                   |✗                          |

2. How It Works — The Naive Algorithm First
Before smart algorithms, understand the brute-force approach. Every other algorithm is an optimization of this.
The Sliding Window Model
Imagine sliding a paper cutout (the pattern) across a sentence (the text), one step at a time:

TEXT:    T H E   C A T   S A T   O N
         ↑
STEP 1: [T H E] vs "SAT" → ✗ mismatch → slide right

         . ↑
STEP 2:  [H E  ] vs "SAT" → ✗ → slide right

                     ... keep sliding ...

                 ↑
STEP 8:         [S A T] vs "SAT" → ✓ MATCH at index 8!


Brute Force Code Logic

for i from 0 to len(T) - len(P):
    match = true
    for j from 0 to len(P):
        if T[i+j] ≠ P[j]:
            match = false
            break
    if match: return i   ← found at position i
return -1                ← not found


Time Complexity of Brute Force

Worst case: O(n × m)
  n = length of text
  m = length of pattern

Example: T = "AAAAAAB", P = "AAAB"
Every window almost matches before failing → very slow.


3. The Smart Algorithms — Cause & Effect
3A. KMP (Knuth-Morris-Pratt)
The core insight: When a mismatch happens, you already know part of the text you just compared. Don’t throw that knowledge away.
The Analogy: Reading a Book with a Bookmark
In brute force, every mismatch sends you all the way back. KMP is like using a bookmark — when you lose your place, you go back only as far as your bookmark, not the beginning.
The Failure Function (LPS Table)
KMP precomputes a table called LPS (Longest Proper Prefix which is also Suffix) for the pattern.

Pattern: A B A B C

LPS computation:
  A → no prefix/suffix match → LPS[0] = 0
  AB → no match             → LPS[1] = 0
  ABA → "A" matches         → LPS[2] = 1
  ABAB → "AB" matches       → LPS[3] = 2
  ABABC → no match          → LPS[4] = 0

LPS Table: [0, 0, 1, 2, 0]


What this means: On a mismatch at position 3 (B), instead of restarting from scratch, you jump back to position LPS[2] = 1. You skip redundant comparisons.
KMP Complexity

Preprocessing (LPS): O(m)
Searching:           O(n)
Total:               O(n + m)  ← always, no worst case trap


3B. Boyer-Moore Algorithm
Core insight: Compare the pattern from right to left, and use two heuristics to skip large chunks.
The Analogy: Proofreading a Document Backwards
You read the last character of the pattern first. If it doesn’t appear anywhere in the text’s current window, you can skip the entire window length forward. This is why Boyer-Moore is often the fastest in practice.

TEXT:    X A B C D A B C Y
PATTERN:     A B C
                 ↑ (compare right to left)

'D' not in pattern → skip entire window forward!


Two Heuristics

1. BAD CHARACTER RULE:
   On mismatch, align pattern so bad character
   aligns with its rightmost occurrence in pattern.

2. GOOD SUFFIX RULE:
   If suffix matched before mismatch, shift pattern
   to align that suffix with its next occurrence.

Take the MAX of both skips → huge jumps possible.


Boyer-Moore Complexity

Best case:  O(n/m)  ← sub-linear! Skips most of text
Worst case: O(n × m) for highly repetitive patterns


3C. Rabin-Karp (Rolling Hash)
Core insight: Instead of comparing characters, compare hash values (numeric fingerprints).
The Analogy: Fingerprinting
Instead of comparing two people face-by-face (slow), you compare fingerprints (fast). If fingerprints differ, skip. If they match, then verify face-to-face.

TEXT:    "abcde"   PATTERN: "cde"

Hash("cde") = 3+4+5 = 12   (simplified hash)

Window 1: hash("abc") = 1+2+3 = 6  ≠ 12 → skip
Window 2: hash("bcd") = 2+3+4 = 9  ≠ 12 → skip
Window 3: hash("cde") = 3+4+5 = 12 = 12 → verify → MATCH ✓


The “Rolling” Part
You don’t recompute the hash from scratch every step. You roll it:

New hash = (Old hash - leftmost char value) + new rightmost char value

This makes each slide O(1) instead of O(m).


Rabin-Karp Complexity

Average: O(n + m)
Worst case: O(n × m) — if hash collisions are frequent
Best use: Multi-pattern search (search for k patterns simultaneously)


4. Visual Algorithm Comparison Diagram

TEXT LENGTH (n) = 1000, PATTERN LENGTH (m) = 10

BRUTE FORCE:  ████████████████████████████  O(n×m) = ~10,000 ops
KMP:          ████████████                  O(n+m) = ~1,010 ops
RABIN-KARP:   ████████████                  O(n+m) = ~1,010 ops (avg)
BOYER-MOORE:  ██████                        O(n/m) = ~100 ops (best)


5. Why & What If — Edge Cases & Variations
❓ Why does KMP never go backward in the text?
Because the LPS table encodes all the “already matched” information. The text pointer only moves forward — making it truly linear.
❓ What if the pattern is longer than the text?
Immediate return: no match possible. This is always the first check any implementation should make.

len(P) > len(T) → return -1 immediately


❓ What if the pattern appears multiple times?
All algorithms can be adapted to collect all positions, not just return the first.

TEXT: "abababab"   PATTERN: "ab"
KMP finds: [0, 2, 4, 6]


❓ What if there are Unicode characters or emojis?
Strings become multi-byte. A character like 😊 is 4 bytes in UTF-8. Naive index math breaks — you must work with code points, not bytes.
❓ What if we need case-insensitive search?
Normalize both text and pattern to lowercase before running any algorithm.

T.lower() and P.lower() → then search


❓ What if the pattern contains wildcards?
Standard algorithms won’t work. You need regex matching or the bitap algorithm, which encodes the pattern as bitmasks.

6. Practical Real-World Applications



|Use Case                         |Algorithm Used              |Why                                 |
|---------------------------------|----------------------------|------------------------------------|
|`Ctrl+F` in a browser/text editor|Boyer-Moore or KMP          |Speed on large documents            |
|DNA sequence matching            |KMP / Aho-Corasick          |Long texts, repetitive patterns     |
|Spam/virus signature detection   |Aho-Corasick                |Many patterns at once               |
|Git diff / file comparison       |Dynamic programming variant |Finding longest common substring    |
|Search engines (indexing)        |Suffix arrays / Suffix trees|Millisecond lookups at massive scale|
|Plagiarism detection             |Rabin-Karp                  |Rolling hash over document chunks   |
|Autocomplete / autocorrect       |Trie (prefix tree)          |Fast prefix matching                |

7. Comparison With Related Concepts

STRING LOOKUP FAMILY TREE:

Exact Match ──────┬── Brute Force       (simple, slow)
                  ├── KMP               (linear, smart skip)
                  ├── Boyer-Moore       (fastest in practice)
                  └── Rabin-Karp        (hashing, multi-pattern)

Approximate Match ┬── Levenshtein       (edit distance)
                  └── Fuzzy search      (typo-tolerant)

Multi-Pattern ────┬── Aho-Corasick      (KMP generalized)
                  └── Rabin-Karp        (multiple hashes)

Structural ───────┬── Suffix Array      (preprocess text, fast queries)
                  ├── Suffix Tree       (O(n) construction)
                  └── Trie              (prefix-based)


Key Differentiators



|             |KMP         |Boyer-Moore |Rabin-Karp  |
|-------------|------------|------------|------------|
|Direction    |Left → Right|Right → Left|Left → Right|
|Preprocessing|Pattern     |Pattern     |Pattern     |
|Best Case    |O(n)        |**O(n/m)**  |O(n+m)      |
|Multi-pattern|No          |No          |**Yes**     |
|Simplicity   |Medium      |Complex     |Medium      |

8. Memory Tips — How to Retain This
Mnemonics
	∙	KMP = “Keep Moving Persistently” — the text pointer never goes back
	∙	Boyer-Moore = “Big Moves” — famous for large skip jumps
	∙	Rabin-Karp = “Rolling Karpet” — rolls the hash across the text
Mental Models to Lock In
	1.	Every algorithm is a smarter sliding window. The window is always the same size as the pattern. The only difference is how far you slide after a mismatch.
	2.	Preprocessing trades setup time for search time. KMP spends O(m) building the LPS table so it can search in O(n). This is the classic “sharpen the axe before chopping” trade-off.
	3.	Hashing = fingerprinting. Rabin-Karp never compares characters if fingerprints differ — same logic as why police use fingerprints before DNA tests.
Practice Progression

Week 1: Implement brute force from scratch
Week 2: Implement KMP + understand LPS table
Week 3: Implement Rabin-Karp with rolling hash
Week 4: Study Boyer-Moore bad character rule
Week 5: Explore Aho-Corasick for multi-pattern


The golden rule of string lookup: The goal is always to avoid redundant comparisons. Every smart algorithm is simply a different strategy for skipping work you’ve already done.
