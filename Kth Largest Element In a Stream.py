class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize min-heap with the first k elements
        self.minHeap = nums, 
        self.k = k
        heapq.heapify(self.minHeap)
        # Keep only the k largest elements
        while len(self.minHeap) > k:               # pop korte thakbo
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap, val)          # Add new element to the min-heap
        if len(self.minHeap) > self.k:             # If heap size exceeds k, remove the smallest element
            heapq.heappop(self.minHeap)
        return self.minHeap[0]                      # Return the current kth largest element
