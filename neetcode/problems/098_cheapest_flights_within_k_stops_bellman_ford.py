"""
98. Cheapest Flights Within K Stops (Bellman-Ford)
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given flights, source, destination, and max stops k, return the cheapest price within at most k stops.

Easy Explanation:
- Given: n, flights, src, dst, k.
- Task: Given flights, source, destination, and max stops k, return the cheapest price within at most k stops.
- Return: an integer.

Input (Example 1):
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1

How to Read the Input:
- `n` = 4 (integer)
- `flights` = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] (2D list (matrix))
- `src` = 0 (integer)
- `dst` = 3 (integer)
- `k` = 1 (integer)

Output (Example 1):
700

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1.
2. Apply the rule in the problem statement: Given flights, source, destination, and max stops k, return the cheapest price within at most k stops.
3. For this example, the correct result is 700.
4. This output matches the required format and the rule defined in the prompt.

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
