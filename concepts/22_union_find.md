# Union-Find (Disjoint Set Union): A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

**Union-Find** (also called **Disjoint Set Union** or **DSU**) is a data structure that efficiently tracks a collection of elements partitioned into **non-overlapping groups** (disjoint sets), supporting two core operations: merging two groups together and determining whether two elements belong to the same group.

```
DISJOINT SETS — the problem Union-Find solves:

  Initial: {0} {1} {2} {3} {4} {5}   ← 6 separate groups

  After union(0,1):  {0,1} {2} {3} {4} {5}
  After union(2,3):  {0,1} {2,3} {4} {5}
  After union(0,2):  {0,1,2,3} {4} {5}
  After union(4,5):  {0,1,2,3} {4,5}

  find(0) == find(3)?  YES  (both in {0,1,2,3}) ✅
  find(0) == find(4)?  NO   (different groups)   ✅
```

**Core components:**

- **Element** — each item tracked by the structure, represented as an integer index 0..n-1
- **Set / Component** — a group of elements; initially each element is its own set
- **Representative (root)** — one designated element that "speaks for" its entire set; two elements are in the same set iff they have the same representative
- **parent[ ]** — the core array; `parent[i]` = the parent of element i in the tree structure; root points to itself: `parent[root] = root`
- **rank[ ] / size[ ]** — auxiliary array tracking tree height (rank) or group size; used to keep trees balanced during union
- **find(x)** — returns the representative (root) of x's set by following parent pointers to the root
- **union(x, y)** — merges the sets containing x and y by making one root point to the other
- **Path compression** — optimization in find: flatten the tree by pointing all traversed nodes directly to the root
- **Union by rank/size** — optimization in union: always attach the smaller tree under the larger to keep height minimal

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # parent[i] = i initially (each is its own root)
        self.rank   = [0] * n          # rank[i] = 0 initially (all single nodes)
        self.components = n            # track number of distinct sets

    def find(self, x):                 # return root of x's set
        ...

    def union(self, x, y):             # merge sets containing x and y
        ...
```

---

## 2. The Physical Analogy: Club Membership

Imagine a university where students form clubs. Initially every student is their own "club of one." When two clubs merge, they pick one president to represent the entire merged club. To check if two students are in the same club, ask each "who is your president?" — if the same person answers, they're in the same club.

```
CLUB ANALOGY:

  Initially:
    Alice → [Alice]    Bob → [Bob]    Carol → [Carol]    Dave → [Dave]

  Alice and Bob merge clubs:
    Bob → Alice (Alice becomes president)
    Alice → [Alice]  (Alice is president, represents {Alice, Bob})

  Carol and Dave merge clubs:
    Dave → Carol (Carol becomes president)
    Carol → [Carol]  (Carol represents {Carol, Dave})

  The two super-clubs merge:
    Carol → Alice (Alice becomes president of everyone)

  Who is Dave's president?
    Dave → Carol → Alice   ← follow the chain to find the president

  Are Bob and Dave in the same club?
    Bob's president:  Bob → Alice
    Dave's president: Dave → Carol → Alice
    Same president (Alice) → SAME CLUB ✅

PATH COMPRESSION optimization:
  After asking "who is Dave's president?" and following Dave→Carol→Alice,
  set Dave's president directly to Alice.
  Next time: Dave → Alice (one hop instead of two).
  The tree flattens over time.
```

---

## 3. The Internal Structure — Trees of Trees

Union-Find represents each set as a **tree** where every node points to its parent, and the root points to itself. The key insight: to identify the set, you only need the root — so `find(x)` climbs to the root.

```
INTERNAL REPRESENTATION after several unions:

  parent = [0, 0, 0, 2, 4, 4]
  index:    0  1  2  3  4  5

  TREE VISUALIZATION:

      0          4
     / \        / \
    1   2      5   (root)
        |
        3

  Sets: {0, 1, 2, 3} with root 0
        {4, 5}       with root 4

  find(3): 3 → parent[3]=2 → parent[2]=0 → parent[0]=0 (root!) → return 0
  find(5): 5 → parent[5]=4 → parent[4]=4 (root!) → return 4
  find(3) == find(5)? 0 == 4? NO → different sets ✅

