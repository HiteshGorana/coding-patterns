# Deep Problem-Solving Foundations (Interview-Ready Guide)

Using `[TOPIC] = Deep Problem-Solving Foundations`.

## 0) Scope (Checklist)
- [x] Problem modeling from story to formal input/output
- [x] Constraints-first algorithm selection
- [x] Correctness proofs (invariant, exchange, induction, contradiction)
- [x] State design (recursion, DP, BFS with extra state)
- [x] Data-structure choice by operation costs
- [x] Monotonicity and binary search thinking
- [x] Graph modeling from non-graph statements
- [x] Complexity budgeting and lower-bound intuition
- [x] Edge-case and adversarial testing
- [x] Optimization path: brute -> better -> optimal

## 1) Foundations
Deep understanding is not memorizing 100 problems.
It is recognizing structural properties and proving why your approach works.

Core principles:
- Model first, pattern second.
- Constraints decide feasible complexity.
- Invariants make solutions reliable.
- Every optimization must preserve correctness.

Mental model:
Every good solution answers three questions:
1. What is the minimal state I must track?
2. What transition updates that state?
3. Why does this guarantee correctness and complexity bounds?

## 2) How it works (Solving Loop)
1. Restate the problem in one line: input -> output -> objective.
2. Write constraints and derive time budget.
3. Start from brute force and identify the bottleneck.
4. Detect key structure: sorted, monotonic, overlapping subproblems, DAG/dependency, connectivity, range query.
5. Choose algorithm family and data structure around that structure.
6. State a quick proof idea before coding.
7. Code with explicit invariants in mind.
8. Test with normal, boundary, and adversarial cases.

Tiny trace:
- Problem: shortest path in a grid with obstacles and equal step cost.
- Structure: unweighted graph shortest path.
- Correct tool: BFS (not DFS).
- Why: BFS explores by layers, so first visit gives shortest distance.

## 3) Important Topics to Learn Deeply
1. Problem modeling and reduction
   - Convert narrative problems into arrays, intervals, trees, graphs, or state machines.
   - Reduce uncommon wording to a standard known form.

2. Complexity budgeting
   - Estimate feasible runtime from `n` before selecting approach.
   - Typical interview budget:
     - `n <= 20`: brute force, backtracking, bitmask.
     - `n <= 1e3`: often `O(n^2)` is acceptable.
     - `n <= 1e5`: target `O(n log n)` or `O(n)`.

3. Correctness proof techniques
   - Loop invariant for two pointers, sliding window, binary search.
   - Exchange argument for greedy.
   - Induction for recursion and DP.
   - Cut/cycle properties for MST and graph correctness.

4. State design
   - Recursion: function parameters must capture full future decision context.
   - DP: define `dp[state]` with exact meaning before transitions.
   - Graph/state BFS: include extra state when constraints depend on history (keys, parity, mask).

5. Monotonicity and decision predicates
   - If a yes/no predicate becomes true and stays true (or false and stays false), binary search on answer applies.
   - Practice proving monotonicity explicitly.

6. Data-structure operation calculus
   - Choose structures by dominant operations:
     - Frequent membership/count: hash map/set.
     - Range min/max/next greater: monotonic stack/deque.
     - Dynamic top-k: heap.
     - Dynamic connectivity: DSU.
     - Dynamic range updates/queries: Fenwick/segment tree.

7. Graph thinking
   - Many non-graph problems are implicit graphs.
   - Choose shortest-path algorithm by edge type:
     - Unweighted: BFS.
     - Non-negative weights: Dijkstra.
     - Negative edges: Bellman-Ford/Floyd-Warshall (by constraints).

8. Optimization ladder
   - Standard upgrade path:
     - Brute force
     - Prune/reorder
     - Precompute (prefix/suffix, sorting)
     - Cache (memoization/DP)
     - Better data structure
     - Mathematical shortcut

9. Edge-case discipline
   - Always test:
     - Empty or single element.
     - All equal or strictly increasing/decreasing.
     - Duplicates and negative values.
     - Overflow-risk values.
     - Disconnected or impossible cases.

10. Communication and implementation discipline
   - Explain tradeoffs, not just final code.
   - Keep variable names tied to state meaning.
   - Validate invariants with a small dry run before finalizing.

## 4) Examples (Deep Thinking in Action)
1. Two Sum
   - Bottleneck in brute force is pair scan `O(n^2)`.
   - Need fast "have we seen complement?" lookup.
   - Hash map gives `O(1)` expected lookup -> `O(n)` total.

2. Koko Eating Bananas
   - Goal is minimum feasible speed.
   - Feasibility predicate "can finish within h hours" is monotonic.
   - Use binary search on answer over speed range.

3. Coin Change (min coins)
   - Greedy fails for arbitrary denominations.
   - Overlapping subproblems + optimal substructure -> DP.
   - `dp[a]` = minimum coins to form amount `a`.

## 5) Why & What-if
Common failure modes:
- Choosing pattern from memory without checking constraints.
- Writing recurrence before defining state meaning.
- Using Dijkstra with negative edges.
- Using greedy without proof.

Recovery questions:
- What exact property am I using?
- Can I produce a counterexample?
- What invariant remains true after each step?

## 6) Complexity and Tradeoffs
- Fastest code is not always safest code under interview pressure.
- Prefer the simplest correct approach within constraints.
Tradeoff checklist:
- Simpler + slightly slower but passes constraints is often better.
- More advanced structures are useful only when bottleneck demands them.

## 7) Real-world uses
- Scheduling and planning under constraints
- Routing and recommendation systems
- Caching and query optimization
- Fraud/anomaly detection with graph modeling

## 8) Comparisons
Pattern memorization vs principle-first thinking:
- Memorization is fast for familiar questions.
- Principle-first adapts to new and twisted questions.

Brute-force-first vs jump-to-optimal:
- Brute force clarifies correctness baseline.
- Then optimize systematically without losing correctness.

## 9) Retention
Cheat sheet:
- Model -> constraints -> bottleneck -> structure -> tool -> proof -> test.
- If your proof is unclear, your solution is not ready.
- If your edge cases are untested, your implementation is not ready.

Weekly deep-practice routine:
1. Pick 2 solved problems and re-derive from scratch without notes.
2. For each, write one-paragraph correctness proof.
3. Create one variant and adapt your solution.
4. Compare two different valid approaches and tradeoffs.
