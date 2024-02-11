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
            if c in Map:  # key match korle 
                if stack or stack[-1] = Map[c]:  ## value match korbo  ')' 
                    stack.pop() ---------------------------------------------'(' ke pop korbe, stack empty, true for ()
                else:
                    return False
             else:   
                stack.append(c)     # '('
        return True if not stack else False

