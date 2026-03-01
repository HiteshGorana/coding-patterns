# Pattern Intuition + Diagrams (Question -> Pattern)

Use this file as a rapid classifier before solving.

How to use while reading a question:
1. Scan for trigger words and constraints.
2. Match the visual shape of the problem to a pattern diagram below.
3. Run the "3-second self-check" before coding.

## 01) Hash Map / Set Lookup

### Diagram
```text
for x in items:
  need info about x?
    -> check map/set in O(1)
  then update map/set
```

### Question Triggers
- "duplicate", "frequency", "first unique", "pair sum"
- Brute force would compare many pairs.

### Intuition Anchor
- "I need memory of what I have already seen."

### 3-Second Self-Check
- Can I answer faster if I store `value -> count/index/state`?

---

## 02) Two Pointers

### Diagram
```text
sorted array
L ---------------- R
 move L or R based on condition
```

### Question Triggers
- Sorted array/string.
- Need pair/triplet relation (`sum`, `diff`, palindrome).

### Intuition Anchor
- "Each pointer move should eliminate impossible answers."

### 3-Second Self-Check
- If I move one pointer, can I prove I never miss optimum?

---

## 03) Sliding Window (Fixed)

### Diagram
```text
[ i ... i+k-1 ] -> slide right by 1
remove left, add right
```

### Question Triggers
- Window size `k` is fixed.
- Need max/min/sum/avg over every size-k segment.

### Intuition Anchor
- "Adjacent windows overlap; reuse prior work."

### 3-Second Self-Check
- Can current window answer be updated with +incoming -outgoing?

---

## 04) Sliding Window (Variable)

### Diagram
```text
expand right -> window invalid?
  yes: shrink left until valid
  no: update answer
```

### Question Triggers
- "Longest/shortest substring/subarray with constraint"
- "At most K distinct", "without repeating", "sum >= target"

### Intuition Anchor
- "Grow to explore, shrink to repair."

### 3-Second Self-Check
- Can a valid window be maintained with two moving boundaries?

---

## 05) Prefix Sum

### Diagram
```text
prefix[i] = sum of [0..i-1]
range(l,r) = prefix[r+1] - prefix[l]
```

### Question Triggers
- Many range sum queries.
- Count subarrays with target sum.

### Intuition Anchor
- "Convert every range to subtraction of two checkpoints."

### 3-Second Self-Check
- Can I precompute cumulative state once and answer ranges quickly?

---

## 06) Binary Search (Index Space)

### Diagram
```text
L ------- mid ------- R
keep half that can still contain target
```

### Question Triggers
- Sorted data.
- Need exact index, lower bound, upper bound.

### Intuition Anchor
- "Keep only the half that might still be correct."

### 3-Second Self-Check
- Is the search condition monotonic across indices?

---

## 07) Binary Search on Answer

### Diagram
```text
answer range [low..high]
check(mid) -> feasible?
true: move left  false: move right
```

### Question Triggers
- "minimum feasible", "maximum feasible"
- Rate/capacity/time threshold problems.

### Intuition Anchor
- "I cannot build answer directly, but I can verify a guess."

### 3-Second Self-Check
- If `x` works, do all larger/smaller values also work?

---

## 08) Sort + Scan

### Diagram
```text
sort first -> linear sweep
neighbors now carry global structure
```

### Question Triggers
- Intervals, conflicts, merging, global ordering.

### Intuition Anchor
- "Sorting reveals structure; scanning exploits it."

### 3-Second Self-Check
- After sort, can one pass solve it?

---

## 09) Greedy

### Diagram
```text
repeat:
  take best local safe choice
```

### Question Triggers
- Min/max optimization with local decision opportunities.
- Can prove local choice never hurts global optimum.

### Intuition Anchor
- "Commit early only if I can justify safety."

### 3-Second Self-Check
- Can I give a short exchange/invariant argument?

---

## 10) Monotonic Stack

### Diagram
```text
stack keeps monotonic values
new value breaks order -> pop and resolve
```

### Question Triggers
- "next greater/smaller", nearest boundary, histogram area.

