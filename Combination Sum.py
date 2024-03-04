https://leetcode.com/problems/combination-sum/description/
https://leetcode.com/problems/combination-sum/solutions/4716412/71-1-approach-1-o-2-n-python-c-step-by-step-explanation/

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):                            
            if total == target:                # # If total sum == the target, we've found a valid combination
                result.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:  # if index is out of bounds or total sum exceeds the target, stop exploring this path
                return
            
            curr.append(candidates[i])               #  Include the current candidate in the combination
            # Explore further combinations with the current candidate
            dfs(i, curr, total + candidates[i]) # dfs(0, [2], 2), dfs(0, [2, 2], 4), dfs(0, [2, 2, 2], 6), dfs(0, [2, 2, 2, 2], 8)... backtrack
            # Backtrack: remove the last candidate to explore combinations without it
            curr.pop()  # dfs(0, [2, 2, 2], 6) theke 2 remove korar pore abar dfs as it is inside-->  
            # Explore combinations without the current candidate
            dfs(i + 1, curr, total) # dfs(1, [2, 2, 2], 6), dfs(1, [2, 2, 2, 3], 9),  dfs(2, [2, 2, 2, 6], 10),  dfs(3, [2, 2, 2, 7], 13)
        
        dfs(0, [], 0)     # Start DFS traversal from index 0 with an empty current combination and total sum 0
        return result
