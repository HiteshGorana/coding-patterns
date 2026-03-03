"""
64. Kth Largest Element in a Stream
Difficulty: Easy

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a class that continuously returns the kth largest element in a stream after each insertion.

What This Problem Is Asking:
- Given: operations.
- Task: Design a class that continuously returns the kth largest element in a stream after each insertion.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["KthLargest(3,[4,5,8,2])", "add(3)", "add(5)", "add(10)", "add(9)", "add(4)"]
Output: [null, 4, 5, 5, 8, 8]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 0 <= nums.length <= 10^4
- 1 <= k <= nums.length + 1
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.
Follow-up:
- None specified.
"""
