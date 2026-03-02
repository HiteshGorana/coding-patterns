# Heap: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

A **heap** is a specialized tree-based data structure that satisfies the **heap property**: every parent node maintains a specific ordering relationship with its children — either always greater (max-heap) or always smaller (min-heap) than them. It is always a **complete binary tree**.

```
MAX-HEAP:                        MIN-HEAP:

         100                              1
        /    \                          /    \
      90      80                       3      2
     /  \    /  \                    /  \   /  \
   50   70  60   40                 7    4  5    6
   /\   /
  20 30 65

Parent ≥ Children (always)       Parent ≤ Children (always)
Root = MAXIMUM element           Root = MINIMUM element
```

**Core components:**

- **Complete binary tree** — every level is fully filled except possibly the last, which fills left to right. This shape is non-negotiable — it's what makes array storage possible.
- **Heap property** — the ordering relationship between every parent and its children (max or min)
- **Root** — the only element directly accessible; always the max (or min)
- **Array representation** — the tree is stored as a flat array using index arithmetic
- **Heapify** — the repair operation that restores the heap property after it's violated
- **Size** — number of elements currently in the heap

The heap makes one promise and keeps it absolutely: **the most extreme element (max or min) is always instantly available at the root, in O(1).**

---

## 2. The Array Representation — The Critical Insight

A heap is conceptually a tree but **physically an array**. This is its most important implementation detail. The complete binary tree shape enables a perfect mapping between tree positions and array indices — no pointers needed.

```
TREE:                    ARRAY:
         100             [_, 100, 90, 80, 50, 70, 60, 40, 20, 30, 65]
        /    \            0   1    2   3   4   5   6   7   8   9   10
      90      80
     /  \    /  \         (index 0 unused — makes math cleaner)
   50   70  60   40
   /\   /
  20 30 65
```

**The index arithmetic — memorize this:**

```
For node at index i:

Parent:       (i - 1) / 2    [or i / 2 if 1-indexed]
Left child:   2 * i + 1      [or 2 * i if 1-indexed]
Right child:  2 * i + 2      [or 2 * i + 1 if 1-indexed]

Example (0-indexed):
  Node 90 is at index 1
  Its parent:      (1-1)/2 = 0  → arr[0]=100 ✅
  Its left child:  2*1+1   = 3  → arr[3]=50  ✅
  Its right child: 2*1+2   = 4  → arr[4]=70  ✅
```

```
WHY THIS WORKS — Complete binary tree guarantee:

Level 0:  1 node    → index 1
Level 1:  2 nodes   → indices 2-3
Level 2:  4 nodes   → indices 4-7
Level 3:  8 nodes   → indices 8-15

Each level's indices are perfectly contiguous.
No gaps, no wasted space, no pointers.
The tree IS the array — same data, two perspectives.
```

This is why heaps are more cache-friendly than pointer-based trees — all data lives in one contiguous block of memory.

---

## 3. The Two Core Repair Operations

Everything a heap does flows from two repair primitives. Understanding them deeply means understanding the entire data structure.

### Sift Up (Bubble Up) — Used After Insertion

When a new element is added at the bottom, it might be larger (in a max-heap) than its parent, violating the heap property. Fix it by repeatedly swapping with its parent until the property is restored.

```
MAX-HEAP — Insert 95:

Step 1: Add to next available spot (end of array)

         100
        /    \
      90      80
     /  \    /  \
   50   70  60   40
   /
  95   ← added here (violates: 95 > 50, its parent)

Step 2: Compare with parent: 95 > 50 → SWAP

         100
        /    \
      90      80
     /  \    /  \
   95   70  60   40
   /
  50

Step 3: Compare with parent: 95 > 90 → SWAP

         100
        /    \
      95      80
     /  \    /  \
   90   70  60   40
   /
  50

Step 4: Compare with parent: 95 < 100 → STOP ✅

         100
        /    \
      95      80
     /  \    /  \
   90   70  60   40
   /
  50
```

