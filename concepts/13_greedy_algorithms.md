# Greedy Algorithms: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

A **greedy algorithm** is an algorithmic paradigm that builds a solution piece by piece, at each step making the choice that looks **best at that moment** — the locally optimal choice — without reconsidering past decisions or worrying about future consequences. It bets that a sequence of locally optimal choices will produce a globally optimal solution.

```
GREEDY DECISION PROCESS:

Current State → Look at available choices → Pick the best-looking one
     ↑                                              |
     └──────────── advance to new state ←───────────┘
                   (no going back)

No backtracking. No reconsideration. Commit and move forward.
```

**Core components:**

- **Greedy choice** — the locally optimal selection made at each step, based solely on current information
- **Greedy choice property** — the theoretical guarantee that a locally optimal choice is always part of some globally optimal solution
- **Optimal substructure** — after making a greedy choice, the remaining subproblem has the same structure as the original (shared with DP, but greedy only needs one subproblem, not all)
- **Feasibility** — each choice must satisfy the problem's constraints
- **Irrevocability** — once made, a choice is never undone
- **Proof of correctness** — the non-obvious but essential step; greedy works only when you can prove that local optimality implies global optimality

The central tension: greedy algorithms are **fast and simple** but only correct for a specific class of problems. Knowing when greedy is valid — and when it silently fails — is the entire skill.

---

## 2. The Physical Analogy: Hiking to the Highest Peak

Imagine trying to reach the highest point in a mountain range, but you can only see your immediate surroundings. A greedy strategy says: **always step in the direction that goes most steeply upward**.

```
MOUNTAIN RANGE PROFILE:

                      ★ (global max)
                     /\
          local max /  \
              /\   /    \
             /  \ /      \
────────────/    X        \──────────
                ↑
         greedy starts here → goes up local hill → gets stuck

Greedy climber:  reaches local maximum, thinks it's done ❌
Optimal climber: explores entire range, finds true peak ✅
```

This analogy captures both when greedy works and when it fails:
- **Flat terrain** (only one peak): greedy always reaches the global maximum ✅
- **Multiple peaks** (local maxima exist): greedy gets trapped ❌

The mathematical guarantee that a problem has "only one effective peak" — that locally good choices lead to the global best — is the **greedy choice property**. Establishing it is what separates valid greedy algorithms from incorrect ones.

---

## 3. The Two Proof Techniques

Every correct greedy algorithm rests on a proof. There are two standard proof structures:

### Proof by Exchange Argument

```
TECHNIQUE: Assume an optimal solution OPT exists that differs from
           the greedy solution GREEDY. Show you can transform OPT
           into GREEDY one swap at a time without worsening the result.
           Conclusion: GREEDY is at least as good as OPT → GREEDY is optimal.

TEMPLATE:
  1. Take any optimal solution OPT.
  2. Find the first position where OPT differs from GREEDY.
  3. "Exchange" OPT's choice at that position with GREEDY's choice.
  4. Show the exchange doesn't make the solution worse.
  5. Repeat until OPT = GREEDY.
  6. Therefore GREEDY is optimal.
```

### Proof by Greedy Stays Ahead

```
TECHNIQUE: Show that at every step, the greedy solution is
           at least as good as any other partial solution
           by some well-chosen measure.

TEMPLATE:
  Define measure M (e.g., "tasks completed by time t").
  Prove: at every step k, M(GREEDY after k steps) ≥ M(any other after k steps).
  Since GREEDY "stays ahead" at every step, it ends ahead.
  Therefore GREEDY is optimal.
```

These proofs aren't just academic formalities — they are the mechanism that tells you **why** greedy works for specific problems and helps you recognize when a problem is greedy-amenable.

---

## 4. Classic Example 1: Activity Selection

**Problem:** Given n activities with start and end times, select the maximum number of non-overlapping activities.

```
Activities (sorted by end time):
  A: [1, 4]
  B: [3, 5]
  C: [0, 6]
  D: [5, 7]
  E: [3, 9]
  F: [6, 10]
  G: [8, 11]

GREEDY CHOICE: Always pick the activity that ends earliest
               (and doesn't conflict with the last selected).

WHY THIS CHOICE? Finishing earliest leaves maximum room for future activities.
```

