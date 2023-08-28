https://leetcode.com/problems/3sum/
https://medium.com/j-t-tech/leetcode-15-3sum-357978a0898d

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: # Requires 3 for a pair of 3
            return []
        elif len(nums) == 3 and sum(nums) == 0: # Naive case; check sum of 3 elements
            return [nums]
        
        res = []
        nums.sort()  # brute-force take , O (n^3) // O(nlogn) # sorting to avoid the duplicate

        for i, a in enumerate(nums):
            
            if a > 0: # Skip positive integers, does not make 0
                break

            if i > 0 and a == nums[i - 1]: #i = 1, 2 ==2/ duplicate   [first nothing satisfies, so increase i 0 to 1,skip rest]
                continue # If this condition is met, the loop uses the continue  to 
                         #skip the rest of the current iteration and move to the next one
                         # The condition i > 0 is there to ensure that this comparison doesn't occur for the first element, 
                         #since there is no previous element to compare with

            l, r = i + 1, len(nums) - 1 # left and right pointer, [1, len(nums)-1]
            while l < r: # dnt overlap 
                threeSum = a + nums[l] + nums[r] # add all 
                if threeSum > 0: # big hole komabo r 
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) # append add element to a list []...dekte L[ r moto //// add kore dibo list a 0 hole 
                    l += 1 # need to update the pointer,  
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:  #  duplicates of left pointer removes or smaller than the target.
                        l += 1 # l update korlei holbe cause while a threSum > 0 hole right pointer -1 korbe
                        
        return res

1. check len(num) < 3 kina?
2. len(nums) == 3 and sum(nums) == 0 ??
3. sob value positive kina? a > 0 ? sorting kore enumerate diye value check ??
4. duplicate kina? index >0 i.e. 2ta hote hobe minimum /// Current == previous value? hole continue
5.then pointer set kora ,, from second index as our first value a=target
6. check left or right pointer duplicate kina?? 



