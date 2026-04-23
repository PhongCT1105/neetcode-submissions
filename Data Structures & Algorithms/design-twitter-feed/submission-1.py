class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.followee = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_followee = self.followee[userId].copy()
        all_followee.add(userId)
        import heapq
        heap = []
        for followee in all_followee:
            posts = self.tweet[followee]
            for post in posts:
                if len(heap) < 10:
                    heapq.heappush(heap, post)
                else:
                    heapq.heappushpop(heap, post)
        heap.sort(reverse = True)
        return [tweetId for time, tweetId in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].remove(followeeId)
