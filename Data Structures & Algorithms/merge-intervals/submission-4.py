class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        res = []
        i, j = 0, 1
        curr = intervals[0]
        while j < len(intervals):
            a, b = intervals[i], intervals[j]
            i += 1
            j += 1
            if curr[1] >= b[1]:
                if j == len(intervals):
                    res.append(curr)
            elif curr[1] >= b[0]:
                curr[1] = b[1]
                if j == len(intervals):
                    res.append(curr)
            else:
                res.append(curr)
                curr = intervals[i]
                if j == len(intervals):
                    res.append(intervals[i])
        return res
