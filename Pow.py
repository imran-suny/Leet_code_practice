Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Input: x = 2.00000, n = 10
Output: 1024.00000

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res   # helper(4, 0), n == 0, return 1. Going back helper(2, 1), res = 1. Since n % 2 = 1%2=1, return x * res, which is 2 * 1 = 2.

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
