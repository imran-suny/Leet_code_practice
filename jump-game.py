https://leetcode.com/problems/jump-game/solutions/4920717/video-move-goal-position/
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
if current position + maximum jump >= goal
[2,3,1,1,4]
       i g
current position + maximum jump >= goal
= 3 + 1 >= 4
= true
------------------------------------------------
i = current position
g = goal

[2,3,1,1,4]
     i g
current position + maximum jump >= goal
= 2 + 1 >= 3
= true

in the end
[2,3,1,1,4]
 g
----------------------------------------------
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

