"""
63. Word Search II
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a board of letters and a list of words, return all words that can be formed by sequentially adjacent letters.

Easy Explanation:
- Given: board, words.
- Task: Given a board of letters and a list of words, return all words that can be formed by sequentially adjacent letters.
- Return: a list/array in the required format.

Input (Example 1):
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]

How to Read the Input:
- `board` = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] (2D list (matrix))
- `words` = ["oath","pea","eat","rain"] (list of strings/values)

Output (Example 1):
["eat", "oath"]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"].
2. Apply the rule in the problem statement: Given a board of letters and a list of words, return all words that can be formed by sequentially adjacent letters.
3. For this example, the correct result is ["eat", "oath"].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

Follow-up:
- None specified.
"""
