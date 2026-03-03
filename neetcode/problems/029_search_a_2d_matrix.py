"""
29. Search a 2D Matrix
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given `m x n` matrix where each row is sorted and first value of each row is greater than last value of previous row, return `True` if target exists.

Easy Explanation:
- Given: matrix, target.
- Task: Given `m x n` matrix where each row is sorted and first value of each row is greater than last value of previous row, return `True` if target exists.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

How to Read the Input:
- `matrix` = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] (2D list (matrix))
- `target` = 3 (integer)

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3.
2. Apply the rule in the problem statement: Given `m x n` matrix where each row is sorted and first value of each row is greater than last value of previous row, return `True` if target exists.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

Follow-up:
- None specified.
"""
