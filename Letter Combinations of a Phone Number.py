https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/4717372/77-1-approach-1-o-3-n-4-m-python-c-step-by-step-explanation/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:   #  In Python, strings are immutable, meaning that each time you concatenate a string, a new string is created
                backtrack(i + 1, curStr + c)   # no need to pop() # abc--def.. 'ad' pore jump backtrack(1, a)-- backtk(2, ae)-  
        if digits:
            backtrack(0, "")
        return res


digits = "23"
digitToChar = { "2": "abc", "3": "def", ..., "9": "wxyz" }

Call backtrack(0, "")
i = 0, currStr = ""
digits[0] = "2", which maps to "abc"
First Level of Recursion (Processing '2'):
Iterate through characters 'a', 'b', 'c'.
First Iteration (c = 'a'):

Call backtrack(1, "a")
i = 1, currStr = "a"
digits[1] = "3", which maps to "def"
Second Level of Recursion (Processing '3' for "a"):

Iterate through characters 'd', 'e', 'f'.
First Iteration (c = 'd'):

Call backtrack(2, "ad")
i = 2, currStr = "ad"
Since len(currStr) == len(digits), add "ad" to res
res = ["ad"]
Second Iteration (c = 'e'):

Call backtrack(2, "ae")
i = 2, currStr = "ae"
Since len(currStr) == len(digits), add "ae" to res
res = ["ad", "ae"]
Third Iteration (c = 'f'):

Call backtrack(2, "af")
i = 2, currStr = "af"
Since len(currStr) == len(digits), add "af" to res
res = ["ad", "ae", "af"]
Backtrack to the First Level.

Second Iteration (c = 'b'):

Call backtrack(1, "b")
i = 1, currStr = "b"
digits[1] = "3", which maps to "def"
Second Level of Recursion (Processing '3' for "b"):

Iterate through characters 'd', 'e', 'f'.
First Iteration (c = 'd'):

Call backtrack(2, "bd")
i = 2, currStr = "bd"
Since len(currStr) == len(digits), add "bd" to res
res = ["ad", "ae", "af", "bd"]
Second Iteration (c = 'e'):

Call backtrack(2, "be")
i = 2, currStr = "be"
Since len(currStr) == len(digits), add "be" to res
res = ["ad", "ae", "af", "bd", "be"]
Third Iteration (c = 'f'):

Call backtrack(2, "bf")
i = 2, currStr = "bf"
Since len(currStr) == len(digits), add "bf" to res
res = ["ad", "ae", "af", "bd", "be", "bf"]
Backtrack to the First Level.

Third Iteration (c = 'c'):

Call backtrack(1, "c")
i = 1, currStr = "c"
digits[1] = "3", which maps to "def"
Second Level of Recursion (Processing '3' for "c"):

Iterate through characters 'd', 'e', 'f'.
First Iteration (c = 'd'):

Call backtrack(2, "cd")
i = 2, currStr = "cd"
Since len(currStr) == len(digits), add "cd" to res
res = ["ad", "ae", "af", "bd", "be", "bf", "cd"]
Second Iteration (c = 'e'):

Call backtrack(2, "ce")
i = 2, currStr = "ce"
Since len(currStr) == len(digits), add "ce" to res
res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce"]
Third Iteration (c = 'f'):

Call backtrack(2, "cf")
i = 2, currStr = "cf"
Since len(currStr) == len(digits), add "cf" to res
res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
