class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len((intervals))
        res = [-1] * n
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()
        print(intervals)
        for i in range(n - 1):
            if intervals[i][1] <= intervals[i + 1][0]:
                res[intervals[i][2]] = intervals[i + 1][2]
        return res