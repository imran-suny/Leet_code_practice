https://leetcode.com/problems/network-delay-time/solutions/4746258/90-1-approach-1-dijkstra-s-algorithm-o-e-log-v-python-c-step-by-step-explanation/
https://leetcode.com/problems/network-delay-time/description/
class Solution:                            # Dijkstra's algorithm--computes shortest path from a starting node to all other nodes
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)      # Create a defaultdict to store the adjacency list representation of the graph
        for u, v, w in times:
            edges[u].append((v, w))                # Populate the adjacency list with the given edges and weights

        minHeap = [(0, k)]                         # k is the starting node and 0 is the distance to k
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)         # Iterate over the neighbors of the current node
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1                                # Update the time to the current distance

            for n2, w2 in edges[n1]:              # Iterate over the neighbors of the current node
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))   # Add the neighbor to the minHeap with updated distance
        return t if len(visit) == n else -1                   # If all nodes have been visited, return the maximum time taken


        # O(E * logV)

Dijkstra’s on directed and undirected graphs. Prim’s is on undirected graphs.  initializes the distance of the source vertex to 0 and all others to infinity.
Dijkstra finds the shortest path from one source to all other vertices.
Prims on spanning tree that covers all vertices with the minimum total edge weight. initializes cost of all vertices to infinity, except for the starting vertex which is set to 0.
