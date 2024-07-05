Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:                  # loop hole false 
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2    # 19%10 = 9 ^2   # 1 %10 = 1 --> 1^2 + 9^2 
            n = n // 10    19//10= 1                #  1//10 = 0 
        return output
