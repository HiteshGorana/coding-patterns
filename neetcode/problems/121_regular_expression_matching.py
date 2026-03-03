"""
121. Regular Expression Matching
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Implement regular expression matching with support for "." and "*" where "*" means zero or more of the preceding element.

Easy Explanation:
- Given: s, p.
- Task: Implement regular expression matching with support for "." and "*" where "*" means zero or more of the preceding element.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
s = "aab", p = "c*a*b"

How to Read the Input:
- `s` = "aab" (string)
- `p` = "c*a*b" (string)

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: s = "aab", p = "c*a*b".
2. Apply the rule in the problem statement: Implement regular expression matching with support for "." and "*" where "*" means zero or more of the preceding element.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

Follow-up:
- None specified.
"""
