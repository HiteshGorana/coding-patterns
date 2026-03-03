"""
93. Reconstruct Itinerary
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given flight tickets [from, to], reconstruct the itinerary starting from JFK using all tickets exactly once and choosing lexical order when multiple valid routes exist.

Easy Explanation:
- Given: tickets.
- Task: Given flight tickets [from, to], reconstruct the itinerary starting from JFK using all tickets exactly once and choosing lexical order when multiple valid routes exist.
- Return: a list/array in the required format.

Input (Example 1):
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

How to Read the Input:
- `tickets` = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] (2D list (matrix))

Output (Example 1):
["JFK","MUC","LHR","SFO","SJC"]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]].
2. Apply the rule in the problem statement: Given flight tickets [from, to], reconstruct the itinerary starting from JFK using all tickets exactly once and choosing lexical order when multiple valid routes exist.
3. For this example, the correct result is ["JFK","MUC","LHR","SFO","SJC"].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters.
- fromi != toi

Follow-up:
- None specified.
"""