**Step-by-step trace:**

```
Sort by end time: A[1,4], B[3,5], C[0,6], D[5,7], E[3,9], F[6,10], G[8,11]

Step 1: Pick A[1,4] (ends earliest). last_end = 4.
        Selected: {A}

        Timeline: ████A████
                  1        4

Step 2: B[3,5]: starts at 3 < 4 = last_end → CONFLICT, skip.
        C[0,6]: starts at 0 < 4 → CONFLICT, skip.
        D[5,7]: starts at 5 ≥ 4 → COMPATIBLE. Pick D. last_end = 7.
        Selected: {A, D}

        Timeline: ████A████ ████D████
                  1        4 5       7

Step 3: E[3,9]: 3 < 7 → skip.
        F[6,10]: 6 < 7 → skip.
        G[8,11]: 8 ≥ 7 → COMPATIBLE. Pick G. last_end = 11.
        Selected: {A, D, G}

        Timeline: ████A████ ████D████ ████G████
                  1        4 5       7 8        11

Answer: 3 activities {A, D, G}. Maximum possible? YES ✅
```

**Exchange argument proof (sketch):**

```
Suppose OPT selects a different first activity X that ends at time t_X ≥ t_A.
Replace X with A (which ends at t_A ≤ t_X):
  - A doesn't conflict with anything X didn't conflict with
    (A ends earlier, so anything compatible with X is compatible with A)
  - Total count stays the same or improves

Repeat for each position where OPT differs from GREEDY.
At each exchange, we never decrease the count.
Therefore GREEDY is at least as good as OPT. ✅
```

---

## 5. Classic Example 2: Huffman Encoding

**Problem:** Given character frequencies, build a prefix-free binary code that minimizes total encoded length.

```
Characters and frequencies:
  A:45  B:13  C:12  D:16  E:9  F:5

GOAL: High-frequency characters get shorter codes,
      low-frequency characters get longer codes.

GREEDY CHOICE: Always merge the two lowest-frequency nodes first.
```

**Building the Huffman tree:**

```
Initial heap (sorted by frequency):
  F:5  E:9  C:12  B:13  D:16  A:45

Step 1: Merge two smallest (F:5, E:9) → internal node FE:14
  Heap: C:12  B:13  FE:14  D:16  A:45

Step 2: Merge (C:12, B:13) → CB:25
  Heap: FE:14  D:16  CB:25  A:45

Step 3: Merge (FE:14, D:16) → FED:30
  Heap: CB:25  FED:30  A:45

Step 4: Merge (CB:25, FED:30) → CBFED:55
  Heap: A:45  CBFED:55

Step 5: Merge (A:45, CBFED:55) → ROOT:100

RESULTING TREE:
              ROOT(100)
             /          \
           A(45)       CBFED(55)
                       /        \
                    CB(25)      FED(30)
                   /    \       /     \
                 C(12) B(13) FE(14)  D(16)
                             /    \
                           F(5)  E(9)

CODES (path from root: left=0, right=1):
  A:  0        (1 bit  — most frequent)
  C:  100      (3 bits)
  B:  101      (3 bits)
  D:  111      (3 bits)
  F:  1100     (4 bits — least frequent)
  E:  1101     (4 bits — least frequent)

TOTAL BITS = 45×1 + 12×3 + 13×3 + 16×3 + 5×4 + 9×4
           = 45 + 36 + 39 + 48 + 20 + 36 = 224 bits

Fixed-length encoding (3 bits each): 300 bits
Huffman savings: 25% compression ✅
```

**Why merge the two smallest?**

```
Each merge creates an internal node. Its frequency = sum of children.
This internal node's frequency gets ADDED to the total encoding cost
every time it appears as an ancestor.

Nodes that are merged EARLY become DEEPER in the tree (longer codes).
So we want LOW-frequency nodes to be deep (merged early) and
HIGH-frequency nodes to be shallow (merged late).

Merging the two smallest first ensures the lowest-frequency
characters always end up deepest. This is provably optimal by
exchange argument: swapping any two characters in the tree
where the lower-frequency one is higher cannot improve total cost.
```

---

## 6. Classic Example 3: Dijkstra's Algorithm as Greedy