**Cause-effect chain:**
```
New element too large →
  Violates heap property with parent →
    Swap with parent →
      Now check with new parent →
        Still too large? Swap again →
          Repeat until heap property satisfied OR reach root
```

**Cost:** O(log n) — at most one swap per level, and there are log n levels.

### Sift Down (Bubble Down) — Used After Extraction

When the root is removed, we move the last element to the root (to maintain complete tree shape), then it might violate the property downward. Fix by repeatedly swapping with the larger child until the property is restored.

```
MAX-HEAP — Extract max (100):

Step 1: Remove root (100). Move last element (50) to root.

          50            ← last element moved here (violates heap)
        /    \
      95      80
     /  \    /  \
   90   70  60   40

Step 2: Compare with children: max(95, 80) = 95 > 50 → SWAP with 95

          95
        /    \
      50      80
     /  \    /  \
   90   70  60   40

Step 3: Compare with children: max(90, 70) = 90 > 50 → SWAP with 90

          95
        /    \
      90      80
     /  \    /  \
   50   70  60   40

Step 4: No children (or children ≤ 50) → STOP ✅

Extracted: 100
Remaining heap is valid.
```

**Cause-effect chain:**
```
Root removed → hole at top →
  Move last element to root (preserves complete tree shape) →
    New root likely too small →
      Compare with both children →
        Swap with LARGER child (preserves heap property with both) →
          Repeat downward until no child is larger →
            Heap property fully restored
```

**Why swap with the LARGER child?**
```
Suppose we have:
       20
      /   \
    80     60

If we swap 20 with 60 (smaller child):
       60
      /   \
    80     20     ← 80 > 60 now! New violation created above.

If we swap 20 with 80 (larger child):
       80
      /   \
    20     60     ← 80 ≥ 60 ✅, 80 ≥ 20 ✅. No new violation.

Always promote the larger child — it's the only safe choice.
```

---

## 4. Core Operations & Their Complexities

| Operation | Process | Time | Notes |
|---|---|---|---|
| `peek()` | Return root | O(1) | Just read arr[0] |
| `push(x)` | Add to end, sift up | O(log n) | At most log n swaps |
| `pop()` | Remove root, sift down | O(log n) | At most log n swaps |
| `heapify([])` | Build heap from array | **O(n)** | Not O(n log n) — see below |
| `size()` | Return element count | O(1) | Track as variable |

### Why Heapify is O(n), Not O(n log n)

This is one of the most surprising results in data structures — worth understanding deeply.

**Naive approach:** Insert n elements one by one = n × O(log n) = O(n log n)

