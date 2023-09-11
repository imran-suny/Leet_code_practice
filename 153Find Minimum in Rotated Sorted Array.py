Input: nums = [3,4,5,1,2]
Output: 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2   # 
            if nums[m] > nums[r]:  # 5>2, 
                l = m + 1     #  l= 2+1=3
            else:
                r = m   # right pointer chnage to mid 
        return nums[l]
