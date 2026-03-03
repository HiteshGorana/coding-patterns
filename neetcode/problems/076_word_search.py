"""
76. Word Search
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a 2D board and a word, return true if the word exists in the grid by adjacent moves without reusing cells.

Easy Explanation:
- Given: board, word.
- Task: Given a 2D board and a word, return true if the word exists in the grid by adjacent moves without reusing cells.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

How to Read the Input:
- `board` = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] (2D list (matrix))
- `word` = "ABCCED" (string)

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED".
2. Apply the rule in the problem statement: Given a 2D board and a word, return true if the word exists in the grid by adjacent moves without reusing cells.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

Follow-up:
- Could you use search pruning to make your solution faster with a larger board?
"""
