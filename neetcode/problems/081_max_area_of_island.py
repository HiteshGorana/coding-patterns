"""
81. Max Area of Island
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a binary grid, return the maximum area of an island (connected 1s in 4 directions).

Easy Explanation:
- Given: grid.
- Task: Given a binary grid, return the maximum area of an island (connected 1s in 4 directions).
- Return: an integer.

Input (Example 1):
grid = [[0,0,1,0,0,0,1,1],[0,0,1,0,1,0,1,1],[0,0,0,0,1,0,0,0],[1,1,0,0,0,0,0,0]]

How to Read the Input:
- `grid` = [[0,0,1,0,0,0,1,1],[0,0,1,0,1,0,1,1],[0,0,0,0,1,0,0,0],[1,1,0,0,0,0,0,0]] (2D list (matrix))

Output (Example 1):
4

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: grid = [[0,0,1,0,0,0,1,1],[0,0,1,0,1,0,1,1],[0,0,0,0,1,0,0,0],[1,1,0,0,0,0,0,0]].
2. Apply the rule in the problem statement: Given a binary grid, return the maximum area of an island (connected 1s in 4 directions).
3. For this example, the correct result is 4.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

Follow-up:
- None specified.
"""
