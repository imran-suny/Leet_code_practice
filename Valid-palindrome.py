Example 1: aba--- is a palindrome   $abd23abc 
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  ## two pointer 
        while l < r:  # majhkaneer ta bas so l<=r na 
            while l < r and not self.alphanum(s[l]):  ##  for the function to convert alphanum// check if alphanum, na hole increment the left pointer, 1
                l += 1
            while l < r and not self.alphanum(s[r]): # jodi alnum na hoy(i.g.-space) , thle increment hole next if loop a
                r -= 1
            if s[l].lower() != s[r].lower():  # only compare when alphanum, otherwise, next pointer 
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") # The ord() function returns the number representing the unicode code of a specified character.
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

#solution 2
    s2 = ""
    for i in s.lower():
        if(i.isalnum()):
            s2 += i
    if(s2 == s2[::-1]):  # The slice starts from the end of the string and moves towards the beginning with a step size of -1/// 
        return True
    return False

#####
original_string = "example"
reversed_string = original_string[::-1]
print(reversed_string)
print result---> elpmaxe

