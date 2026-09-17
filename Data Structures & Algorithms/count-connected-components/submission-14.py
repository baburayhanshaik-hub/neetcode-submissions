class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        def check(x):
            queue = [[x,x]]
            while queue:
                x,p = queue.pop(0)
                if x in visited:
                    continue
                visited.add(x)
                for i in adj[x]:
                    if i!=p:
                        queue.append([i,x])
            return True
            
        count = 0
        for i in range(n):
            if i not in visited:
                check(i)
                count+=1
        return count