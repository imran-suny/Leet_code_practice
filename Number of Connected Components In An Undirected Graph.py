
class Graph:
    def __init__(self, V):
        self.V = V                             # No. of vertices
        self.adj = [[] for i in range(self.V)] # Pointer to an array containing  adjacency lists

    def NumberOfconnectedComponents(self):           
        visited = [False for i in range(self.V)]  # Mark all the vertices as not visited   
        count = 0                                # To store the number of connected  components
        for v in range(self.V):
            if (visited[v] == False):
                self.DFSUtil(v, visited)
                count += 1
        return count
         
    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.adj[v]:
            if (not visited[i]):
                self.DFSUtil(i, visited)
                 
    # Add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
         
# Driver code        
if __name__=='__main__':
     
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    print(g.NumberOfconnectedComponents())
 
