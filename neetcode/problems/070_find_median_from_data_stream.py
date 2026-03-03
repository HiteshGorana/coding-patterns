"""
70. Find Median from Data Stream
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a data structure that supports adding integers from a stream and returning the median at any time.

Easy Explanation:
- Given: operations.
- Task: Design a data structure that supports adding integers from a stream and returning the median at any time.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["addNum(1)", "addNum(2)", "findMedian()", "addNum(3)", "findMedian()"]

How to Read the Input:
- `operations` = ["addNum(1)", "addNum(2)", "findMedian()", "addNum(3)", "findMedian()"] (list of strings/values)

Output (Example 1):
[null, null, 1.5, null, 2.0]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["addNum(1)", "addNum(2)", "findMedian()", "addNum(3)", "findMedian()"].
2. Apply the rule in the problem statement: Design a data structure that supports adding integers from a stream and returning the median at any time.
3. For this example, the correct result is [null, null, 1.5, null, 2.0].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow-up:
- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
