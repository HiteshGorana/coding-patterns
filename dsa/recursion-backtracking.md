# Recursion & Backtracking (Interview-Ready Guide)

Using `[TOPIC] = Recursion & Backtracking`.

## 0) Scope (Checklist)
- [x] Base case design
- [x] Recursion tree / call stack model
- [x] Divide and conquer
- [x] Subsets / permutations / combinations
- [x] N-Queens, Sudoku-like constraints
- [x] Partitioning (palindrome partition)
- [x] Pruning strategies
- [x] Choose/explore/unchoose template

## 1) Foundations
Recursion solves a problem by reducing it to smaller self-similar problems.
Backtracking is recursion + undo, exploring a search tree.

Core terms:
- Base case, recursive case
- Call stack, state, branching factor
- Pruning, feasibility check

Mental model:
- Each recursion call is a node in a decision tree.
- Backtracking explores branches and rolls state back.

## 2) How it works
Cause-effect:
1. Define state parameters precisely.
2. Stop at base case.
3. Generate choices.
4. Recurse on choice.
5. Undo (unchoose) and try next choice.

Tiny trace (subsets of `[1,2]`):
- Start `[]`
- Choose `1` -> `[1]`
- Choose `2` -> `[1,2]` output
- Unchoose `2` -> `[1]` output
- Unchoose `1` -> `[]`
- Choose `2` -> `[2]` output
- Unchoose `2` -> `[]` output

## 3) Patterns (Interview Templates)
1. Divide-and-conquer recursion (`left`, `right`, combine)
2. Include/exclude recursion
3. For-loop choice recursion (combinations/permutations)
4. Constraint backtracking with pruning

Invariants:
- State must be restorable after each call.
- Base case must be reachable for all branches.
- Pruning condition must be logically sound (never cuts valid answer).

Signals:
- "Generate all"
- "Try possibilities under constraints"
- "Tree/graph recursive structure"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Fibonacci with memoization
- Approach: cache overlapping subproblems.

2. Medium: Subsets
- Approach: include/exclude template.
- Trace shown in section 2.

3. Medium: Permutations
- Approach: swap in-place or used[] tracking.

4. Hard: N-Queens
- Approach: row-by-row placement with column/diag sets.
- Prune invalid positions early.

5. Hard: Sudoku Solver
- Approach: choose cell, try valid digits, recurse, backtrack on failure.

## 5) Why & What-if
Edge cases:
- Empty input
- Repeated elements (need dedupe strategy)
- Deep recursion causing stack overflow

Pitfalls:
- Missing unchoose step
- Mutating shared lists without copying at output time
- Weak pruning causing exponential blow-up

Why it works:
- Exhaustive search with correctness from complete branch coverage.
- Pruning keeps only feasible branches.

Variations:
- Convert recursion to iterative stack for deep depth limits.
- Memoize recursive states when overlapping exists (turning into DP).

## 6) Complexity and Tradeoffs
- Depends on branching factor `b` and depth `d`: often `O(b^d)`.
- Space: recursion depth `O(d)` plus state storage.

Tradeoffs:
- Backtracking is general and clear, but can be exponential.
- DP is better when repeated states exist.

## 7) Real-world uses
- Constraint solving (scheduling, puzzles)
- Search in game trees
- Compiler parsing (recursive descent)
- Configuration generation

## 8) Comparisons
- Recursion vs iteration:
  - Recursion is expressive for hierarchical structures.
  - Iteration avoids call-stack limits.
- Backtracking vs DP:
  - Backtracking explores decisions.
  - DP reuses overlapping subproblems.

## 9) Retention
Cheat sheet:
- Template: choose -> recurse -> unchoose.
- Write base case first.
- Add pruning immediately after choice validation.

Recall hooks:
- "Decision tree + undo."
- "If states repeat, memoize."

Practice (10):
1. Easy: Fibonacci Number
2. Easy: Binary Tree Inorder Traversal (recursive)
3. Medium: Subsets
4. Medium: Combinations
5. Medium: Permutations
6. Medium: Palindrome Partitioning
7. Medium: Combination Sum
8. Hard: N-Queens
9. Hard: Sudoku Solver
10. Hard: Word Search II
