"""
125. Gas Station
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given `gas` and `cost`, return start index to complete circuit once, else `-1`.

Easy Explanation:
- Given: gas, cost.
- Task: Given `gas` and `cost`, return start index to complete circuit once, else `-1`.
- Return: an integer.

Input (Example 1):
gas = [1,2,3,4,5], cost = [3,4,5,1,2]

How to Read the Input:
- `gas` = [1,2,3,4,5] (list of values)
- `cost` = [3,4,5,1,2] (list of values)

Output (Example 1):
3

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: gas = [1,2,3,4,5], cost = [3,4,5,1,2].
2. Apply the rule in the problem statement: Given `gas` and `cost`, return start index to complete circuit once, else `-1`.
3. For this example, the correct result is 3.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
- The input is generated such that the answer is unique.

Follow-up:
- None specified.
"""
