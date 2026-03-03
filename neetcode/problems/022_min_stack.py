"""
22. Min Stack
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

What This Problem Is Asking:
- Given: operations.
- Task: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["MinStack", "push(-2)", "push(0)", "push(-3)", "getMin()", "pop()", "top()", "getMin()"]
Output: [null, null, null, null, -3, null, 0, -2]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
Follow-up:
- None specified.
"""
