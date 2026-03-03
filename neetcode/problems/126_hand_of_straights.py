"""
126. Hand of Straights
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given hand and groupSize, return true if cards can be rearranged into groups of groupSize consecutive cards.

Easy Explanation:
- Given: hand, groupSize.
- Task: Given hand and groupSize, return true if cards can be rearranged into groups of groupSize consecutive cards.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3

How to Read the Input:
- `hand` = [1,2,3,6,2,3,4,7,8] (list of values)
- `groupSize` = 3 (integer)

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3.
2. Apply the rule in the problem statement: Given hand and groupSize, return true if cards can be rearranged into groups of groupSize consecutive cards.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- 1 <= hand.length <= 10^4
- 0 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length
- Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Follow-up:
- None specified.
"""
