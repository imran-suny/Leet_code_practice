https://leetcode.com/problems/word-search/description/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])    # Get dimensions of the board
        path = set()                              # Set to keep track of visited cells
 
        def dfs(r, c, i):                         # recursive dfs
            if i == len(word):                    # Base case:if index i equals the length of the word
                return True
            if (
                min(r, c) < 0                # Base case: if current cell is out of bounds or not matching the word character
                or r >= ROWS                 # r,c , HxW of board theke boro na
                or c >= COLS
                or word[i] != board[r][c]    # word er char board a thakte hobe
                or (r, c) in path            # path not visited twice
            ):
                return False
            path.add((r, c))                # if not false, means match, add to path,  Mark current cell as visited
            res = (
                dfs(r + 1, c, i + 1)        # # Recursively explore adjacent cells of (r,c)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))            # # clean, Backtrack: remove current cell from path, we no longer need matching one
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]          # 
            
        for r in range(ROWS):         # Iterate through each cell in the board and start DFS traversal
            for c in range(COLS):     # If DFS traversal from any cell returns True, it means the word exists on the board,
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)
