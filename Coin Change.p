https://leetcode.com/problems/coin-change/description/
https://leetcode.com/problems/coin-change/solutions/4772173/101-1-approach-1-o-n-m-python-c-step-by-step-explanation/
Input: coins = [1, 2, 3, 4] , amount = 7
Output: 2
Explanation: 7 = 3+7

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #   [8, 8, 8, 8, 8, 8, 8, 8]  # dp[0] nisi ei jonno 8 ta 
        dp[0] = 0                        #   Base case: Zero coins are required to make the amount 0
                                         # Iterate through each amount from 1 to 'amount'
        for a in range(1, amount + 1):   # dp[0]=0 so 1 theke start 
            for c in coins:
                                         # Check if the current coin denomination 'c' can contribute to making up the current amount 'a'
                if a - c >= 0:           # amount -coin =1-1=0
                                        # Update 'dp[a]' to the minimum of its current value and '1 + dp[a - c]'
                    dp[a] = min(dp[a], 1 + dp[a - c])  #dp[1]= min (8, 1+0 )= 1,  a=2, c=1 >dp[2]= min(8, 1+1)= d[2]=2, a=2, c=2 >dp[2]= min(2, 1+0)=1 
                                                      # a=3,c=1 dp[3]=min(8,1+2)= 3--> c=3 dp[3]=1 
                                      # a= 4 , dp[4]=1, a=5, min(8, 1+dp[4])= 2,   dp[6] = 1+ dp[5]= 3  dp[7]= min(8, 1+dp[6])= 4, min(4, 1+dp[5])=3 
                                      #dp[7]= min (3, 1+dp[4])= 2 
        return dp[amount] if dp[amount] != amount + 1 else -1  

