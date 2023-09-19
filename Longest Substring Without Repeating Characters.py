Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
  def lengthOfLongestSubstring(s):
        def check(start, end):
            chars = [0] * 128               # 128 ta character 
            for i in range(start, end + 1): # until last 
                c = s[i]                    # ekta element nilam 
                chars[ord(c)] += 1          # convert to asci
                if chars[ord(c)] > 1:       # if duplicate return false , else find length
                    return False
            return True
          
        n = len(s)
        res = 0
        for i in range(n):               # every value in string range all
            for j in range(i, n):        # range from i to n
                if check(i, j):          # check if the contain unique character
                    res = max(res, j - i + 1)  # if true, then find the length j-i+1     len not index so = 2-0+1
        return res
