
class Twitter:
    def __init__(self):  
        self.count = 0                      # Initialize a global counter to track tweet timestamps
        self.tweetMap = defaultdict(list)   # Initialize tweetMap to store user tweets: userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)   # Initialize followMap to store user relationships: userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet with its timestamp to the user's tweetMap
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement the count to simulate decreasing timestamps for newer tweets
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Ensure that the user follows themselves
        self.followMap[userId].add(userId)
        
        # Iterate over users followed by the given userId
        for followeeId in self.followMap[userId]:
            # Check if the followee has any tweets
            if followeeId in self.tweetMap:
                # Get the index of the most recent tweet from the followee
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]    
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])    # Push the tweet onto the min heap along with additional information

        # Retrieve the 10 most recent tweets from the min heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # Append the tweetId to the result list
            res.append(tweetId)
            # If the followee has more tweets, push the next tweet onto the min heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        # Return the result list containing the 10 most recent tweets
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followeeId to the set of users followed by the followerId
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followeeId from the set of users followed by the followerId
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
Iteration 2:
Pop the smallest element: [2, 3, 1, 0] from User 1.
Add 3 to res.
Push the next tweet from User 1: [1, 5, 1, -1].
Iteration 3:
Pop the smallest element: [1, 5, 1, -1] from User 1.
Add 5 to res.
No more tweets from User 1 to push.
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
