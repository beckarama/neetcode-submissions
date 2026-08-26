class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visit, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        