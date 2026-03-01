# Pattern 19: Tree DFS (Preorder / Inorder / Postorder)

## Diagram + Intuition

### Pattern Diagram
```text
solve(node):
  left = solve(node.left)
  right = solve(node.right)
  return combine(left, right, node)
```

### Read-the-Question Trigger Cues
- Path sums, diameter, balanced checks, subtree properties.

### Intuition Anchor
- "Define what recursion returns from a subtree."

### 3-Second Pattern Check
- Can parent answer be built from child answers?

## What This Pattern Solves
Depth-first traversal handles recursive tree properties, path accumulation, and subtree composition.

## Recognition Signals
- Need per-node computation from children.
- Ask for path sum, depth, diameter, subtree validation.
- Tree naturally defined recursively.

## Core Intuition
Each node can be solved using results from left/right subtrees plus local logic.

Traversal roles:
- Preorder: process node before children (state push)
- Inorder: useful for BST ordered output
- Postorder: combine child results upward

## Step-by-Step Method
1. Define recursive function return meaning clearly.
2. Handle base case (`None`) first.
3. Recurse into children.
4. Combine child outputs for current node.
5. Return value for parent context.

## Detailed Example (Diameter of Binary Tree)
1. Recursive function returns subtree height.
2. At each node, candidate diameter is `left_height + right_height`.
3. Track global maximum across all nodes.
4. Return `1 + max(left_height, right_height)` upward.

## Complexity
- Time: `O(n)` visiting each node once
- Space: `O(h)` recursion stack (`h` tree height), `O(n)` worst-case skewed

## Python Template
```python
def tree_dfs(root):
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        ans = max(ans, left + right)
        return 1 + max(left, right)

    dfs(root)
    return ans
```

## Common Pitfalls
- Ambiguous return meaning from recursion.
- Forgetting to use `nonlocal`/global accumulator where needed.
- Mixing edge count and node count in depth/diameter.
- Missing base cases causing null dereferences.

## Variations
- Maximum path sum
- Balanced binary tree
- Path sum I/II/III
- Lowest common ancestor (recursive)

## Interview Tips
- Before coding, state: "dfs(node) returns ___".
- Mention tail-risk of recursion depth on skewed trees.
- Draw one 3-level example to validate combine logic.

## Practice Problems
- Diameter of Binary Tree
- Binary Tree Maximum Path Sum
- Balanced Binary Tree
- Path Sum
