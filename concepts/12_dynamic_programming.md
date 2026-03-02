# Dynamic Programming: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

**Dynamic Programming (DP)** is an algorithmic technique that solves complex problems by breaking them into simpler overlapping subproblems, solving each subproblem exactly once, storing the result, and reusing that stored result whenever the same subproblem appears again — trading memory for time.

```
WITHOUT DP (naive recursion):          WITH DP (memoization):

fib(5)                                 fib(5)
├── fib(4)                             ├── fib(4)
│   ├── fib(3)                         │   ├── fib(3)
│   │   ├── fib(2)                     │   │   ├── fib(2) → computed, stored
│   │   │   ├── fib(1) ✓               │   │   └── fib(1) → computed, stored
│   │   │   └── fib(0) ✓               │   └── fib(2) → REUSED from cache ✅
│   │   └── fib(1) ✓                   └── fib(3) → REUSED from cache ✅
│   └── fib(2)         ← recomputed!
│       ├── fib(1) ✓   ← recomputed!
│       └── fib(0) ✓   ← recomputed!
└── fib(3)             ← recomputed!
    ├── fib(2)         ← recomputed!
    │   ├── fib(1) ✓
    │   └── fib(0) ✓
    └── fib(1) ✓

Calls made: 15                         Calls made: 5 (each subproblem once)
Time: O(2ⁿ)                           Time: O(n)
```

**Core components:**

- **Optimal substructure** — the optimal solution to the problem contains optimal solutions to its subproblems. This is the prerequisite: if subproblem solutions can be composed into the full solution, DP applies.
- **Overlapping subproblems** — the same subproblems are encountered and solved multiple times in naive recursion. This is what makes storing solutions worthwhile.
- **State** — a compact description of a subproblem. Everything the DP needs to know to answer "what is the solution to this subproblem?"
- **Transition (recurrence relation)** — the rule that expresses how the solution to a larger subproblem is built from smaller subproblem solutions.
- **Base cases** — the smallest subproblems whose answers are known directly, without further recursion.
- **Memoization table (cache)** — the storage structure (array, hashmap) where computed results are saved.

---

## 2. The Two Prerequisites — Why They Both Matter

### Optimal Substructure

```
DEFINITION: An optimal solution to the problem can be constructed
            from optimal solutions to its subproblems.

HOLDS FOR:
  Shortest path: shortest path A→C through B
    = shortest path A→B + shortest path B→C ✅

  Fibonacci: fib(n) = fib(n-1) + fib(n-2) ✅

  Knapsack: best value with capacity W using items 1..n
    = best of:
        (don't take item n): best with capacity W, items 1..n-1
        (take item n):       value[n] + best with W-weight[n], items 1..n-1 ✅

DOES NOT HOLD FOR:
  Longest simple path (no repeated vertices):
    Longest path A→C through B ≠ longest A→B + longest B→C
    (the two subpaths might share vertices, making their combination invalid)
    → DP FAILS here ❌

Optimal substructure is why DP solutions are CORRECT.
```

### Overlapping Subproblems

```
DEFINITION: The same subproblems are solved repeatedly
            in a naive recursive approach.

HOLDS:  fib(n) → fib(n-2) appears in multiple branches
        → storing fib(n-2) avoids recomputation ✅

DOESN'T HOLD: Merge sort
  mergesort([1,3,5,2]) splits into mergesort([1,3]) and mergesort([5,2])
  These subproblems NEVER overlap — each half is unique.
  → Memoization would waste memory with no speed benefit ❌
  → Use divide and conquer instead

Overlapping subproblems is why DP is EFFICIENT.
```

---

## 3. The Two Approaches: Top-Down vs Bottom-Up

Every DP problem can be solved in two ways. Understanding both is essential.

### Top-Down: Memoization

