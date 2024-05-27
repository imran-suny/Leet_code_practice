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

First Iteration:

Remove 1: nums = [2, 3]
Recursive call with nums = [2, 3]
Remove 2: nums = [3]
Recursive call with nums = [3]
Base case: return [[3]]
Add 2 to each permutation: [[3, 2]]
Restore 2: nums = [2, 3]
Remove 3: nums = [2]
Recursive call with nums = [2]
Base case: return [[2]]
Add 3 to each permutation: [[2, 3]]
Restore 3: nums = [2, 3]
Add 1 to each permutation: [[3, 2, 1], [2, 3, 1]]
Restore 1: nums = [1, 2, 3]

