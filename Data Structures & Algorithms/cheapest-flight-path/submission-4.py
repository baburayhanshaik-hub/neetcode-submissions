class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        connects = {}
        prices = {}
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        K+=1
        dq = deque()
        ans = float("inf")
        for i,j,k in flights:
            if i in connects:
                connects[i].append(j)
            else:
                connects[i] = [j]
            prices[(i,j)] = k
        hop, weight = 0, 0
        dq.append([hop, weight, src])
        while dq:
            hop, weight, node = dq.popleft()
            for i in connects.get(node,[]):
                new_weight = weight+prices[(node,i)]
                if new_weight<dist[i]:
                    dist[i] = new_weight
                    if i==dst:
                        ans = min(ans,weight+prices[(node,i)])
                    else:
                        if hop+1<K:
                            dq.append([hop+1, weight+prices[(node,i)],i])
        return -1 if ans==float("inf") else ans
                        