"""
45. Reverse Nodes in K-Group
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given `head` and `k`, reverse nodes in groups of size `k`. Remaining nodes less than `k` stay as-is.

Easy Explanation:
- Given: the input shown in the example.
- Task: Given `head` and `k`, reverse nodes in groups of size `k`. Remaining nodes less than `k` stay as-is.
- Return: the value/structure requested by the prompt.

Input (Example 1):
1

How to Read the Input:
- Use the exact input format shown in Example 1.

Output (Example 1):
2 -> 3 -> 4 -> 5`, `k = 2` -> `2 -> 1 -> 4 -> 3 -> 5

How to Read the Output:
- The returned value should be a required result value.

Example 1 Walkthrough:
1. Start with the given input: 1.
2. Apply the rule in the problem statement: Given `head` and `k`, reverse nodes in groups of size `k`. Remaining nodes less than `k` stay as-is.
3. For this example, the correct result is 2 -> 3 -> 4 -> 5`, `k = 2` -> `2 -> 1 -> 4 -> 3 -> 5.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

Follow-up:
- Can you solve the problem in O(1) extra memory space?
"""
