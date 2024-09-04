Input: nums = [1,1,1,1,1], target = 3
Output: 5
https://leetcode.com/problems/target-sum/solutions/4776428/107-1-approach-1-o-2-n-python-c-step-by-step-explanation/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways
        
        def backtrack(i, total):
            # If we have processed all elements in nums check if the total equals the target.
            if i == len(nums):
                return 1 if total == target else 0
        
            if (i, total) in dp:
                return dp[(i, total)]
            
            # Recursively explore two possibilities:
            # 1. Add nums[i] to the total and move to the next index.
            # 2. Subtract nums[i] from the total and move to the next index.
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]
        
        # Start the backtracking process from the beginning of the array
        # with an initial total of 0.
        return backtrack(0, 0)
