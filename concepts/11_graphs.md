# Graphs: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

A **graph** is a mathematical structure that models pairwise relationships between objects. It consists of a set of **vertices** (also called nodes) and a set of **edges** (also called arcs) that connect pairs of vertices.

```
SIMPLE GRAPH:

     A ──── B
     |    / |
     |   /  |
     |  /   |
     C ──── D ──── E

Vertices (V): {A, B, C, D, E}
Edges (E):    {A-B, A-C, B-C, B-D, C-D, D-E}
```

**Core components:**

- **Vertex (node)** — a fundamental unit representing an entity (person, city, webpage, state)
- **Edge (arc)** — a connection representing a relationship between two vertices
- **Adjacency** — two vertices are adjacent if an edge connects them directly
- **Degree** — the number of edges connected to a vertex (in directed graphs: in-degree + out-degree)
- **Path** — a sequence of vertices where each consecutive pair is connected by an edge
- **Cycle** — a path that starts and ends at the same vertex
- **Weight** — an optional value assigned to an edge representing cost, distance, capacity, or strength
- **Direction** — edges can be undirected (mutual relationship) or directed (one-way relationship)

Graphs are the **universal language of relationships**. Anything that can be described as "things connected to other things" is a graph. This is not a metaphor — it is a precise claim that has made graphs the foundational structure of computer science, mathematics, and network science.

---

## 2. The Taxonomy of Graphs

Graphs come in many varieties. Understanding the type determines which algorithms apply.

### By Direction

```
UNDIRECTED:                    DIRECTED (DIGRAPH):

  A ──── B                       A ──→ B
  |      |                       |     ↓
  C ──── D                       C ←── D

Edge A-B means:                Edge A→B means:
  A connects to B AND            A connects to B
  B connects to A                B does NOT connect to A (unless separate edge)

Examples: friendship,          Examples: web links, dependencies,
          roads (2-way)          Twitter follows, task ordering
```

### By Weight

```
UNWEIGHTED:                    WEIGHTED:

  A ──── B                       A ──5── B
  |      |                       |       |
  C ──── D                       3       7
                                 |       |
                                 C ──2── D

All edges equal.               Each edge has a numeric value.
"Is there a path?"             "What is the CHEAPEST path?"
BFS finds shortest hops.       Dijkstra finds shortest cost.
```

### By Cycles

```
CYCLIC:                        ACYCLIC (no cycles):

  A → B                          A → B → D
  ↑   ↓                                ↓
  D ← C                          A → C → D

Contains at least one            No path from any node
closed loop.                     leads back to itself.

DAG = Directed Acyclic Graph     DAGs are used for:
(most important acyclic type)    dependencies, scheduling,
                                 version control, neural nets
```

### By Connectivity

```
CONNECTED:                     DISCONNECTED:

  A──B──C──D                     A──B    D──E
  |     |                        |       |
  E─────F                        C       F

Every vertex reachable          Some vertices unreachable
from every other.               from others.

STRONGLY CONNECTED              WEAKLY CONNECTED
(directed):                     (directed):
  Path from every vertex         Connected if you ignore
  to every other vertex          edge direction
```

### Special Graph Types

```
COMPLETE GRAPH (Kₙ):           BIPARTITE GRAPH:
Every vertex connects           Vertices split into two sets.
to every other.                 Edges ONLY between sets, never within.

  A───B                           Set 1    Set 2
  |╲ /|                           [A]─────[1]
  | X |                           [A]─────[2]
  |/ ╲|                           [B]─────[2]
  C───D                           [B]─────[3]
  K₄: 4 vertices,
  6 edges = n(n-1)/2            Examples: job-applicant matching,
                                user-movie ratings, students-courses

TREE:                           COMPLETE BIPARTITE (K_{m,n}):
Connected acyclic               Every vertex in set 1 connects
undirected graph.               to every vertex in set 2.
Exactly n-1 edges
for n vertices.
```

