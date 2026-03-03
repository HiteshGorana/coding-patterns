"""
116. Interleaving String
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given s1, s2, s3, return true if s3 is formed by an interleaving of s1 and s2.

Easy Explanation:
- Given: s1, s2, s3.
- Task: Given s1, s2, s3, return true if s3 is formed by an interleaving of s1 and s2.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

How to Read the Input:
- `s1` = "aabcc" (string)
- `s2` = "dbbca" (string)
- `s3` = "aadbbcbcac" (string)

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac".
2. Apply the rule in the problem statement: Given s1, s2, s3, return true if s3 is formed by an interleaving of s1 and s2.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.

Follow-up:
- Could you solve it using only O(s2.length) additional memory space?
"""
