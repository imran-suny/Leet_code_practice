Input: s = "aab"     Output: [["a","a","b"],["aa","b"]]
https://leetcode.com/problems/palindrome-partitioning/solutions/4717266/76-1-approach-1-o-n-2-n-python-c-step-by-step-explanation/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start: int, subset):
            if start == len(s):
                result.append(subset[:])
                return
            for end in range(start + 1, len(s) + 1):
                current_sub = s[start:end]
                if is_palindrome(current_sub):
                    path.append(current_sub)
                    backtrack(end, subset)
                    subset.pop()
        result = []
        backtrack(0, [])
        return result

"aab" backtrack(0, []), start = 0, path = []
Loop through end from 1 to 3, For end = 1: current_sub = "a", which is a palindrome., Append "a" to path: path = ["a"], Call backtrack(1, ["a"]).
Second Level of Backtracking:

start = 1, path = ["a"], Loop through end from 2 to 3...For end = 2: current_sub = "a", which is a palindrome.
Append "a" to path: path = ["a", "a"] Call backtrack(2, ["a", "a"]).
Third Level of Backtracking:

start = 2, path = ["a", "a"]...Loop through end from 3 to 3...For end = 3: current_sub = "b", which is a palindrome.
Append "b" to path: path = ["a", "a", "b"]...Call backtrack(3, ["a", "a", "b"]).

Base Case: start = 3 (end of string), path = ["a", "a", "b"]
Append path[:] to result: result = [["a", "a", "b"]]
Backtrack: Remove "b" from path: path = ["a", "a"] Backtrack to Second Level of Backtracking:
----------------------------------------------------------------------------------------------------------------------------------------------------------
start = 2, path = ["a", "a"] Continue loop: No more end to check.
Backtrack: Remove "a" from path: path = ["a"]
Continue First Level of Backtracking:
-----------------------------------------------------------------------------------------------------------------------------------------------------------
start = 1, path = ["a"]
For end = 3: current_sub = "ab", which is not a palindrome.
Continue loop: No more end to check.
Backtrack: Remove "a" from path: path = []
Continue Initial Call:

start = 0, path = []
For end = 2: current_sub = "aa", which is a palindrome.
Append "aa" to path: path = ["aa"]
Call backtrack(2, ["aa"]).
New Second Level of Backtracking:

start = 2, path = ["aa"]
Loop through end from 3 to 3.
For end = 3: current_sub = "b", which is a palindrome.
Append "b" to path: path = ["aa", "b"]
Call backtrack(3, ["aa", "b"]).
New Base Case:
-----------------------------------------------------------------------------------------------------------------------------------------------------------
start = 3 (end of string), path = ["aa", "b"]
Append path[:] to result: result = [["a", "a", "b"], ["aa", "b"]]
Backtrack: Remove "b" from path: path = ["aa"]
Backtrack to Initial Call:

start = 2, path = ["aa"]
Continue loop: No more end to check.
Backtrack: Remove "aa" from path: path = []
End of Backtracking:

start = 0, path = []
Continue loop: No more end to check.
