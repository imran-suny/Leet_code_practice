https://leetcode.com/problems/container-with-most-water/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0                           #  area initially zero, so no negative value
        while l < r:    #closing condition
            currentArea = min(height[l], height[r]) * (r - l)    # area = height x weight/// sob theke kom height select korbo, [r, l theke boro , so (r-l)]          
            res = max(res, currentArea )  # 
            if height[l] < height[r]:     # je choto tare increase korbo
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res

