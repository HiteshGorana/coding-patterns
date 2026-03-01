# Pattern 39: State-space BFS

## Diagram + Intuition

### Pattern Diagram
```text
BFS node = (position, state)
visited tracks full tuple, not just position
```

### Read-the-Question Trigger Cues
- Path feasibility depends on keys, mask, fuel, direction, or configuration.
- Need shortest steps in an unweighted transition graph.

### Intuition Anchor
- "When future options depend on history, history must be encoded inside BFS state."

### 3-Second Pattern Check
- If I reach same location with different state, do outcomes differ?

## What This Pattern Solves
State-space BFS finds shortest path in problems where each node includes extra mutable state beyond position.

## Recognition Signals
- Puzzles: lock wheels, sliding tiles, board transitions.
- Collect-all keys/items before reaching goal.
- Need minimum moves in finite unweighted state graph.

## Core Intuition
Model each unique `(location, state)` as graph node; run BFS over this expanded graph.

## Step-by-Step Method
1. Define state tuple fully (position + metadata).
2. Generate valid neighboring states.
3. Use queue for BFS and visited set on full state tuple.
4. Return first time goal state is dequeued.

## Detailed Example
In Open the Lock, each 4-digit combination is a node; each wheel turn is an edge.

## Complexity
- Time: `O(number_of_states + transitions)`.
- Space: `O(number_of_states)`.

## Python Template
```python
from collections import deque

def shortest_state_bfs(start, is_goal, neighbors):
    q = deque([(start, 0)])
    seen = {start}

    while q:
        state, d = q.popleft()
        if is_goal(state):
            return d
        for nxt in neighbors(state):
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, d + 1))

    return -1
```

## Common Pitfalls
- Visited by position only (incorrect).
- State explosion from unnecessary dimensions.
- Missing constraints when generating next states.

## Variations
- Open the Lock
- Shortest Path to Get All Keys
- Sliding Puzzle
- Snakes and Ladders

## Interview Tips
- Write exact state definition before coding.
- Estimate upper bound on states to justify complexity.

## Practice Problems
- Open the Lock
- Shortest Path to Get All Keys
- Sliding Puzzle
- Snakes and Ladders
