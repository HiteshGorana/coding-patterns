"""
39. Copy List with Random Pointer
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a linked list where each node has a next pointer and a random pointer, return a deep copy of the list.

Easy Explanation:
- Given: head.
- Task: Given a linked list where each node has a next pointer and a random pointer, return a deep copy of the list.
- Return: a list/array in the required format.

Input (Example 1):
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

How to Read the Input:
- `head` = [[7,null],[13,0],[11,4],[10,2],[1,0]] (2D list (matrix))

Output (Example 1):
[[7,null],[13,0],[11,4],[10,2],[1,0]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]].
2. Apply the rule in the problem statement: Given a linked list where each node has a next pointer and a random pointer, return a deep copy of the list.
3. For this example, the correct result is [[7,null],[13,0],[11,4],[10,2],[1,0]].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or is pointing to some node in the linked list.

Follow-up:
- None specified.
"""
