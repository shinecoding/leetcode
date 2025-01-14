class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visitSet = set()

        for pre, cur in prerequisites:
            preMap[cur].append(pre)

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        