```
Dijkstra's shortest path IS a greedy algorithm:
  At each step: pick the unvisited vertex with minimum known distance.
  This is the "greedy choice" — always extend the cheapest known path.

GREEDY CHOICE PROPERTY FOR DIJKSTRA:
  When we pick vertex u with distance d[u], d[u] is FINAL.
  WHY: Any other path to u must go through unvisited vertices,
       all with distance ≥ d[u] (non-negative edges).
       Adding more non-negative edges cannot decrease cost.
       Therefore no cheaper path to u exists.

This greedy justification FAILS for negative edges:
  A future negative edge could create a cheaper path to u.
  Greedy locks in d[u] prematurely → wrong answer.
  → Bellman-Ford (DP, not greedy) handles negative edges.
```

---

## 7. Classic Example 4: Fractional Knapsack

**Problem:** Items with weights and values. Knapsack capacity W. Maximize value. Items can be taken fractionally.

```
Items:           weight  value  value/weight ratio
  Gold dust:       10     60       6.0   ← highest ratio
  Silver dust:     20     100      5.0
  Bronze dust:     30     120      4.0

Capacity W = 50

GREEDY CHOICE: Take items in decreasing order of value/weight ratio.
               Take as much as possible of the current best item.

Step 1: Take ALL Gold dust (10 units, value 60). Remaining: 40.
Step 2: Take ALL Silver dust (20 units, value 100). Remaining: 20.
Step 3: Take 20/30 of Bronze dust (value = 120 × 20/30 = 80).

Total value: 60 + 100 + 80 = 240 ✅  (provably optimal for fractional)
```

**Why does greedy fail for 0/1 knapsack?**

```
0/1 Knapsack (can't split items):
  Items: weight=[10, 20, 30]   value=[60, 100, 120]   W=50

  Greedy by ratio: Take Gold(10, ratio=6.0), Silver(20, ratio=5.0)
    Total: weight=30, value=160. 20 capacity wasted.

  DP optimal: Take Silver(20) + Bronze(30)
    Total: weight=50, value=220 > 160 ✅

  WHY GREEDY FAILS: Can't take a fraction, so a high-ratio item
    that "wastes" capacity can be beaten by a combination of
    lower-ratio items that perfectly fill the knapsack.
    The indivisibility breaks the greedy choice property.
```

---

## 8. Classic Example 5: Minimum Spanning Tree

Both Kruskal's and Prim's algorithms are greedy — they make locally optimal choices that provably yield a globally optimal spanning tree.

### Kruskal's — Greedy by Edge Weight

```
GREEDY CHOICE: Always add the cheapest edge that doesn't create a cycle.

Graph edges sorted by weight:
  (A,B,1), (C,D,2), (A,C,3), (B,C,4), (B,D,5)

Step 1: (A,B,1): no cycle → ADD.    MST: {A-B}
Step 2: (C,D,2): no cycle → ADD.    MST: {A-B, C-D}
Step 3: (A,C,3): no cycle → ADD.    MST: {A-B, C-D, A-C}  ← connects two components
Step 4: (B,C,4): creates cycle A-B-C-A → SKIP.
Step 5: (B,D,5): creates cycle → SKIP.

MST total weight: 1+2+3 = 6 ✅

GREEDY CHOICE PROPERTY (cut property):
  For any cut of the graph (partition of vertices into two sets),
  the minimum-weight edge crossing the cut is in SOME MST.
  → Adding the globally cheapest non-cycle-creating edge is always safe.
```

### Prim's — Greedy by Vertex Expansion

```
GREEDY CHOICE: Always add the cheapest edge connecting the current
               tree to an unvisited vertex.

Start at A. In-tree: {A}

Step 1: Edges from A: (A,B,1),(A,C,3). Cheapest: (A,B,1). Add B.
Step 2: Edges from {A,B}: (A,C,3),(B,C,4),(B,D,5). Cheapest: (A,C,3). Add C.
Step 3: Edges from {A,B,C}: (C,D,2),(B,D,5). Cheapest: (C,D,2). Add D.

MST: {A-B, A-C, C-D}. Total: 1+3+2 = 6 ✅

Same MST, different greedy strategy. Both correct by the cut property.
```

---

## 9. The Greedy Failure Gallery — When Local ≠ Global

Understanding greedy failures is as important as understanding successes.

