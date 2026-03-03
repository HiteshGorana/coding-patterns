"""
7. Valid Sudoku
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Determine if a 9x9 Sudoku board is valid. Digits 1-9 must not repeat in any row, column, or 3x3 sub-box; "." represents empty cells.

Easy Explanation:
- Given: board.
- Task: Determine if a 9x9 Sudoku board is valid. Digits 1-9 must not repeat in any row, column, or 3x3 sub-box; "." represents empty cells.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

How to Read the Input:
- `board` = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] (2D list (matrix))

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]].
2. Apply the rule in the problem statement: Determine if a 9x9 Sudoku board is valid. Digits 1-9 must not repeat in any row, column, or 3x3 sub-box; "." represents empty cells.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.

Follow-up:
- None specified.
"""
