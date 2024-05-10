https://leetcode.com/problems/course-schedule-ii/description/
https://leetcode.com/problems/course-schedule-ii/solutions/4741931/86-1-approach-1-o-v-e-python-c-step-by-step-explanation/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build a dictionary to represent the prerequisite graph
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # Initialize variables to track visited courses and cycles
        output = []
        visit, cycle = set(), set()

        # Define a DFS function to traverse the graph
        def dfs(crs):
            # If the course is in a cycle, return False
            if crs in cycle:
                return False
            # If the course has already been visited, return True
            if crs in visit:
                return True

            # Add the course to the cycle set
            cycle.add(crs)
            # Recursively explore prerequisites
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # Remove the course from the cycle set
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
