"""
58. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Build and return the binary tree from preorder and inorder traversal arrays.

Easy Explanation:
- Given: preorder, inorder.
- Task: Build and return the binary tree from preorder and inorder traversal arrays.
- Return: a list/array in the required format.

Input (Example 1):
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

How to Read the Input:
- `preorder` = [3,9,20,15,7] (list of values)
- `inorder` = [9,3,15,20,7] (list of values)

Output (Example 1):
[3,9,20,null,null,15,7]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7].
2. Apply the rule in the problem statement: Build and return the binary tree from preorder and inorder traversal arrays.
3. For this example, the correct result is [3,9,20,null,null,15,7].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

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
