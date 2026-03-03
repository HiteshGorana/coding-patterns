"""
138. Set Matrix Zeroes
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Given an m x n matrix, if an element is 0 set its entire row and column to 0 in-place.

What This Problem Is Asking:
- Given: matrix.
- Task: Given an m x n matrix, if an element is 0 set its entire row and column to 0 in-place.
- Return: a list/array in the required format.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: This list is the correct result produced from the given input according to the problem rules.

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
