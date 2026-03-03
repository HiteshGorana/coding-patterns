"""
57. Kth Smallest Element in a BST
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a BST and an integer k, return the kth smallest value in the tree.

Easy Explanation:
- Given: root, k.
- Task: Given a BST and an integer k, return the kth smallest value in the tree.
- Return: an integer.

Input (Example 1):
root = [3,1,4,null,2], k = 1

How to Read the Input:
- `root` = [3,1,4,null,2] (list with nullable entries)
- `k` = 1 (integer)

Output (Example 1):
1

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: root = [3,1,4,null,2], k = 1.
2. Apply the rule in the problem statement: Given a BST and an integer k, return the kth smallest value in the tree.
3. For this example, the correct result is 1.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Follow-up:
- If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
