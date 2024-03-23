https://leetcode.com/problems/decode-ways/description/
Input: s = "226", Output: 3 ///koto upaye decode ??
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Memoization
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}          # dp= {3:1}
        def dfs(i):
            if i in dp:           # dfs(0),...   dfs(3) te gele 1 return hobe 
                return dp[i]
            if s[i] == "0":       # base case, 0 diye start hote parbe na 
                return 0
            res = dfs(i + 1)      # res= dfs(1)> dfs(2)> dfs(3) te gele 1 return hobe///means dfs(3) return 1,  
            
            if i + 1 < len(s) and (                                 # double r jonno, 1 or 2 diye start hobe, 11,12--19 or 20,21-26
                  s[i] == "1" or         s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)   #    dfs (2) jabe na cause 2+1< lens(s) not, so dfs (1)
            dp[i] = res             #   [3:1, 2:1] > dfs (1) -- res= 1 [3:1, 2:1  1: 1+1] > dfs(0)--- [3:1, 2:1  1: 2  0: 2+1 [dfs(1) + dfs(2)]))]
            return res
        return dfs(0)

Here's how dfs(2) is calculated:
Check  2 in the dp dictionary. Since it's not, continue with the calculation.
Check if the current digit s[i] is '0'. In this case, s[2] = '6', which is not '0', so we proceed.
Calculate res by recursively calling dfs(i + 1), which is dfs(3). Now, dfs(3) calculates the number of ways to decode the substring starting from index 3. 
Since index 3 is out of bounds (the string has length 3), it returns 1 (because there's one way to decode an empty string).
Back to dfs(1), res becomes res = dfs(2) = 1.
Now, we check if the substring starting from index 1 and the next digit form a valid two-digit encoding.
Since '22' is a valid encoding, we add the number of ways to decode the substring starting from index 2 to res.
Finally, res becomes res = dfs(2) + dfs(3) = 1 + 1 = 2.

        # Dynamic Programming
        dp = {len(s): 1}                     # dp= {3:1}  226   For i = 2   dp= {2:1, 3:1}     For i = 1  dp= {1: 1 + 1, 2;1, 3:1}  For i = 0   dp={0:2 +1 , 1: 2 2;1, 3:1}
        for i in range(len(s) - 1, -1, -1):  #2,1,0
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]          # dp[2]=dp[3]= 1

            if i + 1 < len(s) and (                                  # 2+1<3 not true , 
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]        # dp[2] = dp[4]
        return dp[0]
