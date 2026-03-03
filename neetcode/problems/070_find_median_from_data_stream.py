"""
70. Find Median from Data Stream
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a data structure that supports adding integers from a stream and returning the median at any time.

What This Problem Is Asking:
- Given: operations.
- Task: Design a data structure that supports adding integers from a stream and returning the median at any time.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["addNum(1)", "addNum(2)", "findMedian()", "addNum(3)", "findMedian()"]
Output: [null, null, 1.5, null, 2.0]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.
Follow-up:
- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
