https://leetcode.com/problems/edit-distance/solutions/4781140/110-1-approach-1-o-m-n-python-c-step-by-step-explanation/
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        # Create a 2D array to store the minimum edit distances
        dp = [[float("inf")] * (len(w2) + 1) for i in range(len(w1) + 1)]

        # Base cases: initialize the last row and column of the dp array
        for j in range(len(w2) + 1):
            dp[len(w1)][j] = len(w2) - j
        for i in range(len(w1) + 1):
            dp[i][len(w2)] = len(w1) - i

        # Fill the dp array using a bottom-up approach
        for i in range(len(w1) - 1, -1, -1):
            for j in range(len(w2) - 1, -1, -1):
                # If the characters are equal, no operation needed at this position
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # Minimum edit distance is one plus the minimum of three possible operations
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        # The result is stored in the top-left corner of the dp array
        return dp[0][0]
