# Sorting & Searching (Interview-Ready Guide)

Using `[TOPIC] = Sorting & Searching`.

## 0) Scope (Checklist)
- [x] Quick sort / merge sort / heap sort overview
- [x] Stability, in-place vs extra space
- [x] Custom comparator sorting
- [x] Counting / radix sort basics
- [x] Binary search fundamentals
- [x] Lower/upper bound patterns
- [x] Binary search on answer
- [x] Search in rotated array
- [x] Quickselect / kth element

## 1) Foundations
Sorting organizes data; searching exploits order/monotonicity.

Core terms:
- Stable sort, comparator, partition, pivot
- Lower bound, upper bound, invariant
- Search space vs answer space

Mental model:
- Sort once to simplify many later operations.
- Binary search is "maintain feasible boundary" logic.

## 2) How it works
Cause-effect:
1. Sorting reduces complex relations to adjacent comparisons.
2. Binary search halves candidate space each step.
3. Quickselect partitions to keep only relevant side.

Tiny trace (binary search lower bound of `5` in `[1,3,5,5,8]`):
- `l=0,r=5`
- `mid=2` value `5` -> move `r=2`
- `mid=1` value `3` -> move `l=2`
- stop at `l=2` (first index with value >=5)

## 3) Patterns (Interview Templates)
1. Sort + scan (merge intervals, deduplicate, sweep)
2. Binary search on index
3. Binary search on answer (`is_feasible(x)` monotonic)
4. Partition-based selection (quickselect)

Invariants:
- Binary search half-open form: answer in `[l,r)`.
- For answer search: feasible region monotonic.
- In partition, pivot final index is fixed.

Signals:
- "Find first/last occurrence"
- "Minimize/maximize something with feasibility check"
- "Kth smallest/largest"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: First Bad Version
- Approach: binary search first true in monotonic predicate.

2. Medium: Merge Intervals
- Approach: sort by start; merge with running interval.
- Trace: `[[1,3],[2,6],[8,10]]` -> `[[1,6],[8,10]]`.

3. Medium: Search in Rotated Sorted Array
- Approach: one half is sorted each step; decide side by range check.

4. Hard: Kth Largest Element
- Approach: quickselect average `O(n)`; heap alternative `O(n log k)`.

5. Hard: Capacity To Ship Packages Within D Days
- Approach: binary search answer capacity with feasibility simulation.

## 5) Why & What-if
Edge cases:
- Duplicates in sorted arrays
- Overflow in midpoint (`mid = l + (r-l)/2`)
- Empty input

Pitfalls:
- Infinite loops from bad boundary updates
- Mixing closed and half-open interval styles
- Using unstable sort when stability matters

Why it works:
- Binary search repeatedly discards impossible halves.
- Sorting gives global order guarantees.

Variations:
- If range of values small, counting sort can beat comparison sorts.
- External/streaming data may require heap-based approaches.

## 6) Complexity and Tradeoffs
- Merge sort: `O(n log n)` time, `O(n)` space, stable
- Quick sort: avg `O(n log n)`, worst `O(n^2)`, in-place
- Heap sort: `O(n log n)`, `O(1)` extra, unstable
- Binary search: `O(log n)`
- Quickselect: avg `O(n)`, worst `O(n^2)`

Tradeoffs:
- Stability vs memory
- Deterministic worst-case vs average speed

## 7) Real-world uses
- Database ordering and pagination
- Search/autocomplete indices
- Scheduling and interval conflict detection
- Resource allocation with parametric search

## 8) Comparisons
- Binary search on index vs on answer:
  - Index: sorted data array
  - Answer: monotonic feasibility over numeric domain
- Quickselect vs heap for top-k:
  - One-shot kth: quickselect
  - Streaming top-k: heap

## 9) Retention
Cheat sheet:
- Sorted + exact target -> binary search.
- First/last true -> boundary binary search.
- Overlaps -> sort + scan.
- Kth one-shot -> quickselect.

Recall hooks:
- "Monotonic predicate means binary search on answer."
- "Sort turns chaos into adjacency."

Practice (10):
1. Easy: Binary Search
2. Easy: Search Insert Position
3. Easy: Find First and Last Position
4. Medium: Search in Rotated Sorted Array
5. Medium: Merge Intervals
6. Medium: Kth Largest Element in an Array
7. Medium: Sort Colors (counting/partition)
8. Hard: Median of Two Sorted Arrays
9. Hard: Split Array Largest Sum
10. Hard: Russian Doll Envelopes (sort + LIS)
