
https://leetcode.com/problems/unique-paths/description/
Input: 3 ta row, 7ta column,   m = 3, n = 7
Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n                                 # [1, 1, 1, 1, 1, 1, 1]

        for i in range(m - 1):                        #-1 as range start from 0,    0,1 er jonnno, cause we want last row and last column as 1        
            newRow = [1] * n                          # [1, 1, 1, 1, 1, 1, 1]
            for j in range(n - 2, -1, -1):            j = 5,4,3,2,1,0
                newRow[j] = newRow[j + 1] + row[j]    # [1, 1, 1, 1, 1, 2, 1] ,[1, 1, 1, 1, 3, 2, 1].........               [7, 6, 5, 4, 3, 2, 1]
            row = newRow                              # for i =1,  ........... [28, 21, 15, 10, 6, 3, 1]
        return row[0]                                 # 28 is result

        # O(n * m) O(n)
