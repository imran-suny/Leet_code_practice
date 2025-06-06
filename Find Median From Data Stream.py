class MedianFinder:
    def __init__(self):
        # two heaps: small to store the smaller half as a max heap # large to store the larger half as a min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If large heap is not empty and the number >  smallest number in large heap,
        # push it to the large heap. Otherwise, push the negation of the number to the small heap.
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)            # large a min heap  
        else:
            heapq.heappush(self.small, -1 * num)       # max heap at left side 

        # Balance the heaps by adjusting their sizes if necessary
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
       # If sizes of both heaps are equal, return the average of the maximum element in the small heap and the minimum element in the large heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

import heapq
max_heap = []
heapq.heapify(max_heap)
elements = [4, 2, 7, 1, 9, 5]
for elem in elements:
    heapq.heappush(max_heap, -elem)
    print(max_heap)
while max_heap:
    max_elem = -heapq.heappop(max_heap)
    print(max_elem)
[-4]
[-4, -2]
[-7, -2, -4]
[-7, -2, -4, -1]
[-9, -7, -4, -1, -2]
[-9, -7, -5, -1, -2, -4]
max_heap
9
7
5
4
2
1
A min-heap is often implemented using an array, where for a node at index i,
the left child is at 2*i + 1, the right child is at 2*i + 2, and the parent is at (i - 1) // 2
min_heap = []
heapq.heapify(min_heap)
# Adding elements to the min heap
elements = [4, 2, 7, 1, 9, 5]
for elem in elements:
    heapq.heappush(min_heap, elem)
    print(min_heap)
while min_heap:
    min_elem = heapq.heappop(min_heap)
    print(min_elem)
[4]
[2, 4]
[2, 4, 7]
[1, 2, 7, 4]
[1, 2, 7, 4, 9]
[1, 2, 5, 4, 9, 7]
1
2
4
5
7
9    
