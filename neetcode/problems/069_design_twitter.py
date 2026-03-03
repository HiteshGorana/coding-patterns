"""
Problem:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed. Implement the Twitter class: - Twitter() Initializes your twitter object. - void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId. - List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent. - void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId. - void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Examples:

Example 1:
Input: TBD
Output: TBD
Explanation: This is the expected result for the given input.

Example 2:
Input: TBD
Output: TBD
Explanation: Add another valid example to practice edge cases.

Example 3:
Input: TBD
Output: TBD
Explanation: Add another valid example to practice edge cases.

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
- A user cannot follow himself.

Follow-up:
- None specified.
"""
