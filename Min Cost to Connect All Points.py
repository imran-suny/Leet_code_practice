Time complexity: (O(N^2 * log N)), where (N) is the number of points. Building the adjacency list takes (O(N^2)) time, 
and performing Prim's algorithm with a heap takes (O(N \log N)) time.
Space complexity: (O(N^2)) for the adjacency list and (O(N)) for the minimum heap and the visit set. 
Overall, the space complexity is (O(N^2)).

https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Number of points
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
              
        res = 0
        visit = set()
        # Initialize min heap with starting point
        minH = [[0, 0]]  # [cost, point]   # cost or weight, je choto take pop 
        
        # Prim's Algorithm  finds Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges
        while len(visit) < N:
            cost, i = heapq.heappop(minH)              # Pop minimum cost edge from heap
            if i in visit:                             #  visited hole explore next edges
                continue                      # 1. Create edges using adjacency list 2. pop min/starting point 3. point added to visit 4. Add adjacent nodes to heap
            res += cost
            visit.add(i)
            # Add adjacent nodes to heap
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])  # if the neighbor is not visited, push the edge [neiCost, nei] onto the heap.
        return res

points = [
    [0, 0],  # point 0
    [2, 2],  # point 1
    [3, 10], # point 2
    [5, 2]   # point 3
]
Initialization:
Start with vertex 0.
Heap: [[0, 0]] (initial vertex with cost 0).
MST cost res = 0.
Visited set visit = {}.
First Iteration:

Extract heapq.heappop(minH) -> [0, 0] (cost 0, vertex 0).
Add vertex 0 to MST: visit = {0}.
Push edges from vertex 0 to the heap
[[4, 1], [13, 2], [7, 3]]
Second Iteration:

Extract heapq.heappop(minH) -> [4, 1] (cost 4, vertex 1).
Add vertex 1 to MST: visit = {0, 1}.
Add cost to MST: res = 4.
Push edges from vertex 1 to the heap (excluding already visited):
[[7, 3], [13, 2], [9, 3]]

