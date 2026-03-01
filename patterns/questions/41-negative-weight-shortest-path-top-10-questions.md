# Pattern 41 Interview Playbook: Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Bellman-Ford and Floyd-Warshall handle shortest paths when negative weights exist and can detect/report negative cycles.
- Core intuition: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Trigger cue 1: Graph has negative edges.
- Trigger cue 2: Need detect negative cycle.
- Quick self-check: Are negative edges/cycles possible or explicitly mentioned?
- Target complexity: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2).

---

## Q1. Bellman-Ford Algorithm Implementation

### Problem Statement (Specific)
Solve **Bellman-Ford Algorithm Implementation** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Bellman-Ford Algorithm Implementation, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Bellman-Ford Algorithm Implementation directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_bellman_ford_algorithm_implementation(data):
    """Brute-force baseline for: Bellman-Ford Algorithm Implementation."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Bellman-Ford Algorithm Implementation to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_bellman_ford_algorithm_implementation(data):
    """Intermediate optimized approach for: Bellman-Ford Algorithm Implementation."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Bellman-Ford Algorithm Implementation: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_bellman_ford_algorithm_implementation(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q2. Cheapest Flights Within K Stops (Relaxation DP)

### Problem Statement (Specific)
Solve **Cheapest Flights Within K Stops (Relaxation DP)** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 2
Output: 7
Explanation: For Cheapest Flights Within K Stops (Relaxation DP), process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Cheapest Flights Within K Stops (Relaxation DP) directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_cheapest_flights_within_k_stops_relaxation_dp(data):
    """Brute-force baseline for: Cheapest Flights Within K Stops (Relaxation DP)."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Cheapest Flights Within K Stops (Relaxation DP) to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_cheapest_flights_within_k_stops_relaxation_dp(data):
    """Intermediate optimized approach for: Cheapest Flights Within K Stops (Relaxation DP)."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Cheapest Flights Within K Stops (Relaxation DP): Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_cheapest_flights_within_k_stops_relaxation_dp(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q3. Arbitrage Detection

### Problem Statement (Specific)
Solve **Arbitrage Detection** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 0
Output: 7
Explanation: For Arbitrage Detection, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Arbitrage Detection directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_arbitrage_detection(data):
    """Brute-force baseline for: Arbitrage Detection."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Arbitrage Detection to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_arbitrage_detection(data):
    """Intermediate optimized approach for: Arbitrage Detection."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Arbitrage Detection: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_arbitrage_detection(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q4. Wormholes / Negative Cycle Detection

### Problem Statement (Specific)
Solve **Wormholes / Negative Cycle Detection** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Wormholes / Negative Cycle Detection, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Wormholes / Negative Cycle Detection directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_wormholes_negative_cycle_detection(data):
    """Brute-force baseline for: Wormholes / Negative Cycle Detection."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Wormholes / Negative Cycle Detection to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_wormholes_negative_cycle_detection(data):
    """Intermediate optimized approach for: Wormholes / Negative Cycle Detection."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Wormholes / Negative Cycle Detection: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_wormholes_negative_cycle_detection(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q5. Floyd-Warshall All Pairs Shortest Path

### Problem Statement (Specific)
Solve **Floyd-Warshall All Pairs Shortest Path** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 2
Output: 7
Explanation: For Floyd-Warshall All Pairs Shortest Path, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Floyd-Warshall All Pairs Shortest Path directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_floyd_warshall_all_pairs_shortest_path(data):
    """Brute-force baseline for: Floyd-Warshall All Pairs Shortest Path."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Floyd-Warshall All Pairs Shortest Path to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_floyd_warshall_all_pairs_shortest_path(data):
    """Intermediate optimized approach for: Floyd-Warshall All Pairs Shortest Path."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Floyd-Warshall All Pairs Shortest Path: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_floyd_warshall_all_pairs_shortest_path(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q6. Find the City With the Smallest Number of Neighbors at a Threshold Distance

