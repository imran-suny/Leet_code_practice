Input: nums = [3,4,5,1,2]
Output: 1

# Divide left and right sorted part/// and select a mid pointer also

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2              # 0+4//2 =2 (floor mane purno sonkha)
            if(nums[mid+1] < nums[mid]):           # 1<5 , so retrun 1
                return nums[mid+1]
            
            # right has the min # right a thakle strat k shift korbo
            if nums[mid] > nums[end]:               # right a min hole start pointer to mid+1
                start = mid + 1
                
            # left has the  min                      # end ke mid a niya asbo//left a thakle end ke shift korbo
            else:
                end = mid
                
        return nums[start]
