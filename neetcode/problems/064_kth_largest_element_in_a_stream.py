"""
64. Kth Largest Element in a Stream
Difficulty: Easy

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a class that continuously returns the kth largest element in a stream after each insertion.

Easy Explanation:
- Given: operations.
- Task: Design a class that continuously returns the kth largest element in a stream after each insertion.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["KthLargest(3,[4,5,8,2])", "add(3)", "add(5)", "add(10)", "add(9)", "add(4)"]

How to Read the Input:
- `operations` = ["KthLargest(3,[4,5,8,2])", "add(3)", "add(5)", "add(10)", "add(9)", "add(4)"] (2D list (matrix))

Output (Example 1):
[null, 4, 5, 5, 8, 8]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["KthLargest(3,[4,5,8,2])", "add(3)", "add(5)", "add(10)", "add(9)", "add(4)"].
2. Apply the rule in the problem statement: Design a class that continuously returns the kth largest element in a stream after each insertion.
3. For this example, the correct result is [null, 4, 5, 5, 8, 8].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 0 <= nums.length <= 10^4
- 1 <= k <= nums.length + 1
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.

Follow-up:
- None specified.
"""
