https://leetcode.com/problems/word-break/description/
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true     Explanation: Return true because "leetcode" can be segmented as "leet code".
https://leetcode.com/problems/word-break/solutions/4775602/103-1-approach-1-o-n-2-m-python-c-step-by-step-explanation/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)              # [False, False, False, False, False, False, False, False, False]
        dp[len(s)] = True                        # [False, False, False, False, False, False, False, False, True]

        for i in range(len(s) - 1, -1, -1): 
            for w in wordDict:                    # leet 
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:   # (i=4+ len(w) 4=8)... [4:8] # make dp[4]=true and dp [0]=true
                    dp[i] = dp[i + len(w)]        # dp[4]=dp[8]=true
                if dp[i]:
                    break
                                               print(dp) #[True, False, False, False, True, False, False, False, True]
        return dp[0]
