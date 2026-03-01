# Pattern 20: Tree BFS (Level Order)

## Diagram + Intuition

### Pattern Diagram
```text
queue frontier
process by level_size
```

### Read-the-Question Trigger Cues
- Level-based output, min depth, nearest by levels.

### Intuition Anchor
- "Queue = current frontier of equal distance from root."

### 3-Second Pattern Check
- Does level boundary matter to output?

## What This Pattern Solves
BFS processes tree nodes level by level and is ideal for shortest-level properties.

## Recognition Signals
- Need per-level aggregation (averages, max values, zigzag).
- Need minimum depth or nearest target from root in unweighted tree.
- "Level order traversal" directly indicates BFS.

## Core Intuition
Queue stores frontier of nodes at current depth.  
Process queue in batches by current `level_size` to keep level boundaries clean.

## Step-by-Step Method
1. If root is null, return empty.
2. Initialize queue with root.
3. While queue not empty:
   - capture `level_size`
   - pop exactly that many nodes
   - push children of popped nodes
   - store level result

## Detailed Example (Level Order Traversal)
Tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
Levels become `[[3], [9,20], [15,7]]`.

## Complexity
- Time: `O(n)`
- Space: `O(w)` where `w` is max tree width

## Python Template
```python
from collections import deque

def level_order(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)

    return result
```

## Common Pitfalls
- Iterating over changing queue length without fixed `level_size`.
- Forgetting null root case.
- Using DFS when question specifically needs shortest unweighted level distance.

## Variations
- Zigzag level order traversal
- Right side view
- Minimum depth of binary tree
- Maximum level sum

## Interview Tips
- Mention queue naturally models breadth-first expansion.
- Clarify whether output needs grouped levels or flat order.
- For shortest depth, early return when first leaf is found.

## Practice Problems
- Binary Tree Level Order Traversal
- Binary Tree Zigzag Level Order Traversal
- Minimum Depth of Binary Tree
- Binary Tree Right Side View
