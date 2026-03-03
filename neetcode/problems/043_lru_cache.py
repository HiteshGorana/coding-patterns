"""
43. LRU Cache
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a data structure for Least Recently Used (LRU) cache with O(1) get and put.

What This Problem Is Asking:
- Given: operations.
- Task: Design a data structure for Least Recently Used (LRU) cache with O(1) get and put.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["LRUCache(2)", "put(1,1)", "put(2,2)", "get(1)", "put(3,3)", "get(2)", "put(4,4)", "get(1)", "get(3)", "get(4)"]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
Follow-up:
- None specified.
"""