---

## 3. Graph Representation — How Computers Store Graphs

The choice of representation affects every algorithm's space and time complexity.

### Adjacency Matrix

```
Graph:  A──B, A──C, B──C, B──D

     A  B  C  D
A  [ 0  1  1  0 ]
B  [ 1  0  1  1 ]
C  [ 1  1  0  0 ]
D  [ 0  1  0  0 ]

matrix[i][j] = 1 if edge i→j exists, 0 otherwise
(For weighted: store weight instead of 1)

PROS:                           CONS:
O(1) edge existence check       O(V²) space — wastes memory
  (just read matrix[i][j])        on sparse graphs
O(1) edge add/remove            O(V²) time to find all neighbors
Simple to implement             (must scan entire row)
Good for dense graphs           V = 1 million → 1 TB matrix
```

### Adjacency List

```
Graph:  A──B, A──C, B──C, B──D

A: [B, C]
B: [A, C, D]
C: [A, B]
D: [B]

Each vertex stores only its actual neighbors.

PROS:                           CONS:
O(V + E) space — optimal        O(degree) edge existence check
  for sparse graphs               (scan neighbor list)
O(degree) neighbor iteration    Slightly more complex
Fast for most algorithms        Edge removal: O(degree)
Default choice for most cases

Space comparison:
  Matrix: O(V²)                 V=1M, E=5M: matrix=1TB, list=40MB ✅
  List:   O(V + E)
```

### Edge List

```
Graph: A──B, A──C, B──D

edges = [(A,B), (A,C), (B,D)]   or with weights: [(A,B,5), (A,C,3), (B,D,7)]

PROS:                           CONS:
Simplest representation         O(E) neighbor lookup
O(E) space                      Rarely used in traversal
Ideal for edge-centric          algorithms
algorithms (Kruskal's MST)
```

### Choosing the Right Representation

```
DECISION:
  Sparse graph (E << V²)?  →  Adjacency List     (99% of real problems)
  Dense graph  (E ≈ V²)?   →  Adjacency Matrix
  Need fast edge queries?  →  Adjacency Matrix
  Edge-centric algorithm?  →  Edge List (Kruskal's)
  Default?                 →  Adjacency List

In interviews and practice: adjacency list is almost always correct.
```

---

## 4. The Fundamental Properties — Cause and Effect

### Degree & Handshaking Lemma

```
UNDIRECTED GRAPH:
  Sum of all degrees = 2 × |E|

  WHY: Every edge contributes exactly 2 to the total degree count
       (one for each endpoint). Counting all degrees double-counts
       every edge.

  CONSEQUENCE: In any graph, the number of odd-degree vertices is EVEN.
  (You cannot have exactly one vertex with odd degree.)

DIRECTED GRAPH:
  Sum of in-degrees = Sum of out-degrees = |E|

  WHY: Every directed edge contributes exactly 1 to in-degree total
       (at its head) and 1 to out-degree total (at its tail).
```

### Connectivity and Paths

```
CONNECTED COMPONENTS:
  A maximal set of vertices such that there is a path between every pair.

  [A──B──C]    [D──E]    [F]
  Component 1  Component 2  Component 3

  Count components: run DFS/BFS from each unvisited node.
  Each new traversal = new component.

SHORTEST PATH:
  Unweighted: BFS gives minimum edge count in O(V + E)
  Weighted (non-negative): Dijkstra in O((V+E) log V)
  Weighted (negative edges): Bellman-Ford in O(VE)
  All pairs: Floyd-Warshall in O(V³)
```

### Trees as Special Graphs

```
A TREE is a connected acyclic undirected graph.

Key equivalences — for a connected undirected graph G with n vertices:
  G is a tree
  ⟺ G has exactly n-1 edges
  ⟺ G has no cycles
  ⟺ There is exactly one path between any two vertices
  ⟺ Removing any edge disconnects G
  ⟺ Adding any edge creates exactly one cycle

These are all equivalent definitions. Proving any one proves all.

FOREST = multiple disconnected trees (each component is a tree)
```

