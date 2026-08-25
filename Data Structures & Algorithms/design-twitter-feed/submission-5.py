class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                time, tweetId = self.tweet_map[followeeId][index]

                heapq.heappush(max_heap, [time, tweetId, followeeId, index - 1])
        
        while max_heap and len(res) < 10:
            time, tweetId, followeeId, next_index = heapq.heappop(max_heap)
            res.append(tweetId)

            if next_index >= 0:
                time, tweetId = self.tweet_map[followeeId][next_index]
                heapq.heappush(max_heap, [time, tweetId, followeeId, next_index - 1])
        return res    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
        