"""
143. Detect Squares
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a data structure that adds points and counts the number of axis-aligned squares that can be formed with a given query point.

Easy Explanation:
- Given: operations.
- Task: Design a data structure that adds points and counts the number of axis-aligned squares that can be formed with a given query point.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["add([3,10])", "add([11,2])", "add([3,2])", "count([11,10])", "count([14,8])", "add([11,2])", "count([11,10])"]

How to Read the Input:
- `operations` = ["add([3,10])", "add([11,2])", "add([3,2])", "count([11,10])", "count([14,8])", "add([11,2])", "count([11,10])"] (2D list (matrix))

Output (Example 1):
[null, null, null, 1, 0, null, 2]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["add([3,10])", "add([11,2])", "add([3,2])", "count([11,10])", "count([14,8])", "add([11,2])", "count([11,10])"].
2. Apply the rule in the problem statement: Design a data structure that adds points and counts the number of axis-aligned squares that can be formed with a given query point.
3. For this example, the correct result is [null, null, null, 1, 0, null, 2].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- point.length == 2
- 0 <= x, y <= 1000
- At most 3000 calls in total will be made to add and count.

Follow-up:
- None specified.
"""