**Heapify (Floyd's algorithm):** Start from the last non-leaf node, sift down each node to the correct position.

```
Array: [3, 1, 6, 5, 2, 4]

Build heap: start at index n/2 - 1 = 2 (last non-leaf)

          3
        /   \
       1     6      ← start here (index 2, value 6)
      / \   /
     5   2  4

Step 1: Sift down index 2 (value 6): no children larger → stays
Step 2: Sift down index 1 (value 1): children are 5,2 → swap with 5

          3
        /   \
       5     6
      / \   /
     1   2  4

Step 3: Sift down index 0 (value 3): children are 5,6 → swap with 6

          6
        /   \
       5     3
      / \   /
     1   2  4

Sift down 3: child is 4 → swap with 4

          6
        /   \
       5     4
      / \   /
     1   2  3

Done ✅
```

**Why O(n)?** The key is that most nodes are near the bottom and have very short sift-down paths:

```
Height h nodes in tree:  sift-down cost ≤ h steps

Nodes at height 0 (leaves):    n/2 nodes × 0 swaps
Nodes at height 1:             n/4 nodes × 1 swap
Nodes at height 2:             n/8 nodes × 2 swaps
Nodes at height k:             n/2^(k+1) nodes × k swaps

Total = Σ k × n/2^(k+1) = n × Σ k/2^(k+1)
      = n × 2  (the sum converges to 2)
      = O(n) ✅
```

Intuition: you do very little work on the many leaves (which need no sifting) and a lot of work only at the few nodes near the root (of which there are very few). The heavy work is rare; the cheap work is ubiquitous.

---

## 5. The Heap Sort Algorithm

Heaps give us a beautiful in-place O(n log n) sorting algorithm:

```
Phase 1: Build max-heap from array      O(n)
Phase 2: Repeatedly extract max         O(n log n)
  - Swap root (max) with last element
  - Reduce heap size by 1
  - Sift down new root
  - Repeat n-1 times

Result: array sorted in ascending order, in-place, no extra space
```

```
Array: [3, 1, 6, 5, 2, 4]

After heapify:  [6, 5, 4, 1, 2, 3]  (max-heap)

Iteration 1:
  Swap root(6) with last(3): [3, 5, 4, 1, 2, | 6]
  Sift down 3: [5, 3, 4, 1, 2, | 6]
  Sift down 3: [5, 3, 4, 1, 2, | 6] (3 settles)

Iteration 2:
  Swap root(5) with last(2): [2, 3, 4, 1, | 5, 6]
  Sift down 2: [4, 3, 2, 1, | 5, 6]

...continuing...

Final: [1, 2, 3, 4, 5, 6] ✅

Time: O(n log n)    Space: O(1) in-place   Not stable
```

---

## 6. The K-Problems — Where Heaps Truly Shine

Heaps are the natural tool for any problem involving "the k most/least extreme elements."

### K Largest Elements

```
Find k=3 largest in [3, 1, 5, 12, 2, 11, 7, 8]

Use a MIN-HEAP of size k (counterintuitive but correct):

Why min-heap? The root = smallest of the k largest candidates.
  → Tells you instantly if a new element beats the weakest in your top-k

Process each element x:
  heap.size < k:    push x
  x > heap.peek(): pop min, push x  ← new element evicts weakest top-k
  x ≤ heap.peek(): skip             ← can't be in top-k

Trace:
  Push 3:  heap=[3]
  Push 1:  heap=[1,3]
  Push 5:  heap=[1,3,5]   ← size=k=3
  12 > 1:  pop 1, push 12 → heap=[3,5,12]
  2  > 3?  NO → skip
  11 > 3:  pop 3, push 11 → heap=[5,11,12]
  7  > 5:  pop 5, push 7  → heap=[7,11,12]
  8  > 7:  pop 7, push 8  → heap=[8,11,12]

Result: [8, 11, 12] ✅   Time: O(n log k)   Space: O(k)
```

**The elegant logic:** A min-heap of size k is a "bouncer with a list of k slots." The root is the weakest person in the VIP area. Any newcomer stronger than the weakest gets in (evicting the weakest); anyone weaker is turned away.

### K-th Largest Element

Same pattern: maintain min-heap of size k. After processing all elements, `heap.peek()` = k-th largest. O(n log k).

### Merge K Sorted Lists

```
Lists: [1,4,7], [2,5,8], [3,6,9]

Push first element of each list into min-heap with list index:
heap = [(1,list0), (2,list1), (3,list2)]

WHILE heap not empty:
  Pop minimum (val, list_idx)
  Add to result
  Push next element from list_idx (if exists)

Step 1: Pop (1,0) → result=[1], push (4,0) → heap=[(2,1),(3,2),(4,0)]
Step 2: Pop (2,1) → result=[1,2], push (5,1) → heap=[(3,2),(4,0),(5,1)]
Step 3: Pop (3,2) → result=[1,2,3], push (6,2) → ...
...

Result: [1,2,3,4,5,6,7,8,9] ✅
Time: O(n log k) where n=total elements, k=number of lists
```

---

## 7. The "Why" Questions

### Why always a complete binary tree?

Three reasons working together:

```
1. ARRAY STORAGE: Complete trees map perfectly to arrays with index arithmetic.
   Any missing nodes would break the parent/child index formulas.

2. HEIGHT GUARANTEE: A complete binary tree of n nodes has height exactly ⌊log₂n⌋.
   This guarantees O(log n) for sift-up and sift-down — always.
   A non-complete tree could degenerate (like a linked list, height n).

3. INSERTION POINT: "Add to end of array" = "add to next available left-to-right
   position in last level" — maintaining completeness is free.
```

### Why doesn't the heap maintain full sorted order?

Because **you don't need it**. The heap property is a **partial order** — weaker than total sort, but sufficient for the operations heaps are designed for. Maintaining full sort costs O(n log n). The heap property can be maintained in O(log n) per operation. You pay only for what you use.

```
Heap property guarantees:    arr[parent] ≥ arr[children]   (at every node)
Full sort guarantees:         arr[i] ≥ arr[i+1]             (at every position)

Full sort is strictly stronger. Heap property is just enough to find the max/min instantly.
```

### Why use a min-heap for k largest (not a max-heap)?

```
MAX-HEAP for k largest:
  Build max-heap of ALL n elements → O(n)
  Extract k times → O(k log n)
  Total: O(n + k log n)

  Problem: requires O(n) space regardless of k.
  Worse for streaming data (can't preload everything).

MIN-HEAP of size k:
  Process each element: O(log k) per element
  Total: O(n log k)   Space: O(k)

  When k << n: log k << log n, so this is faster too.
  Works perfectly for streaming — never need all data at once.
```

The min-heap acts as a size-k filter: the smallest of your top-k is always the eviction candidate. Only elements that beat the minimum threshold earn a spot.

---

## 8. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Empty heap, call pop() | **Heap underflow** — must guard with size check |
| All elements identical | Heap property trivially satisfied (parent = child = OK) |
| k > n in k-largest | Return all n elements |
| Single element | peek/pop works; sift-up/down trivially do nothing |
| Negative numbers | Heap comparison is purely by value; negatives handled correctly |
| Push duplicate of max | Two equal maximums at root and child — both valid, heap property satisfied |
| Need k-th smallest | Use max-heap of size k; evict when current < root |
| Need both min and max instantly | Use a **min-max heap** or maintain two heaps (median-finding pattern) |
| Dynamic updates (change a value) | Requires index tracking + sift up or down — standard heap doesn't support O(log n) arbitrary updates without augmentation |

### The Median-Finding Pattern — Two Heaps

```
Find running median of a data stream.

Use TWO heaps:
  max_heap: lower half of elements (gives max of lower half instantly)
  min_heap: upper half of elements (gives min of upper half instantly)

Invariant: max_heap.size() == min_heap.size() ± 1

       max_heap           min_heap
    [1, 2, 3, 4]       [5, 6, 7, 8]
           ↑     ↑
          4       5     ← median = avg(4, 5) = 4.5 (even count)

Add 9:
  Push to min_heap: [5,6,7,8,9]
  Rebalance: pop min of min_heap (5), push to max_heap
  max_heap=[1,2,3,4,5]  min_heap=[6,7,8,9]
  Median = max_heap.peek() = 5 (odd count)

Each insertion: O(log n). Each median query: O(1).
```

This two-heap pattern is elegant: the max-heap's root and min-heap's root are always the two middle elements. The median lives at the boundary between the two halves.

---

## 9. Priority Queue — The Abstract Interface

A **priority queue** is the abstract data type; a **heap** is its most common implementation. This distinction matters:

```
PRIORITY QUEUE (interface):        HEAP (implementation):
  enqueue(item, priority)    →       push(item)
  dequeue()                  →       pop()
  peek()                     →       peek()
  "highest priority first"           "root = most extreme"
```

Other implementations of priority queue exist (sorted array, sorted linked list), but heap is dominant because:

```
              Enqueue    Dequeue    Peek
Sorted array:  O(n)       O(1)      O(1)
Sorted list:   O(n)       O(1)      O(1)
Unsorted array: O(1)      O(n)      O(n)
HEAP:          O(log n)  O(log n)  O(1)    ← optimal balance
```

Heap gives the best overall complexity when you need both frequent insertions and frequent extractions.

---

## 10. Real-World Applications

| Domain | Problem | Heap's Role |
|---|---|---|
| **Operating Systems** | CPU process scheduling | Priority queue of processes; highest priority runs next |
| **Dijkstra's Algorithm** | Shortest path in graphs | Min-heap of (distance, node); always expand nearest unvisited |
| **A* Pathfinding** | Optimal path with heuristic | Min-heap ordered by f(n) = g(n) + h(n) |
| **Event simulation** | Discrete event processing | Min-heap of (timestamp, event); process earliest event first |
| **Data compression** | Huffman encoding | Min-heap builds optimal prefix code from character frequencies |
| **Job schedulers** | Task queue (AWS, Kubernetes) | Priority queue ensures high-priority jobs run first |
| **Stream processing** | Top-k trending items | Min-heap of size k across streaming data |
| **Network routers** | QoS packet scheduling | Priority queue for different traffic classes |
| **Median maintenance** | Real-time statistics | Two-heap pattern for O(log n) insert, O(1) median |
| **Hospital triage** | Emergency room queuing | Priority queue by severity, not arrival time |

### Dijkstra's Algorithm — Heap as the Heart

```
Find shortest path from node A in weighted graph:

min_heap = [(0, A)]    ← (distance, node)
visited = {}
dist = {A: 0, others: ∞}

WHILE heap not empty:
    (d, u) = pop_min()          ← always process nearest unvisited
    IF u in visited: continue
    visited.add(u)
    
    FOR each neighbor v of u:
        new_dist = d + weight(u,v)
        IF new_dist < dist[v]:
            dist[v] = new_dist
            push (new_dist, v)   ← add improved distance

The min-heap guarantees: when we pop a node, its distance is FINAL.
Why? Any other path to it must go through unvisited nodes,
     all of which have distances ≥ current pop distance.

Time: O((V + E) log V) — the log V comes from heap operations.
Without heap (linear scan): O(V²) — worse for sparse graphs.
```

### Huffman Encoding — Heap Building Optimal Code

```
Character frequencies: {A:45, B:13, C:12, D:16, E:9, F:5}

Min-heap by frequency: [(5,F),(9,E),(12,C),(13,B),(16,D),(45,A)]

Step 1: Pop two smallest (5,F) and (9,E), merge into (14,FE)
  Push (14,FE) back
  heap: [(12,C),(13,B),(14,FE),(16,D),(45,A)]

Step 2: Pop (12,C) and (13,B), merge into (25,CB)
  heap: [(14,FE),(16,D),(25,CB),(45,A)]

...continue until one tree remains...

The heap always provides the two least-frequent nodes
to merge next — guaranteeing the optimal prefix code.
```

---

## 11. Comparison With Related Data Structures

```
              ┌──────────────────────────────────────────────────────┐
              │          "GIVE ME THE BEST ELEMENT" STRUCTURES       │
              └─────────────────────────┬────────────────────────────┘
                                        │
        ┌───────────────────┬───────────┴──────────┬────────────────┐
        ▼                   ▼                      ▼                ▼
      HEAP              SORTED ARRAY          BST (balanced)    SKIP LIST
      ────              ────────────          ──────────────    ─────────
      O(1) peek         O(1) peek             O(log n) min/max  O(log n)
      O(log n) push     O(n) insert           O(log n) insert   O(log n)
      O(log n) pop      O(n) delete           O(log n) delete   insert/del
      O(n) build        O(n log n) build      O(n log n) build  Complex
      No order queries  Full order            Full order        Full order
      O(n) search       O(log n) search       O(log n) search   O(log n)
```

**vs. Sorted Array:** If data never changes, sorted array is better (binary search). For dynamic data with frequent insertions/deletions, heap wins.

**vs. Balanced BST (Red-Black, AVL):** BST maintains full sorted order and supports O(log n) search for any element. Heap only gives O(1) access to the extreme element but is simpler, cache-friendlier, and has better constants. If you only need the top/bottom, heap is superior. If you need order queries ("all elements between 5 and 10"), use BST.

**vs. Stack/Queue:** Stack (LIFO) and Queue (FIFO) are access disciplines with no ordering by value. A heap is a queue ordered by value priority rather than arrival time. Priority queue generalizes both — FIFO is priority by insertion time; LIFO is priority by reverse insertion time.

---

## 12. The Decision Framework

```
Do you need quick access to the most extreme element?
    │
    ├── "I only need the min or max" → HEAP (simpler, faster)
    │
    ├── "I need both min and max instantly" → TWO HEAPS or MIN-MAX HEAP
    │
    ├── "I need kth smallest/largest" → HEAP of size k
    │
    ├── "I need order queries (range, rank)" → BALANCED BST
    │
    └── "I need to process events by time/priority" → MIN-HEAP (priority queue)

Is the data static (loaded once, never changes)?
    └── Yes → Heapify in O(n), then extract as needed

Is the data streaming (arriving one at a time)?
    └── Yes → Push each element O(log n), maintain heap invariant

Do you need to sort?
    └── Yes + O(1) space → HEAP SORT
    └── Yes + stability matters → MERGE SORT (heap sort is unstable)
```

---

## 13. Tips for Long-Term Retention

**1. The hospital triage image**
Picture an emergency room where patients are treated by severity, not arrival time. New patients are assessed and placed in the queue by priority. The most critical is always treated next. This is a max-heap where "priority" = severity. It makes the abstract concrete: FIFO is a regular queue; a heap is the priority-aware version.

**2. Array index arithmetic as a chant**
Parent: `(i-1)/2`. Left child: `2i+1`. Right child: `2i+2`. Repeat these until they're reflex. They're the bridge between the tree visualization and the array implementation — knowing them fluently means you can work in either representation.

**3. Sift Up = insertion's repair, Sift Down = extraction's repair**
These two operations are the entire heap. Push uses sift up (new element at bottom might be too large). Pop uses sift down (replacement at root might be too small). Every other operation composes these two.

**4. "Min-heap for k largest" — the counterintuitive anchor**
This trips everyone up. Anchor it with the bouncer analogy: the min-heap root is the *weakest person in the VIP section* — the eviction candidate. A new element must beat the weakest to get in. The heap is the *filter*, not the *collection*: it maintains exactly k "worthy" elements, constantly evicting the least worthy.

**5. O(n) heapify — the surprising result**
Most people guess O(n log n). The real answer is O(n) because most nodes are leaves (zero sift-down cost), and only a logarithmic few are near the root (maximum cost). The work is bottom-heavy, and there are exponentially more nodes at the bottom. This is the key intuition: **sift-down cost is proportional to depth from bottom, and most nodes are near the bottom.**

**6. Heap = partial order by design**
A heap intentionally knows less than a sorted array. It knows "root is max" and "parent ≥ children." It doesn't know if the left subtree's minimum is larger than the right subtree's maximum. This partial knowledge is exactly calibrated to what's needed — and avoiding the extra work of maintaining full order is what buys the O(log n) operations.

---

A heap is fundamentally a **machine for maintaining access to extremes under constant change**. It doesn't try to know where everything is — it only guarantees that the most important thing is always at hand, and that inserting or removing an element restores that guarantee in logarithmic time. That narrow focus, executed with perfect efficiency through the complete binary tree structure, is what makes the heap indispensable everywhere urgent decisions must be made from a changing pool of candidates.
