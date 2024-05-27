Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: 
                result.append(path) 
                return 
            for i in range(len(nums)): 
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
                
        result = [] 
        backtrack(nums, []) 
        return result
      Initial Call: backtrack([1, 2, 3], [])

Loop through [1, 2, 3].
For i = 0, nums[:0] + nums[1:] gives [2, 3] and path + [nums[0]] gives [1].  Call backtrack([2, 3], [1]).
Loop through [2, 3].
For i = 0, nums[:0] + nums[1:] gives [3] and path + [nums[0]] gives [1, 2]. Call backtrack([3], [1, 2]).
Loop through [3].
For i = 0, nums[:0] + nums[1:] gives [] and path + [nums[0]] gives [1, 2, 3] Call backtrack([], [1, 2, 3]).
Since nums is empty, append [1, 2, 3] to result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy
            
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
