#Given an integer array nums, return an array answer such that answer[i] 
#is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]  # num[i]-- * mul(i+1 to len (num)-1, )
Output: [24,12,8,6] # answer [i= ]

nums = [1,2,3,4]
res = [1] * (len(nums))
print(res)
for i in range(1, len(nums)):
    res[i] = res[i-1] * nums[i-1]
    print('pre', res)
postfix = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    print('post', res)
    postfix *= nums[i]
    print('postfix', postfix)
print( res)
 
Output:::: 
[1, 1, 1, 1]
pre [1, 1, 1, 1]
pre [1, 1, 2, 1]
pre [1, 1, 2, 6]
post [1, 1, 2, 6]
postfix 4
post [1, 1, 8, 6]
postfix 12
post [1, 12, 8, 6]
postfix 24
post [24, 12, 8, 6]
postfix 24
[24, 12, 8, 6]