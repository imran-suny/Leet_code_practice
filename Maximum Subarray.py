https://leetcode.com/problems/maximum-subarray/description/
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')  
        cur = float('-inf')  

        # Iterate through each element in the array
        for n in nums:
            # Update cur to be the maximum of either cur + n or n
            cur = max(cur + n, n)
            # Update ans to be the maximum of ans and cur
            ans = max(ans, cur)
            
        return ans  # Return the maximum sum subarray
        
