https://leetcode.com/problems/valid-sudoku/description/
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])  # Output: 1
print(my_dict['d'])  # Raises KeyError: 'd' not in my_dict
rows = {0: {"5", "3", "7"}}   cols = {0: {"5"}, 1: {"3"}, 4: {"7"}}   squares = {(0, 0): {"5", "3"}, (0, 1): {"7"}}

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)                         # collections.defaultdict(set) creates a defaultdict where the default value for any key that hasn't been explicitly set is an empty set (set()).
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]        #  This helps identify the unique 3x3 subgrid for each element in the board.
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

