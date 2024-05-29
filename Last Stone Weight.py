class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stone weights to negative values
        stones = [-s for s in stones]
        # Create a min-heap
        heapq.heapify(stones)

        # Smash stones until only one stone remains
        while len(stones) > 1:
            # Remove the two heaviest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # If weights are not equal, subtract smaller from larger and push the result
            if second > first:
                heapq.heappush(stones, first - second)

        # Append 0 to handle the case when there is only one stone left
        stones.append(0)
        # Return the absolute value of the last stone weight
        return abs(stones[0])
