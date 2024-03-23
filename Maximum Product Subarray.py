https://leetcode.com/problems/maximum-product-subarray/solutions/4772375/102-1-approach-1-o-n-python-c-step-by-step-explanation/
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
  
        res = nums[0]                                 # Initialize the result with the first element of the array
        curMin, curMax = 1, 1                         # Initialize current minimum and maximum product to 1

        for n in nums:
            tmp = curMax * n                          # Calculate the temporary maximum product considering the current maximum product
            curMax = max(n * curMax, n * curMin, n)   # curMax: max (2,2,2) =2,  n=3 max(6, 6, 3) = 6   n= -2 max (-12, -6, -2)
            curMin = min(tmp, n * curMin, n)          # curMin: min (2,2,2) =2,  n=3 max(6, 6, 3)= 3    n= -2 min (-12, -6, -2)  -- -2  
            res = max(res, curMax)                    #2, 6
        return res
