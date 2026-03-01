# Pattern 13: K-Way Merge (Heap)

## Diagram + Intuition

### Pattern Diagram
```text
k sorted lists
push each head -> pop min -> push next from same list
```

### Read-the-Question Trigger Cues
- Merge many sorted sources.
- Need global smallest among k frontiers.

### Intuition Anchor
- "Only k current heads matter at any time."

### 3-Second Pattern Check
- Is each source already sorted?

## What This Pattern Solves
Merges multiple sorted sequences efficiently and processes globally smallest elements in order.

## Recognition Signals
- Input consists of `k` sorted lists/streams.
- Need merged sorted output or smallest range covering all lists.
- Brute force concatenation + sort is too expensive.

## Core Intuition
Keep one active pointer per list and use min-heap keyed by current value.  
At each step, extract smallest head and advance only that list.

## Step-by-Step Method
1. Push first element of each non-empty list with metadata `(value, list_id, index)`.
2. Pop smallest element from heap and append/process it.
3. Advance in same list; push next element if exists.
4. Continue until heap is empty (or condition met).

## Detailed Example (Merge K Sorted Lists)
Lists: `[1,4,5]`, `[1,3,4]`, `[2,6]`
1. Heap starts with first items: `1,1,2`.
2. Pop smallest, push next from that list.
3. Repeating this yields sorted stream: `1,1,2,3,4,4,5,6`.

## Complexity
- Let total elements be `N`, number of lists `k`.
- Time: `O(N log k)`
- Space: `O(k)` heap (excluding output)

## Python Template
```python
import heapq

def merge_k_sorted(lists):
    heap = []
    for i, arr in enumerate(lists):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    out = []
    while heap:
        val, list_id, idx = heapq.heappop(heap)
        out.append(val)
        next_idx = idx + 1
        if next_idx < len(lists[list_id]):
            nxt = lists[list_id][next_idx]
            heapq.heappush(heap, (nxt, list_id, next_idx))

    return out
```

## Common Pitfalls
- Losing list/index metadata, making advancement impossible.
- Pushing all elements initially (defeats `O(k)` heap advantage).
- Not handling empty lists.
- Comparator errors when values equal and metadata types differ.

## Variations
- Merge K Sorted Linked Lists
- Kth smallest across sorted lists/matrix
- Smallest range covering elements from K lists
- External merge of sorted files/chunks

## Interview Tips
- Mention this as "multiway merge, same idea as merge step generalized."
- State `O(N log k)` clearly and contrast with `O(N log N)`.
- Explain tie handling in heap tuples.

## Practice Problems
- Merge k Sorted Lists
- Find K Pairs with Smallest Sums
- Smallest Range Covering Elements from K Lists
