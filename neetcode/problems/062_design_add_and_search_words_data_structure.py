"""
62. Design Add and Search Words Data Structure
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a data structure that supports adding words and searching words where "." can match any letter.

Easy Explanation:
- Given: operations.
- Task: Design a data structure that supports adding words and searching words where "." can match any letter.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["WordDictionary", "addWord("bad")", "addWord("dad")", "addWord("mad")", "search("pad")", "search("bad")", "search(".ad")", "search("b..")"]

How to Read the Input:
- `operations` = ["WordDictionary", "addWord("bad")", "addWord("dad")", "addWord("mad")", "search("pad")", "search("bad")", "search(".ad")", "search("b..")"] (list of strings/values)

Output (Example 1):
[null, null, null, null, False, True, True, True]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["WordDictionary", "addWord("bad")", "addWord("dad")", "addWord("mad")", "search("pad")", "search("bad")", "search(".ad")", "search("b..")"].
2. Apply the rule in the problem statement: Design a data structure that supports adding words and searching words where "." can match any letter.
3. For this example, the correct result is [null, null, null, null, False, True, True, True].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.

Follow-up:
- None specified.
"""