---

## 5. Core Graph Algorithms

### Traversal: BFS and DFS

```
Both visit every reachable vertex exactly once.
Both run in O(V + E).
They differ only in ORDER of exploration.

BFS (queue):   Level by level — finds shortest paths (unweighted)
DFS (stack):   Depth first — finds cycles, topological order, components

For full details: see BFS and DFS deep dives.
```

### Shortest Path: Dijkstra's Algorithm

```
GOAL: Find shortest weighted path from source S to all other vertices.

KEY IDEA: Always extend the shortest known path first.
          Use a min-heap (priority queue) ordered by distance.

dist = {S: 0, all others: ∞}
heap = [(0, S)]

WHILE heap not empty:
    (d, u) = pop_min()
    IF d > dist[u]: continue    ← stale entry, skip

    FOR each neighbor v of u with edge weight w:
        new_dist = dist[u] + w
        IF new_dist < dist[v]:
            dist[v] = new_dist
            push (new_dist, v) to heap    ← relaxation

EXAMPLE:

    S ──2── A ──3── D
    |       |
    4       1
    |       |
    B ──1── C

    dist: {S:0, A:∞, B:∞, C:∞, D:∞}

    Pop (0,S): relax A→2, B→4
    dist: {S:0, A:2, B:4, C:∞, D:∞}

    Pop (2,A): relax C→3, D→5
    dist: {S:0, A:2, B:4, C:3, D:5}

    Pop (3,C): relax B→4 (no improvement)
    Pop (4,B): no unvisited neighbors with improvement
    Pop (5,D): done

    Shortest paths from S: A=2, B=4, C=3, D=5 ✅
```

```
WHY IT WORKS (greedy proof):
  When we pop vertex u with distance d, d is FINAL.
  WHY: all remaining heap entries have distance ≥ d (min-heap property)
       any path to u through those vertices costs ≥ d + positive_weight > d
       so no shorter path to u can be found later.

CRITICAL REQUIREMENT: Edge weights must be NON-NEGATIVE.
  Negative edges break the greedy assumption.
  (Use Bellman-Ford for negative edges.)
```

### Minimum Spanning Tree: Kruskal's and Prim's

```
PROBLEM: Connect all vertices with minimum total edge weight.
  (Used for: network infrastructure, clustering, approximation algorithms)

SPANNING TREE: A tree that includes all vertices of the graph.
  For n vertices: always exactly n-1 edges.
  Many spanning trees exist; MST has minimum total weight.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KRUSKAL'S ALGORITHM (edge-centric, uses Union-Find):

1. Sort ALL edges by weight ascending
2. For each edge (u, v, w) in sorted order:
     IF u and v are in different components:
         ADD edge to MST (merge components)
     ELSE: skip (would create cycle)
3. Stop when n-1 edges added.

EXAMPLE:
  Edges sorted: (A,B,1),(C,D,2),(A,C,3),(B,C,4),(B,D,5)

  (A,B,1): A and B separate → ADD. MST={A-B}
  (C,D,2): C and D separate → ADD. MST={A-B, C-D}
  (A,C,3): A-B component ≠ C-D component → ADD. MST={A-B,C-D,A-C}
  (B,C,4): B and C now in SAME component → SKIP (cycle!)
  (B,D,5): B and D now in SAME component → SKIP (cycle!)

  MST total weight: 1+2+3 = 6 ✅

Time: O(E log E) for sorting + O(E α(V)) for Union-Find
      ≈ O(E log E) overall

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIM'S ALGORITHM (vertex-centric, uses min-heap):

1. Start from any vertex. Mark it in MST.
2. Add all its edges to a min-heap.
3. WHILE MST doesn't include all vertices:
     Pop cheapest edge (u, v, w) from heap.
     IF v already in MST: skip (would create cycle).
     Add v to MST, add edge (u,v) to result.
     Push all edges from v to heap.

Analogous to Dijkstra but minimizes EDGE WEIGHT, not total path cost.
Time: O((V + E) log V) with binary heap.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHEN TO USE WHICH:
  Kruskal's:  sparse graphs (E close to V) — sort fewer edges
  Prim's:     dense graphs (E close to V²) — heap operations dominate
```

