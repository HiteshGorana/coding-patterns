# Pattern 35: Segment Tree / Fenwick Tree

## Diagram + Intuition

### Pattern Diagram
```text
array
 -> tree of aggregated ranges
query/update in O(log n)
```

### Read-the-Question Trigger Cues
- Repeated range query + point/range updates on mutable array.

### Intuition Anchor
- "Pre-aggregate partial ranges for fast incremental changes."

### 3-Second Pattern Check
- Is O(n) per update/query too slow with many operations?

## What This Pattern Solves
Supports dynamic range queries with point/range updates faster than naive recomputation.

## Recognition Signals
- Many operations of:
  - update element(s)
  - query range sum/min/max
- Need better than `O(n)` per query/update on mutable array.

## Core Intuition
Pre-aggregate partial ranges so queries and updates touch only logarithmic number of nodes.

Fenwick Tree (BIT):
- compact structure for prefix aggregates
- very efficient for point update + prefix/range sum

Segment Tree:
- more general; supports min/max/gcd and lazy propagation for range updates

## Fenwick Tree Steps
1. Store partial sums in `bit[1..n]`.
2. Point update adds delta along index jumps by lowbit.
3. Prefix query accumulates while moving index downward by lowbit.
4. Range sum = `prefix(r) - prefix(l-1)`.

## Complexity
- Fenwick: `O(log n)` update/query, `O(n)` space
- Segment tree: `O(log n)` update/query, `O(n)` (typically `4n`) space

## Python Template (Fenwick)
```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, delta):
        idx += 1  # 0-based external, 1-based internal
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx):
        idx += 1
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def range_sum(self, l, r):
        return self.prefix_sum(r) - (self.prefix_sum(l - 1) if l > 0 else 0)
```

## Common Pitfalls
- 0-based vs 1-based indexing confusion.
- Forgetting update should add delta, not assign absolute value (unless converted).
- Choosing Fenwick when operation is non-invertible and segment tree is needed.
- Incorrect lazy propagation for range updates in segment tree.

## Variations
- Range Sum Query - Mutable
- Count of Smaller Numbers After Self (Fenwick + compression)
- Segment tree with lazy propagation for range add/range sum
- Order statistics with BIT on frequency array

## Interview Tips
- Choose Fenwick first for sum-like operations due to simpler implementation.
- Choose segment tree for flexible operations and range updates.
- State complexity and indexing convention before coding.

## Practice Problems
- Range Sum Query - Mutable
- Count of Smaller Numbers After Self
- Create Sorted Array through Instructions
- Segment tree range query/update exercises
