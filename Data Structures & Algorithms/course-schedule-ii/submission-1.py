class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for i,j in prerequisites:
            adj[j].append(i)
            indeg[i]+=1
        print(indeg, adj)
        queue = []
        for i in range(len(indeg)):
            if indeg[i]==0:
                queue.append(i)
        ordr = []
        while queue:
            x = queue.pop(0)
            for i in adj[x]:
                indeg[i]-=1
                if indeg[i]==0:
                    queue.append(i)
            ordr.append(x)
        if numCourses!=len(ordr):
            return []
        print(ordr)
        return ordr