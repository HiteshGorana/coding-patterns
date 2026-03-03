"""
92. Word Ladder
Difficulty: Hard

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given beginWord, endWord, and a word list, return the shortest transformation sequence length.

Easy Explanation:
- Given: beginWord, endWord, wordList.
- Task: Given beginWord, endWord, and a word list, return the shortest transformation sequence length.
- Return: an integer.

Input (Example 1):
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

How to Read the Input:
- `beginWord` = "hit" (string)
- `endWord` = "cog" (string)
- `wordList` = ["hot","dot","dog","lot","log","cog"] (list of strings/values)

Output (Example 1):
5

How to Read the Output:
- The returned value should be an integer.

Example 1 Walkthrough:
1. Start with the given input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"].
2. Apply the rule in the problem statement: Given beginWord, endWord, and a word list, return the shortest transformation sequence length.
3. For this example, the correct result is 5.
4. This output matches the required format and the rule defined in the prompt.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

Follow-up:
- None specified.
"""