```
Start from the original problem.
Recurse downward toward base cases.
Cache results as you go.
On revisit: return cached result immediately.

def fib(n, memo={}):
    if n in memo: return memo[n]      ← check cache first
    if n <= 1:    return n            ← base case
    memo[n] = fib(n-1, memo) + fib(n-2, memo)   ← compute + store
    return memo[n]

FLOW:
  fib(5) not in cache → compute
    fib(4) not in cache → compute
      fib(3) not in cache → compute
        fib(2) not in cache → compute
          fib(1) = 1 (base)
          fib(0) = 0 (base)
        fib(2) = 1 → STORE
      fib(3) = fib(2)+fib(1) = 2 → STORE
    fib(4) = fib(3)+fib(2) = 3 → STORE  (fib(2) from cache ✅)
  fib(5) = fib(4)+fib(3) = 5 → STORE    (fib(3) from cache ✅)
```

### Bottom-Up: Tabulation

```
Start from the base cases.
Fill the DP table iteratively from smallest to largest subproblems.
No recursion — pure iteration.

def fib(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[0] = 0    ← base case
    dp[1] = 1    ← base case
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]    ← transition applied iteratively
    return dp[n]

TABLE:
  i:    0  1  2  3  4  5  6  7
  dp:   0  1  1  2  3  5  8  13

Each cell filled exactly once, left to right.
```

### Choosing Between Them

```
TOP-DOWN (Memoization):              BOTTOM-UP (Tabulation):
───────────────────────              ──────────────────────
Natural: mirrors the problem          Requires thinking about
  statement directly                    filling order carefully
Only computes needed subproblems      Always computes ALL subproblems
  (lazy evaluation)                     (eager evaluation)
Recursion overhead                    No recursion overhead
  (function call stack)                 (pure iteration)
Risk: stack overflow for              No stack overflow risk
  very deep recursion
Easier to write initially             Easier to optimize space
  (just add cache to recursion)         (often only need last row/2 values)

RULE OF THUMB:
  Start with top-down (easier to write).
  Optimize to bottom-up if performance or stack depth matters.
  Optimize further to space-efficient bottom-up when possible.
```

---

## 4. The DP Design Process — A Systematic Framework

Every DP solution follows the same design steps. Master this process, and any DP problem becomes approachable.

```
STEP 1: DEFINE THE STATE
  What information do I need to uniquely describe a subproblem?
  dp[i] means "answer to subproblem with parameter i"
  dp[i][j] means "answer to subproblem with parameters i and j"

STEP 2: WRITE THE TRANSITION
  How does dp[i] depend on smaller subproblems?
  Express dp[i] in terms of dp[j] where j < i (or simpler states).

STEP 3: IDENTIFY BASE CASES
  What are the smallest subproblems with known answers?
  These seed the entire table.

STEP 4: DETERMINE FILL ORDER
  Bottom-up: which subproblems must be filled before others?
  (Usually small → large, but 2D problems may need row-by-row or diagonal)

STEP 5: EXTRACT ANSWER
  Which cell(s) in the table contain the final answer?

STEP 6: OPTIMIZE SPACE (optional)
  Do you actually need the full table, or just the last row/column/few values?
```

---

## 5. Classic Problem 1: 0/1 Knapsack

**Problem:** Given items with weights and values, and a knapsack with capacity W, maximize total value without exceeding capacity. Each item can be used at most once.

