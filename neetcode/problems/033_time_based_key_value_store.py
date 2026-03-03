"""
33. Time Based Key-Value Store
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a time-based key-value store that can set and get values by key and timestamp, returning the latest value at or before the query timestamp.

Easy Explanation:
- Given: operations.
- Task: Design a time-based key-value store that can set and get values by key and timestamp, returning the latest value at or before the query timestamp.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["TimeMap", "set("foo","bar",1)", "get("foo",1)", "get("foo",3)", "set("foo","bar2",4)", "get("foo",4)", "get("foo",5)"]

How to Read the Input:
- `operations` = ["TimeMap", "set("foo","bar",1)", "get("foo",1)", "get("foo",3)", "set("foo","bar2",4)", "get("foo",4)", "get("foo",5)"] (list of strings/values)

Output (Example 1):
[null, null, "bar", "bar", null, "bar2", "bar2"]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["TimeMap", "set("foo","bar",1)", "get("foo",1)", "get("foo",3)", "set("foo","bar2",4)", "get("foo",4)", "get("foo",5)"].
2. Apply the rule in the problem statement: Design a time-based key-value store that can set and get values by key and timestamp, returning the latest value at or before the query timestamp.
3. For this example, the correct result is [null, null, "bar", "bar", null, "bar2", "bar2"].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits.
- 1 <= timestamp <= 10^7
- All the timestamps timestamp of set are strictly increasing.
- At most 2 * 10^5 calls will be made to set and get.

Follow-up:
- None specified.
"""
