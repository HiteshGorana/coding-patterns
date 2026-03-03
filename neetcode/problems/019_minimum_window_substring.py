"""
19. Minimum Window Substring
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given strings `s` and `t`, return the minimum window in `s` containing all chars of `t` (with multiplicity). If none, return `""`.

Easy Explanation:
- Given: s, t.
- Task: Given strings `s` and `t`, return the minimum window in `s` containing all chars of `t` (with multiplicity). If none, return `""`.
- Return: a string.

Input (Example 1):
s = "ADOBECODEBANC", t = "ABC"

How to Read the Input:
- `s` = "ADOBECODEBANC" (string)
- `t` = "ABC" (string)

Output (Example 1):
"BANC"

How to Read the Output:
- The returned value should be a string.

Example 1 Walkthrough:
1. Start with the given input: s = "ADOBECODEBANC", t = "ABC".
2. Apply the rule in the problem statement: Given strings `s` and `t`, return the minimum window in `s` containing all chars of `t` (with multiplicity). If none, return `""`.
3. For this example, the correct result is "BANC".
4. This string is the required result for the given input.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

Follow-up:
- Could you find an algorithm that runs in O(m + n) time?
"""
