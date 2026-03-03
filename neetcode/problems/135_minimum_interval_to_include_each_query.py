"""
135. Minimum Interval to Include Each Query
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
For each query, find the size of the smallest interval [l, r] that includes it, or -1 if none.

Easy Explanation:
- Given: intervals, queries.
- Task: For each query, find the size of the smallest interval [l, r] that includes it, or -1 if none.
- Return: a list/array in the required format.

Input (Example 1):
intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]

How to Read the Input:
- `intervals` = [[1,4],[2,4],[3,6],[4,4]] (2D list (matrix))
- `queries` = [2,3,4,5] (list of values)

Output (Example 1):
[3,3,1,4]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5].
2. Apply the rule in the problem statement: For each query, find the size of the smallest interval [l, r] that includes it, or -1 if none.
3. For this example, the correct result is [3,3,1,4].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- 1 <= intervals.length <= 10^5
- 1 <= queries.length <= 10^5
- intervals[i].length == 2
- 1 <= lefti <= righti <= 10^7
- 1 <= queries[j] <= 10^7

Follow-up:
- None specified.
"""
