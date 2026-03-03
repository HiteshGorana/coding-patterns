"""
95. Network Delay Time (Dijkstra's)
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Given directed travel times times[i] = (u,v,w), return time for all nodes to receive a signal from node k, or -1.

What This Problem Is Asking:
- Given: times, n, k.
- Task: Given directed travel times times[i] = (u,v,w), return time for all nodes to receive a signal from node k, or -1.
- Return: an integer.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: This is the computed value that satisfies the prompt for the given input.

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
Follow-up:
- None specified.
"""
