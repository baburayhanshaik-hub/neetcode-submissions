"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, ints: List[Interval]) -> bool:
        if len(ints)==0:
            return True
        ints.sort(key=lambda x: x.start)
        prev = ints[0].end
        for i in ints[1:]:
            if i.start<prev:
                return False
            else:
                prev=i.end
        return True