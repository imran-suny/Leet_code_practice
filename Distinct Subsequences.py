Input: s = "rabbbit", t = "rabbit"
Output: 3

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Memoization dictionary
        memo = {}
        
        def dfs(i, j):
            if j == len(t):  # If we've matched all characters of t
                return 1
            if i == len(s):  # If we've exhausted all characters of s
                return 0
            if (i, j) in memo:
                return memo[(i, j)]    # dfs(1, 1) many time, memo[(1, 1)] just 1bar calculation
        
            if s[i] == t[j]:
                # If the characters match, either use the character or skip it
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # If they don't match, skip the current character of s
                memo[(i, j)] = dfs(i + 1, j)   
            return memo[(i, j)]
        
        return dfs(0, 0)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]
