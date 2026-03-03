"""
52. Lowest Common Ancestor of a BST
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a BST and two nodes p and q, return their lowest common ancestor.

Easy Explanation:
- Given: root, p, q.
- Task: Given a BST and two nodes p and q, return their lowest common ancestor.
- Return: an integer.

Input (Example 1):
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

How to Read the Input:
- `root` = [6,2,8,0,4,7,9,null,null,3,5] (list with nullable entries)
- `p` = 2 (integer)
- `q` = 8 (integer)

Output (Example 1):
6

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8.
2. Apply the rule in the problem statement: Given a BST and two nodes p and q, return their lowest common ancestor.
3. For this example, the correct result is 6.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

Follow-up:
- None specified.
"""
