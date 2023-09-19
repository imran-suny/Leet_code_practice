https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/
https://takeuforward.org/data-structure/stock-buy-and-sell-dp-35/

Input: prices = [7,1,5,3,6,4]
Output: 5
Bruteforce:
# Calculate the difference between the prices for each pair, and keep track of the maximum difference (profit)
def max_profit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit
	

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
            right += 1    # move left pointer to the right position and increment our right pointer by 1. We always want our left point to be minimum.
        return max_profit
        
1. Initialize  ‘maxProfit’ to 0 and declare  variable ‘mini’ which we will use to keep track of the buying price (minimum price from day 0 to day i) for selling the stock.
2. Traverse the array from index 1 to n-1. We started at index 1 because buying and selling the stock on the 0th day will give us a profit of 0
3. In each iteration, try to find the curProfit. The selling price will be Arr[i] and ‘mini’ will give us the buying price. We calculate the curProfit.
4. Before going to the next iteration, we check if the current price (Arr[i]) is less than the mini value, and we assign it as the new mini value.

int maximumProfit(vector<int> &Arr){
	int maxProfit = 0;
	int mini = Arr[0]; # 
	for(int i=1;i<Arr.size();i++){
        int curProfit = Arr[i] - mini; # profit right-left 
        maxProfit = max(maxProfit,curProfit);
        mini = min(mini,Arr[i]); # select minimum one 
        }
	return maxProfit;
}
int main() {
  vector<int> Arr  ={7,1,5,3,6,4};
  cout<<"The maximum profit by selling the stock is "<<maximumProfit(Arr);
}

  
