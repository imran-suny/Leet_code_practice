https://leetcode.com/problems/sum-of-two-integers/solutions/4927043/blind-75-beats-100-00-11-75/
Input: a = 2, b = 3
Output: 5
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a
