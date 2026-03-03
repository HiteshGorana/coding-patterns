"""
55. Count Good Nodes in Binary Tree
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Count the number of good nodes in a binary tree where a node is good if no node on the path from root to it has a greater value.

Easy Explanation:
- Given: root.
- Task: Count the number of good nodes in a binary tree where a node is good if no node on the path from root to it has a greater value.
- Return: an integer.

Input (Example 1):
root = [3,1,4,3,null,1,5]

How to Read the Input:
- `root` = [3,1,4,3,null,1,5] (list with nullable entries)

Output (Example 1):
4

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: root = [3,1,4,3,null,1,5].
2. Apply the rule in the problem statement: Count the number of good nodes in a binary tree where a node is good if no node on the path from root to it has a greater value.
3. For this example, the correct result is 4.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

Follow-up:
- None specified.
"""