ROOT SELF-REFERENCE:
  parent[root] == root   ← this is how we detect the root
  Stop climbing when parent[x] == x.
```

---

## 4. Find — The Core Lookup Operation

### Naive Find (No Optimization)

```python
def find_naive(self, x):
    while self.parent[x] != x:   # climb until root
        x = self.parent[x]
    return x
```

```
TRACE: find(3) with parent=[0,0,0,2,4,4]

  x=3: parent[3]=2 ≠ 3 → x=2
  x=2: parent[2]=0 ≠ 2 → x=0
  x=0: parent[0]=0 == 0 → RETURN 0 ✅

TIME: O(h) where h = height of tree
  Unoptimized: h can be O(n) (chain tree) → O(n) per find
  With union by rank: h = O(log n) → O(log n) per find
  With path compression: amortized O(α(n)) per find
```

### Path Compression — The Critical Optimization

```
PATH COMPRESSION: After finding the root, make every traversed node
                  point DIRECTLY to the root.

BEFORE find(3):          AFTER find(3) with path compression:

      0                        0
     / \                     / | \
    1   2                   1  2  3    ← 3 now points directly to 0!
        |
        3

Every future operation on 3 now costs O(1) instead of O(3).
The tree FLATTENS automatically over time.
```

**Recursive implementation (path compression):**

```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])   # ← path compression
    return self.parent[x]

HOW IT WORKS:
  find(3):
    parent[3]=2 ≠ 3 → recurse: find(2)
      parent[2]=0 ≠ 2 → recurse: find(0)
        parent[0]=0 == 0 → return 0
      parent[2] = 0  ← PATH COMPRESSION: point 2 directly to root
      return 0
    parent[3] = 0  ← PATH COMPRESSION: point 3 directly to root
    return 0

  After: parent = [0, 0, 0, 0, 4, 4]
  Both 2 and 3 now point directly to root 0. ✅
```

**Iterative implementation (two-pass path compression):**

```python
def find(self, x):
    # Pass 1: Find root
    root = x
    while self.parent[root] != root:
        root = self.parent[root]

    # Pass 2: Path compression — point everything to root
    while self.parent[x] != root:
        next_node = self.parent[x]
        self.parent[x] = root     # point directly to root
        x = next_node

    return root
