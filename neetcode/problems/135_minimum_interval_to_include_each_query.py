"""
135. Minimum Interval to Include Each Query
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
For each query, find the size of the smallest interval [l, r] that includes it, or -1 if none.

What This Problem Is Asking:
- Given: intervals, queries.
- Task: For each query, find the size of the smallest interval [l, r] that includes it, or -1 if none.
- Return: a list/array in the required format.

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: This list is the correct result produced from the given input according to the problem rules.

Constraints:
- 1 <= intervals.length <= 10^5
- 1 <= queries.length <= 10^5
- intervals[i].length == 2
- 1 <= lefti <= righti <= 10^7
- 1 <= queries[j] <= 10^7
Follow-up:
- None specified.
"""
