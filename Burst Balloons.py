Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
class Solution:
    def maxCoins(self, nums: List[int]) -> int:   
        nums = [1] + nums + [1]              # Add dummy balloons with value 1 at the beginning and end of the `nums` array
        memory = {}

        # Define a recursive function `dfs` to compute maximum coins within a range [l, r]
        def dfs(l, r):
            # Base case: If l > r, return 0
            if l > r:
                return 0
            if (l, r) in memory:
                return memory[(l, r)]
            
            # Initialize maximum coins within the range [l, r]
            memory[(l, r)] = 0
            # Iterate over all possible choices of bursting balloons within the range [l, r]
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                # Update maximum coins for the current range [l, r]
                memory[(l, r)] = max(memory[(l, r)], coins)
            
            return memory[(l, r)]
        
        # Call the dfs function with the initial range [1, len(nums) - 2]
        return dfs(1, len(nums) - 2)
