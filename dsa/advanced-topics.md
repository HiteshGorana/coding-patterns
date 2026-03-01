# Advanced / Nice-to-have (Interview-Ready Guide)

Using `[TOPIC] = Advanced / Nice-to-have`.

## 0) Scope (Checklist)
- [x] Segment tree / Fenwick tree (range queries)
- [x] Sparse table (RMQ)
- [x] Monotonicity + convex hull trick (rare)
- [x] Deeper string structures (suffix array/tree - rare)
- [x] Flow algorithms (very rare unless specialized)

## 1) Foundations
These are specialized tools for high-constraint or niche interview problems.

Core terms:
- Point update, range query, lazy propagation
- Prefix frequency tree (Fenwick)
- Idempotent query (`min/max/gcd`) for sparse table
- Residual graph, augmenting path (flow)

Mental model:
- Use only when simpler patterns fail on constraints.

## 2) How it works
Cause-effect:
1. Fenwick/segment tree maintain aggregated range info under updates.
2. Sparse table preprocesses powers of two for static range queries.
3. Convex hull trick optimizes DP with linear transitions.
4. Max flow repeatedly augments feasible path capacity.

Tiny trace (Fenwick prefix sum):
- Add value at index 5 updates multiple tree indices via `i += i&-i`.
- Query prefix(7) accumulates via `i -= i&-i`.
- Range sum `[l..r] = pref(r)-pref(l-1)`.

## 3) Patterns (Interview Templates)
1. Segment tree for dynamic range min/sum/max
2. Fenwick tree for prefix sums and inversion count
3. Sparse table for static RMQ
4. CHT for `dp[i] = min/max(m*x+b)` transitions
5. Dinic/Edmonds-Karp for max flow/min cut

Invariants:
- Tree node stores correct aggregate for interval.
- Lazy tags represent pending updates correctly.
- Flow conservation holds at intermediate nodes.

Signals:
- "Many range queries + updates"
- "Static array with many RMQ queries"
- "DP transition looks linear in `x`"
- "Capacity-limited routing/matching"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Range Sum Query Mutable
- Approach: Fenwick or segment tree.

2. Medium: Count of Smaller Numbers After Self
- Approach: Fenwick with coordinate compression.

3. Medium: Static RMQ queries
- Approach: sparse table preprocess.

4. Hard: DP optimization with lines
- Approach: convex hull trick or Li Chao tree.

5. Hard: Maximum Bipartite Matching / Max Flow
- Approach: build flow network and run max flow.

## 5) Why & What-if
Edge cases:
- Coordinate compression for large value ranges
- 1-indexed vs 0-indexed Fenwick confusion
- Overflow in aggregated sums

Pitfalls:
- Incorrect lazy propagation push/pull logic
- Wrong segment boundaries
- Overusing advanced DS where simpler methods pass

Why it works:
- Data structures preserve partial aggregates, avoiding full rescans.

Variations:
- Persistent segment tree for versioned queries.
- Min-cost max-flow for weighted assignments.

## 6) Complexity and Tradeoffs
- Fenwick: update/query `O(log n)`, space `O(n)`
- Segment tree: update/query `O(log n)`, space `O(4n)`
- Sparse table: preprocess `O(n log n)`, query `O(1)` (idempotent ops)
- Max flow (Dinic): roughly `O(EV^2)` worst-case, often faster in practice

Tradeoffs:
- Powerful but implementation-heavy and bug-prone.

## 7) Real-world uses
- Analytics dashboards with mutable range metrics
- Ranking/inversion statistics
- Network throughput optimization
- Advanced text indexing/search

## 8) Comparisons
- Fenwick vs segment tree:
  - Fenwick simpler for prefix-like operations.
  - Segment tree supports wider operation range and lazy updates.
- Sparse table vs segment tree:
  - Sparse table for static arrays.
  - Segment tree for updates.

## 9) Retention
Cheat sheet:
- Dynamic range sum -> Fenwick.
- Dynamic complex range query/update -> segment tree.
- Static RMQ -> sparse table.
- Capacity constraints -> flow.

Recall hooks:
- "Static data: preprocess hard, query fast."
- "Updates required: tree structures."

Practice (10):
1. Easy: Range Sum Query Mutable
2. Easy: Range Sum Query 2D Immutable (prefix baseline)
3. Medium: Count of Smaller Numbers After Self
4. Medium: My Calendar II (segment/tree-line-sweep hybrid)
5. Medium: Falling Squares
6. Hard: Sliding Window Median (ordered DS insight)
7. Hard: Dynamic RMQ with updates
8. Hard: Minimum Cost to Connect with constraints (flow/MST variants)
9. Hard: Assignment Problem (flow/bitmask DP)
10. Hard: Advanced DP optimization with Li Chao/CHT
