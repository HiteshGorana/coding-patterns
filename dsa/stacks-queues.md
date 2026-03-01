# Stacks & Queues (Interview-Ready Guide)

Using `[TOPIC] = Stacks & Queues`.

## 0) Scope (Checklist)
- [x] Valid parentheses / expression evaluation ideas
- [x] Monotonic stack (next greater/smaller)
- [x] Largest rectangle / histogram patterns
- [x] Queue patterns (BFS)
- [x] Deque patterns
- [x] Monotonic queue (sliding window max/min)
- [x] Circular queue concepts

## 1) Foundations
Stack = LIFO. Queue = FIFO. Deque = both ends.

Core terms:
- Push/pop/top
- Enqueue/dequeue/front
- Monotonic increasing/decreasing container
- Indices vs values in stack/deque

Mental model:
- Stack keeps unresolved past candidates.
- Queue manages processing order layers (BFS).
- Deque can maintain window candidates efficiently.

## 2) How it works
Cause-effect:
1. Stack resolves "nearest previous/next constraint" by popping invalid tops.
2. Queue ensures earliest discovered is processed first (shortest path in unweighted graph).
3. Monotonic deque removes worse candidates, keeping front as answer.

Tiny trace (next greater for `[2,1,2]`):
- i=0 val=2, stack=[] push0
- i=1 val=1, top=2>1 push1
- i=2 val=2, pop1 -> ans[1]=2; pop0? equal no; push2
- leftover indices have no next greater -> -1

## 3) Patterns (Interview Templates)
1. Bracket validation stack
2. Monotonic stack for next greater/smaller and range boundaries
3. BFS queue for shortest steps in unweighted graphs/grids
4. Monotonic deque for sliding window max/min
5. Circular buffer with `(idx+1)%cap`

Invariants:
- Monotonic stack keeps strict order by value.
- BFS queue contains current frontier in discovery order.
- Deque front is always best candidate for current window.

Signals:
- "Nearest greater/smaller"
- "Process level by level"
- "Window max/min in O(n)"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Valid Parentheses
- Approach: push openings, pop on matching closings.
- Trace: `"()[]{}"` -> stack empty at end => valid.

2. Medium: Daily Temperatures
- Approach: decreasing stack of indices.
- Trace: `[73,74,75,71]` -> when 74 arrives, resolve 73.

3. Medium: Sliding Window Maximum
- Approach: decreasing deque of indices.
- Trace for `[1,3,-1,-3,5]`, `k=3` -> max sequence `[3,3,5]`.

4. Hard: Largest Rectangle in Histogram
- Approach: monotonic increasing stack with sentinel.
- Key: popped bar gets maximal width from previous smaller to current smaller.

ASCII histogram idea:
```text
heights: 2 1 5 6 2 3
           ^ pop bars when current < stack top
```

## 5) Why & What-if
Edge cases:
- Empty input
- Duplicate heights with strict/non-strict pop condition
- Window size `k=1` or `k=n`

Pitfalls:
- Forgetting to store indices (not only values)
- Not removing out-of-window deque indices
- Missing final stack flush in histogram

Why it works:
- Each index pushed/popped at most once => linear time.

Variations:
- Evaluate expressions with operator precedence (two stacks).
- 0-1 BFS uses deque with front/back insertion by edge weight.

## 6) Complexity and Tradeoffs
- Stack/queue operations: `O(1)` each
- Monotonic stack/deque patterns: `O(n)` total
- BFS: `O(V+E)` time, `O(V)` space

Tradeoffs:
- Deque gives optimal window extremes; heap gives simpler but `O(n log k)`.

## 7) Real-world uses
- Undo/redo stacks
- Task scheduling queues
- BFS in routing/state exploration
- Stream analytics sliding window metrics

## 8) Comparisons
- Stack vs recursion: similar call behavior, explicit stack avoids recursion limits.
- Queue BFS vs stack DFS: BFS for shortest edges, DFS for deep traversal.
- Monotonic deque vs heap window max: deque is faster asymptotically.

## 9) Retention
Cheat sheet:
- Nearest something -> monotonic stack.
- Level shortest path (unweighted) -> BFS queue.
- Window max/min -> monotonic deque.

Recall hooks:
- "Push once, pop once -> O(n)."
- "Frontier order gives shortest levels."

Practice (10):
1. Easy: Valid Parentheses
2. Easy: Implement Queue using Stacks
3. Easy: Implement Stack using Queues
4. Medium: Daily Temperatures
5. Medium: Next Greater Element II
6. Medium: Sliding Window Maximum
7. Medium: Number of Recent Calls (queue)
8. Hard: Largest Rectangle in Histogram
9. Hard: Maximal Rectangle
10. Hard: Basic Calculator II/III