### Topological Sort

```
GOAL: Order vertices of a DAG such that for every edge u→v,
      u appears before v. (Task scheduling, dependency resolution.)

METHOD 1: DFS-based (post-order reversal)
  Run DFS; push each vertex to stack AFTER all its descendants finish.
  Reverse the stack = topological order.

METHOD 2: Kahn's Algorithm (BFS-based, in-degree)

  1. Compute in-degree of every vertex.
  2. Add all vertices with in-degree 0 to queue (no prerequisites).
  3. WHILE queue not empty:
       u = dequeue → add to result
       FOR each neighbor v of u:
           in_degree[v]--
           IF in_degree[v] == 0: enqueue v   ← all prerequisites done
  4. IF result.length < V: CYCLE EXISTS (some vertices never reached 0)

EXAMPLE: Course prerequisites
  Math101 → Math201 → Math301
  Eng101  → Math201

  In-degrees: Math101=0, Eng101=0, Math201=2, Math301=1

  Queue: [Math101, Eng101]
  Process Math101 → Math201 in-degree: 2→1
  Process Eng101  → Math201 in-degree: 1→0 → enqueue Math201
  Process Math201 → Math301 in-degree: 1→0 → enqueue Math301
  Process Math301

  Topological order: Math101, Eng101, Math201, Math301 ✅
```

### Union-Find (Disjoint Set Union)

```
GOAL: Efficiently track which vertices belong to the same connected component.
      Support two operations:
        FIND(x): which component does x belong to?
        UNION(x,y): merge the components containing x and y.

STRUCTURE: Each component has a representative (root).
  parent[x] = x's parent node (root points to itself)

NAIVE IMPLEMENTATION:
  find(x): follow parent pointers to root
  union(x,y): set root of one component to point to root of other

WITH OPTIMIZATIONS:
  PATH COMPRESSION: When finding root, make all nodes point directly to root.
    find(x):
      if parent[x] != x:
          parent[x] = find(parent[x])   ← path compression
      return parent[x]

  UNION BY RANK: Always attach smaller tree under larger tree.
    union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry: return   ← already same component
        if rank[rx] < rank[ry]: rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]: rank[rx]++

WITH BOTH OPTIMIZATIONS:
  find and union both run in O(α(n)) amortized
  where α = inverse Ackermann function ≈ effectively O(1) for all practical n

APPLICATIONS:
  Kruskal's MST (detect cycle = same component?)
  Connected components
  Network connectivity
  Percolation problems
```

### Strongly Connected Components (SCC)

```
In a DIRECTED graph, an SCC is a maximal set of vertices where
every vertex is reachable from every other.

A ←→ B      Here A→B→C→A form one SCC.
↓    ↑      D is its own SCC (can reach nothing that reaches back).
C ───┘  D

KOSARAJU'S ALGORITHM (two-pass DFS):
  1. Run DFS on original graph; push vertices to stack in FINISH ORDER.
  2. Transpose the graph (reverse all edge directions).
  3. Run DFS on transposed graph in REVERSE FINISH ORDER.
     Each DFS tree in step 3 = one SCC.

WHY IT WORKS:
  In the original graph, if u can reach v, v cannot reach u (different SCC).
  In the transposed graph, the reachability is reversed.
  Running DFS in reverse finish order ensures we find the "source" SCC first,
  and the transposed graph ensures we only visit vertices within that SCC.

Time: O(V + E) — two DFS passes.

TARJAN'S ALGORITHM (single-pass DFS):
  Uses a stack and "low-link" values to find SCCs in one pass.
  Also O(V + E) — more complex but single traversal.

APPLICATIONS:
  Web page clustering, social network community detection,
  compiler optimization, deadlock detection.
```

