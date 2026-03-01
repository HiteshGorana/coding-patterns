# Pattern 34: Design Data Structures

## Diagram + Intuition

### Pattern Diagram
```text
API constraints -> combine DS
hash map + DLL / heap / stack / queue
```

### Read-the-Question Trigger Cues
- "Design class with O(1)/O(log n) ops".

### Intuition Anchor
- "No single DS fits all methods; compose two or more."

### 3-Second Pattern Check
- Can I map each method to a supporting structure + invariant?

## What This Pattern Solves
Builds custom APIs with strict operation guarantees (usually O(1) or O(log n)).

## Recognition Signals
- Prompt asks to implement class with methods and complexity constraints.
- Need mixed operations like insert/delete/get-random/min/max/recent access.
- Stateful object with repeated calls.

## Core Intuition
Combine primitive data structures to satisfy all constraints:
- Hash map for direct lookup
- Doubly linked list for O(1) ordered removal/insertion
- Heap for prioritized retrieval
- Timestamp/value maps for temporal queries

## Step-by-Step Design Workflow
1. List required methods and target complexity.
2. Choose underlying structures for each method.
3. Define invariants (what must always remain true).
4. Implement helper operations first.
5. Analyze each method complexity.

## Detailed Example (LRU Cache)
Goal: `get/put` in `O(1)` with eviction of least recently used key.
1. Hash map: `key -> node`.
2. Doubly linked list stores usage order (head most recent, tail least recent).
3. `get`: move node to front.
4. `put`: insert/update front; if capacity exceeded, remove tail and delete map entry.

## Complexity
- Usually per operation as required by prompt (`O(1)` for LRU).
- Space: proportional to number of stored entries.

## Python Template (LRU Skeleton)
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()  # dummy head
        self.tail = Node()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # add helper methods: remove(node), insert_front(node), get, put
```

## Common Pitfalls
- Violating complexity constraints with hidden linear scans.
- Forgetting to keep map and linked list synchronized.
- Edge-case bugs around empty/full structure boundaries.
- Missing duplicate-key update behavior.

## Variations
- Min Stack
- Time Based Key-Value Store
- RandomizedSet
- LFU Cache (more complex invariants)

## Interview Tips
- Start with API + complexity table before coding.
- Speak invariants explicitly to avoid implementation drift.
- Use dummy head/tail nodes to simplify linked list edge cases.

## Practice Problems
- LRU Cache
- Min Stack
- Insert Delete GetRandom O(1)
- Time Based Key-Value Store
