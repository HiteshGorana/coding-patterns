"""
98. Cheapest Flights Within K Stops (Bellman-Ford)
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Given flights, source, destination, and max stops k, return the cheapest price within at most k stops.

What This Problem Is Asking:
- Given: n, flights, src, dst, k.
- Task: Given flights, source, destination, and max stops k, return the cheapest price within at most k stops.
- Return: an integer.

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: This is the computed value that satisfies the prompt for the given input.

Constraints:
- 2 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 10^4
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst
Follow-up:
- None specified.
"""
