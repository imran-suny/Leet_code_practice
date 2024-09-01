https://leetcode.com/problems/longest-palindromic-substring/description/
Input: s = "babad"
Output: "bab"
Input: s = "cbbd"
Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""                                  # Initialize an empty string to store the longest palindromic substring found so far      
        resLen = 0                                # Initialize a variable to keep track of the length of the longest palindrome           
        for i in range(len(s)):                   # Iterate through each character in the string     
            
            l, r = i, i                           # Odd-length palindromes: # Set left and right pointers to the current index
            while l >= 0 and r < len(s) and s[l] == s[r]:    
                if (r - l + 1) > resLen:          # Check if substring between l and r is a palindrome
                    res = s[l : r + 1]            # Update res if a longer palindrome is found 
                    resLen = r - l + 1            # Update resLen with the new palindrome length
                   
                l -= 1                             # Move left pointer to the left           
                r += 1                             # Move right pointer to the right
           
            l, r = i, i + 1     
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]      
                    resLen = r - l + 1      
                l -= 1          
                r += 1          
        return res          
        # Return the longest palindromic substring found
