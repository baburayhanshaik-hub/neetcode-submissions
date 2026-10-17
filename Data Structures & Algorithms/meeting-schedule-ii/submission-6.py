import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = []

        for x in intervals:
            l, r = x.start, x.end

            if rooms and rooms[0] <= l:
                heapq.heappop(rooms)

            heapq.heappush(rooms, r)

        return len(rooms)