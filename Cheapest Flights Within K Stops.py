https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/4746492/91-1-approach-1-bellman-ford-algorithm-o-n-k-python-c-step-by-step-explanation/
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
Bellman-Ford algorithm
class Solution:
    def findCheapestPrice( self, n: int, flights: List[List[int]], src: int, dst: int, k: int ) -> int:
        prices = [float("inf")] * n                     # Initialize an array to store the minimum prices to reach each city     
        prices[src] = 0                                 # Set the price to reach the source city to 0
    
        for i in range(k + 1):                          # Iterate through k + 1 iterations to consider up to k stops
            tmpPrices = prices.copy()                   # Create a copy of the current prices array
            # Iterate through each flight
            for s, d, p in flights:                     # s=source, d=destination, p=price
                if prices[s] == float("inf"):           # Check if there's a flight from the source city and the price to reach it is not infinity
                    continue
                
                if prices[s] + p < tmpPrices[d]:        # Update the temporary prices array if the new price is cheaper
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices                         # Update the prices array with the values from the temporary prices array 
                                                       # If the price to reach the destination city is still infinity, return -1; otherwise, return the price
        return -1 if prices[dst] == float("inf") else prices[dst]
