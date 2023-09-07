Problem:
Input: s = "()[]{}"
Output: true
Input: s = "(]"
Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"} # 
        stack = [] # 

        for c in s:
            if c not in Map:
                stack.append(c) 
                continue   # append [  ( [ {   ]  # cuase era nai key te  
            if not stack or stack[-1] != Map[c]:  # if stack not empty and na mille [ stake value != Map value ]  { exist in key value, so pop()-- last er ra '{'
                 return False
            stack.pop()

        return not stack

