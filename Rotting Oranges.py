https://leetcode.com/problems/rotting-oranges/solutions/4733472/84-1-approach-1-o-m-n-python-c-step-by-step-explanation/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):           # Iterate through the grid to find fresh and rotten oranges
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))                # Add initially rotten oranges to the queue

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()                   # Extract a rotten orange from the queue

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                                                      # if in bounds and nonrotten, make rotten # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1               # Return the time taken to rot all oranges if all are rotten, otherwise return -1