---

## 6. The "Why" Questions

### Why can't Dijkstra handle negative edge weights?

```
DIJKSTRA'S GREEDY ASSUMPTION:
  "When I pop vertex u with distance d, d is final — no shorter path exists."

  This holds ONLY when all edge weights are non-negative.
  Why? Because any alternative path through unvisited vertices
       would cost AT LEAST d (all future edge additions are non-negative).

NEGATIVE EDGE BREAKS THIS:

    S ──3── A ──(-5)── B
    S ──1── B

    Dijkstra pops B with distance 1 (via S→B). Marks B FINAL.
    Later: S→A→B costs 3 + (-5) = -2 < 1. SHORTER PATH EXISTS.
    But Dijkstra already marked B final and won't revisit it.
    WRONG ANSWER. ❌

FIX: Use Bellman-Ford for graphs with negative edges.
  Bellman-Ford relaxes ALL edges V-1 times — no greedy assumption.
  Time: O(VE) — slower but correct for negative edges.
  Can also detect negative cycles (no shortest path if one exists).
```

### Why does a tree always have exactly n-1 edges?

```
PROOF BY INDUCTION:
  Base case: n=1 vertex, 0 edges. Connected, acyclic. 1-1=0 ✅

  Inductive step: Assume true for all trees with < n vertices.
    Take a tree T with n vertices.
    Remove any leaf (degree-1 vertex) and its edge.
    Result: tree with n-1 vertices → has (n-1)-1 = n-2 edges.
    Add back the leaf and its edge: n vertices, n-2+1 = n-1 edges. ✅

INTUITION:
  Start with n isolated vertices (0 edges, n components).
  Each edge added reduces component count by exactly 1
    (only if it connects different components — no cycles).
  To get from n components to 1 (connected), need exactly n-1 edges.
  Add a n-th edge → creates a cycle (both endpoints already connected).
```

### Why is topological sort impossible if a cycle exists?

```
Suppose cycle: A → B → C → A

Topological order requires:
  A before B (edge A→B)
  B before C (edge B→C)
  C before A (edge C→A)

  A before B before C before A → A must come before itself.
  CONTRADICTION. No linear ordering satisfies all constraints.

Kahn's algorithm detects this: if a cycle exists, some vertices
always maintain in-degree > 0 (the cycle members) and are never
enqueued. Result length < V → cycle detected.
```

---

## 7. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Graph is empty (no vertices) | All algorithms trivially return empty results |
| Graph has no edges | n isolated components; BFS/DFS visit single nodes; MST impossible |
| Graph is disconnected | Single BFS/DFS misses some components; outer loop over all vertices needed |
| Self-loop (edge from vertex to itself) | Adjacency matrix: diagonal entry = 1; DFS/BFS: skip (already visited); cycle detection: immediate cycle |
| Parallel edges (multigraph) | Adjacency matrix loses one; adjacency list keeps all; most algorithms treat as single weighted edge |
| Negative cycle exists | Bellman-Ford detects it; Dijkstra gives wrong answer; shortest path undefined (can decrease forever) |
| All edge weights equal | Dijkstra = BFS (same result); use BFS (simpler, faster) |
| Complete graph | MST selection is trivial; all-pairs shortest paths expensive; O(V²) edges makes algorithms expensive |
| Graph is a single cycle | DFS finds back edge immediately; topological sort fails; BFS traverses all nodes in one pass |
| DAG but source has no path to target | Dijkstra/BFS returns ∞; must check if target was reached |

### The Negative Cycle Problem

