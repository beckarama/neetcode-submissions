class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.follow_map[userId].add(userId)
        for follower in self.follow_map[userId]:
            if follower in self.tweet_map:
                index = len(self.tweet_map[follower]) - 1
                count, tweetId = self.tweet_map[follower][index]

                heapq.heappush(maxHeap, [count, tweetId, follower, index - 1])
        
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, next_index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if next_index >= 0:
                count, tweetId = self.tweet_map[followeeId][next_index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, next_index - 1])
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
