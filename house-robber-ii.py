https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Return the maximum of three scenarios:
        # 1. Robbing the first house and skipping the last house.
        # 2. Robbing the last house and skipping the first house.
        # if only one [1], hence num[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        rob1, rob2 = 0, 0  
        
        # Iterate through the house values
        for n in nums:
            # Calculate the new maximum amount considering two scenarios:
            # 1. Robbing the current house and the amount obtained from robbing two houses ago.
            # 2. Not robbing the current house and maintaining the previous maximum.
            newRob = max(rob1 + n, rob2)
            rob1 = rob2  
            rob2 = newRob  
        return rob2  
