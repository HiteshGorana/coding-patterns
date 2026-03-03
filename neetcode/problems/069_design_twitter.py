"""
69. Design Twitter
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem Statement:
Design a simplified Twitter with postTweet, getNewsFeed, follow, and unfollow.

Easy Explanation:
- Given: operations.
- Task: Design a simplified Twitter with postTweet, getNewsFeed, follow, and unfollow.
- Return: a list/array in the required format.

Input (Example 1):
operations = ["Twitter", "postTweet(1,5)", "getNewsFeed(1)", "follow(1,2)", "postTweet(2,6)", "getNewsFeed(1)", "unfollow(1,2)", "getNewsFeed(1)"]

How to Read the Input:
- `operations` = ["Twitter", "postTweet(1,5)", "getNewsFeed(1)", "follow(1,2)", "postTweet(2,6)", "getNewsFeed(1)", "unfollow(1,2)", "getNewsFeed(1)"] (list of strings/values)

Output (Example 1):
[null, null, [5], null, null, [6,5], null, [5]]

How to Read the Output:
- The returned value should be a list/array.
- The order and structure should match the problem requirement.

Example 1 Walkthrough:
1. Start with the given input: operations = ["Twitter", "postTweet(1,5)", "getNewsFeed(1)", "follow(1,2)", "postTweet(2,6)", "getNewsFeed(1)", "unfollow(1,2)", "getNewsFeed(1)"].
2. Apply the rule in the problem statement: Design a simplified Twitter with postTweet, getNewsFeed, follow, and unfollow.
3. For this example, the correct result is [null, null, [5], null, null, [6,5], null, [5]].
4. Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
- A user cannot follow himself.

Follow-up:
- None specified.
"""
