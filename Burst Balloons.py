Input: nums = [3,1,5,8]  Output: 167 O(n^3)
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
class Solution:
    def maxCoins(self, nums: List[int]) -> int:   
        nums = [1] + nums + [1]              # Add dummy balloons with value 1 at the beginning and end of the `nums` array
        memory = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memory:
                return memory[(l, r)]
            
            # Initialize maximum coins within the range [l, r]
            memory[(l, r)] = 0
            # Iterate over all possible choices of bursting balloons within the range [l, r]
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]  # if nums[i] pops last
                coins += dfs(l, i - 1) + dfs(i + 1, r)        # left and right sub array 
                # Update maximum coins for the current range [l, r]
                memory[(l, r)] = max(memory[(l, r)], coins)
            
            return memory[(l, r)]
        return dfs(1, len(nums) - 2)     # nums = [1] + nums + [1]  , len(nums) - 1 gives last value, so -2 gives nums
