"""
37. Reorder List
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given list `L0 -> L1 -> . -> Ln`, reorder it to `L0 -> Ln -> L1 -> Ln-1 -> ...`.

Easy Explanation:
- Given: the input shown in the example.
- Task: Given list `L0 -> L1 -> ... -> Ln`, reorder it to `L0 -> Ln -> L1 -> Ln-1 -> ...`.
- Return: the value/structure requested by the prompt.

Input (Example 1):
1

How to Read the Input:
- Use the exact input format shown in Example 1.

Output (Example 1):
2 -> 3 -> 4 -> 5` becomes `1 -> 5 -> 2 -> 4 -> 3

How to Read the Output:
- The returned value should be a required result value.

Example 1 Walkthrough:
1. Start with the given input: 1.
2. Apply the rule in the problem statement: Given list `L0 -> L1 -> . -> Ln`, reorder it to `L0 -> Ln -> L1 -> Ln-1 -> ...`.
3. For this example, the correct result is 2 -> 3 -> 4 -> 5` becomes `1 -> 5 -> 2 -> 4 -> 3.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

Follow-up:
- None specified.
"""
