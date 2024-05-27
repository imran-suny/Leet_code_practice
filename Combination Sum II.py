https://leetcode.com/problems/combination-sum-ii/solutions/4780196/c-and-python3-backtracking-optimal-approach-0-ms-beats-100/
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, subset, tot):
            if tot == target:
                ans.append(subset[:])
                return
            if i >= len(candidates) or tot > target:
                return
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:          # Skip duplicates to avoid repeating the same combination.
                    continue
                subset.append(candidates[idx])
                backtrack(idx + 1, comb, tot + candidates[idx])
                subset.pop()
        candidates.sort()
        backtrack(0, [], 0)
        return ans
