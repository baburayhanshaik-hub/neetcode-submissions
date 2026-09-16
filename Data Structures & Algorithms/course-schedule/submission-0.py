class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = {}
        visited = set()
        for i,j in prerequisites:
            if course.get(i)!=None:
                course[i].append(j)
            else:
                course[i]=[j]
        def dfs(x):
            if x in visited:
                return False
            if course.get(x)==[]:
                return True
            visited.add(x)
            for i in course.get(x,[]):
                if not dfs(i):
                    return False
            visited.remove(x)
            course[x]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True