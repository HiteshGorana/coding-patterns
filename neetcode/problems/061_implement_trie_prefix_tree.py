"""
61. Implement Trie (Prefix Tree)
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Implement a trie with insert, search, and startsWith operations.

What This Problem Is Asking:
- Given: operations.
- Task: Implement a trie with insert, search, and startsWith operations.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["Trie", "insert("apple")", "search("apple")", "search("app")", "startsWith("app")", "insert("app")", "search("app")"]
Output: [null, null, True, False, True, null, True]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
Follow-up:
- None specified.
"""
