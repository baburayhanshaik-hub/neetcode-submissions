class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        count = 0
        queue = [[0,0]]
        while queue:
            x,p = queue.pop(0)
            if x in visited:
                return False
            visited.add(x)
            count+=1
            for i in adj[x]:
                if i!=p:
                    queue.append([i,x])
        if count!=n:
            return False
        return True