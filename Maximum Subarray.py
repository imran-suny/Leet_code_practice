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