```
Items:    weight=[2,3,4,5]   value=[3,4,5,6]   capacity W=5

STEP 1: STATE
  dp[i][w] = maximum value using first i items with capacity w

STEP 2: TRANSITION
  For each item i, two choices:
    DON'T take item i: dp[i][w] = dp[i-1][w]
    TAKE item i (if weight[i] ≤ w): dp[i][w] = value[i] + dp[i-1][w - weight[i]]

  dp[i][w] = max(dp[i-1][w],  value[i] + dp[i-1][w - weight[i]])
                  ↑                        ↑
             skip item i             take item i

STEP 3: BASE CASES
  dp[0][w] = 0 for all w  (no items → value = 0)
  dp[i][0] = 0 for all i  (no capacity → value = 0)

STEP 4: FILL TABLE (item by item, capacity by capacity)

Items: (w=2,v=3),(w=3,v=4),(w=4,v=5),(w=5,v=6)

     cap→  0  1  2  3  4  5
item 0:    0  0  0  0  0  0    ← base case: no items
item 1:    0  0  3  3  3  3    ← item(2,3): take if cap≥2
item 2:    0  0  3  4  4  7    ← item(3,4): take if cap≥3
item 3:    0  0  3  4  5  7    ← item(4,5): take if cap≥4
item 4:    0  0  3  4  5  7    ← item(5,6): 6+dp[3][0]=6 < 7, no change

STEP 5: ANSWER = dp[4][5] = 7 ✅
  (Take items 1 and 2: weight=2+3=5, value=3+4=7)
```

**Tracing the optimal items (backtracking the DP table):**

```
dp[4][5]=7: same as dp[3][5]? YES → item 4 NOT taken
dp[3][5]=7: same as dp[2][5]? YES → item 3 NOT taken
dp[2][5]=7: same as dp[1][5]? NO (dp[1][5]=3) → item 2 TAKEN
  → remaining capacity = 5-3=2, move to dp[1][2]
dp[1][2]=3: same as dp[0][2]? NO (dp[0][2]=0) → item 1 TAKEN

Items taken: 1 and 2. Value: 3+4=7. Weight: 2+3=5. ✅
```

---

## 6. Classic Problem 2: Longest Common Subsequence (LCS)

**Problem:** Find the length of the longest subsequence common to two strings. A subsequence maintains relative order but doesn't need to be contiguous.

```
s1 = "ABCBDAB"    s2 = "BDCAB"    LCS = "BCAB" or "BDAB" = length 4

STEP 1: STATE
  dp[i][j] = length of LCS of s1[0..i-1] and s2[0..j-1]

STEP 2: TRANSITION
  IF s1[i-1] == s2[j-1]:           ← characters match
      dp[i][j] = dp[i-1][j-1] + 1  ← extend LCS by 1
  ELSE:                             ← characters don't match
      dp[i][j] = max(dp[i-1][j],   ← skip s1[i-1]
                     dp[i][j-1])    ← skip s2[j-1]

STEP 3: BASE CASES
  dp[0][j] = 0 for all j  (empty s1 → LCS = 0)
  dp[i][0] = 0 for all i  (empty s2 → LCS = 0)

STEP 4: FILL TABLE

      ""  B  D  C  A  B
  ""   0  0  0  0  0  0
  A    0  0  0  0  1  1
  B    0  1  1  1  1  2
  C    0  1  1  2  2  2
  B    0  1  1  2  2  3
  D    0  1  2  2  2  3
  A    0  1  2  2  3  3
  B    0  1  2  2  3  4   ← dp[7][5] = 4 ✅

KEY TRANSITIONS HIGHLIGHTED:
  dp[2][1]: s1[1]='B' == s2[0]='B' → dp[1][0]+1 = 0+1 = 1 ✅
  dp[7][5]: s1[6]='B' == s2[4]='B' → dp[6][4]+1 = 3+1 = 4 ✅
```

---

## 7. Classic Problem 3: Coin Change

**Problem:** Given coin denominations and a target amount, find the minimum number of coins to make the amount.

```
coins = [1, 5, 6, 9]    amount = 11

STEP 1: STATE
  dp[i] = minimum coins needed to make amount i

STEP 2: TRANSITION
  dp[i] = min(dp[i - coin] + 1)  for each coin where coin ≤ i
          ↑
  "use this coin, + 1 coin for the remaining amount"

STEP 3: BASE CASES
  dp[0] = 0        (0 coins needed for amount 0)
  dp[i] = ∞ initially (amount i not yet reachable)

STEP 4: FILL TABLE

  i:     0   1   2   3   4   5   6   7   8   9   10  11
  dp:    0   1   2   3   4   1   1   2   2   1   2   2

  Trace dp[11]:
    coin=1: dp[10]+1 = 2+1 = 3
    coin=5: dp[6]+1  = 1+1 = 2   ← minimum
    coin=6: dp[5]+1  = 1+1 = 2   ← tied
    coin=9: dp[2]+1  = 2+1 = 3

  dp[11] = 2   (coins: 5+6=11 or 6+5=11) ✅

STEP 5: ANSWER = dp[11] = 2
```

