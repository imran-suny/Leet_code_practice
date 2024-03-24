https://leetcode.com/problems/longest-increasing-subsequence/solutions/4775787/104-1-approach-1-o-n-2-python-c-step-by-step-explanation/
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)                          # [1,1,1,1,1,1,1,1]

        for i in range(len(nums) - 1, -1, -1):         # 7,6,5
            for j in range(i + 1, len(nums)):          # 101, 18
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])   # list[5] = 2 
        return max(LIS) 

