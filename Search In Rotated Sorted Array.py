Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:    # but target in right half 
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:   # # but target in left half 
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
      

