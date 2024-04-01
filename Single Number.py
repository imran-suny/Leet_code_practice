https://leetcode.com/problems/single-number/description/
Input: nums = [2,2,1]
Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
