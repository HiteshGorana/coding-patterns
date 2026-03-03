"""
62. Design Add and Search Words Data Structure
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a data structure that supports adding words and searching words where "." can match any letter.

What This Problem Is Asking:
- Given: operations.
- Task: Design a data structure that supports adding words and searching words where "." can match any letter.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["WordDictionary", "addWord("bad")", "addWord("dad")", "addWord("mad")", "search("pad")", "search("bad")", "search(".ad")", "search("b..")"]
Output: [null, null, null, null, False, True, True, True]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.
Follow-up:
- None specified.
"""
