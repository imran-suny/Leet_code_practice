https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/4723066/82-1-approach-1-o-m-n-python-c-step-by-step-explanation/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        # Define DFS function to traverse the matrix and mark cells reachable
        def dfs(r, c, visit, prevHeight):
            # Base cases for termination of DFS traversal
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == rows
                or c == cols
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            # Recursive calls for DFS traversal in four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # DFS from top and bottom borders to mark cells reachable by Pacific and Atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # DFS from left and right borders to mark cells reachable by Pacific and Atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # Find cells reachable from both oceans and store their coordinates in res
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
