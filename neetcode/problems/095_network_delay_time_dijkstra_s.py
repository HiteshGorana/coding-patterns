"""
95. Network Delay Time (Dijkstra's)
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given directed travel times times[i] = (u,v,w), return time for all nodes to receive a signal from node k, or -1.

Easy Explanation:
- Given: times, n, k.
- Task: Given directed travel times times[i] = (u,v,w), return time for all nodes to receive a signal from node k, or -1.
- Return: an integer.

Input (Example 1):
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2

How to Read the Input:
- `times` = [[2,1,1],[2,3,1],[3,4,1]] (2D list (matrix))
- `n` = 4 (integer)
- `k` = 2 (integer)

Output (Example 1):
2

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2.
2. Apply the rule in the problem statement: Given directed travel times times[i] = (u,v,w), return time for all nodes to receive a signal from node k, or -1.
3. For this example, the correct result is 2.
4. This output matches the required format and the rule defined in the prompt.

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
