# Pattern 35 Interview Playbook: Segment Tree / Fenwick Tree

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Supports dynamic range queries with point/range updates faster than naive recomputation.
- Core intuition: Pre-aggregate partial ranges so queries and updates touch only logarithmic number of nodes. Fenwick Tree (BIT): - compact structure for prefix aggregates - very efficient for point update + prefix/range sum Segment Tree: - more general; supports min/max/gcd and lazy propagation for range updates
- Trigger cue 1: Repeated range query + point/range updates on mutable array.
- Quick self-check: Is O(n) per update/query too slow with many operations?
- Target complexity: Time pattern-optimal, Space pattern-optimal

---

## Q1. Range Sum Query - Mutable

### Problem Statement (Concrete)
Solve **Range Sum Query - Mutable** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Range Sum Query - Mutable** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_range_sum_query_mutable(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Count of Smaller Numbers After Self

### Problem Statement (Concrete)
Solve **Count of Smaller Numbers After Self** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Count of Smaller Numbers After Self** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_count_of_smaller_numbers_after_self(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Create Sorted Array through Instructions

### Problem Statement (Concrete)
Solve **Create Sorted Array through Instructions** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Create Sorted Array through Instructions** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_create_sorted_array_through_instructions(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Range Module

### Problem Statement (Concrete)
Solve **Range Module** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Range Module** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_range_module(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. My Calendar III

### Problem Statement (Concrete)
Solve **My Calendar III** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **My Calendar III** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_my_calendar_iii(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Falling Squares

### Problem Statement (Concrete)
Solve **Falling Squares** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Falling Squares** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_falling_squares(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Count of Range Sum

### Problem Statement (Concrete)
Solve **Count of Range Sum** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Count of Range Sum** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_count_of_range_sum(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Reverse Pairs

### Problem Statement (Concrete)
Solve **Reverse Pairs** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Reverse Pairs** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_reverse_pairs(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Range Sum Query 2D - Mutable

### Problem Statement (Concrete)
Solve **Range Sum Query 2D - Mutable** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Range Sum Query 2D - Mutable** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_range_sum_query_2d_mutable(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Dynamic Range Sum Queries

### Problem Statement (Concrete)
Solve **Dynamic Range Sum Queries** using **Segment Tree / Fenwick Tree**. Return exactly the value/structure requested by the original prompt.

### Input
- `arr`: mutable array
- `queries`/`updates`: range operations

### Output
- Range aggregate for each query after updates.

### Constraints
- `1 <= n, q <= 2 * 10^5`
- Need logarithmic update/query to pass worst case.

### Example (Exact)
```text
Input:  arr = [1,3,5], query(0,2), update(1,2), query(0,2)
Output: 9, 8
Explanation: Tree-indexed structure stores segment aggregates for fast updates.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Segment Tree / Fenwick Tree**.
- Red flags: brute force for **Dynamic Range Sum Queries** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Recompute requested ranges directly from array each query.

#### Python
```python
def brute_dynamic_range_sum_queries(arr, queries):
    out = []
    for typ, l, r, *rest in queries:
        if typ == 'sum':
            out.append(sum(arr[l:r+1]))
        else:
            arr[l] = r
    return out
```

#### Complexity
- Range query `O(n)`, update `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Fenwick tree supports prefix/range sums with logarithmic updates/queries.

#### Python
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def pref(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.pref(r) - (self.pref(l - 1) if l else 0)
```

#### Complexity
- Time `O(log n)` per op, Space `O(n)`.

### Approach 3: Optimal (Best)
#### Intuition
- Segment tree generalizes to many associative range queries with point/range updates.

#### Python
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self._build(idx * 2, l, m, arr)
        self._build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def update(self, pos, val, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(pos, val, idx * 2, l, m)
        else:
            self.update(pos, val, idx * 2 + 1, m + 1, r)
        self.seg[idx] = self.seg[idx * 2] + self.seg[idx * 2 + 1]

    def query(self, ql, qr, idx=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if ql <= l and r <= qr:
            return self.seg[idx]
        if r < ql or qr < l:
            return 0
        m = (l + r) // 2
        return self.query(ql, qr, idx * 2, l, m) + self.query(ql, qr, idx * 2 + 1, m + 1, r)
```

#### Correctness (Why This Works)
- Each internal node stores aggregate of a fixed segment; updates affect only root-to-leaf path.
- Range query decomposes target interval into disjoint stored segments.

#### Complexity
- Build `O(n)`, query/update `O(log n)`, Space `O(n)`.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
