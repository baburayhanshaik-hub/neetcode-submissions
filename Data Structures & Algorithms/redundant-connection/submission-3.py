class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        visited = set()
        nmax = 0
        for i,j in edges:
            if adj.get(i)==None:
                adj[i]=[j]
            else:
                adj[i].append(j)
            if adj.get(j)==None:
                adj[j]=[i]
            else:
                adj[j].append(i)
            nmax = max(nmax,i,j)
        print(adj)
        found = set()
        point = None
        def dfs(x,p):
            nonlocal point
            if x in visited:
                point = x
                print(point)
                return True
            visited.add(x)
            for i in adj[x]:
                if i!=p:
                    if dfs(i,x):
                        if point:
                            found.add((i,x))
                            if x == point:
                                point = None
                        return True
        for i in range(1,nmax+1):
            if i not in visited:
                print("outside",i)
                x = dfs(i,i)
                print(x)
                print(found)
                if x:
                    for i,j in edges[::-1]:
                        if (i,j) in found or (j,i) in found:
                            return [i,j]
                
        return []

