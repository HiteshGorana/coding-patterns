"""
60. Serialize and Deserialize Binary Tree
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design serialize and deserialize functions for a binary tree so that deserializing serialized data reconstructs the original tree.

Easy Explanation:
- Given: root, decoded.
- Task: Design serialize and deserialize functions for a binary tree so that deserializing serialized data reconstructs the original tree.
- Return: a list/array in the required format.

Input (Example 1):
root = [1,2,3,null,null,4,5]; decoded = deserialize(serialize(root))

How to Read the Input:
- `root` = [1,2,3,null,null,4,5]; decoded = deserialize(serialize(root)) (operation/value expression)

Output (Example 1):
[1,2,3,null,null,4,5]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: root = [1,2,3,null,null,4,5]; decoded = deserialize(serialize(root)).
2. Apply the rule in the problem statement: Design serialize and deserialize functions for a binary tree so that deserializing serialized data reconstructs the original tree.
3. For this example, the correct result is [1,2,3,null,null,4,5].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

Follow-up:
- None specified.
"""
