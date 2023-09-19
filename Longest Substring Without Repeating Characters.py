Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
  def lengthOfLongestSubstring(s):      # bruteforce  O(n^3) space: O(min(N, M)), as HashSet is used. N is the length of the string and M is the size of the substrings
        def check(start, end):
            chars = [0] * 128               # 128 ta character 
            for i in range(start, end + 1): # until last 
                c = s[i]                    # ekta element nilam 
                chars[ord(c)] += 1          # convert to asci
                if chars[ord(c)] > 1:       # if duplicate return 0 , else find length
                    return False
            return True
          
        n = len(s)
        res = 0
        for i in range(n):               # every value in string range all
            for j in range(i, n):        # range from i to n
                if check(i, j):          # check if the contain unique character
                    res = max(res, j - i + 1)  # if true, then find the length j-i+1     len not index so = 2-0+1
        return res

Sliding window: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0 
        charSet = set()     # to keep track of unique characters
        left = 0            # left and right pointer to represent the boundaries of the current substring.
        
        for right in range(n):   # We iterate through the string using the right pointer.
            if s[right] not in charSet:
                charSet.add(s[right])  # If the current character is not in the set (charSet), it means we have a new unique character.
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet: # we move the left pointer forward, removing characters from the set until the repeating character is no longer present
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