**The intuition:** For each amount, try every coin and ask "if I use this coin, how many coins do I need for the rest?" Take the minimum. The DP table stores the answer to each "how many for the rest?" query.

---

## 8. Classic Problem 4: Longest Increasing Subsequence (LIS)

**Problem:** Find the length of the longest strictly increasing subsequence.

```
arr = [10, 9, 2, 5, 3, 7, 101, 18]    LIS = [2,3,7,18] or [2,5,7,18] = length 4

STEP 1: STATE
  dp[i] = length of LIS ending at index i (element arr[i] is the LAST element)

STEP 2: TRANSITION
  dp[i] = 1 + max(dp[j])  for all j < i where arr[j] < arr[i]
          ↑                ↑
     at minimum,        extend the longest valid LIS
     LIS of length 1    ending before i

STEP 3: BASE CASES
  dp[i] = 1 for all i  (every single element is an LIS of length 1)

STEP 4: FILL + TRACE

  i:    0    1    2    3    4    5    6    7
  arr: 10    9    2    5    3    7   101   18
  dp:   1    1    1    2    2    3    4    4

  dp[3]=2: arr[2]=2 < arr[3]=5 → dp[2]+1=2 ✅
  dp[5]=3: arr[4]=3 < arr[5]=7 → dp[4]+1=3 ✅
           arr[3]=5 < arr[5]=7 → dp[3]+1=3 (tied)
           arr[2]=2 < arr[5]=7 → dp[2]+1=2 (worse)
  dp[6]=4: arr[5]=7 < arr[6]=101 → dp[5]+1=4 ✅

STEP 5: ANSWER = max(dp) = 4 ✅
```

---

## 9. Classic Problem 5: Edit Distance

**Problem:** Find the minimum operations (insert, delete, replace) to transform string s1 into s2.

```
s1 = "horse"    s2 = "ros"    Answer: 3

STEP 1: STATE
  dp[i][j] = minimum operations to transform s1[0..i-1] into s2[0..j-1]

STEP 2: TRANSITION
  IF s1[i-1] == s2[j-1]:
      dp[i][j] = dp[i-1][j-1]         ← no operation needed (chars match)
  ELSE:
      dp[i][j] = 1 + min(
          dp[i-1][j],                  ← DELETE s1[i-1]
          dp[i][j-1],                  ← INSERT s2[j-1]
          dp[i-1][j-1]                 ← REPLACE s1[i-1] with s2[j-1]
      )

STEP 3: BASE CASES
  dp[i][0] = i  (delete all i chars of s1 to get empty string)
  dp[0][j] = j  (insert all j chars of s2 from empty string)

STEP 4: FILL TABLE

      ""  r  o  s
  ""   0  1  2  3
  h    1  1  2  3
  o    2  2  1  2
  r    3  2  2  2
  s    4  3  3  2
  e    5  4  4  3   ← dp[5][3] = 3 ✅

OPERATIONS:
  horse → rorse (replace h→r)
  rorse → rose  (delete r)
  rose  → ros   (delete e)
  3 operations ✅
```

---

## 10. The DP Patterns Taxonomy

Most DP problems belong to recognizable pattern families:

