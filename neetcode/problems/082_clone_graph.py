"""
82. Clone Graph
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy of the graph.

Easy Explanation:
- Given: adjList.
- Task: Given a reference of a node in a connected undirected graph, return a deep copy of the graph.
- Return: a list/array in the required format.

Input (Example 1):
adjList = [[2,4],[1,3],[2,4],[1,3]]

How to Read the Input:
- `adjList` = [[2,4],[1,3],[2,4],[1,3]] (2D list (matrix))

Output (Example 1):
[[2,4],[1,3],[2,4],[1,3]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: adjList = [[2,4],[1,3],[2,4],[1,3]].
2. Apply the rule in the problem statement: Given a reference of a node in a connected undirected graph, return a deep copy of the graph.
3. For this example, the correct result is [[2,4],[1,3],[2,4],[1,3]].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Follow-up:
- None specified.
"""
