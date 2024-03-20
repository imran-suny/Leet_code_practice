Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
] Output: "wertf"
https://www.youtube.com/watch?v=IIgisEKjCKA

class Solution:
    def alienOrder(self, words: List[str]) -> str:
                                                              # make a graph   
      adj = {char: set() for word in words for char in word}  # w: [],  r : [] 
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]                   # wrt, wrf 
            minLen = min(len(w1), len(w2))                    # 3 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):   0,1,2
                if w1[j] != w2[j]:    w=w, r=r,   t!=f
                    print(w1[j], w2[j])   
                    adj[w1[j]].add(w2[j])    #  adj    w: [e], r: [t], t: [f], f:[w], e:[r] 
                    break

        visited = {}  #  # {char: bool} False: unvisited, True: visiting
        res = []

        def dfs(char): 
            if char in visited:                 # visited hole empty/cycle na hole results
                return visited[char]  

            visited[char] = True
            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True                     #If cycle is detected, return True   w not in visited, w:true,      e: true [w r neighbor]               r: t, t: t, f:true              
            visited[char] = False                   # # Backtrack: Mark the current character as not being visited in the current path 
            res.append(char)                        # f, t,r,e, w


        for char in adj:
            if dfs(char):    #If a cycle is detected during DFS, return an empty string indicating invalid alien orde
                return ""                         # sesh hole w pabe, cycle hole return empty string 
        res.reverse()
        return "".join(res)


adj = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [5],
    5: []
}

visited = {}  # {node: bool} False: unvisited, True: visiting
res = []

def dfs(node):
    if node in visited:
        return visited[node]
    visited[node] = True
    for neighbor in adj[node]:
        if dfs(neighbor):
            return True
    visited[node] = False
    res.append(node)
for node in adj:
    if dfs(node):
        print("Cycle detected!")
        break
res.reverse()
print("DFS order:", res)

Start DFS from node 1.
Visit node 1 and mark it as visited.
Explore neighbors of node 1: nodes 2 and 3.
Start DFS from node 2 (neighbor of node 1).
Visit node 2 and mark it as visited.
Explore neighbors of node 2: node 4.
Start DFS from node 4 (neighbor of node 2).
Visit node 4 and mark it as visited.
Explore neighbors of node 4: node 5.
Start DFS from node 5 (neighbor of node 4).
Visit node 5 and mark it as visited.
Node 5 has no outgoing edges, so append it to the result list.
Backtrack to node 4.
Node 4 has been fully explored, so append it to the result list.
Backtrack to node 2.
Node 2 has been fully explored, so append it to the result list.
Backtrack to node 1.
Node 1 has one more unvisited neighbor (node 3).
Start DFS from node 3 (neighbor of node 1).
Visit node 3 and mark it as visited.
Node 3 has no outgoing edges, so append it to the result list.
Backtrack to node 1.
Node 1 has been fully explored, so append it to the result list
[5, 4, 2, 3, 1]
