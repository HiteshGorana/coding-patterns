"""
84. Rotting Oranges
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a grid of oranges, return the minimum minutes until no fresh orange remains, or -1 if impossible.

Easy Explanation:
- Given: grid.
- Task: Given a grid of oranges, return the minimum minutes until no fresh orange remains, or -1 if impossible.
- Return: an integer.

Input (Example 1):
grid = [[2,1,1],[1,1,0],[0,1,1]]

How to Read the Input:
- `grid` = [[2,1,1],[1,1,0],[0,1,1]] (2D list (matrix))

Output (Example 1):
4

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: grid = [[2,1,1],[1,1,0],[0,1,1]].
2. Apply the rule in the problem statement: Given a grid of oranges, return the minimum minutes until no fresh orange remains, or -1 if impossible.
3. For this example, the correct result is 4.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.

Follow-up:
- None specified.
"""