### Intuition Anchor
- "Unresolved elements wait on a stack until a breaker appears."

### 3-Second Self-Check
- Does each element need nearest bigger/smaller on one side?

---

## 11) Monotonic Queue / Deque

### Diagram
```text
window moves -> expire front
insert new -> pop worse from back
front = best in current window
```

### Question Triggers
- Sliding window max/min in strict O(n).

### Intuition Anchor
- "Deque stores only candidates that can still win."

### 3-Second Self-Check
- Do I need best value per moving window with index expiry?

---

## 12) Top K with Heap

### Diagram
```text
keep heap size = k
candidate better than root? replace root
```

### Question Triggers
- "top k", "kth largest/smallest", streaming k-best.

### Intuition Anchor
- "Maintain only what can still be in final top-k."

### 3-Second Self-Check
- Can partial ordering beat full sorting here?

---

## 13) K-Way Merge (Heap)

### Diagram
```text
k sorted lists
push each head -> pop min -> push next from same list
```

### Question Triggers
- Merge many sorted sources.
- Need global smallest among k frontiers.

### Intuition Anchor
- "Only k current heads matter at any time."

### 3-Second Self-Check
- Is each source already sorted?

---

## 14) Fast & Slow Pointers

### Diagram
```text
slow = +1, fast = +2
if cycle -> they meet
```

### Question Triggers
- Linked list cycle, middle node, repeated-state loops.

### Intuition Anchor
- "Different speeds expose structure without extra memory."

### 3-Second Self-Check
- Can two-speed traversal detect cycle/phase alignment?

---

## 15) Linked List Reversal / In-place Ops

### Diagram
```text
prev <- curr -> next
save next, reverse pointer, advance
```

### Question Triggers
- Reverse list/all/part/k-group in O(1) extra space.

### Intuition Anchor
- "Pointer rewiring with strict bookkeeping."

### 3-Second Self-Check
- Can I do this with `prev, curr, next` safely?

---

## 16) Cyclic Sort

### Diagram
```text
value x belongs to index x (or x-1)
swap until each value is in its home slot
```

### Question Triggers
- Array values in bounded range `0..n` or `1..n`.
- Missing/duplicate/corrupt numbers.

### Intuition Anchor
- "Use value as address."

### 3-Second Self-Check
- Is there a natural correct index for each value?

---

## 17) Intervals Line Sweep

### Diagram
```text
[start:+1, end:-1] events
sort by time -> running active count
```

### Question Triggers
- Max overlaps, active intervals over time.

### Intuition Anchor
- "Track population changes at event points, not every timestamp."

### 3-Second Self-Check
- Can intervals be converted to enter/exit events?

---

## 18) Matrix Traversal (Grid BFS/DFS)

### Diagram
```text
grid => graph
cell -> neighbors (4/8 dirs)
visit once
```

### Question Triggers
- Islands/regions/flood fill/shortest steps in unweighted grid.

### Intuition Anchor
- "Treat grid as implicit graph."

### 3-Second Self-Check
- Is this a connectivity or shortest-unweighted path problem on cells?

---

## 19) Tree DFS

### Diagram
```text
solve(node):
  left = solve(node.left)
  right = solve(node.right)
  return combine(left, right, node)
```

### Question Triggers
- Path sums, diameter, balanced checks, subtree properties.

### Intuition Anchor
- "Define what recursion returns from a subtree."

### 3-Second Self-Check
- Can parent answer be built from child answers?

---

## 20) Tree BFS (Level Order)

### Diagram
```text
queue frontier
process by level_size
```

### Question Triggers
- Level-based output, min depth, nearest by levels.

### Intuition Anchor
- "Queue = current frontier of equal distance from root."

### 3-Second Self-Check
- Does level boundary matter to output?

---

## 21) Binary Search Tree Rules

### Diagram
```text
left < node < right
inorder traversal => sorted values
```

### Question Triggers
- Validate BST, kth smallest, predecessor/successor, range query.

### Intuition Anchor
- "Ordering constraint lets me prune search."