```
Path: S → A → B → A → B → A → B → ... (infinite loop through cycle)
Each traversal of A→B→A costs 3 + (-5) = -2.
After k traversals: total cost = initial + k×(-2) → -∞

No "shortest path" exists — you can always make it shorter.
Bellman-Ford: if any distance improves on the V-th relaxation pass,
a negative cycle is reachable. Report "no solution."
```

---

## 8. Advanced Graph Properties

### Bipartite Detection

```
A graph is bipartite ⟺ it contains no odd-length cycle.

BFS 2-coloring:
  Color source RED.
  Color all neighbors BLUE.
  Color their neighbors RED.
  If any neighbor has SAME color as current → ODD CYCLE → not bipartite.

      R──B──R
      |     |          Coloring succeeds → bipartite ✅
      B──R──B

      R──B
       \ |             R-R edge found → not bipartite ❌
        R

APPLICATIONS:
  Matching problems (assign workers to jobs)
  Conflict-free scheduling
  Two-team tournament brackets
```

### Eulerian and Hamiltonian Paths

```
EULERIAN PATH: visits every EDGE exactly once.
EULERIAN CIRCUIT: Eulerian path that starts and ends at same vertex.

Existence conditions (undirected):
  Eulerian CIRCUIT exists ⟺ graph is connected AND every vertex has EVEN degree.
  Eulerian PATH exists   ⟺ graph is connected AND exactly 2 vertices have ODD degree.
                           (path starts at one odd-degree vertex, ends at the other)

Why? Each time you enter a vertex, you must be able to leave it (except start/end).
     So all intermediate vertices need paired edges (even degree).

HAMILTONIAN PATH: visits every VERTEX exactly once.
HAMILTONIAN CIRCUIT: visits every vertex exactly once, returns to start.

No efficient existence check known.
Hamiltonian circuit = Traveling Salesman Problem (NP-complete).
No polynomial algorithm exists (unless P=NP).

This contrast is important:
  Eulerian: polynomial solution exists (Hierholzer's O(E))
  Hamiltonian: NP-complete — fundamental hardness of graph theory
```

### Graph Coloring

```
PROBLEM: Assign colors to vertices such that no two adjacent vertices
         share the same color. Minimize the number of colors.

CHROMATIC NUMBER χ(G): minimum colors needed to color graph G.

  Path graph:      χ = 2 (alternate two colors)
  Cycle (even n):  χ = 2 (bipartite)
  Cycle (odd n):   χ = 3 (odd cycle, needs third color)
  Complete Kₙ:     χ = n (every vertex adjacent to every other)

GREEDY COLORING (not always optimal but practical):
  Process vertices in some order.
  Assign each vertex the smallest color not used by its neighbors.

4-COLOR THEOREM: Every planar graph (drawable without crossing edges)
  can be colored with at most 4 colors.
  Proved in 1976 — first major theorem proved with computer assistance.

APPLICATIONS:
  Register allocation (compiler optimization)
  Scheduling (conflicting exams, tasks)
  Map coloring (adjacent regions different colors)
  Frequency assignment (radio towers)
```

---

## 9. Real-World Applications

| Domain | Problem | Graph's Role |
|---|---|---|
| **Navigation** | GPS routing (Google Maps) | Weighted directed graph; Dijkstra/A* finds shortest path |
| **Social networks** | Friend suggestions, communities | Undirected graph; BFS for degrees, SCC for communities |
| **Internet** | Web page ranking (PageRank) | Directed graph of hyperlinks; random walk analysis |
| **Compilers** | Dependency resolution, dead code | DAG; topological sort for build order |
| **Databases** | Query optimization | Join graph; optimal traversal order |
| **Biology** | Protein interaction networks | Undirected weighted graph; centrality measures |
| **Finance** | Portfolio correlation, fraud detection | Weighted complete graph; clustering |
| **Logistics** | Supply chain, delivery routing | Weighted directed graph; TSP variants |
| **Networking** | Internet routing protocols | Weighted graph; Dijkstra (OSPF), Bellman-Ford (RIP) |
| **Machine learning** | Neural networks, knowledge graphs | DAG (forward pass), knowledge graph (reasoning) |
| **Version control** | Git commit history | DAG; merge is finding common ancestor |
| **Games** | Pathfinding (A*), game state space | Weighted grid graph; A* with heuristic |

