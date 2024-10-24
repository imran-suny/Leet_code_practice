Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
1. get count dictionary // reverse count store // append the number in new list // if len list == k, return list[0:1]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0) # {1:3, 2:2, 3:1} 
        
        freq = [[] for i in range(len(nums) + 1)] # [ [], [], [], [], [], [], [] ] #         
        for n, c in count.items(): # n = index(1), c = count(3) 
            freq[c].append(n) # [[], [], [], [1], [], [], []]  #appends index-- 1:3,1 3 bar, so 3 er ghore 1..                                             
            print (freq) # [[], [3], [2], [1], [], [], []]   # boro ta last a  
        res = []
        for i in range(len(freq) - 1, 0, -1): # #range(6, 0, -1)...6theke start to 0,,,step= -1
            for n in freq[i]: # [[], [3], [2], [1], [], [], []], 6number empty, n =2...
                res.append(n) # nothing to add// komte komte 3 a jbe, maybe [3,4,5] thqkte pare freq[i]a
                if len(res) == k: #  res = [1, 2] 
                    return res
