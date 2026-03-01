# Graphs (Interview-Ready Guide)

Using `[TOPIC] = Graphs`.

## 0) Scope (Checklist)
- [x] Representations (adj list/matrix, edge list)
- [x] BFS/DFS traversals
- [x] Connected components
- [x] Cycle detection (directed/undirected)
- [x] Topological sort (Kahn/DFS)
- [x] Shortest paths: BFS, Dijkstra, Bellman-Ford, Floyd-Warshall
- [x] Union-Find / DSU
- [x] Minimum spanning tree (Kruskal/Prim)
- [x] Bipartite check
- [x] Grid graphs (islands, multi-source BFS)

## 1) Foundations
Graph = vertices + edges (directed/undirected, weighted/unweighted).

Core terms:
- Neighbor, degree, path, cycle, component
- DAG, topological order
- Relaxation (shortest path update)

Mental model:
- Traversal answers reachability.
- Shortest-path algorithms differ by edge constraints.
- DSU manages dynamic connectivity.

## 2) How it works
Cause-effect:
1. BFS explores in increasing edge distance (unweighted shortest path).
2. DFS explores depth for structure (cycles, topo via finish order).
3. Dijkstra uses min-distance frontier (non-negative weights).
4. Bellman-Ford relaxes all edges repeatedly (handles negative edges).
5. MST picks cheapest edges while avoiding cycles.

Tiny trace (unweighted shortest path):
- Graph: `0-1-2`, `0-3`, `3-2`
- BFS from `0`: level0 `{0}`, level1 `{1,3}`, level2 `{2}`
- Shortest distance to `2` is 2 edges.

## 3) Patterns (Interview Templates)
1. BFS queue with `visited`
2. DFS recursion/stack with color/state
3. Topological sort (Kahn indegree queue)
4. Dijkstra (priority queue + relax)
5. DSU (`find` + `union` with path compression/rank)

Invariants:
- Visited nodes are processed once.
- In Dijkstra, popped node has finalized shortest distance.
- Kahn queue always contains indegree-0 nodes.
- DSU roots represent disjoint components.

Signals:
- "Dependencies/order constraints" -> topo
- "Shortest path" -> choose by weights
- "Dynamic merging/connectivity" -> DSU

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Number of Islands
- Approach: DFS/BFS on grid components.

2. Medium: Course Schedule
- Approach: detect cycle with topo sort; feasible if all nodes processed.

3. Medium: Network Delay Time
- Approach: Dijkstra from source.

4. Hard: Redundant Connection / MST
- Approach: DSU for cycle edge or Kruskal for MST.

5. Hard: Cheapest Flights Within K Stops
- Approach: layered BFS/DP/Bellman-Ford variant by stops.

## 5) Why & What-if
Edge cases:
- Disconnected graphs
- Multiple edges/self loops
- Negative weights/cycles

Pitfalls:
- Forgetting to reset visited between component scans
- Using Dijkstra with negative edges
- Not handling directed vs undirected cycle logic separately

Why it works:
- Each algorithm is built around a property: level order, relaxation correctness, or cut/cycle property.

Variations:
- 0-1 BFS for edges with weights {0,1}
- Floyd-Warshall for dense all-pairs and small `n`

## 6) Complexity and Tradeoffs
- BFS/DFS: `O(V+E)`
- Topo sort: `O(V+E)`
- Dijkstra: `O((V+E) log V)` with heap
- Bellman-Ford: `O(VE)`
- Floyd-Warshall: `O(V^3)`
- DSU ops: near `O(1)` amortized
- Kruskal: `O(E log E)`, Prim: `O(E log V)`

Tradeoffs:
- Simpler algorithms may be slower but robust for constraints (Bellman-Ford).

## 7) Real-world uses
- Routing/navigation
- Build systems dependency resolution
- Social network connectivity
- Clustering and network design (MST)

## 8) Comparisons
- BFS vs DFS:
  - BFS shortest unweighted path.
  - DFS structure/cycle/path existence.
- Dijkstra vs Bellman-Ford:
  - Dijkstra faster but no negative edges.
  - Bellman-Ford handles negatives and detects negative cycles.
- Kruskal vs Prim:
  - Kruskal edge-centric with DSU.
  - Prim grows tree from a node.

## 9) Retention
Cheat sheet:
- Unweighted shortest -> BFS.
- DAG order -> topo sort.
- Non-negative weighted shortest -> Dijkstra.
- Negative edges -> Bellman-Ford.
- Connectivity merges -> DSU.

Recall hooks:
- "BFS by layers, Dijkstra by cheapest frontier."
- "DSU answers who is connected now."

Practice (10):
1. Easy: Find if Path Exists in Graph
2. Easy: Number of Islands
3. Medium: Clone Graph
4. Medium: Course Schedule
5. Medium: Bipartite Graph
6. Medium: Network Delay Time
7. Medium: Number of Provinces (DSU)
8. Hard: Alien Dictionary
9. Hard: Critical Connections in a Network
10. Hard: Min Cost to Connect All Points
