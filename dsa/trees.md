# Trees (Interview-Ready Guide)

Using `[TOPIC] = Trees`.

## 0) Scope (Checklist)
- [x] Traversals (pre/in/post, level order)
- [x] DFS vs BFS
- [x] Height, diameter, balanced checks
- [x] Path problems (root-to-leaf, any-to-any)
- [x] LCA concepts
- [x] Serialize/deserialize basics
- [x] BST insert/search/delete concepts
- [x] Validate BST
- [x] Kth smallest / order statistics ideas
- [x] Successor/predecessor and transforms

## 1) Foundations
Trees are hierarchical acyclic structures. Binary trees have at most two children.

Core terms:
- Root, leaf, depth, height
- Subtree, ancestor, descendant
- BST invariant: `left < node < right`

Mental model:
- Tree recursion solves local node + child subproblems.
- Traversal order decides when node state is processed.

## 2) How it works
Cause-effect:
1. DFS recursively propagates information up/down.
2. BFS processes levels for shortest unweighted depth.
3. BST ordering enables logarithmic operations when balanced.

Tiny trace (inorder of BST with nodes `2<-3->5` and left child `1`):
- Visit left subtree (`1,2`)
- Visit node (`3`)
- Visit right (`5`)
- Inorder result sorted: `[1,2,3,5]`

## 3) Patterns (Interview Templates)
1. DFS return-value template (height, balance, sums)
2. DFS with global answer (diameter/max path)
3. BFS queue level template
4. BST range/inorder template
5. LCA recursion template

Invariants:
- DFS function contract is explicit (what it returns for subtree).
- For BST validation keep allowed `(low, high)` range.
- In BFS, queue holds current level frontier.

Signals:
- Hierarchical parent-child structure
- "Path", "ancestor", "level", "balanced"
- Ordered traversal requirements -> BST

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Maximum Depth of Binary Tree
- Approach: `1 + max(depth(left), depth(right))`.

2. Medium: Validate BST
- Approach: recursive bounds, not just parent compare.

3. Medium: Binary Tree Level Order Traversal
- Approach: BFS queue by level size.

4. Hard: Lowest Common Ancestor
- Approach: recurse both sides; if split occurs, current node is LCA.

5. Hard: Serialize/Deserialize Binary Tree
- Approach: preorder with null markers or level-order encoding.

ASCII:
```text
    3
   / \
  5   1
     / \
    0   8
LCA(5,8)=3
```

## 5) Why & What-if
Edge cases:
- Empty tree
- Single node
- Skewed tree (linked-list shape)

Pitfalls:
- Forgetting null base case
- Confusing height vs depth
- BST validation error by local child check only

Why it works:
- Tree has no cycles; each subtree is an independent smaller problem.

Variations:
- Iterative traversal using explicit stack
- Parent pointers simplify ancestor queries

## 6) Complexity and Tradeoffs
- Traversals: `O(n)` time
- DFS recursive space: `O(h)` where `h` is height
- BFS space: up to `O(width)`
- Balanced BST ops: `O(log n)`, worst skewed `O(n)`

Tradeoffs:
- Recursive code concise; iterative avoids recursion depth limits.

## 7) Real-world uses
- File systems and DOM trees
- Database indexes (BST variants, B-trees conceptually)
- Org charts and dependency hierarchies
- Expression trees in compilers

## 8) Comparisons
- DFS vs BFS:
  - DFS for deep structural properties.
  - BFS for shortest level distance.
- BST vs heap:
  - BST supports ordered search.
  - Heap supports fast top element only.

## 9) Retention
Cheat sheet:
- Preorder: node-left-right
- Inorder: left-node-right
- Postorder: left-right-node
- BST validate with bounds
- Diameter often uses height function

Recall hooks:
- "Define subtree contract first."
- "Inorder of BST is sorted."

Practice (10):
1. Easy: Invert Binary Tree
2. Easy: Maximum Depth of Binary Tree
3. Medium: Validate BST
4. Medium: Binary Tree Level Order Traversal
5. Medium: Kth Smallest in BST
6. Medium: Construct Binary Tree from Traversals
7. Medium: Lowest Common Ancestor of BST
8. Hard: Lowest Common Ancestor of Binary Tree
9. Hard: Serialize and Deserialize Binary Tree
10. Hard: Binary Tree Maximum Path Sum
