https://leetcode.com/problems/climbing-stairs/solutions/4752945/94-1-approach-1-o-n-python-c-step-by-step-explanation/
memoization:
def climbStairs(n):
    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return 1
        if i < 0:
            return 0
        memo[i] = helper(i - 1) + helper(i - 2)
        return memo[i]

    return helper(n)
# Example usage:
n = 3
print(climbStairs(n))  # Output should be 8

DP: 
class Solution:
    def climbStairs(self, n: int) -> int:
       
        if n <= 3:                      # Base cases: If n is 1, 2, or 3, return n directly as there are no steps to climb or only one way to climb them.
            return n
                                        # We set n1 to 2 and n2 to 3 because these are the number of distinct ways to reach the first and second steps, respectively.
        n1, n2 = 2, 3

        # Iterate from the third step up to the nth step
        for i in range(4, n + 1):
                                         # Calculate the number of ways to reach the current step by adding the number of ways to reach the (i-1)th step and the (i-2)th step.
            temp = n1 + n2
                                         # Update n1 and n2 to represent the number of ways to reach the (i-1)th and ith steps, respectively.
            n1 = n2     # 3
            n2 = temp   # 5
        return n2
