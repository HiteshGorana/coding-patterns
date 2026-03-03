"""
93. Reconstruct Itinerary
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Given flight tickets [from, to], reconstruct the itinerary starting from JFK using all tickets exactly once and choosing lexical order when multiple valid routes exist.

What This Problem Is Asking:
- Given: tickets.
- Task: Given flight tickets [from, to], reconstruct the itinerary starting from JFK using all tickets exactly once and choosing lexical order when multiple valid routes exist.
- Return: a list/array in the required format.

Example 1:

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Explanation: This list is the correct result produced from the given input according to the problem rules.

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
