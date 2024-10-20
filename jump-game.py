https://leetcode.com/problems/jump-game/solutions/4920717/video-move-goal-position/
Input: nums = [2,3,1,1,4]
Output: true
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

