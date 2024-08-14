# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left   # All elements to left of fill index are less than or equal to the pivot.

        for i in range(left, right):                         # nums = [3, 2, 1, 5, 4], left = 0, and right = 4
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]    #  3, 2, 1  num [0]= num[i=0], .... 
                fill += 1                                    # After the loop, the fill index is 3, and nums[fill] = 5
        nums[fill], nums[right] = nums[right], nums[fill]    # The pivot is 4, located at nums[right] = nums[4], swap, [3, 2, 1, 4, 5]
        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:   nums = [3, 2, 1, 5, 6, 4] and k = 2
        k = len(nums) - k        #   k =6-2=4   zero based index, 5 hole total, 3rd smallest corresponds to the 2nd largest element in the list.
        left, right = 0, len(nums) - 1   # 0, 5 

        while left < right:
            pivot = self.partition(nums, left, right)  # returns the final index of the pivot after partitioning.  #   pivot = 4

            if pivot < k:                         #  pivot is smaller than the k-th largest element,    let pivot= 2, 2<4: left= 2+1 = 3 
                left = pivot + 1                  # search in right subarray
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]
