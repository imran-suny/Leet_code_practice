Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Input: s = "a", t = "aa"
Output: ""
sliding window: count t, and find similar number of t in s, similar hole find len of window, 
remove from left, updte the two count again, check window[s[l]] < countT[s[l]]?
the character s[l] is 'O', and window['O'] is 1, while countT['O'] is 0 (as 'O' is not in string t). 
The condition window[s[l]] < countT[s[l]] is false, so the code doesn't decrement have.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:  # value same hole 
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:   #A remove korar pore, A in countT=true, window{A:0}<countT{A:1}, value have kome jabe, 
                    have -= 1
                l += 1                                               # left barate thakbo
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
