class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0]+cost+[0]
        n = len(cost)
        stairs = [float("inf") for i in range(n+1)]
        visited = {0:0, 1:cost[0]}
        def func(n):
            if n in visited:
                return visited[n]
            ans = min(cost[n-1]+func(n-1),cost[n-2]+func(n-2))
            visited[n] = ans
            return ans
        return func(n)