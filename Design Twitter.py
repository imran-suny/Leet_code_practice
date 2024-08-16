
class Twitter:
    def __init__(self):  
        self.count = 0                      # Initialize a global counter to track tweet timestamps
        self.tweetMap = defaultdict(list)   # Initialize tweetMap to store user tweets: userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)   # Initialize followMap to store user relationships: userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)           #  Ensure that the user follows themselves
        for followeeId in self.followMap[userId]:   
            if followeeId in self.tweetMap:         # Check if the followee has any tweets
                index = len(self.tweetMap[followeeId]) - 1   # most recent tweet/ located at last index of tweet list
                count, tweetId = self.tweetMap[followeeId][index]    # more recent tweets have higher count values
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])   # index-1: next tweet to look at from this followee

        # Retrieve the 10 most recent tweets from the min heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # If the followee has more tweets, push the next tweet onto the min heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


User 1 follows User 2 and User 3.
Tweet data:
User 1's tweets: [(3, 101), (2, 3), (1, 5)]
User 2's tweets: [(4, 201), (3, 102)]
User 3's tweets: [(5, 301), (2, 6)]

minHeap initially contains:
[(3, 101, 1, 1)] from User 1   (index-1 = 2-1=2 , index -1 =2-1=1)
[(4, 201, 2, 0)] from User 2
[(5, 301, 3, 0)] from User 3
Iteration 1:
Pop the smallest element: [3, 101, 1, 1] from User 1....Add 101 to res.
Push the next tweet from User 1: [2, 3, 1, 0].
Iteration 2: Pop the smallest element: [2, 3, 1, 0] from User 1.
Add 3 to res. Push the next tweet from User 1: [1, 5, 1, -1].
Iteration 3: Pop the smallest element: [1, 5, 1, -1] from User 1.
Add 5 to res. No more tweets from User 1 to push.

Iteration 4:
Pop the smallest element: [4, 201, 2, 0] from User 2.
Add 201 to res.
Push the next tweet from User 2: [3, 102, 2, -1].
Iteration 5:
Pop the smallest element: [3, 102, 2, -1] from User 2.
Add 102 to res.
No more tweets from User 2 to push.
Iteration 6:
Pop the smallest element: [5, 301, 3, 0] from User 3.
Add 301 to res.
Push the next tweet from User 3: [2, 6, 3, -1].
Iteration 7:
Pop the smallest element: [2, 6, 3, -1] from User 3.
Add 6 to res.
No more tweets from User 3 to push.
Final res List:
The res list will contain the 10 most recent tweet IDs (or fewer if there aren't 10 tweets), ensuring they are displayed in the correct order of recency.
In this example, the res list would be [301, 201, 102, 101, 3, 6, 5]