### 3-Second Self-Check
- Can BST ordering remove half/subtree work?

---

## 22) Backtracking

### Diagram
```text
choose -> recurse -> unchoose
DFS over decision tree
```

### Question Triggers
- Need all combinations/permutations or constrained existence.

### Intuition Anchor
- "Build partial answer; undo when returning."

### 3-Second Self-Check
- Is this an exponential choice tree where pruning helps?

---

## 23) Trie (Prefix Tree)

### Diagram
```text
root
 └─ a ─ p ─ p* ─ l ─ e*
```
(`*` = end of word)

### Question Triggers
- Prefix search, dictionary, autocomplete, many shared prefixes.

### Intuition Anchor
- "Store characters as paths, not full repeated strings."

### 3-Second Self-Check
- Do prefix checks happen frequently?

---

## 24) Graph BFS/DFS

### Diagram
```text
for each unvisited node:
  traverse component via BFS/DFS
```

### Question Triggers
- Components, reachability, clone/traverse graph.

### Intuition Anchor
- "Visited set prevents cycles and repeated work."

### 3-Second Self-Check
- Is this a generic graph traversal with V+E structure?

---

## 25) Topological Sort

### Diagram
```text
DAG + indegree
queue indegree-0 nodes
pop -> reduce neighbors indegree
```

### Question Triggers
- Prerequisites/dependency ordering.

### Intuition Anchor
- "Do tasks only when prerequisites are cleared."

### 3-Second Self-Check
- Is graph directed and dependency-based?

---

## 26) Union-Find (DSU)

### Diagram
```text
find(x) -> root
union(a,b) -> merge roots
```

### Question Triggers
- Dynamic connectivity, redundant edge, component count.

### Intuition Anchor
- "Represent each component by a root id."

### 3-Second Self-Check
- Am I repeatedly asking if two nodes belong to same group?

---

## 27) Shortest Path (Dijkstra / 0-1 BFS)

### Diagram
```text
min-heap of (dist,node)
pop closest unresolved node -> relax edges
```

### Question Triggers
- Weighted shortest path with non-negative weights.
- Only 0/1 weights -> deque-based 0-1 BFS.

### Intuition Anchor
- "Expand cheapest frontier first."

### 3-Second Self-Check
- Is distance cost weighted (not just step count)?

---

## 28) Dynamic Programming (1D)

### Diagram
```text
dp[i] depends on earlier states
fill left -> right
```

### Question Triggers
- Max/min/count ways over linear index.
- Overlapping subproblems in recursion.

### Intuition Anchor
- "State at i summarizes all best history needed."

### 3-Second Self-Check
- Can I define `dp[i]` with a small recurrence?

---

## 29) Dynamic Programming (2D)

### Diagram
```text
dp[i][j] table
cell uses top/left/diag (or variants)
```

### Question Triggers
- Two-dimensional state: strings, grids, pair indices.

### Intuition Anchor
- "Each cell is a smaller subproblem answer."

### 3-Second Self-Check
- Do I naturally need two coordinates for state?

---

## 30) Knapsack DP

### Diagram
```text
for each item:
  for capacity:
    skip vs take
```

### Question Triggers
- Pick/skip under capacity/target constraints.

### Intuition Anchor
- "Every item decision: include or exclude."

### 3-Second Self-Check
- Is this subset decision under a budget-like limit?

---

## 31) Interval / Partition DP

### Diagram
```text
dp[l][r]
try split k in [l..r-1]
combine left + right + merge cost
```

### Question Triggers
- Best way to parenthesize/split intervals.

### Intuition Anchor
- "Answer for range comes from best split point."

### 3-Second Self-Check
- Is problem about partitioning a contiguous segment?

---

## 32) Bit Manipulation

### Diagram
```text
mask operations:
set: x | (1<<b)
check: x & (1<<b)
toggle: x ^ (1<<b)
```

### Question Triggers
- XOR uniqueness, subset masks, bit count/power-of-two checks.

### Intuition Anchor
- "Use bits as compact boolean array."

### 3-Second Self-Check
- Can binary properties replace heavier data structures?

