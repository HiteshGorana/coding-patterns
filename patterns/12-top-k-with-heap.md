# Pattern 12: Top K with Heap

## Diagram + Intuition

### Pattern Diagram
```text
keep heap size = k
candidate better than root? replace root
```

### Read-the-Question Trigger Cues
- "top k", "kth largest/smallest", streaming k-best.

### Intuition Anchor
- "Maintain only what can still be in final top-k."

### 3-Second Pattern Check
- Can partial ordering beat full sorting here?

## What This Pattern Solves
Efficiently maintains the `k` largest/smallest/frequent elements without full sorting.

## Recognition Signals
- Prompt says "top k", "kth largest", "k closest", "streaming top values".
- Need partial ordering, not full sorted output.
- Large `n`, small `k` where `O(n log n)` sort is avoidable.

## Core Intuition
Use a heap of size `k`:
- for k largest, keep min-heap so smallest of top-k sits at root
- when new value beats root, replace root

This ensures heap always stores best `k` candidates seen so far.

## Step-by-Step Method
1. Initialize empty heap.
2. Push first `k` elements.
3. For each remaining element:
   - compare with heap root
   - if better candidate, pop root and push new element
4. Heap contains top `k` answers.

## Detailed Example (Kth Largest Element)
For `nums = [3,2,1,5,6,4], k = 2`:
1. Heap starts with `[3,2]` -> root `2`.
2. Value `1` ignored (not larger than root).
3. Value `5` replaces `2`, heap becomes `[3,5]`.
4. Value `6` replaces `3`, heap becomes `[5,6]`.
5. Value `4` ignored. Root `5` is 2nd largest.

## Complexity
- Time: `O(n log k)`
- Space: `O(k)` (plus maps when counting frequencies)

## Python Template
```python
import heapq

def top_k_largest(nums, k):
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap  # unsorted top-k
```

## Common Pitfalls
- Using max-heap for k largest without controlling size (wastes memory/time).
- Forgetting output heap is not fully sorted.
- For frequency problems, not pairing `(freq, value)` correctly.
- Mistakes with tuple ordering in Python heap.

## Variations
- Top K Frequent Elements (heap over frequency map)
- K Closest Points to Origin
- Kth Smallest in Sorted Matrix (heap-based merge)
- Streaming median with two heaps

## Interview Tips
- Compare with sorting: `O(n log n)` vs `O(n log k)`.
- Mention when quickselect may be better average-case.
- Clarify whether final answer needs sorted order.

## Practice Problems
- Kth Largest Element in an Array
- Top K Frequent Elements
- K Closest Points to Origin
- Find Median from Data Stream
