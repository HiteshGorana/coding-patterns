# Greedy (Interview-Ready Guide)

Using `[TOPIC] = Greedy`.

## 0) Scope (Checklist)
- [x] Greedy choice property intuition
- [x] Interval scheduling / merge intervals
- [x] Huffman-like merge cost patterns
- [x] Jump game patterns
- [x] Gas station / candy / ratings style
- [x] Greedy + heap combos

## 1) Foundations
Greedy builds solution by taking the best local choice at each step.

Core terms:
- Greedy-choice property
- Exchange argument
- Feasibility + local optimal move

Mental model:
- If local best can be proven safe globally, greedy is optimal.

## 2) How it works
Cause-effect:
1. Sort or prioritize candidates.
2. Repeatedly pick best current option.
3. Maintain feasibility constraints.

Tiny trace (interval scheduling max non-overlap):
- Intervals sorted by end: `(1,2),(2,3),(1,3),(3,4)`
- Pick `(1,2)`, then `(2,3)`, skip `(1,3)`, pick `(3,4)`
- Count = 3

## 3) Patterns (Interview Templates)
1. Sort by finishing time/start/cost ratio
2. Reachability range update (jump game)
3. Local balance reset (gas station)
4. Min-heap merge smallest first (Huffman-like)

Invariants:
- Current solution remains feasible.
- Chosen local step does not reduce best possible future outcome.

Signals:
- "Minimum number of ...", "maximum non-overlap"
- "Can reach end?" with local reach updates
- "Combine smallest repeatedly"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Jump Game
- Approach: keep farthest reachable index.

2. Medium: Non-overlapping Intervals
- Approach: sort by end; greedily keep interval with earliest end.

3. Medium: Gas Station
- Approach: if tank negative, restart from next index.

4. Hard: Minimum Cost to Connect Sticks
- Approach: min-heap, always merge smallest two.

5. Hard: Candy
- Approach: two passes left->right and right->left constraints.

## 5) Why & What-if
Edge cases:
- Equal keys/ties in sort
- Impossible configurations

Pitfalls:
- Assuming greedy without proof
- Sorting by wrong key
- Forgetting tie-break implications

Why it works:
- Proof usually via exchange argument or cut property.

Variations:
- When greedy fails, DP is often needed.
- Greedy + heap handles dynamic best choice.

## 6) Complexity and Tradeoffs
- Usually `O(n log n)` due to sorting/heap, sometimes `O(n)`
- Space `O(1)` to `O(n)` depending on data structure

Tradeoffs:
- Simpler and fast when valid.
- Can be subtly wrong without proof.

## 7) Real-world uses
- Scheduling jobs/meetings
- Compression (Huffman coding)
- Resource allocation and batching
- Network design heuristics

## 8) Comparisons
- Greedy vs DP:
  - Greedy picks local best once.
  - DP evaluates many states for guaranteed optimum.
- Greedy vs brute force:
  - Greedy drastically faster when property holds.

## 9) Retention
Cheat sheet:
- Interval maximize count -> sort by end.
- Merge-cost minimization -> heap smallest pairs.
- Reachability -> maintain farthest index.

Recall hooks:
- "Local best is safe only with proof."
- "Sort key decides greedy correctness."

Practice (10):
1. Easy: Jump Game
2. Easy: Assign Cookies
3. Medium: Non-overlapping Intervals
4. Medium: Partition Labels
5. Medium: Gas Station
6. Medium: Queue Reconstruction by Height
7. Medium: Reorganize String (greedy + heap)
8. Hard: Candy
9. Hard: Minimum Number of Refueling Stops
10. Hard: IPO / Maximize Capital
