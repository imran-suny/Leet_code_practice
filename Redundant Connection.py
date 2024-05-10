https://leetcode.com/problems/redundant-connection/description/
https://leetcode.com/problems/redundant-connection/solutions/4742021/87-1-approach-1-o-n-a-n-python-c-step-by-step-explanation/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
######examples
par = {1: 1, 2: 1, 3: 2, 4: 2, 5: 4}
find(5)...
Start with p = 5; since par[p] is 4, update p = 4.
par[4] is 2, update p = 2.
par[2] is 1, update p = 1. Now, p == par[p].
Since you've reached the root, return 1.
