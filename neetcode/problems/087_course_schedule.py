"""
87. Course Schedule
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Given numCourses and prerequisite pairs, return true if you can finish all courses.

Easy Explanation:
- Given: numCourses, prerequisites.
- Task: Given numCourses and prerequisite pairs, return true if you can finish all courses.
- Return: a boolean value (`True` or `False`).

Input (Example 1):
numCourses = 2, prerequisites = [[1,0]]

How to Read the Input:
- `numCourses` = 2 (integer)
- `prerequisites` = [[1,0]] (2D list (matrix))

Output (Example 1):
True

How to Read the Output:
- The returned value should be a boolean.
- Return `True` if the condition is satisfied; otherwise return `False`.

Example 1 Walkthrough:
1. Start with the given input: numCourses = 2, prerequisites = [[1,0]].
2. Apply the rule in the problem statement: Given numCourses and prerequisite pairs, return true if you can finish all courses.
3. For this example, the correct result is True.
4. For this input, the required condition is satisfied, so the result is `True`.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

Follow-up:
- None specified.
"""
