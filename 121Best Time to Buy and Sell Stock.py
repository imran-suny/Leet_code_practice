https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/
https://takeuforward.org/data-structure/stock-buy-and-sell-dp-35/

Input: prices = [7,1,5,3,6,4]
Output: 5
## 2 pointer solution 
class Solution:
    def maxProfit(self,prices):
        left = 0                     #Buy #left pointer first one or buy
        right = 1                    #Sell # 2nd or sell 
        max_profit = 0               # of course we need to calculate maximum profit
        while right < len(prices):   # 5<6 right array lenngth theke 1 kom hobe
            currentProfit = prices[right] - prices[left]   # current Profit buy-sell,,, arr[l-r]
            if prices[left] < prices[right]:               #if selling price is greater than buying price
                max_profit =max(currentProfit,max_profit)  #
            else:
                left = right                               # 7,1 = -6// so left ke update left = right and right += 1 ke always update korbo 
            right += 1
        return max_profit

  
