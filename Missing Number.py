https://leetcode.com/problems/missing-number/solutions/4754401/beats-98-users-4-approaches-c-java-python-javascript-explained/
https://leetcode.com/problems/missing-number/
Input: nums = [3,0,1]
Output: 2


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i           # 0^1^2^3 exclusive Xor with 0, keep the same number 
        for num in nums:       # 3,0,1 
            ans ^= num         # ans  ans^= num---> 0^1^2^3 exclusive Xor with 3,0,1 ....finds the missing number
        return ans

