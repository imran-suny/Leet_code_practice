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

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char): 
            if char in visited:                 # visited hole empty/cycle na hole results
                return visited[char]  

            visited[char] = True
            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True                     #  w not in visited, w:true,      e: true [w r neighbor]               r: t, t: t, f:true              
            visited[char] = False                   # cycle hole false 
            res.append(char)                        # f, t,r,e, w


        for char in adj:
            if dfs(char):    # dfs return true or false: true hole empty string , res a result reverse hoye save
                return ""                         # sesh hole w pabe, cycle hole return empty string 
        res.reverse()
        return "".join(res)
