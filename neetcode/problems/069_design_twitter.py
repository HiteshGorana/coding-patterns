"""
69. Design Twitter
Difficulty: Medium

Topics:
- TBD

Companies:
- TBD

Hint:
- TBD

Problem:
Design a simplified Twitter with postTweet, getNewsFeed, follow, and unfollow.

What This Problem Is Asking:
- Given: operations.
- Task: Design a simplified Twitter with postTweet, getNewsFeed, follow, and unfollow.
- Return: a list/array in the required format.

Example 1:

Input: operations = ["Twitter", "postTweet(1,5)", "getNewsFeed(1)", "follow(1,2)", "postTweet(2,6)", "getNewsFeed(1)", "unfollow(1,2)", "getNewsFeed(1)"]
Output: [null, null, [5], null, null, [6,5], null, [5]]
Explanation: Each entry is the return value for each operation in order (`null` for constructors/void operations).

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
- A user cannot follow himself.
Follow-up:
- None specified.
"""
