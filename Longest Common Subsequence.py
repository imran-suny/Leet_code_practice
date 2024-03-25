https://leetcode.com/problems/longest-common-subsequence/description/
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
https://leetcode.com/problems/longest-common-subsequence/solutions/4776734/108-1-approach-1-o-m-n-python-c-step-by-step-explanation/

[0 for j in range(len(text2) + 1)]---> [0, 0, 0, 0] eke 6bar repeat....1row and 1 coloum extra 0 to stop...
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]   # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]           # match hole diagonal ...[0,0] r digonal [1,1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])  # na hole max between right and down dp [0,0]--> [0,1] [1,0]

        return dp[0][0]

