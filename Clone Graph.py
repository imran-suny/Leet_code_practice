https://leetcode.com/problems/clone-graph/solutions/4722818/80-1-approach-1-o-v-e-python-c-step-by-step-explanation/

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        # Dictionary to map original nodes to their corresponding clones
        oldToNew = {} # key:value
                                           # DFS function to clone the graph recursively
        def dfs(node):
                                           # If the node already has a clone, return it
            if node in oldToNew:           # key 
                return oldToNew[node]       

            # Create a new clone for the current node
            copy = Node(node.val)          # new node
            oldToNew[node] = copy          # mapping with new node and old 
            
            # Recursively clone each neighbor of the current node
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))
                
            return copy

        # Start DFS traversal from the input node and return its clone
        return dfs(node) if node else None
