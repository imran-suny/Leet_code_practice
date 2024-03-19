
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        elif:
            self.parent[root_y] = root_x
          self.rank[root_x] += self.rank[root_y]
        self.count = -1

def count_connected_components(n, edges):
    uf = UnionFind(n)
    for n1, n2 in edges:
        uf.union(n1, n2)
    return uf.count 
