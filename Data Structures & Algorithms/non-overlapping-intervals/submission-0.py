class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        n = len(intervals)
        intervals.sort()
        prev = intervals[0][1]
        for i,j in intervals[1:]:
            if i>=prev:
                prev = j
            else:
                count+=1
                prev=min(prev,j)
        return count