```

---

## 5. Union — The Merge Operation

### Naive Union (No Optimization)

```python
def union_naive(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
        self.parent[root_x] = root_y   # arbitrarily attach x's tree under y's
```

```
PROBLEM WITH NAIVE UNION:
  If we always attach root_x under root_y, trees can degenerate
  into chains (linked lists).

  union(0,1): parent[0]=1    → tree: 1←0
  union(1,2): parent[1]=2    → tree: 2←1←0
  union(2,3): parent[2]=3    → tree: 3←2←1←0
  union(3,4): parent[3]=4    → tree: 4←3←2←1←0

  find(0) must traverse 4 levels → O(n) ❌
```

### Union by Rank

```
STRATEGY: Always attach the tree with SMALLER RANK (height)
          under the tree with LARGER RANK.
          This keeps the tree height O(log n).

RANK DEFINITION: Upper bound on the height of the tree.
  Initial rank: 0 (single nodes)
  When merging two trees of EQUAL rank: attach one under other, increment rank.
  When merging trees of DIFFERENT rank: attach smaller under larger, rank unchanged.

def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x == root_y:
        return False          # already in same set

    # Attach smaller rank tree under larger rank tree
    if self.rank[root_x] < self.rank[root_y]:
        root_x, root_y = root_y, root_x   # ensure root_x has >= rank

    self.parent[root_y] = root_x          # attach y's tree under x's root

    if self.rank[root_x] == self.rank[root_y]:
        self.rank[root_x] += 1            # only increment when equal

    self.components -= 1                  # one fewer component
    return True

RANK UPDATE RULE:
  rank[x] > rank[y]: attach y under x → rank[x] unchanged ✅
  rank[x] < rank[y]: attach x under y → rank[y] unchanged ✅
  rank[x] == rank[y]: attach y under x → rank[x]++ (tree gets taller) ✅
```

**Visual trace of union by rank:**

```
TRACE: union(0,1), union(2,3), union(0,2)

Initial:  [0] [1] [2] [3]   ranks=[0,0,0,0]

union(0,1): rank[0]==rank[1]==0 → attach 1 under 0, rank[0]++
  parent=[0,0,2,3], rank=[1,0,0,0]
  Tree:   0      2      3
          |
          1

union(2,3): rank[2]==rank[3]==0 → attach 3 under 2, rank[2]++
  parent=[0,0,2,2], rank=[1,0,1,0]
  Tree:   0      2
          |      |
          1      3

union(0,2): rank[0]==rank[2]==1 → attach 2 under 0, rank[0]++
  parent=[0,0,0,2], rank=[2,0,1,0]
  Tree:     0
           / \
          1   2
              |
              3

  Height = 2 = O(log 4) ✅  (not 3 as naive would give)

find(3): 3→2→0  (2 hops vs potentially 3 with naive) ✅
```

### Union by Size (Alternative to Rank)

```python
def __init__(self, n):
    self.parent = list(range(n))
    self.size   = [1] * n          # each component starts with size 1

def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x == root_y: return False

    # Attach smaller tree under larger tree
    if self.size[root_x] < self.size[root_y]:
        root_x, root_y = root_y, root_x

    self.parent[root_y] = root_x           # smaller under larger
    self.size[root_x] += self.size[root_y] # update size of new root
    self.components -= 1
    return True

ADVANTAGE OF SIZE OVER RANK:
  size gives the EXACT count of elements in each component.
  rank is just an approximation of height.
  Use size when you need component sizes.
  Use rank when you only need connectivity.
```

---

## 6. The Combined Algorithm — Full Implementation

```python
class UnionFind:
    def __init__(self, n):
        self.parent     = list(range(n))
        self.rank       = [0] * n
        self.size       = [1] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False                 # already connected

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x]  += self.size[root_y]

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def component_size(self, x):
        return self.size[self.find(x)]
```

---

## 7. Complexity Analysis — The Inverse Ackermann Function

```
WITHOUT ANY OPTIMIZATION:
  find:  O(n) worst case (chain tree)
  union: O(n) (because of find)

WITH UNION BY RANK ONLY:
  Tree height bounded by O(log n)
  find:  O(log n)
  union: O(log n)

WITH PATH COMPRESSION ONLY:
  Amortized O(log n) per operation

WITH BOTH (path compression + union by rank):
  Amortized O(α(n)) per operation
  α = inverse Ackermann function

THE INVERSE ACKERMANN FUNCTION:
  α(n) is the inverse of the incredibly fast-growing Ackermann function.

  α(n) ≤ 4 for ALL practical values of n:
    α(1) = 0
    α(2) = 1
    α(4) = 2
    α(16) = 3
    α(65536) = 4
    α(2^65536) = 5     ← more atoms than in the observable universe

  For ANY n you will ever encounter in practice: α(n) ≤ 4.

  MEANING: find and union run in EFFECTIVELY O(1) amortized time.

  n operations on n elements: O(n × α(n)) ≈ O(n × 4) = O(n) total.

WHY NOT JUST SAY O(1)?
  Technically α(n) is not constant — it grows, just infinitely slowly.
  In theory: O(α(n)).
  In practice: O(1).
  In interviews: "nearly O(1) amortized" or "effectively O(1)".
```

---

## 8. Complete Step-by-Step Trace

Building Union-Find for n=6 with operations: union(0,1), union(2,3), union(1,2), union(4,5), union(3,4), then check connected(0,5).

```
INITIAL STATE:
  parent = [0, 1, 2, 3, 4, 5]
  rank   = [0, 0, 0, 0, 0, 0]
  size   = [1, 1, 1, 1, 1, 1]
  components = 6

  Trees: [0] [1] [2] [3] [4] [5]

