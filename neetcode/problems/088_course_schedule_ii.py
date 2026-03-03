"""
88. Course Schedule II
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Return one valid ordering of courses to finish all courses given prerequisite pairs.

What This Problem Is Asking:
- Given: numCourses, prerequisites.
- Task: Return one valid ordering of courses to finish all courses given prerequisite pairs.
- Return: a list/array in the required format.

Example 1:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]
Explanation: This list is the correct result produced from the given input according to the problem rules.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct.
Follow-up:
- None specified.
"""
