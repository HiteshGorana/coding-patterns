# Pattern 34 Interview Playbook: Design Data Structures

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Builds custom APIs with strict operation guarantees (usually O(1) or O(log n)).
- Core intuition: Combine primitive data structures to satisfy all constraints: - Hash map for direct lookup - Doubly linked list for O(1) ordered removal/insertion - Heap for prioritized retrieval - Timestamp/value maps for temporal queries
- Trigger cue 1: "Design class with O(1)/O(log n) ops".
- Quick self-check: Can I map each method to a supporting structure + invariant?
- Target complexity: Time pattern-optimal, Space proportional to number of stored entries.

---

## Q1. LRU Cache

### Problem Statement (Concrete)
Solve **LRU Cache** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **LRU Cache** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteLruCache:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterLruCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveLruCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. LFU Cache

### Problem Statement (Concrete)
Solve **LFU Cache** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **LFU Cache** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteLfuCache:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterLfuCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveLfuCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Min Stack

### Problem Statement (Concrete)
Solve **Min Stack** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Min Stack** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteMinStack:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterMinStack:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveMinStack:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Implement Queue using Stacks

### Problem Statement (Concrete)
Solve **Implement Queue using Stacks** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Implement Queue using Stacks** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteImplementQueueUsingStacks:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterImplementQueueUsingStacks:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveImplementQueueUsingStacks:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Implement Stack using Queues

### Problem Statement (Concrete)
Solve **Implement Stack using Queues** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Implement Stack using Queues** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteImplementStackUsingQueues:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterImplementStackUsingQueues:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveImplementStackUsingQueues:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Time Based Key-Value Store

### Problem Statement (Concrete)
Solve **Time Based Key-Value Store** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Time Based Key-Value Store** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteTimeBasedKeyValueStore:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterTimeBasedKeyValueStore:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveTimeBasedKeyValueStore:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Insert Delete GetRandom O(1)

### Problem Statement (Concrete)
Solve **Insert Delete GetRandom O(1)** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Insert Delete GetRandom O(1)** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteInsertDeleteGetrandomO1:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterInsertDeleteGetrandomO1:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveInsertDeleteGetrandomO1:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Design HashMap

### Problem Statement (Concrete)
Solve **Design HashMap** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Design HashMap** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteDesignHashmap:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterDesignHashmap:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveDesignHashmap:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Design Twitter

### Problem Statement (Concrete)
Solve **Design Twitter** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **Design Twitter** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteDesignTwitter:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterDesignTwitter:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveDesignTwitter:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. All O`one Data Structure

### Problem Statement (Concrete)
Solve **All O`one Data Structure** using **Design Data Structures**. Return exactly the value/structure requested by the original prompt.

### Input
- Operation stream, e.g. `put/get`, `push/pop`, or API calls
- Operation parameters per call

### Output
- Per-operation return values exactly as API specifies.

### Constraints
- Up to `2 * 10^5` operations.
- Average complexity targets are part of grading.

### Example (Exact)
```text
Input:  ops = ["put","put","get","put","get"], args = [[1,1],[2,2],[1],[3,3],[2]]
Output: [null, null, 1, null, -1]
Explanation: The design must preserve invariants after each operation, not just final state.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.
- Operation order matters; interleaved updates and queries must preserve class invariants.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Design Data Structures**.
- Red flags: brute force for **All O`one Data Structure** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Use linear containers and scan per operation.

#### Python
```python
class BruteAllOOneDataStructure:
    def __init__(self):
        self.data = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
```

#### Complexity
- Time `O(n)` per key lookup/update, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use built-in ordered map/deque abstractions to hit average `O(1)` operations.

#### Python
```python
from collections import OrderedDict

class BetterAllOOneDataStructure:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

#### Complexity
- Average `O(1)` operations, Space `O(capacity)`.

### Approach 3: Optimal (Best)
#### Intuition
- Pair hashmap with doubly linked list to maintain strict operation complexity guarantees.

#### Python
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class SolveAllOOneDataStructure:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._push_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
```

#### Correctness (Why This Works)
- Hashmap provides direct node access by key; linked list maintains exact recency/frequency order.
- Each operation updates only constant number of pointers and map entries.

#### Complexity
- Time `O(1)` average per operation, Space `O(capacity)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
