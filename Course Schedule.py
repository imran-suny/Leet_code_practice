https://leetcode.com/problems/course-schedule/solutions/4733651/85-1-approach-1-o-v-e-python-c-step-by-step-explanation/
Input: numCourses = 2, prerequisites = [[1,0]] crs, pre
Output: true
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
       
        preMap = {i: [] for i in range(numCourses)}  # Initialize a dictionary to map each course to its prerequisites   {0: [], 1: []}                                           
        for crs, pre in prerequisites:               # Populate the preMap with prerequisite relationships
            preMap[crs].append(pre)                  #    {0: [], 1: [0]}  # 1 ache map a , 1 a append hobe 
       
        visiting = set()                             # Set to keep track of courses currently being visited during DFS
        
        def dfs(crs):                                # Define a DFS function to check for cycles and explore prerequisites
      
            if crs in visiting:                      # If the course is already being visited, there is a cycle
                return False                                              
            if preMap[crs] == []:                    # If there are no prerequisites, this course can be completed
                return True

            # Mark the course as visiting and explore its prerequisites
            visiting.add(crs)
            for pre in preMap[crs]:                  # for every prerequisites
                if not dfs(pre):
                    return False
            # Remove the course from visiting set and mark its prerequisites as completed
            visiting.remove(crs)
            preMap[crs] = []
            return True

        # Iterate through each course and initiate DFS traversal
        for c in range(numCourses):
            if not dfs(c):
                return False
        # If all DFS traversals complete without cycles, return True
        return True
