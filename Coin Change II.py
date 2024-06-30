https://leetcode.com/problems/coin-change-ii/solutions/4787842/111-2-approach-2-dynamic-programming-o-m-n-python-c-step-by-step-explanation/
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # MEMOIZATION  # Time: O(n*m)  # Memory: O(n*m)
        cache = {}
        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)

        # DYNAMIC PROGRAMMING # Time: O(n*m)  # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)               # [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):  #2,1,0
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:                #  if current coin denomination can contribute to the amount a
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
Final DP Table:
[1, 1, 1, 1]
[1, 0, 0, 0]  # dp[1][2]= dp[1][3] =0    dp[a][i] = dp[a][i + 1]  ### 1 er jonno,,,  dp[a][i] += dp[a - coins[i]][i]    dp[1-1][i],, dp[0][0]
[2, 1, 0, 0]
[2, 0, 0, 0]
[3, 1, 0, 0]
[4, 1, 1, 0]
