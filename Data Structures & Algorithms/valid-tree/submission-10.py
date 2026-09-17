class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        print(adj)
        visited = set()
        count = 0
        queue = [[0,0]]
        while queue:
            x,p = queue.pop(0)
            print(x,p)
            print(adj[x])
            if x in visited:
                print("here")
                return False
            visited.add(x)
            count+=1
            for i in adj[x]:
                if i!=p:
                    queue.append([i,x])
        if count!=n:
            print(count, n)
            return False
        return True