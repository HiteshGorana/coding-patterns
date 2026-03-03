"""
127. Merge Triplets to Form Target Triplet
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given triplets and target, determine if you can select and merge triplets so the max at each position equals target.

Easy Explanation:
- Given: triplets, target.
- Task: Given triplets and target, determine if you can select and merge triplets so the max at each position equals target.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]

How to Read the Input:
- `triplets` = [[2,5,3],[1,8,4],[1,7,5]] (2D list (matrix))
- `target` = [2,7,5] (list of values)

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5].
2. Apply the rule in the problem statement: Given triplets and target, determine if you can select and merge triplets so the max at each position equals target.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- 1 <= triplets.length <= 10^5
- triplets[i].length == target.length == 3
- 1 <= ai, bi, ci, x, y, z <= 1000

Follow-up:
- None specified.
"""
