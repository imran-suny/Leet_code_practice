Input: s = "AABABBA", k = 1
Output: 4 
Input: s = "ABAB", k = 2
Output: 4
# letter thakle window, window hole left and right pointer .... l= 0, r = with a for loop [0,.. len(s)], sob gula... len = r-l+1 [as both l, r, starts from 0, so len=1]
#The window is valid if the (window length) -  (most frequent character)<= k
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}                                 # for get method we need a dict 
        l = 0                                      # left pointer 
        res = 0
        maxf=0
        for r in range(len(s)):                    # right pointer, automatically updated with +1
            count[s[r]] = 1 + count.get(s[r], 0) 
            maxf = max(maxf, count[s[r]])
            while ((r - l + 1) - maxf) > k:  # update left pointer                       (window length) -  (most frequent character) > k
                count[s[l]] -= 1                       # remove left postion value  
                l += 1                               # update left pointer 
        res = max (res, r-l+1)
        return res

More efficinet:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}        
        l = 0
        maxf = 0  # we are counting max frewuncy of char
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])    #  so we dont need to scan everytime max(count.values())  to find the max value
            if (r - l + 1) - maxf > k:      # (len-maxf) <=k, so we want maxf more.. 6-3= 3>2 , so update left pointer.. 6-5=1 <2, so right pointer len = barbe ,, so maxf effect fele only..
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)

