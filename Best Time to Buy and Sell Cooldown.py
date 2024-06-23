https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}  # Dictionary to store memoization results

        def dfs(i, buying):
            if i >= len(prices): # Base case: if we have reached the end of prices list
                return 0
            if (i, buying) in memory:                    # If the result for the current state is already memoized, return it
                return memory[(i, buying)]

            # Explore the cooldown state
            cooldown = dfs(i + 1, buying)
            
            if buying:
                     # If in buying state, two options: # 1. Buy the stock and move to the next day in selling state # 2. Skip buying and remain in buying state (cooldown)
                buy = dfs(i + 1, not buying) - prices[i]                 
                memory[(i, buying)] = max(buy, cooldown)    # Select the option that maximizes profit
            else:
                     # If in selling state, we have two options: # 1. Sell the stock and skip the cooldown day # 2. Skip selling and move to the next day in cooldown state
                sell = dfs(i + 2, not buying) + prices[i]
                memory[(i, buying)] = max(sell, cooldown)
            return memory[(i, buying)]   # Return the maximum profit achievable for the current state

        return dfs(0, True)
