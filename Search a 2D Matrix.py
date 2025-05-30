https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1          ##Binary Search for the Correct Row:
        while top <= bot:
            row = (top + bot) // 2            # the target is greater than the largest element in the current row.
            if target > matrix[row][-1]:     # target> last element, target cannot be in this row or any row before it, so the search continues in rows below
                top = row + 1           
            elif target < matrix[row][0]:    #  if the target is less than the smallest element in the current row.
                bot = row - 1                 # row = (0 + 0) // 2 = 0
            else:
                break

        if not (top <= bot):            ## Check if the Row was Found:
            return False
        
      row = (top + bot) // 2            ##Binary Search within the Row:   row = (0 + 0) // 2 = 0
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
