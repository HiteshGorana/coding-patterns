# Pattern 21: Binary Search Tree (BST) Rules

## Diagram + Intuition

### Pattern Diagram
```text
left < node < right
inorder traversal => sorted values
```

### Read-the-Question Trigger Cues
- Validate BST, kth smallest, predecessor/successor, range query.

### Intuition Anchor
- "Ordering constraint lets me prune search."

### 3-Second Pattern Check
- Can BST ordering remove half/subtree work?

## What This Pattern Solves
Leverages BST ordering to speed up search, validation, and rank queries.

## Recognition Signals
- Tree with left `< node <` right ordering.
- Need kth smallest/largest, range queries, predecessor/successor.
- Validation of BST structure.

## Core Intuition
Inorder traversal of valid BST yields sorted sequence.  
Use value bounds during DFS to validate global constraints, not just local child checks.

## Step-by-Step Method (Validate BST)
1. DFS with allowed range `(low, high)` for each node.
2. For node value `v`, require `low < v < high`.
3. Left child range becomes `(low, v)`.
4. Right child range becomes `(v, high)`.

## Step-by-Step Method (Kth Smallest)
1. Perform inorder traversal iteratively or recursively.
2. Count visited nodes.
3. Return value at count `k`.

## Complexity
- Search/insert/delete average `O(log n)`, worst `O(n)` if skewed
- Validation traversal: `O(n)`
- Kth inorder: `O(h + k)` iterative early stop

## Python Template (Validation)
```python
def is_valid_bst(root):
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))
```

## Common Pitfalls
- Checking only immediate children instead of full ancestor bounds.
- Mishandling duplicates (BST definition usually strict inequality).
- Integer boundary overflow in fixed-width languages.
- Assuming balanced tree complexity without guarantee.

## Variations
- Kth smallest in BST
- Lowest common ancestor in BST
- Convert sorted array/list to BST
- BST iterator with amortized `O(1)` next

## Interview Tips
- State strict inequality policy for duplicates.
- Mention iterative inorder option to avoid deep recursion.
- If performance matters, discuss self-balancing trees for guaranteed log height.

## Practice Problems
- Validate Binary Search Tree
- Kth Smallest Element in a BST
- Lowest Common Ancestor of a BST
- Binary Search Tree Iterator
