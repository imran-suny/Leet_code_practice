#Given an integer array nums, return an array answer such that answer[i] 
#is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]  # num[i]-- * mul(i+1 to len (num)-1, )
Output: [24,12,8,6] # answer [i= ]

nums = [1,2,3,4]
res = [1] * (len(nums))              #[1, 1, 1, 1]

for i in range(1, len(nums)):        # prefix means left to right multiplication, first value 1 as no prefix (2nd to last 1,2,3)
    res[i] = res[i-1] * nums[i-1]    # res [1 x 1 1] = res[0]*num[0] = 1*1 = x te boshbe  
    print('pre', res)                # res [1 1 x 1] = res[1]*num[1] = 1*2 = x te boshbe
postfix = 1
for i in range(len(nums) - 1, -1, -1):   # postfix reverse mul [24,24,12,4] // for each mul Prefix*Postfix  # [3, 2, 1] 0 hole, -1 hole sob [3, 2, 1, 0]
    res[i] = res[i] * postfix                 # to keep last position fix, mul with 1. postfix =1 res[4] = res[4]*1= res[4]
    print('post', res)                   # multiplies the current value at index i in the res with the current value of the postfix variable.
    postfix = postfix * nums[i]                # portfix = 1 * num[last] = 1*4 = 4 
    print('postfix', postfix)            # 4*2= 8 
print( res)

Output:::: 
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