────────────────────────────────
union(0, 1):
  find(0)=0, find(1)=1  (different roots)
  rank[0]==rank[1]==0 → attach 1 under 0, rank[0]++

  parent = [0, 0, 2, 3, 4, 5]
  rank   = [1, 0, 0, 0, 0, 0]
  size   = [2, 1, 1, 1, 1, 1]
  components = 5

  Trees:  0    [2] [3] [4] [5]
          |
          1

────────────────────────────────
union(2, 3):
  find(2)=2, find(3)=3
  rank[2]==rank[3]==0 → attach 3 under 2, rank[2]++

  parent = [0, 0, 2, 2, 4, 5]
  rank   = [1, 0, 1, 0, 0, 0]
  size   = [2, 1, 2, 1, 1, 1]
  components = 4

  Trees:  0    2    [4] [5]
          |    |
          1    3

────────────────────────────────
union(1, 2):
  find(1): parent[1]=0, parent[0]=0 → root=0
  find(2): parent[2]=2 → root=2
  rank[0]==rank[2]==1 → attach 2 under 0, rank[0]++

  parent = [0, 0, 0, 2, 4, 5]
  rank   = [2, 0, 1, 0, 0, 0]
  size   = [4, 1, 2, 1, 1, 1]
  components = 3

  Trees:    0        [4] [5]
           / \
          1   2
              |
              3

────────────────────────────────
union(4, 5):
  find(4)=4, find(5)=5
  rank equal → attach 5 under 4, rank[4]++

  parent = [0, 0, 0, 2, 4, 4]
  rank   = [2, 0, 1, 0, 1, 0]
  size   = [4, 1, 2, 1, 2, 1]
  components = 2

  Trees:    0        4
           / \       |
          1   2      5
              |
              3

────────────────────────────────
union(3, 4):
  find(3): parent[3]=2, parent[2]=0, parent[0]=0 → root=0
    PATH COMPRESSION: parent[3]=0, parent[2]=0 (already 0)
  find(4): parent[4]=4 → root=4
  rank[0]=2 > rank[4]=1 → attach 4 under 0

  parent = [0, 0, 0, 0, 0, 4]   ← 3 now points to 0 (path compression!)
  rank   = [2, 0, 1, 0, 1, 0]
  size   = [6, 1, 2, 1, 2, 1]
  components = 1

  Tree:       0
           /  |  \ \
          1   2   4  3    ← 3 path-compressed directly to 0!
              |   |
              (3 moved) 5

────────────────────────────────
connected(0, 5)?
  find(0)=0
  find(5): parent[5]=4, parent[4]=0 → root=0
    PATH COMPRESSION: parent[5]=0

  find(0)==find(5)? 0==0 → TRUE ✅
  All 6 elements are now in one component.
```

---

## 9. The "Why" Questions

### Why does path compression not break correctness?

```
CORRECTNESS REQUIREMENT: find(x) must return the same root
  as before path compression.

PATH COMPRESSION changes ONLY the parent pointers along the path.
It does NOT change which element is the root.
The root still points to itself: parent[root] == root.

BEFORE compression: 3→2→0  (root is 0)
AFTER  compression: 3→0    (root is still 0)

The SET membership is unchanged — 3 still belongs to the set with root 0.
We just changed HOW we reach that root (shorter path).

INVARIANT maintained: find(x) returns the root of x's set.
The root identity never changes — only the path to it shortens. ✅
```

### Why does union by rank guarantee O(log n) height?

```
CLAIM: A tree of rank r contains at least 2^r nodes.

PROOF BY INDUCTION:
  Base: rank 0 tree has 1 = 2^0 node ✅

  Inductive step: Trees of rank r are created by merging two trees
    of rank r-1 (only way rank increases — when both equal).
    By induction, each rank r-1 tree has ≥ 2^(r-1) nodes.
    Merged tree has ≥ 2^(r-1) + 2^(r-1) = 2^r nodes ✅

CONSEQUENCE:
  If tree has rank r: it has ≥ 2^r nodes.
  Total nodes n ≥ 2^r → r ≤ log₂(n).
  Maximum rank (= maximum height) = O(log n). ✅

