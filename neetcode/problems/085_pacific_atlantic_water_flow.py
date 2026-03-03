"""
85. Pacific Atlantic Water Flow
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a heights matrix, return coordinates where water can flow to both the Pacific and Atlantic oceans.

Easy Explanation:
- Given: heights.
- Task: Given a heights matrix, return coordinates where water can flow to both the Pacific and Atlantic oceans.
- Return: a list/array in the required format.

Input (Example 1):
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

How to Read the Input:
- `heights` = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] (2D list (matrix))

Output (Example 1):
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]].
2. Apply the rule in the problem statement: Given a heights matrix, return coordinates where water can flow to both the Pacific and Atlantic oceans.
3. For this example, the correct result is [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Follow-up:
- None specified.
"""
