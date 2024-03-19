Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

# Problem is free on Lintcode
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}  # hashmap for every node, adjacency list 
        for n1, n2 in edges:       # 0,1              0, 2                               [0,3],                                  [0,3], 
            adj[n1].append(n2)     # 0:[1]  1:[0]     0:[1, 2]  1:[0]  2: [0]             0:[1, 2, 3]  1:[0]  2: [0]  3: [0]      0:[1, 2, 3]  1:[0, 4]  2: [0]  3: [0]   4: [1]
            adj[n2].append(n1)     # [[1, 2, 3], [0, 4], [0], [0], [1]]

        visit = set()

        def dfs(i, prev):
            if i in visit:         #  loop 
                return False

            visit.add(i)
            for j in adj[i]:       # adj [0] --  [1, 2, 3]
                if j == prev:      # -1 != 0          
                    continue
                if not dfs(j, i):   #  loop dfs(1, 0)  (2,0), (3,0)       prev = updated by i
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
    
    
    
    # alternative solution via DSU O(ElogV) time complexity and 
    # save some space as we don't recreate graph\tree into adjacency list prior dfs and loop over the edge list directly
    
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Cycle detected
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def is_valid_tree(n, edges):
    if len(edges) != n - 1:
        return False  # Number of edges should be n - 1 for a tree
    
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return False  # Cycle detected
    
    # Check if all nodes are connected
    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            return False  # Not all nodes are connected 
    return True

# Example usage:
n = 5
edges = [(0, 1), (0, 2), (0, 3), (1, 4)]
print(is_valid_tree(n, edges))  # Output should be Tru



