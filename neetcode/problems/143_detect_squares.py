"""
143. Detect Squares
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a data structure that adds points and counts the number of axis-aligned squares that can be formed with a given query point.

What This Problem Is Asking:
- Given: operations.
- Task: Design a data structure that adds points and counts the number of axis-aligned squares that can be formed with a given query point.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["add([3,10])", "add([11,2])", "add([3,2])", "count([11,10])", "count([14,8])", "add([11,2])", "count([11,10])"]
Output: [null, null, null, 1, 0, null, 2]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- point.length == 2
- 0 <= x, y <= 1000
- At most 3000 calls in total will be made to add and count.
Follow-up:
- None specified.
"""