```
┌─────────────────────────────────────────────────────────────┐
│                    DP PATTERN FAMILIES                       │
└──────────────────────────────┬──────────────────────────────┘
                               │
    ┌──────────────────────────┼───────────────────────────┐
    │              │           │           │               │
    ▼              ▼           ▼           ▼               ▼
LINEAR DP      2D/GRID DP  INTERVAL DP  TREE DP      SUBSET/BITMASK DP
─────────       ────────    ───────────  ───────      ─────────────────
1D state        2D state    dp[i][j]     State on     State = subset
dp[i] from      Grid paths  = answer     tree nodes   of elements
dp[i-1],        LCS         for range    Computed     Traveling
dp[i-2]...      Edit dist   [i..j]       bottom-up    salesman,
                Knapsack     Matrix       from leaves  assignments
Fibonacci       Unique paths chain mult  to root
Coin change
Climbing stairs
LIS, House rob
```

### Pattern Recognition Guide

```
PROBLEM SIGNATURE              → LIKELY PATTERN

"Minimum/maximum of sequence"  → Linear DP (1D state)
"Subsequence / substring"      → 2D DP on two sequences (LCS, edit distance)
"Grid path counting/optimize"  → 2D DP on grid coordinates
"Partition array optimally"    → Interval DP or linear DP with choices
"Subset with property"         → Knapsack variant or bitmask DP
"Decision at each step"        → Linear DP with choice at each position
"Tree structure"               → Tree DP (DFS + DP combined)
"At most k operations"         → Add k as a DP dimension
"Two sequences, align them"    → 2D DP (LCS, edit distance family)
```

---

## 11. Space Optimization — The Next Level

Once you have a correct DP solution, you can often reduce space dramatically.

### Rolling Array Optimization

```
OBSERVATION: Many DP transitions only look at the previous row/element.
             You don't need to keep the entire table.

FIBONACCI:
  Naive:    dp = [0, 1, 1, 2, 3, 5, 8, ...]   O(n) space
  Optimized: only need last two values

  prev2, prev1 = 0, 1
  for i in range(2, n+1):
      curr = prev1 + prev2
      prev2, prev1 = prev1, curr
  return prev1                               O(1) space ✅

COIN CHANGE:
  dp[i] only depends on dp[i-coin] for each coin.
  For smallest coin = 1: only depends on dp[i-1].
  1D array, updated in-place. O(amount) space, not O(coins × amount).

LCS / EDIT DISTANCE:
  dp[i][j] only depends on dp[i-1][j], dp[i][j-1], dp[i-1][j-1].
  Only need the CURRENT ROW and PREVIOUS ROW.
  Space: O(min(m,n)) instead of O(m×n).

  prev_row = [0, 1, 2, ..., n]   ← base case row
  for i in range(1, m+1):
      curr_row = [i] + [0]*n     ← base case for this row
      for j in range(1, n+1):
          if s1[i-1] == s2[j-1]:
              curr_row[j] = prev_row[j-1]
          else:
              curr_row[j] = 1 + min(prev_row[j], curr_row[j-1], prev_row[j-1])
      prev_row = curr_row        ← slide the window
```

### Knapsack 1D Optimization

```
ORIGINAL: dp[i][w] — O(n×W) space
OPTIMIZED: dp[w] — O(W) space

KEY INSIGHT: dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]])
  Iterate w from HIGH to LOW to ensure we use dp[i-1] values
  (high-to-low prevents using the same item twice in this pass)

dp = [0] * (W + 1)
for item in items:
    for w in range(W, item.weight - 1, -1):   ← HIGH TO LOW
        dp[w] = max(dp[w], item.value + dp[w - item.weight])

Space: O(W) instead of O(n×W) ✅

If iterating LOW TO HIGH: allows reusing items → becomes unbounded knapsack
(changing just the iteration direction changes the problem variant!)
```

---

## 12. The "Why" Questions

### Why does memoization turn exponential into polynomial?

```
WITHOUT MEMO: Each subproblem recomputed every time it's needed.
  fib(n) has O(2ⁿ) recursive calls — exponential tree.

WITH MEMO: Each unique subproblem computed ONCE, then served from cache.
  fib(n) has O(n) unique subproblems: fib(0), fib(1), ..., fib(n).
  Each computed once: O(n) total work.

The number of UNIQUE subproblems is the key metric.
  If there are P unique subproblems, each taking T time:
  Total time = O(P × T)

  Fibonacci: P = n, T = O(1) → O(n)
  Knapsack:  P = n×W, T = O(1) → O(n×W)
  Edit dist: P = m×n, T = O(1) → O(m×n)
```

