https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0                              # Initialize variables to track maximum values obtained from robbing

        # Iterate through the array of house values
        for n in nums:
                                                      # Calculate the maximum value obtained from robbing the current house or not robbing it
            temp = max(n + rob1, rob2)
            rob1 = rob2                               # Update variables for the next iteration
            rob2 = temp
            
        # Return the maximum value obtained without alerting the police
        return rob2
