https://leetcode.com/problems/longest-increasing-subsequence/solutions/4775787/104-1-approach-1-o-n-2-python-c-step-by-step-explanation/
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)                          # [1,1,1,1,1,1,1,1]

        for i in range(len(nums) - 1, -1, -1):         # i = 7, j =8 out of bound...
            for j in range(i + 1, len(nums)):          # i=6, j =7 num [6] = 101, num[7]= 18 false if condition
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])   # list[5] = 2 
        return max(LIS) 