### Why bottom-up and top-down give identical results?

```
They compute the SAME recurrence relation in different orders.
Both respect the dependency structure (smaller subproblems first).

Top-down:   computes what the recursion needs, in the order it needs it.
Bottom-up:  computes all subproblems in a predetermined order.

Any valid topological ordering of the dependency DAG works for bottom-up.
Top-down implicitly finds one such ordering via the call stack.

They are dual views of the same computation.
```

### Why can't DP solve all optimization problems?

```
DP requires OPTIMAL SUBSTRUCTURE.
Some problems don't have it:

LONGEST SIMPLE PATH: (no repeated vertices)
  Suppose longest path A→D is A→B→C→D.
  Is A→B the longest simple path from A to B? NOT NECESSARILY.
  A→C→B might be longer — but then A→C→B→C→D repeats C.
  The subproblems INTERFERE with each other.
  No way to combine subsolutions without checking feasibility.
  → DP fails. Problem is NP-hard.

GAME THEORY (adversarial): some game states require knowing
  the OPPONENT's optimal strategy simultaneously.
  Standard DP can handle minimax, but not all game structures.

KEY TEST: "Can I make a locally optimal choice at each subproblem
           and be guaranteed a globally optimal result?"
  YES → DP likely works
  NO  → might need different approach (branch and bound, ILP, heuristics)
```

---

## 13. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Subproblems don't overlap | Memoization wastes memory; use divide and conquer instead |
| No optimal substructure | DP gives wrong answer; problem may be NP-hard |
| Very large state space | Memory limit exceeded; consider if some dimensions can be compressed |
| Negative values in array | Many DP formulations still work; initialize to -∞ instead of 0 where needed |
| Empty string / array input | Base cases handle it; dp[0] or dp[0][0] is the empty-input answer |
| Need to reconstruct path (not just count) | Store "choice made" table alongside dp table; backtrack to reconstruct |
| Infinite values possible | Use appropriate sentinel (float('inf') for min, float('-inf') for max) |
| Multiple dimensions needed | Add dimension to state; space grows multiplicatively |
| Target is unreachable | dp[target] stays at ∞ (min problems) or 0 (count problems) |
| Circular dependencies in subproblems | DP is inapplicable; cycle in dependency = not a DAG |

### Path Reconstruction Pattern

```
PROBLEM: Not just "what's the minimum cost" but "WHICH choices achieve it?"

SOLUTION: Maintain a parallel "choice" array alongside the dp array.

For Coin Change:
  dp[i] = minimum coins for amount i
  choice[i] = which coin was used to achieve dp[i]

  For each i: when dp[i] updates via coin c:
    choice[i] = c

  Reconstruct:
    amount = 11, choice[11] = 6 → used coin 6
    amount = 5,  choice[5]  = 5 → used coin 5
    amount = 0 → done

  Coins used: [6, 5] ✅

For LCS:
  At each dp[i][j], store whether we:
    - matched (characters equal, came from diagonal)
    - skipped s1 (came from left)
    - skipped s2 (came from above)
  Backtrack the stored choices from dp[m][n] to dp[0][0].
```

---

## 14. Real-World Applications

| Domain | Problem | DP's Role |
|---|---|---|
| **Bioinformatics** | DNA sequence alignment | Edit distance / LCS between gene sequences |
| **Compilers** | Optimal code generation | DP over expression trees for register allocation |
| **Finance** | Option pricing (Binomial model) | DP over price trees computes option value |
| **NLP** | Viterbi algorithm (HMMs) | DP finds most likely sequence of hidden states |
| **Robotics** | Motion planning | DP over state space finds optimal trajectory |
| **Games** | Chess endgame tablebases | DP precomputes optimal play for all positions |
| **Networking** | Routing optimization | DP over network topology (Bellman-Ford IS DP) |
| **Logistics** | Vehicle routing, scheduling | DP over subsets of deliveries/tasks |
| **Image processing** | Seam carving (content-aware resize) | DP finds minimum-energy seam to remove |
| **Text editors** | Diff / patch tools (git diff) | Edit distance finds minimum changes |