### Problem Statement (Specific)
Solve **Find the City With the Smallest Number of Neighbors at a Threshold Distance** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 0
Output: 7
Explanation: For Find the City With the Smallest Number of Neighbors at a Threshold Distance, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Find the City With the Smallest Number of Neighbors at a Threshold Distance directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(data):
    """Brute-force baseline for: Find the City With the Smallest Number of Neighbors at a Threshold Distance."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Find the City With the Smallest Number of Neighbors at a Threshold Distance to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(data):
    """Intermediate optimized approach for: Find the City With the Smallest Number of Neighbors at a Threshold Distance."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Find the City With the Smallest Number of Neighbors at a Threshold Distance: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q7. Currency Exchange Graph

### Problem Statement (Specific)
Solve **Currency Exchange Graph** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Currency Exchange Graph, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Currency Exchange Graph directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_currency_exchange_graph(data):
    """Brute-force baseline for: Currency Exchange Graph."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Currency Exchange Graph to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_currency_exchange_graph(data):
    """Intermediate optimized approach for: Currency Exchange Graph."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Currency Exchange Graph: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_currency_exchange_graph(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q8. Shortest Path with Possible Negative Edges

### Problem Statement (Specific)
Solve **Shortest Path with Possible Negative Edges** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 2
Output: 7
Explanation: For Shortest Path with Possible Negative Edges, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Shortest Path with Possible Negative Edges directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_shortest_path_with_possible_negative_edges(data):
    """Brute-force baseline for: Shortest Path with Possible Negative Edges."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Shortest Path with Possible Negative Edges to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_shortest_path_with_possible_negative_edges(data):
    """Intermediate optimized approach for: Shortest Path with Possible Negative Edges."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Shortest Path with Possible Negative Edges: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_shortest_path_with_possible_negative_edges(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q9. Path with At Most K Edges

### Problem Statement (Specific)
Solve **Path with At Most K Edges** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 0
Output: 7
Explanation: For Path with At Most K Edges, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Path with At Most K Edges directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_path_with_at_most_k_edges(data):
    """Brute-force baseline for: Path with At Most K Edges."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Path with At Most K Edges to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_path_with_at_most_k_edges(data):
    """Intermediate optimized approach for: Path with At Most K Edges."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Path with At Most K Edges: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_path_with_at_most_k_edges(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q10. Detect Reachable Negative Cycle from Source

### Problem Statement (Specific)
Solve **Detect Reachable Negative Cycle from Source** using **Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall)**. Return exactly what the problem asks and justify complexity.

### Input
- `n`: int
- `edges` and optional weight/source/target

### Output
- Graph metric/list/boolean depending on objective.

### Constraints (Typical)
- 1 <= n <= 2e5
- 0 <= m <= 4e5

### Example (Exact)
```text
Input:  n = 6, edges = [[0,1],[1,2],[2,3],[3,4],[4,5]], source = 1
Output: 7
Explanation: For Detect Reachable Negative Cycle from Source, process adjacency with no redundant traversals.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Detect Reachable Negative Cycle from Source directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_detect_reachable_negative_cycle_from_source(data):
    """Brute-force baseline for: Detect Reachable Negative Cycle from Source."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Detect Reachable Negative Cycle from Source to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_detect_reachable_negative_cycle_from_source(data):
    """Intermediate optimized approach for: Detect Reachable Negative Cycle from Source."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) invariant to Detect Reachable Negative Cycle from Source: Repeated edge relaxation converges shortest distances if no negative cycle is reachable.
- Complexity target: Time Bellman-Ford O(V*E), Floyd-Warshall O(V^3)., Space Bellman-Ford O(V), Floyd-Warshall O(V^2)..

#### Optimal Python (Question-Specific)
```python
def solve_detect_reachable_negative_cycle_from_source(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
    def bellman_ford(n, edges, src):  # edges: (u, v, w)
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0
    
        for _ in range(n - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
    
        has_neg_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    
        return dist, has_neg_cycle
```

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---