WHY EQUAL RANK MERGE INCREASES RANK?
  Two equal-rank trees merge → one becomes a child of the other.
  The parent's height increases by 1 (the child adds a level).
  So we increment rank to reflect the taller tree.

WHY DIFFERENT RANK MERGE DOESN'T INCREASE RANK?
  Smaller rank tree attaches BELOW the larger.
  The larger tree's maximum depth is unchanged — we added nodes to
  an existing branch, not to the deepest branch.
  So rank stays the same. ✅
```

### Why does the combination of both optimizations give O(α(n))?

```
INTUITION (not full proof — the full proof is complex):

  Path compression makes trees "flat" — future finds are fast.
  Union by rank makes trees "balanced" — finds are already reasonably fast.

  ALONE:
    Path compression alone: O(log n) amortized
    Union by rank alone: O(log n) worst case

  TOGETHER:
    Path compression flattens trees over time.
    Union by rank ensures trees don't get tall in the first place.
    Tall trees (from union by rank) get flattened the first time they're traversed.
    After flattening, they stay flat.

    The interaction: path compression "pays" for its work by reducing
    future work. Union by rank ensures there's not much to pay in the
    first place. Together they achieve O(α(n)) amortized.

    This was proven by Tarjan in 1975.
    The proof uses a potential function argument showing total work
    across all operations is O(n × α(n)).

THE PRACTICAL TAKEAWAY:
  With both optimizations: Union-Find is essentially O(1) per operation.
  This is one of the most efficient data structures ever devised
  for its specific problem. ✅
```

---

## 10. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| union(x, x) — same element | find(x)==find(x) → already same set, no-op, return False |
| find on uninitialized element | Array bounds error; must validate 0 ≤ x < n |
| Trying to union elements from 0 to n-1 where n is large | Only affects memory O(n); time per operation still O(α(n)) |
| Calling union after all elements are in one set | No-op (same root); components stays at 1; correctly returns False |
| Path compression makes rank stale | Rank becomes an overestimate; this is intentional and fine — rank is just an upper bound, not exact height |
| Weighted union-find (weighted edges) | Requires storing weight offsets during path compression; used for "weighted quick union" variant |
| Dynamic elements (add new elements) | Extend parent/rank/size arrays; new element starts as its own component |
| Deleting an element from a set | Standard Union-Find doesn't support deletion; need "virtual nodes" or offline processing |
| Rollback (undo unions) | Need a stack to record union history; path compression must be disabled (breaks rollback) |
| Checking if a graph has a cycle | Union edges; if union(u,v) returns False → u,v already connected → cycle exists |

### Union-Find Without Path Compression (for Rollback)

```
PROBLEM: Some algorithms need to UNDO unions (offline graph problems).

PATH COMPRESSION breaks rollback because it modifies parent pointers
of non-direct ancestors — hard to undo efficiently.

SOLUTION: Use UNION BY RANK only (no path compression).
  Rollback = restore the single parent pointer that changed in union.
  Store undo stack: [(old_parent, old_rank)]

class RollbackUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.history = []          # stack of (node, old_parent, node, old_rank)

    def find(self, x):             # NO path compression
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            self.history.append(None)   # no-op marker
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        # Record state before change
        self.history.append((ry, self.parent[ry], rx, self.rank[rx]))
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

    def rollback(self):
        entry = self.history.pop()
        if entry is None: return       # undo no-op
        ry, old_parent_ry, rx, old_rank_rx = entry
        self.parent[ry] = old_parent_ry
        self.rank[rx]   = old_rank_rx  # restore rank

Time without path compression: O(log n) per find (not O(α(n))).
Trade-off: rollback capability at the cost of slightly slower find.
```

---

## 11. Classic Applications

### Connected Components in a Graph

```
PROBLEM: Given n nodes and edges, find the number of connected components.

def count_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components

