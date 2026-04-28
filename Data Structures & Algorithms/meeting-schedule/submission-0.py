"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def get_start(self, interval):
        return interval.start

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return intervals
        
        intervals.sort(key=self.get_start)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start1, end1 = res[-1].start, res[-1].end
            start2, end2 = intervals[i].start, intervals[i].end
            if start2 <= end1:
                return False
            else:
                res.append(intervals[i])

        return True
        
