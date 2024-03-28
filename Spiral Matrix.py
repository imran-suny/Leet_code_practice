https://leetcode.com/problems/spiral-matrix/description/
https://leetcode.com/problems/spiral-matrix/solutions/3502600/python-java-c-simple-solution-easy-to-understand/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1
        result = []
        
        while len(result) < rows * cols:
            for i in range(left, right+1):            # top row-- top--- i column change 
                result.append(matrix[top][i])
            top += 1                                  # top count --1
            
            for i in range(top, bottom+1):            # top to bottom from right
                result.append(matrix[i][right])       # row change, column =right 
            right -= 1                                # right komte thakte jeetu niche jabe 
            
            if top <= bottom:                          # top and bottom overlap na kora porjinto 
                for i in range(right, left-1, -1):     #reverse from right to left 
                    result.append(matrix[bottom][i])   # coum change, bottom 
                bottom -= 1
            
            if left <= right:                           # get every i in the left col
                for i in range(bottom, top-1, -1):      
                    result.append(matrix[i][left])      # row change, coloum left 
                left += 1
        
        return result
      