### Seam Carving — DP Running in Your Image Editor

```
PROBLEM: Resize an image by removing pixels while preserving content.
  Naive crop: cuts important content.
  Seam carving: removes a vertical "seam" (one pixel per row) of
                minimum visual importance.

DP FORMULATION:
  energy[r][c] = visual importance of pixel (r,c)
    (gradient magnitude — high at edges, low in flat areas)

  dp[r][c] = minimum total energy of any seam ending at (r,c)

  TRANSITION:
    dp[r][c] = energy[r][c] + min(dp[r-1][c-1],
                                   dp[r-1][c],
                                   dp[r-1][c+1])
    "best seam to here = my energy + best of the three pixels above me"

  ANSWER: seam ends at min(dp[last_row])
  RECONSTRUCT: backtrack from minimum in last row to find exact seam.
  REMOVE: delete that pixel from each row, shift left.
  REPEAT: for desired new width.

This runs in O(rows × cols) per seam removal.
Used in Adobe Photoshop's "Content-Aware Scale."
```

### Viterbi Algorithm — DP in Speech Recognition

```
PROBLEM: Given a sequence of observed sounds, find the most likely
         sequence of words/phonemes (hidden states).

Hidden Markov Model:
  States: hidden (word/phoneme sequences)
  Observations: audio features at each timestep
  Transitions: probability of state-to-state changes
  Emissions: probability of observation given state

DP FORMULATION:
  dp[t][s] = maximum probability of any state sequence ending
             in state s at time t

  TRANSITION:
    dp[t][s] = emission(s, obs[t]) × max_over_prev_states(
                 dp[t-1][prev] × transition(prev, s)
               )

  ANSWER: backtrack from max(dp[last_t]) to reconstruct state sequence.

This is bottom-up DP over a sequence.
Every voice assistant (Siri, Alexa) uses this or its descendants.
```

---

## 15. Comparison With Related Techniques

```
              ┌──────────────────────────────────────────────────────────┐
              │              ALGORITHM DESIGN PARADIGMS                   │
              └──────────────────────────┬───────────────────────────────┘
                                         │
       ┌──────────────────┬──────────────┼─────────────────┬─────────────┐
       ▼                  ▼             ▼                  ▼             ▼
  DYNAMIC              GREEDY       DIVIDE &          BACKTRACKING   BRUTE FORCE
  PROGRAMMING                       CONQUER
  ───────────          ──────       ─────────         ────────────   ───────────
  Subproblems          Locally       Independent       Build + undo   Try all
  overlap →            optimal       subproblems       choices        possibilities
  store results        choice →      (no overlap)
                       global opt
  Optimal              Optimal       Optimal           May find all   Correct
  (if OPT substr.)     (if correct)  (proof by         solutions      but slow
                                     induction)
  Poly-time            Poly-time     Poly-time          Exponential   Exponential
  (if poly states)     O(n) or       (merge sort,       (with         
                       O(n log n)    FFT, etc.)         pruning)
  Knapsack             Activity      Merge sort         N-Queens       Password
  LCS, edit dist       selection     Binary search      Sudoku         brute-force
  Shortest path        Dijkstra*     FFT                Permutations
  Coin change          Huffman
```

**DP vs Greedy — the most important comparison:**

