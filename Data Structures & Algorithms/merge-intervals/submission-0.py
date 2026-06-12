class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])
        prev_interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            # Previous not overlap
            if prev_interval[1] < intervals[i][0]:
                res.append(prev_interval)
                prev_interval = intervals[i]
            # Previous overlap:
            elif prev_interval[1] >= intervals[i][0]:
                prev_interval = [min(intervals[i][0], prev_interval[0]), max(intervals[i][1], prev_interval[1])]
        res.append(prev_interval)
        return res