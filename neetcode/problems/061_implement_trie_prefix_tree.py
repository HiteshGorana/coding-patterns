"""
61. Implement Trie (Prefix Tree)
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Implement a trie with insert, search, and startsWith operations.

Easy Explanation:
- Given: operations.
- Task: Implement a trie with insert, search, and startsWith operations.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["Trie", "insert("apple")", "search("apple")", "search("app")", "startsWith("app")", "insert("app")", "search("app")"]

How to Read the Input:
- `operations` = ["Trie", "insert("apple")", "search("apple")", "search("app")", "startsWith("app")", "insert("app")", "search("app")"] (list of strings/values)

Output (Example 1):
[null, null, True, False, True, null, True]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["Trie", "insert("apple")", "search("apple")", "search("app")", "startsWith("app")", "insert("app")", "search("app")"].
2. Apply the rule in the problem statement: Implement a trie with insert, search, and startsWith operations.
3. For this example, the correct result is [null, null, True, False, True, null, True].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Follow-up:
- None specified.
"""
