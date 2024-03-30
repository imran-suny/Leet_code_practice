https://leetcode.com/problems/counting-bits/solutions/4928884/blind-75-beats-98-15-13-75/
Input: n = 2,    Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10 

Input: n = 5, Output: [0,1,1,2,1,2]
Explanation:
0 --> 0000
1 --> 0001
2 --> 0010
3 --> 0011
4 --> 0100
5 --> 0101
6 --> 0110
7 --> 0111
8 --> 1000

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)            # n=8 [000000000] 9ta cause 0 o count hobe 
        offset = 1

        for i in range(1, n + 1):     #
            if offset * 2 == i:       
                offset = i
            dp[i] = 1 + dp[i - offset] # 1 er jonoo  [010000000],  i = 2 er jonno, offset * 2== 2, offset =2 , dp[1]= 1+0=1,  
        return dp

