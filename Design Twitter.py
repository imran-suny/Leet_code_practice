
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
