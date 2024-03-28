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
            for i in range(left, right+1):            # get every i in the top row
                result.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom+1):            # get every i in the right col
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:                            # get every i in the bottom row
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:                            # get every i in the left col
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
      
