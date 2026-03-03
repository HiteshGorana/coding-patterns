"""
121. Regular Expression Matching
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Implement regular expression matching with support for "." and "*" where "*" means zero or more of the preceding element.

What This Problem Is Asking:
- Given: s, p.
- Task: Implement regular expression matching with support for "." and "*" where "*" means zero or more of the preceding element.
- Return: a boolean value (`True` or `False`).

Example 1:

Input: s = "aab", p = "c*a*b"
Output: True
Explanation: For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
Follow-up:
- None specified.
"""
