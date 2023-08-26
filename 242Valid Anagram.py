
##  Sorting/// #  time complexity of O(n log n) 
class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if s[i] in hashmap, then 1 and continue, or else value: 0+1=1,key = a/b..
            countT[t[i]] = 1 + countT.get(t[i], 0) # second string 
        return countS == countT

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

countS = {}
s = 'anagram'
for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            print(countS)     
{'a': 1}
{'a': 1, 'n': 1}
{'a': 2, 'n': 1}
{'a': 2, 'n': 1, 'g': 1}
{'a': 2, 'n': 1, 'g': 1, 'r': 1}
{'a': 3, 'n': 1, 'g': 1, 'r': 1}
{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
>             
        