EXAMPLE: n=5, edges=[(0,1),(1,2),(3,4)]
  Initial: 5 components
  union(0,1): 4 components
  union(1,2): 3 components  (0,1,2 now connected)
  union(3,4): 2 components
  Answer: 2 ✅ (components {0,1,2} and {3,4})

TIME: O(n + E × α(n)) ≈ O(n + E)
```

### Cycle Detection in Undirected Graph

```
PROBLEM: Does an undirected graph contain a cycle?

INSIGHT: When processing edge (u,v):
  If u and v are ALREADY in the same component → edge creates a CYCLE.
  If different components → merge them (tree edge, no cycle).

def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):   # union returns False = already connected
            return True           # this edge creates a cycle
    return False

EXAMPLE: n=4, edges=[(0,1),(1,2),(2,3),(3,0)]
  union(0,1): success → no cycle
  union(1,2): success → no cycle
  union(2,3): success → no cycle
  union(3,0): find(3)==find(0)? YES → CYCLE DETECTED ✅

WHY THIS WORKS:
  A connected graph with n nodes and n-1 edges is a TREE (no cycle).
  Adding one more edge to a connected component always creates a cycle.
  Union-Find detects the moment two already-connected nodes are re-connected.
```

### Kruskal's Minimum Spanning Tree

```
PROBLEM: Find minimum weight edges connecting all n nodes (MST).

ALGORITHM:
  1. Sort edges by weight ascending.
  2. For each edge (u, v, weight):
       If u and v NOT in same component:
         ADD edge to MST (it's safe — doesn't create cycle)
         union(u, v)
  3. Stop when n-1 edges added (MST complete).

def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])   # sort by weight
    uf = UnionFind(n)
    mst = []
    mst_weight = 0

    for u, v, w in edges:
        if uf.union(u, v):           # different components = safe to add
            mst.append((u, v, w))
            mst_weight += w
            if len(mst) == n - 1:
                break                # MST complete

    return mst, mst_weight

EXAMPLE: n=4, edges=[(0,1,1),(2,3,2),(0,2,3),(1,3,4),(0,3,5)]

  Sorted: [(0,1,1),(2,3,2),(0,2,3),(1,3,4),(0,3,5)]

  (0,1,1): diff components → ADD, union(0,1). MST=[(0,1,1)]
  (2,3,2): diff components → ADD, union(2,3). MST=[(0,1,1),(2,3,2)]
  (0,2,3): diff components → ADD, union(0,2). MST=[(0,1,1),(2,3,2),(0,2,3)]
  3 edges added = n-1 = 3 → DONE ✅

  MST weight: 1+2+3 = 6 ✅

TIME: O(E log E) for sorting + O(E × α(n)) for union-find ≈ O(E log E)
```

### Number of Islands

```
PROBLEM: Given a grid of '1's (land) and '0's (water), count islands.

APPROACH: Treat each '1' cell as a node.
  Union adjacent '1' cells.
  Count remaining components among '1' cells.

def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    # Map 2D cell (r,c) to 1D index
    def idx(r, c): return r * cols + c

    # Initialize: count only land cells as components
    uf = UnionFind(rows * cols)
    land_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                land_count += 1
            else:
                uf.parent[idx(r,c)] = -1   # mark water (optional)

    # Override components to count only land
    uf.components = land_count

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        uf.union(idx(r,c), idx(nr,nc))

    return uf.components

GRID EXAMPLE:
  1 1 0 0 0
  1 1 0 0 0
  0 0 1 0 0
  0 0 0 1 1

  Islands: {(0,0),(0,1),(1,0),(1,1)}, {(2,2)}, {(3,3),(3,4)} → 3 ✅
```

### Redundant Connection

```
PROBLEM: Given a tree with one extra edge added, find the redundant edge
         (the one creating the cycle).

def find_redundant(edges):
    n = len(edges)
    uf = UnionFind(n + 1)   # nodes labeled 1..n

    for u, v in edges:
        if not uf.union(u, v):   # already connected → this edge is redundant
            return [u, v]

    return []

EXAMPLE: edges=[(1,2),(1,3),(2,3)]

  union(1,2): success
  union(1,3): success
  union(2,3): find(2)==find(3)? Both in {1,2,3} → return [2,3] ✅