```
GREEDY: Make the locally optimal choice at each step.
  Never reconsider past choices.
  Works when local optimum → global optimum (greedy stays provable).

DP: Consider ALL choices at each step, store the best.
  Recombines subproblem solutions.
  Works when optimal substructure holds (broader condition).

GREEDY ⊆ DP in power:
  Every problem solvable by greedy is also solvable by DP (with more work).
  Some problems require DP that greedy gets wrong.

COIN CHANGE example:
  Greedy: always take the largest coin that fits.
  coins = [1, 3, 4], amount = 6
  Greedy: 4+1+1 = 3 coins
  DP:     3+3   = 2 coins ✅  (greedy WRONG here)

  But for standard US coins [1,5,10,25]: greedy works correctly.
  The difference: US coins have special structure greedy exploits.
```

**DP vs Divide and Conquer:**

```
DIVIDE AND CONQUER:           DYNAMIC PROGRAMMING:
  Split into subproblems        Split into subproblems
  INDEPENDENT (no overlap)      OVERLAPPING (same subproblem appears multiple times)
  Combine results               Store and reuse results

  Merge sort:                   Fibonacci:
    mergesort([1,3,5,2])          fib(5) calls fib(3) AND fib(4)
    splits into                   fib(4) also calls fib(3)
    mergesort([1,3]) +            fib(3) is SHARED → memoize it
    mergesort([5,2])
    These NEVER share data.       Without memo: exponential
    No memoization benefit.       With memo: linear

KEY QUESTION: "Do subproblems share sub-subproblems?"
  YES → DP
  NO  → Divide and Conquer
```

---

## 16. Tips for Long-Term Retention

**1. The three-word essence: "remember to reuse"**
DP is fundamentally about not repeating work. Compute once, store, reuse. Every DP solution is the answer to: "what work am I doing more than once, and can I cache it?" Start there, and the rest follows.

**2. Start with the recurrence, not the code**
Before writing any code, write the mathematical recurrence. What is dp[i]? What is dp[i][j]? How does it relate to dp[i-1] or dp[i-1][j]? If you can write this clearly, the code is almost mechanical. Most DP bugs come from coding before the recurrence is clear.

**3. The Fibonacci gateway drug**
Fibonacci is the "hello world" of DP. It perfectly illustrates both problems (exponential without DP, linear with) and both solutions (top-down with memo, bottom-up with table). When explaining DP to anyone — including yourself — start here. Every other DP problem is a variation on this core idea.

**4. State definition is everything**
The hardest part of DP is not the code — it's defining what dp[i] (or dp[i][j]) MEANS. Write it in plain English: "dp[i] is the minimum cost to reach position i." Once this definition is airtight, the transition almost writes itself. Sloppy state definitions = bugs that are nearly impossible to trace.

**5. Pattern recognition over problem memorization**
Don't memorize solutions to 100 DP problems. Learn the 6-8 patterns: linear DP, 2D sequence DP (LCS family), grid DP, interval DP, knapsack variants, tree DP, bitmask DP. When you see a new problem, ask "which pattern does this fit?" The answer gives you the state and transition structure immediately.

**6. Top-down first, optimize later**
When solving a new DP problem: first write the brute-force recursive solution. Then add memoization (top-down DP). Then if needed, convert to bottom-up. Then if needed, optimize space. This progression is reliable and avoids the disorientation of jumping straight to an optimized solution.

**7. "What decision am I making at each step?"**
For every DP problem, there is a sequence of decisions. At each decision point, you have some choices. The DP state captures "where am I in the sequence" and "what constraints carry forward." The transition captures "for each choice, what's the cost and what's the next state?" Framing it this way converts DP from abstract technique to concrete decision modeling.

---

Dynamic Programming is fundamentally about recognizing that **the same question keeps getting asked**, and answering it once instead of endlessly. The exponential blowup of recursive enumeration collapses into polynomial time the moment you realize that the branching tree of subproblems is actually a much smaller DAG — and that traversing a DAG only requires visiting each node once. That insight — exponential appearance, polynomial reality — is DP's core gift. It transforms problems that seem computationally intractable into problems that fit in a table, and it does so not through approximation or heuristics, but through exact, provably optimal reasoning stored one cell at a time.
