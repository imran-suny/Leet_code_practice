
class Twitter:
    def __init__(self):  
        self.count = 0                      # track tweet timestamps
        self.tweetMap = defaultdict(list)   # store user tweets: userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)   # k kake follow korse : userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None: k kkn ki post korse 
        self.tweetMap[userId].append([self.count, tweetId])  #[[0, 101], [-1, 102]]
        self.count -= 1
# User 1's tweets: [(3, 101), (2, 3), (1, 5)] 2's tweets: [(4, 201), (3, 102)] 3's tweets: [(5, 301), (2, 6)]
    def getNewsFeed(self, userId: int) -> List[int]: 
        res = []
        minHeap = []
        self.followMap[userId].add(userId)           #  Ensure that the user follows themselves
        for followeeId in self.followMap[userId]:   
            if followeeId in self.tweetMap:         # Check if the followee has any tweets
                index = len(self.tweetMap[followeeId]) - 1   # most recent tweet/ located at last index of tweet list
                count, tweetId = self.tweetMap[followeeId][index]    # more recent tweets have higher count values
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])   # index-1: next tweet to look at from this followee
                # minHeap = [[3, 101, 1, 1], [4, 201, 2, 0], [5, 301, 3, 0]]
        # Retrieve the 10 most recent tweets from the min heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)  #[5, 301, 3, 0]
            res.append(tweetId)
            # If the followee has more tweets, push the next tweet onto the min heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]  # next tweet from User 3 is (2, 6)-- [2, 6, 3, -1])
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) #minHeap = [[3, 101, 1, 1], [4, 201, 2, 0], [2, 6, 3, -1]]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

Second pop:

The most recent tweet is (4, 201) from User 2.
heapq.heappop(minHeap) pops [4, 201, 2, 0].
res = [301, 201] (Tweet ID 201 is added to the news feed).
The next tweet from User 2 is (3, 102) (Tweet ID 102 at time 3), so push that into the heap: heapq.heappush(minHeap, [3, 102, 2, -1]).
Now, minHeap = [[3, 101, 1, 1], [3, 102, 2, -1], [2, 6, 3, -1]].
Third pop:

The most recent tweet is (3, 101) from User 1.
heapq.heappop(minHeap) pops [3, 101, 1, 1].
res = [301, 201, 101] (Tweet ID 101 is added to the news feed).
The next tweet from User 1 is (2, 3) (Tweet ID 3 at time 2), so push that into the heap: heapq.heappush(minHeap, [2, 3, 1, 0]).
Now, minHeap = [[3, 102, 2, -1], [2, 6, 3, -1], [2, 3, 1, 0]].
Fourth pop:

The most recent tweet is (3, 102) from User 2.
heapq.heappop(minHeap) pops [3, 102, 2, -1].
res = [301, 201, 101, 102] (Tweet ID 102 is added to the news feed).
Now, minHeap = [[2, 6, 3, -1], [2, 3, 1, 0]].
Fifth pop:

The most recent tweet is (2, 6) from User 3.
heapq.heappop(minHeap) pops [2, 6, 3, -1].
res = [301, 201, 101, 102, 6] (Tweet ID 6 is added to the news feed).
Now, minHeap = [[2, 3, 1, 0]].
Sixth pop:

The most recent tweet is (2, 3) from User 1.
heapq.heappop(minHeap) pops [2, 3, 1, 0].
res = [301, 201, 101, 102, 6, 3] (Tweet ID 3 is added to the news feed).
The next tweet from User 1 is (1, 5) (Tweet ID 5 at time 1), so push that into the heap: heapq.heappush(minHeap, [1, 5, 1, -1]).
Now, minHeap = [[1, 5, 1, -1]].
Continue Until 10 Tweets:

The loop continues until res contains 10 tweets, or there are no more tweets left to pop from the heap.
