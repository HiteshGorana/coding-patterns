"""
130. Insert Interval
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given non-overlapping sorted intervals and one new interval, insert and merge as needed.

Easy Explanation:
- Given: intervals, newInterval.
- Task: Given non-overlapping sorted intervals and one new interval, insert and merge as needed.
- Return: a list/array in the required format.

Input (Example 1):
intervals = [[1,3],[6,9]], newInterval = [2,5]

How to Read the Input:
- `intervals` = [[1,3],[6,9]] (2D list (matrix))
- `newInterval` = [2,5] (list of values)

Output (Example 1):
[[1,5],[6,9]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: intervals = [[1,3],[6,9]], newInterval = [2,5].
2. Apply the rule in the problem statement: Given non-overlapping sorted intervals and one new interval, insert and merge as needed.
3. For this example, the correct result is [[1,5],[6,9]].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5

Follow-up:
- None specified.
"""
