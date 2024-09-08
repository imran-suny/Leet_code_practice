https://leetcode.com/problems/number-of-1-bits/description/
Input: n = 2147483645

Output: 30

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:               # n !< =0 
            n &= n - 1         # n= n & (n-1)             for n=1000001, n-1 = 1000000       n & (n-1) = 1000000  &   0111111     n = 0   
            res += 1
        return res

Shifting by 1 
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:               # n !< =0 
            res = res+ n%2         # 1011 % 2 = 1, 101% 2 = 1 , 10%2 =0 1% 2 = 1 , so total 3 1 
            n = n >> 1   # vagsesh and right shift mane right theke ekta bad
        return res
