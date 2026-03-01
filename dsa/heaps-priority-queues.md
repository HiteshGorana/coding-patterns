# Heaps / Priority Queues (Interview-Ready Guide)

Using `[TOPIC] = Heaps / Priority Queues`.

## 0) Scope (Checklist)
- [x] Min-heap vs max-heap
- [x] Top-K / Kth largest/smallest
- [x] Merge K sorted lists/arrays
- [x] Streaming median (two heaps)
- [x] Task scheduling patterns

## 1) Foundations
A heap is a complete binary tree (usually array-backed) with heap-order property.

Core terms:
- Min-heap, max-heap
- Push, pop, peek
- Heapify up/down

Mental model:
- Heap gives fast access to current best candidate, not full sorted order.

## 2) How it works
Cause-effect:
1. Push inserts at end then bubble-up.
2. Pop top swaps with end then bubble-down.
3. Maintain size `k` heap for top-k streaming.

Tiny trace (k=2 largest in `[3,1,5,2]`, min-heap):
- Push 3 -> `[3]`
- Push 1 -> `[1,3]`
- Push 5 -> `[1,3,5]` size>2 pop1 -> `[3,5]`
- Push 2 -> `[2,5,3]` size>2 pop2 -> `[3,5]`
- Answer heap has top 2 largest: 3 and 5

## 3) Patterns (Interview Templates)
1. Top-k with size-limited heap
2. K-way merge with heap of current heads
3. Two-heaps median (`maxLeft`, `minRight`)
4. Greedy scheduling by earliest finish/cost with heap

Invariants:
- Top-k min-heap keeps smallest among current top-k at root.
- Two-heaps median keeps sizes balanced (`|lenL-lenR|<=1`) and `maxLeft <= minRight`.
- K-way merge heap stores one candidate per list/stream.

Signals:
- "Need current min/max repeatedly"
- "Kth or top-k"
- "Merge many sorted sources"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Kth Largest Element in Stream
- Approach: min-heap size `k`.

2. Medium: Top K Frequent Elements
- Approach: frequency map + min-heap on count.

3. Medium: Merge K Sorted Lists
- Approach: push list heads; pop smallest and push its next.

4. Hard: Find Median from Data Stream
- Approach: two heaps with rebalance.

5. Hard: Task Scheduler variants
- Approach: max-heap for remaining counts + cooldown queue.

## 5) Why & What-if
Edge cases:
- `k=0`, `k>n`
- Duplicate values
- Continuous stream (unbounded input)

Pitfalls:
- Using wrong heap direction
- Forgetting rebalance in two-heaps median
- Comparator errors in tuples

Why it works:
- Heap-order guarantees root is best candidate in `O(1)` peek and `O(log n)` updates.

Variations:
- If data is static and single query, quickselect may be better.
- If key range small, counting array may outperform heap.

## 6) Complexity and Tradeoffs
- Push/pop: `O(log n)`
- Peek: `O(1)`
- Build heap from array: `O(n)`
- Top-k streaming: `O(n log k)`
- K-way merge: `O(N log k)` for total `N` elements

Tradeoffs:
- Better than full sort when only partial order needed.
- Does not support fast arbitrary search/removal.

## 7) Real-world uses
- Job/task schedulers
- Event simulation
- Streaming analytics top-k
- Network routing priority handling

## 8) Comparisons
- Heap vs balanced BST:
  - Heap: faster top access, poorer ordered iteration.
  - BST: full order operations.
- Heap vs sort:
  - Heap good for online/streaming.
  - Sort good for complete offline ordering.

## 9) Retention
Cheat sheet:
- Top-k largest -> min-heap size k.
- Top-k smallest -> max-heap size k.
- Median stream -> two heaps.
- Merge k sorted -> heap of heads.

Recall hooks:
- "Heap stores just enough order."
- "Root is the current winner."

Practice (10):
1. Easy: Kth Largest Element in a Stream
2. Easy: Last Stone Weight
3. Medium: Top K Frequent Elements
4. Medium: K Closest Points to Origin
5. Medium: Merge K Sorted Lists
6. Medium: Reorganize String (heap + greedy)
7. Hard: Find Median from Data Stream
8. Hard: Sliding Window Median
9. Hard: IPO / Maximize Capital
10. Hard: Task Scheduler II variants
