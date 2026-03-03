"""
86. Surrounded Regions
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Capture all regions of "O" that are completely surrounded by "X" in a 2D board.

Easy Explanation:
- Given: board.
- Task: Capture all regions of "O" that are completely surrounded by "X" in a 2D board.
- Return: a list/array in the required format.

Input (Example 1):
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

How to Read the Input:
- `board` = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]] (2D list (matrix))

Output (Example 1):
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]].
2. Apply the rule in the problem statement: Capture all regions of "O" that are completely surrounded by "X" in a 2D board.
3. For this example, the correct result is [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

Follow-up:
- None specified.
"""
