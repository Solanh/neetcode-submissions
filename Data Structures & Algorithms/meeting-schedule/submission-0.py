"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        valid = True
        if len(intervals) <= 1:
            return valid



        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                valid = False
                break

        return valid