### Failure 1: Coin Change with Non-Standard Denominations

```
coins = [1, 3, 4]    target = 6

GREEDY (largest coin first):
  Take 4: remaining = 2
  Take 1: remaining = 1
  Take 1: remaining = 0
  Total: 3 coins

OPTIMAL (DP):
  Take 3: remaining = 3
  Take 3: remaining = 0
  Total: 2 coins ✅

WHY GREEDY FAILS:
  Choosing the locally largest coin (4) misses the combination
  that perfectly partitions the target (3+3).
  The greedy choice is not part of any optimal solution here.
  No exchange argument can rescue it.

WHEN GREEDY WORKS (US coins [1,5,10,25]):
  The denominations have a special divisibility structure.
  Each coin is a multiple of smaller coins — greedy choices
  are provably optimal by induction on this structure.
```

### Failure 2: 0/1 Knapsack

```
Already shown above. Summary:
  Fractional version: greedy by ratio is optimal ✅
  Integer version:    greedy by ratio can be arbitrarily bad ❌

  Example where greedy is worst possible:
    items = [(weight=1, value=1), (weight=W, value=W)]
    Greedy picks item 1 (ratio 1) first, then can't fit item 2.
    Gets value 1. Optimal: just item 2, value W.
    Ratio: 1/W → arbitrarily bad as W grows.
```

### Failure 3: Shortest Path with Negative Edges

```
Already shown in Dijkstra section.
Greedy "locks in" a distance prematurely.
A future negative edge could offer a cheaper route.
→ Greedy commits too early when future decisions can improve past ones.
```

### Failure 4: Traveling Salesman (Nearest Neighbor)

```
GREEDY: From current city, always go to the nearest unvisited city.

  Cities: A-B:1, B-C:1, C-D:1, D-A:1, A-C:10, B-D:10

  Greedy from A: A→B(1)→C(1)→D(1)→A(1) = 4 ✅ (happens to be optimal here)

  But with different weights, nearest neighbor can be significantly
  worse than optimal. TSP greedy produces tours ~20-25% above optimal
  on average. For worst case: can be O(log n) times optimal.

TSP is NP-hard. No polynomial-time algorithm guarantees optimality.
Greedy gives a fast approximation but no optimality guarantee.
```

---

## 10. The "Why" Questions

### Why does greedy work for activity selection but not scheduling to minimize total wait?

```
ACTIVITY SELECTION (maximize count):
  Greedy by earliest end time → optimal ✅

  Exchange argument: replacing any later-ending activity with
  an earlier-ending one never reduces the count.

MINIMIZE TOTAL WEIGHTED COMPLETION TIME:
  Jobs with different weights: should you always pick the shortest job?
  
  Only if we're minimizing total completion time (unweighted).
  For weighted: schedule in order of weight/processing_time ratio.
  
  WRONG greedy: shortest job first (ignores weights).
  RIGHT greedy: highest weight/time ratio first.

  KEY: The choice of WHAT to optimize determines WHICH greedy is correct.
  Different objective → different greedy choice → different proof required.
```

### Why is "earliest deadline first" optimal for scheduling without missing deadlines?

```
PROBLEM: Tasks with deadlines and equal durations. Maximize tasks completed on time.

GREEDY: Process tasks in order of earliest deadline.

PROOF (greedy stays ahead):
  Suppose we have two tasks A (deadline 3) and B (deadline 5).
  If we process B before A:
    A might miss its deadline (processed after time 3).
    B would complete before time 5 anyway.
  If we process A before B:
    A meets its deadline (processed before time 3).
    B has more time remaining → also meets deadline.
  Processing the earlier-deadline task first is always at least as good.
  → By induction, always processing the earliest deadline first is optimal.
```

### Why does Huffman produce an optimal prefix-free code?

```
PROOF SKETCH (exchange argument):

CLAIM: If x and y are the two least-frequent characters, there exists
       an optimal tree where x and y are the deepest nodes (siblings).

PROOF: Take any optimal tree T.
  Let a and b be the two deepest sibling nodes (longest codes).
  Since x and y have the smallest frequencies and a,b are deepest:
    freq(x) ≤ freq(a) and freq(y) ≤ freq(b)
  
  Swap x with a: cost change = (depth_a - depth_x) × (freq(x) - freq(a)) ≤ 0
  (Moving lower-frequency to deeper position doesn't increase cost)
  
  After swap, x and a are in each other's position.
  Do the same for y and b.
  
  Result: x and y are the deepest nodes, cost ≤ original optimal cost.
  Therefore the greedy first step (merge x and y) is valid.
  
  By induction on the merged tree: Huffman produces optimal code. ✅
```

