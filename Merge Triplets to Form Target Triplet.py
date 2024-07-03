Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()  # Initialize a set to store indices of matching elements
        
        # Iterate through each triplet
        for t in triplets:
            # If any element of the triplet is greater than the corresponding element of the target triplet, skip
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # Check if any element of the triplet matches the corresponding element of the target triplet
            for i, v in enumerate(t):
                if v == target[i]:
                    ans.add(i)  # Add the index of the matching element to the set
        
        # Check if all three indices are present in the set
        return len(ans) == 3
