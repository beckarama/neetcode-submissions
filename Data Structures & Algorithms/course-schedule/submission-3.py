class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if adjList[crs] == []:
                return True

            visiting.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            adjList[crs] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True