---

## 33) Math / Number Theory

### Diagram
```text
problem -> formula/invariant
use gcd/mod/fastpow/combinatorics
```

### Question Triggers
- Divisibility, modular cycles, huge exponents, prime logic.

### Intuition Anchor
- "Exploit algebraic structure instead of simulation."

### 3-Second Self-Check
- Is there a known math identity that collapses complexity?

---

## 34) Design Data Structures

### Diagram
```text
API constraints -> combine DS
hash map + DLL / heap / stack / queue
```

### Question Triggers
- "Design class with O(1)/O(log n) ops".

### Intuition Anchor
- "No single DS fits all methods; compose two or more."

### 3-Second Self-Check
- Can I map each method to a supporting structure + invariant?

---

## 35) Segment Tree / Fenwick Tree

### Diagram
```text
array
 -> tree of aggregated ranges
query/update in O(log n)
```

### Question Triggers
- Repeated range query + point/range updates on mutable array.

### Intuition Anchor
- "Pre-aggregate partial ranges for fast incremental changes."

### 3-Second Self-Check
- Is O(n) per update/query too slow with many operations?

---

## 36) Meet in the Middle

### Diagram
```text
left half -> all subset sums
right half -> all subset sums
sort one side + binary search combine
```

### Question Triggers
- Constraints suggest brute force `2^n` is too large but `n` is only around `30..45`.
- Subset/partition/sum objective where combining two halves is natural.

### Intuition Anchor
- "Split once, solve both halves exactly, then combine efficiently."

### 3-Second Self-Check
- Can I reduce `2^n` to roughly `2^(n/2)` per side?

---

## 37) Bitmask DP / State Compression DP

### Diagram
```text
dp[mask][u] = best with visited set=mask ending at u
transition by adding one bit at a time
```

### Question Triggers
- State is naturally a subset of items/nodes.
- Need exact optimization over visited/unvisited sets.

### Intuition Anchor
- "Encode set membership in bits so transitions become constant-time mask operations."

### 3-Second Self-Check
- Is `n` small enough that `2^n` states are feasible?

---

## 38) Multi-source BFS

### Diagram
```text
enqueue all sources at distance 0
BFS wave expands simultaneously
```

### Question Triggers
- Need nearest distance to any of many sources.
- Diffusion/spread problems in unweighted grid/graph.

### Intuition Anchor
- "Start BFS from all valid origins at once to get globally shortest expansion levels."

### 3-Second Self-Check
- Can I treat every source as level-0 and expand in one BFS?

---

## 39) State-space BFS

### Diagram
```text
BFS node = (position, state)
visited tracks full tuple, not just position
```

### Question Triggers
- Path feasibility depends on keys, mask, fuel, direction, or configuration.
- Need shortest steps in an unweighted transition graph.

### Intuition Anchor
- "When future options depend on history, history must be encoded inside BFS state."

### 3-Second Self-Check
- If I reach same location with different state, do outcomes differ?

---

## 40) Minimum Spanning Tree (Kruskal / Prim)

### Diagram
```text
Kruskal: sort edges by weight -> union if no cycle
Prim: grow tree from seed with min outgoing edge
```

### Question Triggers
- Connect all vertices with minimum sum weight.
- Need exactly `n-1` edges without cycles.

### Intuition Anchor
- "MST picks cheapest safe edges that keep global connectivity optimal."

### 3-Second Self-Check
- Is this 'connect everything at min total edge cost' rather than shortest path from one source?

---

## 41) Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)

### Diagram
```text
Bellman-Ford: relax all edges V-1 times
extra pass improvement -> negative cycle
Floyd: k as intermediate for all-pairs
```

### Question Triggers
- Graph has negative edges.
- Need detect negative cycle.
- Need all-pairs shortest paths with moderate `n`.

### Intuition Anchor
- "Dijkstra breaks on negative weights, so switch to relaxation-based algorithms."

### 3-Second Self-Check
- Are negative edges/cycles possible or explicitly mentioned?

---

## 42) SCC / Bridges / Articulation Points

