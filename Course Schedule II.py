https://leetcode.com/problems/course-schedule-ii/description/
https://leetcode.com/problems/course-schedule-ii/solutions/4741931/86-1-approach-1-o-v-e-python-c-step-by-step-explanation/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visit, cycle = set(), set()

        # Define a DFS function to traverse the graph
        def dfs(crs):         
            if crs in cycle:  # If the course is in a cycle, means node-1 theke start kore dfs node-1 a jay jodi
                return False
            if crs in visit:  # If the course has already been visited, 2-[], visited hole return true 
                return True

            cycle.add(crs)     # Add the course to the cycle set, dfs er last value 
            # Recursively explore prerequisites
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # Remove the course from the cycle set/ dfs er last value
            cycle.remove(crs)
            # Add the course to the visited set and output list
            visit.add(crs)
            output.append(crs)
            return True

        # Iterate through each course and initiate DFS traversal
        for c in range(numCourses):
            if dfs(c) == False:
                return []  # If a cycle is detected, return an empty array
        return output  # Otherwise, return the valid course order
