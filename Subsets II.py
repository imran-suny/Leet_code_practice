Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset =[]
        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            # All subsets that don't include nums[i]
            while i+1  < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
