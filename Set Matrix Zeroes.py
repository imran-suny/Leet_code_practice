https://leetcode.com/problems/set-matrix-zeroes/description/
https://takeuforward.org/data-structure/set-matrix-zero/
https://leetcode.com/problems/set-matrix-zeroes/solutions/2525398/all-approaches-from-brute-force-to-optimal-with-easy-explanation/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero///first row skip,      
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0       # first row kore kore felbo 
                    if r > 0:              # except row zero///for row zero--we have a dedicated flag 
                        matrix[r][0] = 0   # first column zero
                    else:
                        rowZero = True      # for row zero

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:   # first row or colum zero hole, sob 0
                    matrix[r][c] = 0    

        if matrix[0][0] == 0:       
            for r in range(ROWS):       # first column zero
                matrix[r][0] = 0

        if rowZero:                      # fisr row zero
            for c in range(COLS):
                matrix[0][c] = 0
