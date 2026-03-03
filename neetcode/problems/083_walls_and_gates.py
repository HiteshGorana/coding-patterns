"""
83. Walls and Gates
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Fill each empty room with the distance to its nearest gate; if unreachable, keep it as INF.

Easy Explanation:
- Given: rooms.
- Task: Fill each empty room with the distance to its nearest gate; if unreachable, keep it as INF.
- Return: a list/array in the required format.

Input (Example 1):
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

How to Read the Input:
- `rooms` = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]] (2D list (matrix))

Output (Example 1):
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]].
2. Apply the rule in the problem statement: Fill each empty room with the distance to its nearest gate; if unreachable, keep it as INF.
3. For this example, the correct result is [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- See original LeetCode constraints for this problem.

Follow-up:
- None specified.
"""
