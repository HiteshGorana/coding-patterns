"""
88. Course Schedule II
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Return one valid ordering of courses to finish all courses given prerequisite pairs.

Easy Explanation:
- Given: numCourses, prerequisites.
- Task: Return one valid ordering of courses to finish all courses given prerequisite pairs.
- Return: a list/array in the required format.

Input (Example 1):
numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]

How to Read the Input:
- `numCourses` = 4 (integer)
- `prerequisites` = [[1,0],[2,0],[3,1],[3,2]] (2D list (matrix))

Output (Example 1):
[0,1,2,3]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]].
2. Apply the rule in the problem statement: Return one valid ordering of courses to finish all courses given prerequisite pairs.
3. For this example, the correct result is [0,1,2,3].
4. This output matches the required format and the rule defined in the prompt.

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
