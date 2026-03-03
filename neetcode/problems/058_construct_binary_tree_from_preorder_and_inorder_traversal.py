"""
58. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Build and return the binary tree from preorder and inorder traversal arrays.

What This Problem Is Asking:
- Given: preorder, inorder.
- Task: Build and return the binary tree from preorder and inorder traversal arrays.
- Return: a list/array in the required format.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
Follow-up:
- None specified.
"""