The last edge that attempts to connect an already-connected pair is redundant.
```

---

## 12. Real-World Applications

| Domain | Problem | Union-Find's Role |
|---|---|---|
| **Network connectivity** | Are servers A and B connected? | Union network links; query connectivity in O(α(n)) |
| **Image processing** | Connected pixel regions | Union adjacent same-colored pixels; find regions |
| **Social networks** | Friend groups / communities | Union friend edges; count or identify clusters |
| **Percolation theory** | Does liquid flow through the grid? | Union open cells; check if top connects to bottom |
| **Kruskal's MST** | Minimum cost network | Union edges greedily without creating cycles |
| **Compiler optimization** | Equivalent expression detection | Union equivalent variables/expressions |
| **Blockchain** | Transaction graph connectivity | Union transaction inputs/outputs |
| **Physics simulation** | Particle cluster formation | Union particles that come into contact |
| **Game development** | Dungeon connectivity | Ensure all rooms reachable via doors |
| **Dynamic connectivity** | Online graph connectivity queries | Union edges as they arrive; answer connectivity queries |

### Percolation — Union-Find in Physics and Statistics

```
PERCOLATION PROBLEM (Princeton textbook):
  N×N grid of sites. Each site open (probability p) or blocked.
  System "percolates" if there's a path of open sites from top to bottom.

  Used in: material science (does current flow?),
           oil recovery (does fluid flow through rock?),
           epidemiology (does infection spread?).

UNION-FIND SOLUTION:
  Create virtual TOP node (index N²) and BOTTOM node (index N²+1).
  Union each open site in row 0 with TOP.
  Union each open site in row N-1 with BOTTOM.
  Union each adjacent pair of open sites.

  System percolates iff connected(TOP, BOTTOM).

  ┌─────────────────┐
  │  VIRTUAL TOP    │   ← node N²
  └──┬──┬──┬──┬──┬─┘
     │  │  │  │  │
  Row 0: open sites union with TOP

  ... grid cells ...

  Row N-1: open sites union with BOTTOM
     │  │  │  │  │
  ┌──┴──┴──┴──┴──┴─┐
  │  VIRTUAL BOTTOM │  ← node N²+1
  └─────────────────┘

  percolates() { return uf.connected(N*N, N*N+1); }

This uses Union-Find with exactly 2 extra nodes to solve what would
otherwise require a complex DFS/BFS at each site-opening step.
O(α(n)) per site opening and O(α(n)) to check percolation — nearly free.
```

---

## 13. Comparison With Related Data Structures

```
              ┌──────────────────────────────────────────────────────────┐
              │           CONNECTIVITY / GROUPING STRUCTURES              │
              └──────────────────────────┬───────────────────────────────┘
                                         │
       ┌──────────────────┬──────────────┼──────────────┬────────────────┐
       ▼                  ▼             ▼              ▼                ▼
  UNION-FIND           DFS/BFS        HASH MAP       SEGMENT TREE    ADJ. LIST
  ──────────           ───────        ────────       ────────────    ─────────
  Dynamic conn.        Static graph   Group by key   Range queries   Static graph
  O(α(n)) query        O(V+E) full    O(1) lookup    O(log n)        O(V+E) DFS
  O(α(n)) union        scan           O(n) grouping  No connectivity  traversal
  Online queries       Offline only   No merging     No connectivity
  No path info         Full path      No merging
  No delete            No dynamic     No merging
  Connectivity         Connectivity   Grouping       Aggregate        Traversal
  MST, cycles          Reachability   Counting       Range sum/max    All paths
