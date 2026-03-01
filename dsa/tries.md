# Tries (Interview-Ready Guide)

Using `[TOPIC] = Tries`.

## 0) Scope (Checklist)
- [x] Insert/search/prefix
- [x] Auto-complete/prefix counting
- [x] Word search on grid (trie + DFS)
- [x] Bitwise trie (max XOR) basics

## 1) Foundations
A trie is a prefix tree where each edge represents a character/bit.

Core terms:
- Node, child map/array
- End-of-word marker
- Prefix count
- Bitwise trie (0/1 branches)

Mental model:
- Share common prefixes to compress repeated prefix checks.

## 2) How it works
Cause-effect:
1. Insert follows/creates path by characters.
2. Search requires path + end marker.
3. Prefix query only needs path existence.
4. Bitwise trie greedily picks opposite bit for max XOR.

Tiny trace (`insert "cat"`, then search `"ca"`):
- Root -> `c` -> `a` -> `t` mark end
- Search `"ca"` path exists but no end marker at `a` => full-word false, prefix true

## 3) Patterns (Interview Templates)
1. Basic dictionary trie
2. Prefix count trie (`count_prefix`)
3. Trie + DFS pruning for board word search
4. Bitwise trie for xor optimization

Invariants:
- Path from root encodes exact prefix.
- End marker distinguishes word vs prefix.
- In board search, remove impossible branches early.

Signals:
- "Starts with/prefix/autocomplete"
- "Many repeated dictionary lookups"
- "Max XOR pair/subarray"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Implement Trie
- Methods: `insert`, `search`, `startsWith`.

2. Medium: Replace Words
- Approach: insert roots; for each word find shortest prefix root.

3. Medium: Map Sum Pairs
- Approach: trie with subtree aggregate or separate map+trie.

4. Hard: Word Search II
- Approach: trie dictionary + DFS grid; mark visited and prune.

5. Hard: Maximum XOR of Two Numbers
- Approach: bitwise trie over 31/63 bits.

## 5) Why & What-if
Edge cases:
- Empty string as valid key
- Non-lowercase alphabets / unicode
- Duplicate insertions

Pitfalls:
- Forgetting end marker updates
- Excessive memory for sparse alphabets if fixed array used
- Missing backtracking reset in grid DFS

Why it works:
- Prefix search becomes path traversal proportional to key length.

Variations:
- Compressed trie (radix tree)
- Ternary search tree
- Aho-Corasick for multi-pattern matching

## 6) Complexity and Tradeoffs
- Insert/search/prefix: `O(L)` where `L` is key length
- Space: `O(total characters stored)` with node overhead

Tradeoffs:
- Faster prefix queries than hash maps, but more memory.
- Hash map better for exact lookup only.

## 7) Real-world uses
- Autocomplete/search suggestions
- Spell checking
- IP routing prefix matching
- Malware/signature matching (variants)

## 8) Comparisons
- Trie vs hash set:
  - Trie supports prefix queries efficiently.
  - Hash set is simpler for exact membership only.
- Trie vs sorted list + binary search:
  - Trie better for many online prefix operations.

## 9) Retention
Cheat sheet:
- Exact word -> need end marker true.
- Prefix check -> path exists.
- Grid words -> trie + DFS + prune.
- XOR max -> choose opposite bit if possible.

Recall hooks:
- "Path equals prefix."
- "Trie buys prefix speed with memory."

Practice (10):
1. Easy: Implement Trie (Prefix Tree)
2. Easy: Design Add and Search Words Data Structure
3. Medium: Replace Words
4. Medium: Map Sum Pairs
5. Medium: Longest Word in Dictionary
6. Medium: Stream of Characters
7. Hard: Word Search II
8. Hard: Maximum XOR of Two Numbers
9. Hard: Maximum XOR With an Element From Array
10. Hard: Concatenated Words
