from collections import defaultdict, deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for src, dst in sorted(tickets):                    # Sort tickets lexicographically and populate the graph
            graph[src].append(dst)
     # print(graph): defaultdict(<class 'collections.deque'>, {'JFK': deque(['ACL', 'MUC']), 'LHR': deque(['SFO']), 'MUC': deque(['LHR']), 'SFO': deque(['SJC'])})
        itinerary = []     
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].popleft()  # ACL
                dfs(next_airport)  # ACL nai r so exit from while loop and add 
            itinerary.append(airport)  #  print('gggggg', itinerary)
            
        dfs("JFK")
        return itinerary[::-1] 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
            
        dfs('JFK')
        return res[::-1]
        
# tickets =  [["MUC", "LHR"], ["JFK", "MUC"], ["JFK", "ACL"], ["SFO", "SJC"], ["LHR", "SFO"]]
deque(['ACL', 'MUC'])
gggggg ['ACL']
deque(['MUC'])
deque(['LHR'])
deque(['SFO'])
deque(['SJC'])
gggggg ['ACL', 'SJC']
gggggg ['ACL', 'SJC', 'SFO']
gggggg ['ACL', 'SJC', 'SFO', 'LHR']
gggggg ['ACL', 'SJC', 'SFO', 'LHR', 'MUC']
gggggg ['ACL', 'SJC', 'SFO', 'LHR', 'MUC', 'JFK']
# Output: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC', 'ACL']


graph="JFK":deque(["ATL","MUC"]),"MUC":deque(["LHR"]),"LHR":deque(["SFO"]),"SFO":deque(["SJC"]),"ATL":deque(["JFK","SFO"])
Start at "JFK":
dfs("JFK")
  "JFK" -> "ATL":
     dfs("ATL")
        "ATL" -> "JFK":
           dfs("JFK")
             "JFK" -> "MUC":
                dfs("MUC")
                  "MUC" -> "LHR":
                     dfs("LHR")
                        "LHR" -> "SFO":
                           dfs("SFO")
                            "SFO" -> "SJC":
                               dfs("SJC")
                                 "SJC" has no more destinations; append "SJC"
                                Append "SFO"
                          Append "LHR"
                  Append "MUC"
             Append "JFK"
     "ATL" -> "SFO":
 dfs("SFO")
dfs("SJC") was already called, so append "SFO"
Append "ATL"
Append "JFK
