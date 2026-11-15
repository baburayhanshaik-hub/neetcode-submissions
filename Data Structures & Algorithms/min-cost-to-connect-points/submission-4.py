class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dic = {}
        n = len(points)
        def calc(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        for i,j in points:
            dic[(i,j)] = float("inf")
        f,l = points[0]
        dic[(f,l)] = 0
        ans = 0
        que = [(0,f,l)]
        while que:
            w,ff,ll = heapq.heappop(que)
            if w<=dic[(ff,ll)]:
                ans+=w
                for i in range(n):
                    f,l = points[i]
                    res = calc((ff,ll),(f,l))
                    if dic[(f,l)]>res:
                        dic[(f,l)] = res
                        heapq.heappush(que,(res,f,l))
        return ans