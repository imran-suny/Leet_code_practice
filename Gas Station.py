Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2] nOutput: 3
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3. Therefore, return 3 as the starting index.
https://leetcode.com/problems/gas-station/solutions/4871928/120-1-approach-1-o-n-python-c-step-by-step-explanation/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        # Check if the total gas available is less than the total cost of traveling
        if sum(gas) < sum(cost):
            return -1
        
        total = 0  # Initialize the net gas difference
        res = 0    # Initialize the starting index
        
        # Iterate through the gas stations
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            # If the net gas difference becomes negative, reset to zero and update the starting index
            if total < 0:
                total = 0
                res = i + 1   
        return res
      
