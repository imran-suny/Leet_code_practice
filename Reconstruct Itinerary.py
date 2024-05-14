from collections import defaultdict, deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for src, dst in sorted(tickets):                    # Sort tickets lexicographically and populate the graph
            graph[src].append(dst)
        
        itinerary = []     
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].popleft()  # Get the next destination
                dfs(next_airport)
            itinerary.append(airport)
        
        dfs("JFK")
        return itinerary[::-1]

# sol = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# print(sol.findItinerary(tickets))  # Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
