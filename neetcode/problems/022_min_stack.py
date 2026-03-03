"""
22. Min Stack
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Easy Explanation:
- Given: operations.
- Task: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["MinStack", "push(-2)", "push(0)", "push(-3)", "getMin()", "pop()", "top()", "getMin()"]

How to Read the Input:
- `operations` = ["MinStack", "push(-2)", "push(0)", "push(-3)", "getMin()", "pop()", "top()", "getMin()"] (list of strings/values)

Output (Example 1):
[null, null, null, null, -3, null, 0, -2]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["MinStack", "push(-2)", "push(0)", "push(-3)", "getMin()", "pop()", "top()", "getMin()"].
2. Apply the rule in the problem statement: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
3. For this example, the correct result is [null, null, null, null, -3, null, 0, -2].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Follow-up:
- None specified.
"""
