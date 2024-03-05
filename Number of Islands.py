https://leetcode.com/problems/number-of-islands/description/
DFS- stack, recursive, if visited=='1'
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()   # visit should be a set, so no duplicate
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (                     # base/stopping case 
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"   # grid value 0 hole
                or (r, c) in visit     # already visit hole 
            ):
                return

            visit.add((r, c))         # add visiting point 
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]   # all fourth direction
            for dr, dc in directions:
                dfs(r + dr, c + dc)                          # check 1 kina/ island kina ?
              
# From every position, we check if there is an island by [3,3] = 1 and [3,3] not in the visit list 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Version From Video
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

         def bfs(r,c):
             q = deque()           # we make a queue
             visited.add((r,c))
             q.append((r,c))      #we add root/[0,0]
           
             while q:
                 row,col = q.popleft()  # we deque or pop the root 
                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                 for dr,dc in directions:
                     r,c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                         q.append((r , c ))   # we append child 
                         visited.add((r, c )) # add visit 

         for r in range(rows):
             for c in range(cols):
               
                 if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)  # check island kina 
                     islands +=1 

         return islands

