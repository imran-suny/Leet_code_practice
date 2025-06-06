Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

https://leetcode.com/problems/interleaving-string/solutions/4776962/109-1-approach-1-recursive-approach-o-m-n-python-c-step-by-step-explanation/
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
## cache 
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}  
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True       
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)
