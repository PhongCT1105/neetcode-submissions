class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            # New Intervals come before current interval
            if newInterval[1] < intervals[i][0]:
                return res + [newInterval] + intervals[i:]
            # New interval overlap with current interval
            elif newInterval[0] <= intervals[i][1]:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            # New interval come after current interval
            else:
                res.append(intervals[i])
        res.append(newInterval)
        return res