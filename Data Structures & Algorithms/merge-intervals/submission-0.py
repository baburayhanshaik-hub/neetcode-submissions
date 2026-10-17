class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        n = len(intervals)
        res.append(intervals[0])
        for i in range(1,n):
            x = res[-1]
            if intervals[i][0]<=x[1]:
                x[1] = max(x[1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res