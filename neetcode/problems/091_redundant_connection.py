"""
91. Redundant Connection
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given edges of a graph that started as a tree with one extra edge, return that redundant edge.

Easy Explanation:
- Given: edges.
- Task: Given edges of a graph that started as a tree with one extra edge, return that redundant edge.
- Return: a list/array in the required format.

Input (Example 1):
edges = [[1,2],[1,3],[2,3]]

How to Read the Input:
- `edges` = [[1,2],[1,3],[2,3]] (2D list (matrix))

Output (Example 1):
[2,3]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: edges = [[1,2],[1,3],[2,3]].
2. Apply the rule in the problem statement: Given edges of a graph that started as a tree with one extra edge, return that redundant edge.
3. For this example, the correct result is [2,3].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

Follow-up:
- None specified.
"""
