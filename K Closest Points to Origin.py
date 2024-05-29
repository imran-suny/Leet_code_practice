https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
                                            # Calculate distances and store them along with point coordinates
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append((distance, x, y))
        
                                            # Heapify the list to create a min-heap
        heapq.heapify(minHeap)
        
                                            # Extract K smallest distances and return their corresponding points
        res = []
        for _ in range(k):
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res
