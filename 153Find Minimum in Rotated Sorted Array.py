Input: nums = [3,4,5,1,2]
Output: 1

# Divide left and right sorted part/// and select a mid pointer also

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2   # 
            if nums[m] > nums[r]:  # 5>2, 
                l = m + 1     #  l= 2+1=3
            else:
                r = m   # right pointer change to mid if nums[m] < nums[r] or nums[m] < nums[l]
        return nums[l]
