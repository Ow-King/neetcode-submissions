class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        visited = set()
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        def dfs(course):
            # cycle found
            if course in visited:
                return False

            # there are no more prereqs
            if prereqMap[course] == []:
                return True

            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            prereqMap[course] = [] # dont check it over again

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        # Create a graph of the courses
        # Keep track of all of the visited classes
        # Perform DFS on the classes, if a loop is found that means 