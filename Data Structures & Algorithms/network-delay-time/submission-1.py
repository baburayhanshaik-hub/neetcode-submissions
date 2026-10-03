from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        nodes = [float("inf") for _ in range(n+1)]
        nodes[k] = 0
        visited = set()
        for i,j,t in times:
            if i in graph:
                graph[i].append([j,t])
            else:
                graph[i] = [[j,t]]
        def func(node,time):
            que = [[node,time]]
            visited.add(node)
            while que:
                node = que.pop(0)
                val,time = node[0], node[1]
                print(node)
                for i in graph[val]:
                    if nodes[val]+i[1]<nodes[i[0]]:
                        nodes[i[0]] = nodes[val]+i[1]
                    if i[0] not in visited:
                        que.append([i[0],nodes[val]+i[1]])
                    for j in range(len(que)):
                        if que[j][0]==i[0]:
                            que[j][1] =  nodes[val]+i[1]
                    visited.add(i[0])
                que.sort(key = lambda x:x[1])
        func(k,0)
        print(graph)
        print(nodes)
        return -1 if max(nodes[1:])==float("inf") else max(nodes[1:])