"""
138. Set Matrix Zeroes
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given an m x n matrix, if an element is 0 set its entire row and column to 0 in-place.

Easy Explanation:
- Given: matrix.
- Task: Given an m x n matrix, if an element is 0 set its entire row and column to 0 in-place.
- Return: a list/array in the required format.

Input (Example 1):
matrix = [[1,1,1],[1,0,1],[1,1,1]]

How to Read the Input:
- `matrix` = [[1,1,1],[1,0,1],[1,1,1]] (2D list (matrix))

Output (Example 1):
[[1,0,1],[0,0,0],[1,0,1]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: matrix = [[1,1,1],[1,0,1],[1,1,1]].
2. Apply the rule in the problem statement: Given an m x n matrix, if an element is 0 set its entire row and column to 0 in-place.
3. For this example, the correct result is [[1,0,1],[0,0,0],[1,0,1]].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Follow-up:
- A straightforward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?
"""
