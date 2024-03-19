https://www.youtube.com/watch?v=qWGh4S86Exw
https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
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

############# dfs solution ############
n = 5= given nodes 
edges = [(0, 1), (1, 2), (3, 4)]

def dfs(graph, visited, node):
    visited.add(node)                   # 0, 
    for neighbor in graph[node]:        # 1, 0, 2,1 ==visited , stop dfs stop , count +1,  then node 1 r jonno dfs 
        if neighbor not in visited:
            dfs(graph, visited, neighbor)

def count_connected_components(n, edges):       # make edges 
    graph = [ [] for _ in range(n)]
    for u, v in edges:         # 0,1 ,,, graph[0]= 1,  graph[1]= [0,.. next 2 
        graph[u].append(v)  
        graph[v].append(u)#  [[1], [0, 2], [1], [4], [3]]

    visited = set()
    count = 0
    for i in range(n):             # evry node, if not visited visit using dfs and count +1
        if i not in visited:
            dfs(graph, visited, i)
            count += 1
    return count

# Example usage:
n = 5
edges = [(0, 1), (1, 2), (3, 4)]
print(count_connected_components(n, edges))  # Output should be 2

