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
