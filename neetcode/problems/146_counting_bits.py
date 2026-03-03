"""
146. Counting Bits
Difficulty: Easy

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given an integer n, return an array ans where ans[i] is the number of 1 bits in i for 0 <= i <= n.

Easy Explanation:
- Given: n.
- Task: Given an integer n, return an array ans where ans[i] is the number of 1 bits in i for 0 <= i <= n.
- Return: a list/array in the required format.

Input (Example 1):
n = 5

How to Read the Input:
- `n` = 5 (integer)

Output (Example 1):
[0,1,1,2,1,2]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: n = 5.
2. Apply the rule in the problem statement: Given an integer n, return an array ans where ans[i] is the number of 1 bits in i for 0 <= i <= n.
3. For this example, the correct result is [0,1,1,2,1,2].
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- 0 <= n <= 10^5

Follow-up:
- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
