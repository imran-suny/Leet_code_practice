Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []                # List to store the maximum values for each sliding window
        q = collections.deque()  # Deque to store indices of elements in the current window
        left = right = 0         # Pointers for the sliding window

        while right < len(nums):
            # Pop smaller values from the back of the deque
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # Remove the leftmost value if it's outside the current window
            if left > q[0]:
                q.popleft()

            # If the window size is reached, append the maximum value to the result
            if (right + 1) >= k:
                ans.append(nums[q[0]])
                left += 1
            right += 1

        return ans
        
Initialization:
output = []
r = 0:
nums[0] = 1
q = deque([0])

r = 1:
nums[1] = 3
q = deque([1]) (after popping index 0)

r = 2:
nums[2] = -1
q = deque([1, 2])
Window size is 3, append nums[1] = 3 to output.
output = [3]
l = 1

r = 3:
nums[3] = -3
q = deque([1, 2, 3])
Remove index 1 (out of bounds for window size 3)
Window size is 3, append nums[1] = 3 to output.
output = [3, 3]
l = 2

r = 4:
nums[4] = 5
q = deque([4]) (after popping indices 3, 2, and 1)
Window size is 3, append nums[4] = 5 to output.
output = [3, 3, 5]
l = 3

r = 5:
nums[5] = 3
q = deque([4, 5])
Window size is 3, append nums[4] = 5 to output.
output = [3, 3, 5, 5]
l = 4

r = 6:
nums[6] = 6
q = deque([6]) (after popping indices 5 and 4)
Window size is 3, append nums[6] = 6 to output.
output = [3, 3, 5, 5, 6]
l = 5

r = 7:
nums[7] = 7
q = deque([7]) (after popping index 6)
Window size is 3, append nums[7] = 7 to output.
output = [3, 3, 5, 5, 6, 7]
l = 6
