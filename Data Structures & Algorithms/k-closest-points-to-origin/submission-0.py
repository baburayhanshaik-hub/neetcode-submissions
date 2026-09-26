class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i,j in points:
            heapq.heappush(res,(-(i**2+j**2),i,j))
            if len(res)>k:
                heapq.heappop(res)
        for i in res:
            return [[j,k] for i,j,k in res]