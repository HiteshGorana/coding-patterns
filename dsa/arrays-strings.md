# Arrays & Strings (Interview-Ready Guide)

Using `[TOPIC] = Arrays & Strings`.

## 0) Scope (Checklist)
- [x] Array traversal, counting, prefix/suffix
- [x] Two pointers
- [x] Sliding window
- [x] Prefix sums / difference arrays
- [x] Subarray patterns
- [x] Sorting-based tricks (merge intervals, duplicates)
- [x] String traversal + parsing
- [x] Two pointers / sliding window on strings
- [x] Rolling hash basics
- [x] Pattern matching basics (KMP/Z-function idea)
- [x] Anagrams / frequency methods

## 1) Foundations
Arrays are contiguous memory sequences; strings are arrays of characters with text constraints.

Core terms:
- Indexing, subarray, substring, subsequence
- Prefix/suffix, window, pointer, frequency map
- In-place vs extra memory

Mental model:
- Arrays/strings are mostly scan-and-update problems.
- Keep only the minimum state needed (two pointers, counts, prefix sum).

## 2) How it works
Cause-effect flow:
1. Choose linear scan if order matters and constraints are local.
2. Use two pointers when both ends or sorted order helps.
3. Use sliding window when answer is a valid contiguous range.
4. Use prefix sums when many range queries appear.
5. Use sorting when pair/group relations become easier globally.

Tiny trace (longest substring without repeat for `"abca"`):
- `L=0,R=0`: `"a"` valid, best=1
- `R=1`: `"ab"` valid, best=2
- `R=2`: `"abc"` valid, best=3
- `R=3` sees duplicate `a`; move `L` to `1`, window `"bca"` valid, best=3

## 3) Patterns (Interview Templates)
Common templates:
1. Two pointers (`l`, `r`) with monotonic movement.
2. Sliding window with "expand right, shrink left until valid".
3. Prefix sum hash (`sum -> first/last index`).
4. Sort + scan for interval merge and duplicate grouping.
5. Frequency array/map for anagram and counting constraints.

Invariants:
- Window invariant: current `[l..r]` satisfies rule.
- Two-pointer invariant: pointers never move backward (linear time).
- Prefix invariant: `pref[i]` stores sum up to `i`.

Signals:
- "Longest/shortest subarray or substring with condition"
- "Find pair in sorted array"
- "Range sum quickly"
- "Group equal or overlapping items"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Two Sum
- Problem: find indices `i,j` such that `a[i]+a[j]=target`.
- Approach: hash map of seen value -> index.
- Trace: `[2,7,11], target=9`: see `2` store; see `7`, need `2`, found.

2. Medium: Product of Array Except Self
- Approach: prefix product pass + suffix product pass.
- Trace for `[1,2,3,4]`:
  - Prefix contributes `[1,1,2,6]`
  - Suffix multiply gives `[24,12,8,6]`

3. Medium: Longest Substring Without Repeating Characters
- Approach: sliding window + last index map.
- Trace: `"pwwkew"` -> best window `"wke"` length 3.

4. Hard: Minimum Window Substring
- Approach: frequency need/have with variable window.
- Trace (small): `s="ADOBEC", t="ABC"` -> first valid window `"ADOBEC"` then shrink.

ASCII window:
```text
s: A D O B E C
   L         R   (valid when all required counts met)
```

## 5) Why & What-if
Edge cases:
- Empty array/string, single element
- All duplicates or all unique
- Negative numbers break some monotonic-window assumptions

Pitfalls:
- Off-by-one in window size (`r-l+1`)
- Updating answer before restoring window validity
- Confusing substring (contiguous) vs subsequence

Why it works:
- Monotonic pointer movement gives `O(n)`.
- Prefix sums transform range sums into constant-time difference.

Variations:
- Streaming input: use rolling window state only.
- Large alphabet: use hash map instead of fixed array.

## 6) Complexity and Tradeoffs
- Two pointers: usually `O(n)` time, `O(1)` extra space.
- Sliding window with maps: `O(n)` average, `O(k)` space.
- Prefix sums: build `O(n)`, query `O(1)`.
- Sorting-based: `O(n log n)` but simplifies logic.

Tradeoffs:
- Hash maps are faster average but use more memory.
- Sorting may lose original index order unless tracked.

## 7) Real-world uses
- Log processing on contiguous time windows
- Text analytics and token frequency
- Compression/search preprocessing (rolling hash)
- Monitoring systems with moving averages

## 8) Comparisons
- Two pointers vs sliding window:
  - Two pointers: symmetric comparisons, sorted arrays.
  - Sliding window: maintain validity constraints.
- Prefix sum vs brute-force range:
  - Prefix sum for repeated queries.
- KMP/Z vs naive matching:
  - Linear preprocessing for repeated pattern checks.

## 9) Retention
Cheat sheet:
- Pair in sorted array -> two pointers.
- Contiguous + condition -> sliding window.
- Many range sums -> prefix sum.
- Overlaps/merges -> sort + scan.

Recall hooks:
- "Expand, violate, shrink, record."
- "Prefix turns interval work into subtraction."

Practice (10):
1. Easy: Remove Duplicates from Sorted Array
2. Easy: Valid Anagram
3. Easy: Best Time to Buy/Sell Stock
4. Medium: 3Sum
5. Medium: Longest Repeating Character Replacement
6. Medium: Subarray Sum Equals K
7. Medium: Merge Intervals
8. Hard: Minimum Window Substring
9. Hard: Sliding Window Maximum
10. Hard: Find All Anagrams in a String