```

**Union-Find vs DFS/BFS:**
DFS/BFS computes connectivity by traversing the entire graph — O(V+E) per query. Union-Find precomputes connectivity incrementally — O(α(n)) per query after O(E) preprocessing. For a single connectivity check, DFS is simpler. For many connectivity queries as edges are dynamically added, Union-Find dominates.

**Union-Find vs Hash Map of sets:**
You could represent groups as a hash map from representative to set of members. But merging two sets requires O(smaller set size) to move elements — O(n) worst case. Union-Find merges in O(α(n)) by updating a single parent pointer. For merge-heavy operations, Union-Find is orders of magnitude faster.

**Union-Find vs Segment Tree:**
Different problems entirely. Segment tree handles range aggregate queries (sum, min, max) over arrays. Union-Find handles set connectivity and merging. They both achieve efficient queries through hierarchical tree structure, but operate on fundamentally different problem domains.

---

## 14. The Decision Framework

```
Should I use Union-Find?

Is the problem about GROUPING or CONNECTIVITY?
    │
    ├── "Are X and Y in the same group/component?"
    │       → Union-Find ✅
    │
    ├── "How many distinct groups exist?"
    │       → Union-Find (track components count) ✅
    │
    ├── "Merge two groups together"
    │       → Union-Find ✅
    │
    ├── "Find the minimum edges to connect all nodes"
    │       → Union-Find + Kruskal's MST ✅
    │
    ├── "Detect if adding an edge creates a cycle"
    │       → Union-Find (union returns False = cycle) ✅
    │
    ├── "Find a PATH between two nodes"
    │       → BFS/DFS (Union-Find doesn't store paths) ❌
    │
    ├── "Find SHORTEST path"
    │       → Dijkstra/BFS (Union-Find has no concept of path length) ❌
    │
    └── "Need to DELETE elements from groups"
            → Union-Find doesn't support deletion natively ❌
              (use alternative approaches)

KEY SIGNAL WORDS: "connected", "same component", "same group",
                  "merge", "join", "union", "number of islands",
                  "cycle detection", "redundant edge", "MST"
```

---

## 15. Tips for Long-Term Retention

**1. The club president image**
Every element points to its group's "president." To check if two people are in the same group, ask each "who is your president?" If the same person answers — same group. Path compression = after you find the president, update your own record to point directly to them. This image makes find, path compression, and union all feel obvious.

**2. Two arrays, two optimizations, one idea**
`parent[]` is the structure. `rank[]` (or `size[]`) is the balance. Path compression (in find) and union by rank (in union) are the two optimizations. Learn them as a pair: compression flattens trees after the fact; rank keeps them from getting tall in the first place. Together they achieve O(α(n)).

**3. Union returns False = cycle detected**
This is the single most useful pattern in competitive programming. Process edges one by one; when `union(u,v)` returns False (u and v already connected), you've found a cycle or redundant edge. This pattern appears in cycle detection, redundant connection, Kruskal's MST, and many graph problems.

**4. α(n) is effectively 4 — just say "constant time"**
Don't get lost in the Ackermann function. For any input you'll ever process, α(n) ≤ 4. In interviews and practice, say "amortized nearly O(1)" or "O(α(n)) which is effectively constant." The important thing is why — path compression + union by rank together — not the exact mathematical bound.

**5. Virtual nodes extend Union-Find's power**
Add extra nodes to represent abstract concepts: virtual TOP and BOTTOM for percolation, virtual "super-source" for multi-source problems. This technique lets Union-Find answer questions it wasn't directly designed for. When a Union-Find problem seems to require global state, ask "can I add a virtual node?"

**6. The component count is a free bonus**
Initialize `components = n`. Decrement by 1 on every successful union. At any point, `components` equals the number of distinct groups. This free bookkeeping answers "how many islands?" or "when does the network first become fully connected?" without any extra cost.

---

Union-Find is fundamentally about **making group membership as cheap as possible**. The naive approach — scan all elements to find group boundaries — is O(n) per query. Sorting with merge is O(n log n). Hash maps of sets give O(1) queries but O(n) merges. Union-Find achieves O(α(n)) for BOTH queries AND merges simultaneously — a result that seems impossible until you see the insight: representing groups as trees where only the root matters, compressing paths so trees stay flat, and balancing merges so trees never get tall. The result is a data structure so efficient that for any practical purpose, every operation is free — yet it detects cycles, builds minimum spanning trees, counts connected components, and models physical percolation all with the same simple two-array structure.