### PageRank — Graph Theory Running the Internet

```
Google's PageRank models the web as a directed graph:
  Vertices = web pages
  Edges    = hyperlinks (A→B means page A links to page B)

CORE IDEA: A page is important if important pages link to it.
  PageRank(v) = Σ [PageRank(u) / out_degree(u)]  for each u→v

This is a system of linear equations over the graph structure.
Solved iteratively: start with uniform ranks, repeatedly update.
Converges to the dominant eigenvector of the adjacency matrix.

MATHEMATICAL FOUNDATION:
  The web graph defines a random walk (surfer clicks random links).
  PageRank = probability that a random surfer is at page v at steady state.
  Vertices with many high-rank inbound edges capture more "random surfer time."

The entire multi-trillion-dollar search industry is built on
computing a vector over a directed graph.
```

### Network Flow — Graphs as Capacity Systems

```
MAX FLOW PROBLEM: Given a directed graph with edge capacities,
  find the maximum amount of flow from source S to sink T.

  S ──10── A ──10── T
  |               ↑
  └────10── B ──10┘

  Max flow = 20 (two parallel paths, each carries 10).

FORD-FULKERSON ALGORITHM:
  1. Find any path S→T with remaining capacity (augmenting path).
  2. Push as much flow as possible along that path.
  3. Update residual capacities (forward - flow, backward + flow).
  4. Repeat until no augmenting path exists.

MAX FLOW = MIN CUT (Ford-Fulkerson theorem):
  The maximum flow equals the minimum cut capacity.
  MIN CUT: minimum total capacity of edges whose removal
           disconnects S from T.

APPLICATIONS:
  Network bandwidth, traffic flow, bipartite matching,
  image segmentation, baseball elimination.
```

---

## 10. Comparison With Related Structures

```
              ┌──────────────────────────────────────────────────────────┐
              │                    RELATIONAL STRUCTURES                  │
              └────────────────────────────┬─────────────────────────────┘
                                           │
         ┌─────────────────────┬───────────┴──────────┬──────────────────┐
         ▼                     ▼                      ▼                  ▼
       GRAPH                  TREE                 LINKED LIST        MATRIX
       ─────                  ────                 ───────────        ──────
       Any connections        Hierarchical         Linear chain       Grid structure
       Cycles possible        No cycles            No branches        Fixed topology
       Any degree             1 parent (except      Degree 2 max      Degree 4 max
                              root)                 (prev+next)        (up/down/left/right)
       Most general           Special case of       Special case of    Special case of
                              graph (connected,     graph (path)       graph (planar grid)
                              acyclic, undirected)
```

**Graph vs Tree:**
A tree is a connected acyclic undirected graph. Every tree is a graph, but not every graph is a tree. Trees have strict structure (exactly one path between any two vertices); graphs allow cycles, disconnection, and multiple paths. Tree algorithms are simpler because the structure is more constrained.

**Graph vs Linked List:**
A linked list is a graph where every node has at most two connections (prev and next) and there are no cycles (in a singly linked list). It's the most constrained graph possible — a path graph.

**Graph vs Hash Map:**
Hash maps store key-value pairs with no inherent relationship between keys. Graphs store relationships between entities as first-class data. When the connections between entities are the point — use a graph. When lookup by key is the point — use a hash map.

---

## 11. The Algorithm Selection Framework

