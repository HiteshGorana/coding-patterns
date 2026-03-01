# Linked Lists (Interview-Ready Guide)

Using `[TOPIC] = Linked Lists`.

## 0) Scope (Checklist)
- [x] Reversal (iterative/recursive)
- [x] Fast/slow pointers (cycle detect, middle)
- [x] Merge two lists, sort list (merge sort)
- [x] Remove Nth from end
- [x] Intersection of lists
- [x] Copy list with random pointer
- [x] LRU cache pattern (DLL + hash map)

## 1) Foundations
Linked lists store nodes connected by pointers, not contiguous memory.

Core terms:
- `head`, `next`, `prev`, dummy/sentinel node
- Singly vs doubly linked list
- Cycle, tail, pointer rewiring

Mental model:
- Most problems are safe pointer updates with strict order.
- Dummy node and two pointers reduce edge-case bugs.

## 2) How it works
Cause-effect:
1. Keep references before rewiring (`next = cur.next`).
2. Reconnect links in controlled order.
3. Use fast/slow for relative position without length precompute.
4. Use hash map when extra relation exists (`random`, LRU key->node).

Tiny trace (iterative reverse `1->2->3`):
- Start: `prev=null, cur=1`
- Step1: `1.next=null`, move `prev=1, cur=2`
- Step2: `2.next=1`, move `prev=2, cur=3`
- Step3: `3.next=2`, move `prev=3, cur=null`
- Result head: `3->2->1`

## 3) Patterns (Interview Templates)
1. Dummy head for insertion/deletion near front.
2. Fast/slow pointers for middle and cycle.
3. Two-pass or one-pass gap method for Nth from end.
4. Merge template for sorted lists.
5. Hash + DLL template for `O(1)` LRU operations.

Invariants:
- No node should be orphaned: store `next` first.
- Fast moves 2, slow moves 1; meeting implies cycle.
- In merge, tail always points to last node of output.

Signals:
- "In-place without extra array"
- "Cycle/middle/intersection"
- "Cache with recency updates"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Reverse Linked List
- Approach: iterative `prev, cur, nxt`.
- Trace: shown above.

2. Medium: Remove Nth Node From End
- Approach: advance `fast` by `n`, then move both until `fast.next=null`.
- Dummy handles removing original head.
- Trace: `1->2->3->4->5`, `n=2` -> remove `4`.

3. Medium: Detect Cycle (Floyd)
- Approach: fast/slow; if meet, cycle exists.
- Trace: slow `1,2,3,4...` fast `1,3,5,3...` meet at cycle.

4. Hard: Copy List with Random Pointer
- Approach: map old node -> new node, then wire `next` and `random`.
- Alt: interleaving nodes for `O(1)` extra (harder).

5. Hard: LRU Cache
- Approach: hash map key->DLL node; head/tail sentinels for MRU/LRU moves.
- `get` and `put`: move node to front in `O(1)`.

## 5) Why & What-if
Edge cases:
- Empty list, one node, two nodes
- Remove head/tail
- Even vs odd length middle choice

Pitfalls:
- Losing `next` before rewiring
- Forgetting dummy when deleting head
- Infinite loop due to bad pointer update order

Why it works:
- Each operation updates only local links while preserving chain connectivity.

Variations:
- Circular linked list
- Doubly linked list simplifies deletion but uses more space

## 6) Complexity and Tradeoffs
- Reverse: `O(n)` time, `O(1)` space
- Cycle detect: `O(n)` time, `O(1)` space
- Merge two sorted lists: `O(n+m)`
- Copy random list: `O(n)` time, `O(n)` map space (or `O(1)` extra via weaving)
- LRU: `O(1)` average per op, `O(capacity)` space

Tradeoffs:
- Hash-assisted approaches are simpler and safer for complex pointer relations.

## 7) Real-world uses
- Browser history (DLL)
- OS memory allocator free lists
- LRU caches in DBs and web systems
- Streaming pipeline buffers

## 8) Comparisons
- Array vs linked list:
  - Array: fast random access
  - Linked list: fast local insert/delete with node reference
- Fast/slow vs hash set cycle detection:
  - Fast/slow `O(1)` space, hash set simpler conceptually

## 9) Retention
Cheat sheet:
- Use dummy node for delete/merge.
- Rewiring order: save next, redirect current, advance.
- Fast/slow for relative position.

Recall hooks:
- "Never cut a link before saving where it goes."
- "Gap of `n` nodes solves Nth-from-end."

Practice (10):
1. Easy: Reverse Linked List
2. Easy: Merge Two Sorted Lists
3. Easy: Linked List Cycle
4. Medium: Remove Nth Node From End
5. Medium: Reorder List
6. Medium: Intersection of Two Linked Lists
7. Medium: Sort List
8. Hard: Copy List with Random Pointer
9. Hard: Reverse Nodes in K-Group
10. Hard: LRU Cache