### Diagram
```text
DFS timestamps + low-link
low[child] > tin[parent] => bridge
low[child] >= tin[parent] => articulation
SCC via stack order
```

### Question Triggers
- Need critical edges/nodes whose removal disconnects graph.
- Need strongly connected components in directed graph.

### Intuition Anchor
- "Low-link values summarize whether a DFS subtree can reconnect to an ancestor."

### 3-Second Self-Check
- Does question ask for critical links/cut vertices/strongly connected blocks?

---

## 43) Tree Rerooting DP

### Diagram
```text
DFS1: compute subtree contribution
DFS2: reroot transfer parent->child to fill all answers
```

### Question Triggers
- Need answer for every node as root.
- Naive re-run DFS/BFS per root is too slow (`O(n^2)`).

### Intuition Anchor
- "Compute once for one root, then transfer answers along edges in O(1) per move."

### 3-Second Self-Check
- Can answer at child be derived from parent answer by local adjustment?

---

## 44) Binary Lifting (LCA / Kth Ancestor)

### Diagram
```text
up[v][j] = 2^j-th ancestor of v
raise nodes by binary decomposition of jump length
```

### Question Triggers
- Large number of ancestor/LCA queries.
- Static tree (preprocessing is allowed).

### Intuition Anchor
- "Precompute powers-of-two jumps so each query is answered in logarithmic time."

### 3-Second Self-Check
- Will many online queries justify `O(n log n)` preprocessing?

---

## 45) Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher)

### Diagram
```text
KMP: prefix-function fallback
Z: longest prefix match at each index
Rabin-Karp: rolling hash
Manacher: palindrome radii in O(n)
```

### Question Triggers
- Need fast substring matching across large texts.
- Need all pattern occurrences or linear palindrome computation.

### Intuition Anchor
- "Preprocess string structure once, then answer matching/palindrome queries without restarting work."

### 3-Second Self-Check
- Does naive matching restart too often and become `O(n*m)`?

---


# Global Pattern Classifier (Fast Decision Tree)

```text
Q1: Need all combos/permutations? -> Backtracking
Q2: Need shortest path?
    - unweighted -> BFS
    - weighted non-negative -> Dijkstra
Q3: Need contiguous subarray/substring?
    - fixed length -> Sliding Window (Fixed)
    - constraint-based length -> Sliding Window (Variable)
Q4: Need range sums/updates?
    - immutable queries -> Prefix Sum
    - mutable many updates -> Fenwick/Segment Tree
Q5: Need pair in sorted array? -> Two Pointers
Q6: Need "min/max feasible" threshold? -> Binary Search on Answer
Q7: Dependency ordering in DAG? -> Topological Sort
Q8: Dynamic connectivity? -> Union-Find
Q9: Repeated choose/skip optimization? -> DP/Knapsack
Q10: Next greater/smaller boundary? -> Monotonic Stack/Deque
Q11: n around 40 subset optimization? -> Meet in the Middle
Q12: State is subset over small n (<=20)? -> Bitmask DP
Q13: Multiple starting points, nearest source distance? -> Multi-source BFS
Q14: Position + extra state defines node? -> State-space BFS
Q15: Connect all nodes at minimum total cost? -> MST (Kruskal/Prim)
Q16: Negative edges or negative-cycle detection? -> Bellman-Ford/Floyd-Warshall
Q17: Critical links/nodes or SCC decomposition? -> SCC/Bridges/Articulation
Q18: Need answer for every possible tree root? -> Tree Rerooting DP
Q19: Many ancestor/LCA queries on fixed tree? -> Binary Lifting
Q20: Advanced substring/palindrome linear matching? -> KMP/Z/Rabin-Karp/Manacher
```

# Intuition Training Routine (Daily, 20-30 min)

1. Pick 5 random problems.
2. Before solving, write only pattern guess + one-line reason.
3. After solving, compare with actual best pattern.
4. Track mistakes in a "misclassification log" by trigger phrase.
5. Revisit this file and memorize failed triggers.

This routine builds the exact skill you asked for: recognizing pattern quickly from problem language.
