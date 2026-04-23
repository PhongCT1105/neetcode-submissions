import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)  # userId -> set of followeeIds
        self.tweetMap = defaultdict(list)  # userId -> list of (time, tweetId)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # Include user's own tweets
        followees = self.followMap[userId].copy()
        followees.add(userId)  # User should see their own tweets
        
        # Use a max-heap (negative time for max-heap behavior)
        heap = []
        
        # For each followee, get their most recent tweet
        for followeeId in followees:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                tweets = self.tweetMap[followeeId]
                time, tweetId = tweets[-1]  # Most recent tweet
                heapq.heappush(heap, (-time, tweetId, followeeId, len(tweets) - 1))
        
        # Get top 10 tweets
        result = []
        while heap and len(result) < 10:
            neg_time, tweetId, followeeId, index = heapq.heappop(heap)
            result.append(tweetId)
            
            # If there are more tweets from this user, add the next one
            if index > 0:
                next_time, next_tweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush(heap, (-next_time, next_tweetId, followeeId, index - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)