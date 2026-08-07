class Twitter:

    def __init__(self):
        self.user_following = defaultdict(set)
        # 1: [2,3,4,5]
        self.user_tweets = defaultdict(list)
        # 5: [(2, 25), (3, 941), (9, 231)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        relevant_users = set(self.user_following[userId])
        relevant_users.add(userId)
        
        for u in relevant_users:
            for time, tweetId in self.user_tweets[u]:
                heapq.heappush(minHeap, (time, tweetId))

                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        return [tweetId for time, tweetId in sorted(minHeap, reverse=True)]
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
        