---

## 11. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| All activities have the same end time | Any single one is a valid greedy choice; all have equal count |
| Two items have equal priority in greedy | Either choice is correct (ties don't affect optimality in most greedy algorithms) |
| Huffman with all equal frequencies | Any valid tree structure is optimal; Huffman builds a balanced tree |
| Activity selection with weighted activities | Greedy by earliest end fails; need DP (weighted job scheduling) |
| Fractional knapsack with W = 0 | Base case: take nothing, value = 0 |
| Graph has no MST (disconnected) | Kruskal/Prim find forest, not tree; each component gets its own tree |
| Dijkstra on unweighted graph | Degenerates to BFS (all edge weights = 1, greedy choice is trivial) |
| Greedy produces wrong answer | The problem likely lacks greedy choice property; switch to DP or backtracking |
| Need to verify greedy correctness | Attempt exchange argument; if it fails, greedy is likely wrong for that problem |

### When Greedy Choices Tie

```
TIES IN ACTIVITY SELECTION:
  Two activities with same end time — which to pick?
  ANSWER: Either. The exchange argument shows both lead to optimal.
  
  Proof: Both activities end at time t. At most one can be in any
         solution that picks activities ending at t (they share end time
         but might have different start times — check if they overlap).
  
  In practice: break ties arbitrarily for correctness;
               break ties by secondary criteria for desired output.
```

---

## 12. Greedy Algorithm Design Framework

```
STEP 1: IDENTIFY THE GREEDY CHOICE
  What is the "locally optimal" thing to do at each step?
  Common patterns:
    → Pick the smallest/largest (by some measure)
    → Pick the earliest/latest (deadline, end time, start time)
    → Pick the highest ratio (value/weight, benefit/cost)
    → Pick the cheapest (minimum weight edge, minimum distance)

STEP 2: PROVE THE GREEDY CHOICE PROPERTY
  "There exists an optimal solution that makes this greedy choice first."
  Use exchange argument or greedy stays ahead.
  If you CANNOT prove this → greedy may be wrong → use DP.

STEP 3: PROVE OPTIMAL SUBSTRUCTURE
  "After making the greedy choice, the remaining problem has
   the same structure as the original."
  The greedy choice reduces to a smaller instance of the same problem.

STEP 4: IMPLEMENT
  Usually simple: sort + single pass, or sort + priority queue.

STEP 5: VERIFY WITH COUNTEREXAMPLES
  Test on small cases where greedy might fail.
  If any case breaks it → find the correct greedy choice or use DP.
```

---

## 13. Real-World Applications

| Domain | Problem | Greedy's Role |
|---|---|---|
| **Data compression** | Huffman coding | Optimal prefix-free codes (ZIP, JPEG, MP3) |
| **Networking** | Dijkstra's routing (OSPF protocol) | Shortest path in router tables |
| **Infrastructure** | Power grid, network wiring | MST minimizes cable cost |
| **Operating systems** | CPU scheduling (shortest job first) | Minimize average wait time |
| **Wireless networks** | Bandwidth allocation | Fractional knapsack variant |
| **Finance** | Portfolio optimization (simplified) | Greedy asset selection by return/risk ratio |
| **Biology** | Sequence assembly | Greedy overlap graphs for genome assembly |
| **Caching** | Optimal page replacement (Bélády's) | Evict page needed furthest in future |
| **Encoding** | Arithmetic coding, LZ compression | Greedy symbol matching |
| **Clustering** | Single-linkage hierarchical clustering | Greedy merge by minimum distance |

### Bélády's Algorithm — The Provably Optimal Cache Replacement

```
PROBLEM: Cache has k slots. Pages requested in sequence.
         On cache miss, which page to evict?

GREEDY CHOICE: Always evict the page that will be needed
               FURTHEST IN THE FUTURE (or never again).

PROOF (exchange argument):
  Any algorithm that evicts a page needed sooner
  will incur at least as many misses as Bélády's.
  Evicting the furthest-future page delays the next miss
  as long as theoretically possible.

Cache requests: A B C D A B E A B C D E
Cache size: 3

Bélády's trace:
  A: miss → cache[A]
  B: miss → cache[A,B]
  C: miss → cache[A,B,C]
  D: miss, evict A (next needed at step 5, C next at step 10, B at step 6)
           Actually: evict C (needed furthest) → cache[A,B,D]
  ...

CATCH: Requires FUTURE KNOWLEDGE. Optimal but not implementable online.
       Used as theoretical benchmark to evaluate other cache policies (LRU, LFU).
       The greedy choice is perfect but omniscient.
```

### Interval Scheduling in Operating Systems

```
CPU has tasks with deadlines (all duration 1 unit):
  Task A: deadline 4, profit 70
  Task B: deadline 1, profit 20
  Task C: deadline 1, profit 50
  Task D: deadline 3, profit 60
  Task E: deadline 2, profit 100

GREEDY: Sort by profit descending. Schedule each task in the
        latest available time slot before its deadline.

Sort: E(100), A(70), D(60), C(50), B(20)

Slots: [_, _, _, _]  (indices 1-4)

E: deadline=2, latest open slot ≤ 2 is slot 2 → place E at slot 2
   [_, E, _, _]

A: deadline=4, latest open slot ≤ 4 is slot 4 → place A at slot 4
   [_, E, _, A]

D: deadline=3, latest open slot ≤ 3 is slot 3 → place D at slot 3
   [_, E, D, A]

C: deadline=1, latest open slot ≤ 1 is slot 1 → place C at slot 1
   [C, E, D, A]

B: deadline=1, no open slot ≤ 1 → CANNOT SCHEDULE

Schedule: C, E, D, A  Profit: 50+100+60+70 = 280 ✅
```

---

## 14. Comparison With Related Techniques

```
              ┌───────────────────────────────────────────────────────────┐
              │                ALGORITHM DESIGN PARADIGMS                  │
              └──────────────────────────┬────────────────────────────────┘
                                         │
        ┌─────────────────┬──────────────┼───────────────┬────────────────┐
        ▼                 ▼             ▼               ▼                ▼
     GREEDY            DYNAMIC       DIVIDE &       BACKTRACKING      BRUTE FORCE
                       PROGRAMMING    CONQUER
     ──────            ───────────   ─────────      ────────────      ───────────
     One choice        All choices   Independent    All choices        All choices
     per step          per step,     subproblems,   + undo on          no pruning
     irrevocable       store best    recombine      failure
     
     O(n log n)        O(n²) to      O(n log n)     Exponential        Exponential
     typically         O(n^k)        typically      (with pruning)
     
     Correct only      Always        Always          Always             Always
     with proof        correct if    correct         correct            correct
                       OPT substr.   (typically)     (exhaustive)
     
     Local → Global    Global via    Correctness     Explores all       No
     (requires proof)  subproblems   by induction    possibilities      shortcutting
```

**Greedy vs Dynamic Programming — the deepest comparison:**

```
BOTH require OPTIMAL SUBSTRUCTURE.

DIFFERENCE IN HOW THEY USE IT:

Greedy:
  Makes ONE choice at each step (the greedy choice).
  Reduces to ONE subproblem.
  Never needs to compare alternative choices.
  Fast: O(n log n) or O(n) typically.
  Correct: only when greedy choice property holds.

DP:
  Considers ALL choices at each step.
  Reduces to MULTIPLE subproblems (one per choice).
  Stores results of all subproblems, takes the best.
  Slower: O(n²) or higher typically.
  Correct: whenever optimal substructure holds.

RELATIONSHIP:
  Greedy is a special case of DP where only one subproblem matters.
  Every correct greedy algorithm can be expressed as a DP,
  but with only one branch explored per step.
  
  DP: dp[i] = max(dp[i-1], dp[i-2]+val[i])    ← considers both choices
  Greedy: just take the best-looking option now  ← considers one choice

DECISION RULE:
  Try greedy first (simpler, faster).
  If you can't prove the greedy choice property → use DP.

COIN CHANGE:
  Standard denominations (1,5,10,25): greedy ✅ (provable)
  Arbitrary denominations: DP required ✅
```

**Greedy vs Divide and Conquer:**

```
DIVIDE AND CONQUER:
  Split problem into INDEPENDENT subproblems.
  Solve each separately.
  Combine solutions.
  (Merge sort, FFT, binary search)

GREEDY:
  Single sequential scan.
  Each step makes one irrevocable choice.
  No combining phase — result built incrementally.
  (Huffman, activity selection, Dijkstra)

They rarely compete — applied to different problem structures.
```

---

## 15. The Greedy vs DP Decision Flowchart

```
Can you identify a locally optimal choice that is ALWAYS
part of a globally optimal solution?
    │
    ├── YES (can prove greedy choice property)
    │     └── Does making this choice reduce to a SMALLER
    │         instance of the SAME problem?
    │               └── YES → GREEDY ALGORITHM ✅
    │                         (fast, simple, elegant)
    │
    └── NO (cannot prove greedy choice property, or
            multiple local choices must be explored)
          └── Do subproblems OVERLAP?
                └── YES → DYNAMIC PROGRAMMING ✅
                └── NO  → DIVIDE AND CONQUER ✅

QUICK TEST for greedy:
  "If I make the locally best choice RIGHT NOW, can I PROVE
   it's safe — that I'm not closing off better futures?"
  YES → greedy
  UNCERTAIN → try to construct a counterexample
              If you find one → DP
              If you can't → attempt exchange argument proof
```

---

## 16. Tips for Long-Term Retention

**1. The "no regrets" mental model**
Greedy is the "no regrets" algorithm. You make the best decision you can see right now, you commit to it, and you never look back. Problems where this works have the property that hindsight would never improve your choice. Problems where this fails are ones where "I wish I hadn't taken that option earlier" can happen.

**2. Two questions before coding**
Before writing any greedy algorithm, answer both: (1) "What is the greedy choice?" and (2) "Can I prove this choice is always safe?" If you can't answer both convincingly, you either haven't found the right greedy choice, or the problem isn't greedy-solvable.

**3. Sort → Scan is the greedy heartbeat**
The vast majority of greedy algorithms follow this pattern: sort by some criterion, then scan linearly making greedy choices. Activity selection: sort by end time, scan. Kruskal's: sort by edge weight, scan. Huffman: sort by frequency (use min-heap for dynamic updates), merge. When you identify a greedy problem, immediately ask "what do I sort by?"

**4. The failure cases are as important as the successes**
Memorize the coin change failure (non-standard denominations) and the 0/1 knapsack failure. These two cases are the canonical demonstrations of greedy's limits. When you see a new optimization problem, ask "does it look like these failures?" If yes — reach for DP.

**5. Exchange argument in one sentence**
"Suppose an optimal solution differs from greedy — swap greedy's choice in, show it doesn't hurt — therefore greedy is optimal." This one-sentence template is the structure of almost every greedy correctness proof. Practice applying it to new problems before looking up the answer.

**6. Greedy = DP with one branch**
Conceptually, every greedy algorithm is a DP where only one choice is ever worth considering at each step. If you're unsure whether greedy or DP is correct, code the DP first. If you notice that one of the choices always dominates the others, you've just discovered the greedy choice and can simplify to a greedy algorithm.

**7. The ratio heuristic**
Many greedy algorithms reduce to "sort by ratio: value/weight, profit/time, benefit/cost." When you see a problem where items have two attributes and you're trying to maximize or minimize something, try computing the ratio and sorting by it. This is the greedy fingerprint for resource-allocation problems.

---

Greedy algorithms are fundamentally about **trust** — trust that local wisdom compounds into global wisdom, that the best immediate choice never needs to be reconsidered. That trust is sometimes warranted, sometimes catastrophically wrong, and the entire discipline of greedy algorithm design is learning to tell the difference. When the greedy choice property holds, you are rewarded with algorithms of breathtaking simplicity and speed — a single sorted pass that somehow achieves optimality. When it doesn't hold, greedy becomes a cautionary tale about how locally rational decisions can lead to globally suboptimal outcomes. The key is not blind application but disciplined proof: commit to the local choice only when you can demonstrate, rigorously, that no future regret is possible.