```
GRAPH PROBLEM TYPE → ALGORITHM

Traversal (visit all nodes):
  → BFS (level order, shortest hops) or DFS (deep exploration)

Shortest path, single source, unweighted:
  → BFS  O(V+E)

Shortest path, single source, non-negative weights:
  → Dijkstra  O((V+E) log V)

Shortest path, single source, negative edges:
  → Bellman-Ford  O(VE)

Shortest path, ALL pairs:
  → Floyd-Warshall  O(V³)

Minimum spanning tree:
  → Kruskal (sparse) or Prim (dense)  O(E log E) or O((V+E) log V)

Topological ordering (DAG):
  → Kahn's or DFS post-order  O(V+E)

Connected components (undirected):
  → DFS/BFS with outer loop, or Union-Find  O(V+E) or O(V α(V))

Strongly connected components (directed):
  → Kosaraju's or Tarjan's  O(V+E)

Cycle detection:
  → DFS with recursion stack (directed), parent tracking (undirected)

Bipartite check:
  → BFS 2-coloring  O(V+E)

Maximum flow:
  → Ford-Fulkerson, Edmonds-Karp, Dinic's  O(VE²) to O(V²E)

Dynamic connectivity / union queries:
  → Union-Find with path compression  O(α(V)) per operation
```

---

## 12. Tips for Long-Term Retention

**1. The map analogy — always start here**
A graph is a map. Cities are vertices. Roads are edges. One-way streets are directed edges. Toll roads are weighted edges. This analogy covers 90% of graph intuitions: shortest path = fastest route, connected components = which cities can you reach, MST = minimum road network to connect all cities.

**2. Every data structure you know is a graph**
Linked list = path graph. Tree = connected acyclic graph. Grid = planar graph with degree-4 nodes. Arrays = path graph with indexed vertices. When you see a new data structure, ask: "what kind of graph is this?" This unifies all of data structures under one framework.

**3. The two representations and when to use them**
Adjacency list: default (sparse graphs, most problems). Adjacency matrix: when you constantly need "does edge (u,v) exist?" Internalize the space tradeoff: list is O(V+E), matrix is O(V²). For V=1M, E=5M: list=40MB, matrix=4TB. The choice is obvious in practice.

**4. Algorithm selection by problem signature**
- "Shortest path, no weights" → BFS
- "Shortest path, weights ≥ 0" → Dijkstra
- "Order tasks with dependencies" → Topological sort
- "Connect everything cheaply" → MST
- "Are these two things connected?" → Union-Find
- "Find all tight-knit groups (directed)" → SCC

**5. DFS reveals structure; BFS reveals distance**
This is the deepest intuition about the two traversals. DFS's finishing times encode topological order and SCC structure. BFS's level structure encodes distance. When a problem cares about the STRUCTURE of the graph (cycles, ordering, components), think DFS. When it cares about DISTANCE (shortest path, minimum hops), think BFS.

**6. The Union-Find reflex**
Any time a problem involves dynamically connecting things and asking "are X and Y connected?", Union-Find is the answer. It's O(α(n)) ≈ O(1) per operation — essentially free. Kruskal's MST, percolation, dynamic connectivity — all use Union-Find. Train the reflex: "connectivity query over changing set" → Union-Find.

**7. Graphs are the language of relationships**
When a problem describes entities with relationships between them — friendships, dependencies, connections, links, routes, flows — you are looking at a graph. The act of MODELING a problem as a graph (choosing what are vertices and what are edges) is more important than knowing any specific algorithm. Master the modeling, and the algorithm selection follows naturally.

---

Graphs are the most powerful and general structure in all of computer science because they are the mathematical formalization of **connection** itself. Every network, every relationship, every dependency, every route is a graph. The algorithms that operate on graphs — finding paths, ordering dependencies, connecting efficiently, routing flow — are not just theoretical tools. They run the internet's routing, power Google's search rankings, optimize supply chains, model protein interactions, and enable every GPS navigation system on Earth. To understand graphs deeply is to hold the key to an enormous fraction of all computational problems ever posed.
