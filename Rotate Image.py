https://leetcode.com/problems/rotate-image/description/
1  2  3             
4  5  6
7  8  9 
Transpose the matrix by swapping elements along the main diagonal, then symmetrically flip it for the desired rotation.
After transpose, it will be swap(matrix[i][j], matrix[j][i])
1  4  7
2  5  8
3  6  9
Then flip the matrix horizontally. (swap(matrix[i][j], matrix[i][matrix.length-1-j])
7  4  1
8  5  2
9  6  3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """ Do not return anything, modify matrix in-place instead """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse_rows(matrix):
            for r in range(len(matrix)):
                left, right = 0, len(matrix) - 1
                while left < right:
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left += 1
                    right -= 1

        transpose(matrix)
        reverse_rows(matrix)      

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i]                    # save the topleft
              
                matrix[top][l + i] = matrix[bottom - i][l]      # move bottom left into top left       # i komte thakbe bottom r, 7 r pore 4.....
               
                matrix[bottom - i][l] = matrix[bottom][r - i]   # move bottom right into bottom left   # i komte thakbe bottom r, 9-8

                matrix[bottom][r - i] = matrix[top + i][r]      # move top right into bottom right  # top i barbe  3>6

                matrix[top + i][r] = topLeft                    # move top left into top right
            r -= 1
            l += 1
